import json
from datetime import datetime, timezone
from typing import Annotated, Any
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session, selectinload

from backend.ontology_service.app.database import get_db
from backend.ontology_service.app.models import (
    DataImportRun,
    DataSourceConnection,
    DataSourceMapping,
    ObjectRecord,
    ObjectType,
    Ontology,
    PropertyDefinition,
)
from backend.ontology_service.app.schemas.data_sources import (
    DataImportRunResponse,
    DataMappingResponse,
    DataMappingUpsert,
    DataPreviewIssue,
    DataPreviewItem,
    DataPreviewResponse,
    DataRowsRequest,
    DataSourceCreate,
    DataSourceResponse,
)
from backend.ontology_service.app.security import Actor, get_current_user, require_role
from backend.ontology_service.app.services.action_engine import validate_record_properties
from backend.ontology_service.app.services.audit import record_audit

router = APIRouter(prefix="/api/data-sources", tags=["数据源与映射"])


@router.get("", response_model=list[DataSourceResponse])
def list_data_sources(
    _actor: Annotated[Actor, Depends(get_current_user)],
    session: Annotated[Session, Depends(get_db)],
    ontology_id: UUID | None = None,
) -> list[DataSourceResponse]:
    statement = (
        select(DataSourceConnection)
        .options(selectinload(DataSourceConnection.mappings), selectinload(DataSourceConnection.runs))
        .order_by(DataSourceConnection.updated_at.desc())
    )
    if ontology_id is not None:
        statement = statement.where(DataSourceConnection.ontology_id == ontology_id)
    connections = session.scalars(statement).all()
    return [
        DataSourceResponse(
            id=connection.id,
            ontology_id=connection.ontology_id,
            created_by_id=connection.created_by_id,
            name=connection.name,
            description=connection.description,
            connector_type=connection.connector_type,
            status=connection.status,
            mapping_count=len(connection.mappings),
            last_run_status=connection.runs[0].status if connection.runs else None,
            last_run_at=connection.runs[0].created_at if connection.runs else None,
            created_at=connection.created_at,
        )
        for connection in connections
    ]


@router.post("", response_model=DataSourceResponse, status_code=status.HTTP_201_CREATED)
def create_data_source(
    body: DataSourceCreate,
    actor: Annotated[Actor, Depends(require_role("admin", "editor"))],
    session: Annotated[Session, Depends(get_db)],
) -> DataSourceResponse:
    ontology = session.get(Ontology, body.ontology_id)
    if ontology is None:
        raise HTTPException(status_code=404, detail="本体不存在")
    connection = DataSourceConnection(
        ontology_id=ontology.id,
        created_by_id=UUID(actor.id),
        name=body.name,
        description=body.description,
        connector_type=body.connector_type,
    )
    session.add(connection)
    try:
        session.flush()
        record_audit(
            session,
            actor_id=actor.id,
            event_type="datasource.connection.created",
            resource_type="data_source",
            resource_id=connection.id,
            details={"ontology_id": str(ontology.id), "connector_type": connection.connector_type},
        )
        session.commit()
        session.refresh(connection)
    except IntegrityError as exc:
        session.rollback()
        raise HTTPException(status_code=409, detail="此本体中已存在同名数据源") from exc
    return DataSourceResponse(
        id=connection.id,
        ontology_id=connection.ontology_id,
        created_by_id=connection.created_by_id,
        name=connection.name,
        description=connection.description,
        connector_type=connection.connector_type,
        status=connection.status,
        created_at=connection.created_at,
    )


@router.get("/{connection_id}/mappings", response_model=list[DataMappingResponse])
def list_mappings(
    connection_id: UUID,
    _actor: Annotated[Actor, Depends(get_current_user)],
    session: Annotated[Session, Depends(get_db)],
) -> list[DataMappingResponse]:
    _require_connection(session, connection_id)
    mappings = session.scalars(
        select(DataSourceMapping)
        .where(DataSourceMapping.connection_id == connection_id)
        .options(selectinload(DataSourceMapping.object_type))
        .order_by(DataSourceMapping.created_at)
    ).all()
    return [_mapping_response(mapping) for mapping in mappings]


