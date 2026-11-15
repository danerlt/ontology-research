import json
from typing import Any
from uuid import UUID

from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session, selectinload

from backend.ontology_service.app.models import LinkType, ObjectLink, ObjectRecord, ObjectType, PropertyDefinition
from backend.ontology_service.app.schemas.proposals import DerivedPropertyDefinitionInput
from backend.ontology_service.app.services.derived_properties import validate_definition

MAX_PATH_OBJECTS = 1000


def preview_derived_property(
    session: Session,
    *,
    ontology_id: UUID,
    object_id: UUID,
    definition: DerivedPropertyDefinitionInput,
    actor_role: str,
    snapshot: dict[str, Any],
) -> dict[str, Any]:
    normalized = definition.model_dump(mode="json")
    errors = validate_definition(snapshot, normalized)
    if errors:
        raise HTTPException(status_code=422, detail={"message": "派生属性定义校验失败", "errors": errors})

    root = session.scalar(
        select(ObjectRecord)
        .where(ObjectRecord.id == object_id)
        .options(selectinload(ObjectRecord.object_type).selectinload(ObjectType.properties))
    )
    if root is None or root.object_type.ontology_id != ontology_id:
        raise HTTPException(status_code=404, detail="起始对象不存在")
    if root.object_type.api_name != normalized["object_type_api_name"]:
        raise HTTPException(status_code=422, detail="起始对象类型与派生属性定义不匹配")

    current_type_id = root.object_type_id
    states: list[tuple[ObjectRecord, list[dict[str, Any]]]] = [(root, [])]
    for index, step in enumerate(normalized["path"], start=1):
        link = session.scalar(
            select(LinkType).where(
                LinkType.ontology_id == ontology_id,
                LinkType.api_name == step["link_api_name"],
            )
        )
        if link is None:
            raise HTTPException(status_code=422, detail=f"第 {index} 步链接尚未发布到主本体，当前无法读取实例")
        direction = step["direction"]
        if direction == "outgoing":
            if link.source_type_id != current_type_id:
                raise HTTPException(status_code=422, detail=f"第 {index} 步出向链接起点不连续")
            next_type_id = link.target_type_id
            edge_statement = select(ObjectLink).where(
                ObjectLink.link_type_id == link.id,
                ObjectLink.source_object_id.in_([record.id for record, _ in states]),
            )
        else:
            if link.target_type_id != current_type_id:
                raise HTTPException(status_code=422, detail=f"第 {index} 步入向链接终点不连续")
            next_type_id = link.source_type_id
            edge_statement = select(ObjectLink).where(
                ObjectLink.link_type_id == link.id,
                ObjectLink.target_object_id.in_([record.id for record, _ in states]),
            )

        edges = list(session.scalars(edge_statement.order_by(ObjectLink.id)).all())
        destination_ids = {
            edge.target_object_id if direction == "outgoing" else edge.source_object_id
            for edge in edges
        }
        destination_records = session.scalars(
            select(ObjectRecord)
            .where(ObjectRecord.id.in_(destination_ids))
            .options(selectinload(ObjectRecord.object_type).selectinload(ObjectType.properties))
            .order_by(ObjectRecord.id)
        ).all() if destination_ids else []
        record_by_id = {record.id: record for record in destination_records}
        states_by_id: dict[UUID, list[tuple[ObjectRecord, list[dict[str, Any]]]]] = {}
        for record, trace in states:
            states_by_id.setdefault(record.id, []).append((record, trace))

        next_states: list[tuple[ObjectRecord, list[dict[str, Any]]]] = []
        for edge in edges:
            current_id = edge.source_object_id if direction == "outgoing" else edge.target_object_id
            destination_id = edge.target_object_id if direction == "outgoing" else edge.source_object_id
            destination = record_by_id.get(destination_id)
            if destination is None or destination.object_type_id != next_type_id:
                continue
            for current, trace in states_by_id.get(current_id, []):
                next_states.append((destination, [
                    *trace,
                    {
                        "step": index,
                        "link_api_name": link.api_name,
                        "direction": direction,
                        "from_object_id": str(current.id),
                        "to_object_id": str(destination.id),
                        "source_object_id": str(edge.source_object_id),
                        "target_object_id": str(edge.target_object_id),
                    },
                ]))
                if len(next_states) > MAX_PATH_OBJECTS:
                    raise HTTPException(status_code=413, detail="试算命中对象超过 1000 条，请缩短路径或缩小数据范围")
        states = next_states
        current_type_id = next_type_id

    terminal = session.scalar(
        select(PropertyDefinition).where(
            PropertyDefinition.object_type_id == current_type_id,
            PropertyDefinition.api_name == normalized["terminal_property_api_name"],
        )
    )
    if terminal is None:
        raise HTTPException(status_code=422, detail="派生属性终点字段尚未发布，当前无法试算")
    if actor_role == "viewer" and terminal.sensitive:
        raise HTTPException(status_code=403, detail="当前项目角色无权读取敏感终点属性")

    values: list[Any] = []
    trace: list[dict[str, Any]] = []
    ignored_null_count = 0
    for record, path_trace in states:
        value = record.properties.get(terminal.api_name)
        trace.extend(path_trace)
        trace.append({
            "step": len(normalized["path"]) + 1,
            "object_id": str(record.id),
            "property_api_name": terminal.api_name,
            "value": value,
        })
        if value is None:
            ignored_null_count += 1
        else:
            values.append(value)

    aggregation = normalized.get("aggregation")
    if aggregation == "count":
        value = len(states)
        matched_count = len(states)
    elif aggregation == "sum":
        value = sum(values) if values else 0
        matched_count = len(values)
    elif aggregation == "average":
        value = sum(values) / len(values) if values else None
        matched_count = len(values)
    elif aggregation == "minimum":
        value = min(values) if values else None
        matched_count = len(values)
    elif aggregation == "maximum":
        value = max(values) if values else None
        matched_count = len(values)
    elif aggregation == "collect_list":
        value = values
        matched_count = len(values)
    elif aggregation == "collect_set":
        unique_values = {json.dumps(item, sort_keys=True, ensure_ascii=False): item for item in values}
        value = [unique_values[key] for key in sorted(unique_values)]
        matched_count = len(values)
    else:
        if len(states) > 1:
            raise HTTPException(status_code=422, detail="路径实际命中多个对象，但定义未包含聚合器")
        value = values[0] if values else None
        matched_count = len(values)

    warnings = []
    if not states:
        warnings.append("路径未命中任何终点对象。")
    if ignored_null_count:
        warnings.append(f"有 {ignored_null_count} 个终点属性为空，已按空值规则跳过。")
    return {
        "object_id": object_id,
        "api_name": normalized["api_name"],
        "value": value,
        "result_type": normalized["data_type"],
        "aggregation": aggregation,
        "matched_count": matched_count,
        "path_object_count": len(states),
        "ignored_null_count": ignored_null_count,
        "trace": trace,
        "warnings": warnings,
    }