@router.put("/{connection_id}/mappings", response_model=DataMappingResponse)
def upsert_mapping(
    connection_id: UUID,
    body: DataMappingUpsert,
    actor: Annotated[Actor, Depends(require_role("admin", "editor"))],
    session: Annotated[Session, Depends(get_db)],
) -> DataMappingResponse:
    connection = _require_connection(session, connection_id)
    object_type = session.scalar(
        select(ObjectType)
        .where(
            ObjectType.ontology_id == connection.ontology_id,
            ObjectType.api_name == body.object_type_api_name,
        )
        .options(selectinload(ObjectType.properties))
    )
    if object_type is None:
        raise HTTPException(status_code=404, detail="目标对象类型不存在于此本体")
    if body.primary_key_field not in body.field_mappings:
        raise HTTPException(status_code=422, detail="主键来源列必须包含在字段映射中")
    if body.field_mappings[body.primary_key_field] != object_type.primary_key_property:
        raise HTTPException(status_code=422, detail="主键来源列必须映射到对象类型主键属性")
    source_fields = [name.strip() for name in body.field_mappings]
    if any(not name for name in source_fields) or len(source_fields) != len(set(source_fields)):
        raise HTTPException(status_code=422, detail="来源列名不能为空或重复")
    target_properties = list(body.field_mappings.values())
    if len(target_properties) != len(set(target_properties)):
        raise HTTPException(status_code=422, detail="多个来源列不能映射到同一个本体属性")
    known_properties = {definition.api_name for definition in object_type.properties}
    unknown_properties = set(target_properties) - known_properties
    if unknown_properties:
        raise HTTPException(status_code=422, detail=f"本体属性不存在：{', '.join(sorted(unknown_properties))}")

    mapping = session.scalar(
        select(DataSourceMapping).where(
            DataSourceMapping.connection_id == connection.id,
            DataSourceMapping.object_type_id == object_type.id,
        )
    )
    if mapping is None:
        mapping = DataSourceMapping(connection_id=connection.id, object_type_id=object_type.id)
        session.add(mapping)
    mapping.primary_key_field = body.primary_key_field
    mapping.field_mappings = dict(body.field_mappings)
    record_audit(
        session,
        actor_id=actor.id,
        event_type="datasource.mapping.saved",
        resource_type="data_source_mapping",
        resource_id=mapping.id,
        details={"object_type_api_name": object_type.api_name, "field_count": len(body.field_mappings)},
    )
    session.commit()
    session.refresh(mapping)
    mapping.object_type = object_type
    return _mapping_response(mapping)


@router.post("/{connection_id}/mappings/{mapping_id}/preview", response_model=DataPreviewResponse)
def preview_import(
    connection_id: UUID,
    mapping_id: UUID,
    body: DataRowsRequest,
    actor: Annotated[Actor, Depends(get_current_user)],
    session: Annotated[Session, Depends(get_db)],
) -> DataPreviewResponse:
    connection, mapping, object_type = _require_mapping(session, connection_id, mapping_id)
    if actor.role not in {"admin", "editor"}:
        raise HTTPException(status_code=403, detail="只有本体编辑者可以预览数据导入")
    items, errors = _preview_rows(session, mapping, object_type, body.rows)
    return DataPreviewResponse(
        valid=not errors,
        rows_total=len(body.rows),
        items=[DataPreviewItem(**item) for item in items[:200]],
        errors=[DataPreviewIssue(**issue) for issue in errors],
    )


@router.post(
    "/{connection_id}/mappings/{mapping_id}/import",
    response_model=DataImportRunResponse,
    status_code=status.HTTP_201_CREATED,
)
def import_rows(
    connection_id: UUID,
    mapping_id: UUID,
    body: DataRowsRequest,
    actor: Annotated[Actor, Depends(require_role("admin", "editor"))],
    session: Annotated[Session, Depends(get_db)],
) -> DataImportRunResponse:
    connection, mapping, object_type = _require_mapping(session, connection_id, mapping_id)
    items, errors = _preview_rows(session, mapping, object_type, body.rows)
    run = DataImportRun(
        connection_id=connection.id,
        mapping_id=mapping.id,
        actor_id=UUID(actor.id),
        status="running",
        rows_total=len(body.rows),
        rows_imported=0,
        errors=errors,
    )
    session.add(run)
    session.flush()
    if errors:
        run.status = "failed"
        run.completed_at = datetime.now(timezone.utc)
        record_audit(
            session,
            actor_id=actor.id,
            event_type="datasource.import.failed",
            resource_type="data_import_run",
            resource_id=run.id,
            details={"rows_total": run.rows_total, "error_count": len(errors)},
        )
        session.commit()
        raise HTTPException(
            status_code=422,
            detail={"message": "数据导入校验失败，未写入任何对象", "errors": errors},
        )

    try:
        with session.begin_nested():
            session.add_all(
                ObjectRecord(
                    object_type_id=object_type.id,
                    primary_key_value=item["primary_key_value"],
                    properties=item["properties"],
                )
                for item in items
            )
            session.flush()
            run.status = "completed"
            run.rows_imported = len(items)
            run.errors = []
            run.completed_at = datetime.now(timezone.utc)
            record_audit(
                session,
                actor_id=actor.id,
                event_type="datasource.import.completed",
                resource_type="data_import_run",
                resource_id=run.id,
                details={
                    "connection_id": str(connection.id),
                    "mapping_id": str(mapping.id),
                    "object_type_api_name": object_type.api_name,
                    "rows_total": run.rows_total,
                    "rows_imported": run.rows_imported,
                },
            )
            session.flush()
    except IntegrityError:
        run.status = "failed"
        run.rows_imported = 0
        run.errors = [{"row": 0, "field": mapping.primary_key_field, "message": "导入期间主键冲突；未写入任何对象"}]
        run.completed_at = datetime.now(timezone.utc)
        session.commit()
        raise HTTPException(status_code=409, detail="导入期间数据发生并发变化，请重新预览")
    session.commit()
    session.refresh(run)
    return DataImportRunResponse.model_validate(run)


@router.get("/{connection_id}/runs", response_model=list[DataImportRunResponse])
def list_import_runs(
    connection_id: UUID,
    _actor: Annotated[Actor, Depends(get_current_user)],
    session: Annotated[Session, Depends(get_db)],
) -> list[DataImportRunResponse]:
    _require_connection(session, connection_id)
    runs = session.scalars(
        select(DataImportRun)
        .where(DataImportRun.connection_id == connection_id)
        .order_by(DataImportRun.created_at.desc())
        .limit(100)
    ).all()
    return [DataImportRunResponse.model_validate(run) for run in runs]


def _require_connection(session: Session, connection_id: UUID) -> DataSourceConnection:
    connection = session.get(DataSourceConnection, connection_id)
    if connection is None:
        raise HTTPException(status_code=404, detail="数据源连接不存在")
    return connection


def _require_mapping(
    session: Session,
    connection_id: UUID,
    mapping_id: UUID,
) -> tuple[DataSourceConnection, DataSourceMapping, ObjectType]:
    connection = _require_connection(session, connection_id)
    mapping = session.scalar(
        select(DataSourceMapping)
        .where(DataSourceMapping.id == mapping_id, DataSourceMapping.connection_id == connection.id)
        .options(selectinload(DataSourceMapping.object_type).selectinload(ObjectType.properties))
    )
    if mapping is None:
        raise HTTPException(status_code=404, detail="此数据源下不存在该映射")
    return connection, mapping, mapping.object_type


def _mapping_response(mapping: DataSourceMapping) -> DataMappingResponse:
    return DataMappingResponse(
        id=mapping.id,
        connection_id=mapping.connection_id,
        object_type_id=mapping.object_type_id,
        object_type_api_name=mapping.object_type.api_name,
        object_type_display_name=mapping.object_type.display_name,
        primary_key_field=mapping.primary_key_field,
        field_mappings=mapping.field_mappings,
        updated_at=mapping.updated_at,
    )


def _preview_rows(
    session: Session,
    mapping: DataSourceMapping,
    object_type: ObjectType,
    rows: list[dict[str, Any]],
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    errors: list[dict[str, Any]] = []
    items: list[dict[str, Any]] = []
    definitions = {definition.api_name: definition for definition in object_type.properties}
    seen_primary_keys: set[str] = set()
    seen_unique: dict[str, set[str]] = {
        definition.api_name: set()
        for definition in object_type.properties
        if definition.unique_value and definition.api_name != object_type.primary_key_property
    }
    if mapping.field_mappings.get(mapping.primary_key_field) != object_type.primary_key_property:
        return [], [{"row": 0, "field": mapping.primary_key_field, "message": "映射的主键属性已不再是对象类型主键，请更新映射"}]
    unknown_targets = set(mapping.field_mappings.values()) - set(definitions)
    if unknown_targets:
        return [], [{"row": 0, "field": name, "message": f"映射目标属性已不存在：{name}"} for name in sorted(unknown_targets)]

    for row_index, row in enumerate(rows, start=1):
        if not isinstance(row, dict):
            errors.append({"row": row_index, "field": "row", "message": "每行数据必须是字段和值组成的对象"})
            continue
        missing_columns = set(mapping.field_mappings) - set(row)
        if missing_columns:
            for column in sorted(missing_columns):
                errors.append({"row": row_index, "field": column, "message": "来源列不存在"})
            continue
        properties = {
            target: _coerce_source_value(definitions[target], row[source])
            for source, target in mapping.field_mappings.items()
        }
        primary_value = properties.get(object_type.primary_key_property)
        if not isinstance(primary_value, str) or not primary_value:
            errors.append({"row": row_index, "field": mapping.primary_key_field, "message": "主键值必须是非空字符串"})
            continue
        if primary_value in seen_primary_keys:
            errors.append({"row": row_index, "field": mapping.primary_key_field, "message": f"导入文件内出现重复主键：{primary_value}"})
            continue
        seen_primary_keys.add(primary_value)
        existing_id = session.scalar(
            select(ObjectRecord.id).where(
                ObjectRecord.object_type_id == object_type.id,
                ObjectRecord.primary_key_value == primary_value,
            )
        )
        if existing_id is not None:
            errors.append({"row": row_index, "field": mapping.primary_key_field, "message": f"主键已存在于本体对象中：{primary_value}"})
            continue
        try:
            validated_properties = validate_record_properties(session, object_type, properties)
        except HTTPException as exc:
            errors.append({"row": row_index, "field": "row", "message": str(exc.detail)})
            continue

        row_has_duplicate_unique = False
        for property_name, values in seen_unique.items():
            value = validated_properties.get(property_name)
            if value is None:
                continue
            unique_key = str(value)
            if unique_key in values:
                errors.append({"row": row_index, "field": property_name, "message": "导入文件内出现重复唯一属性值"})
                row_has_duplicate_unique = True
            values.add(unique_key)
        if row_has_duplicate_unique:
            continue
        items.append(
            {
                "row": row_index,
                "primary_key_value": primary_value,
                "properties": validated_properties,
            }
        )
    return items, errors


def _coerce_source_value(definition: PropertyDefinition, value: Any) -> Any:
    if not isinstance(value, str):
        return value
    normalized = value.strip()
    if definition.data_type == "integer":
        try:
            return int(normalized)
        except ValueError:
            return value
    if definition.data_type == "number":
        try:
            return float(normalized)
        except ValueError:
            return value
    if definition.data_type == "boolean":
        if normalized.lower() in {"true", "1"}:
            return True
        if normalized.lower() in {"false", "0"}:
            return False
        return value
    if definition.data_type == "json":
        try:
            return json.loads(value)
        except json.JSONDecodeError:
            return value
    return value
