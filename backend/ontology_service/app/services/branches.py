from copy import deepcopy
from typing import Any
from uuid import UUID

from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session, selectinload

from backend.ontology_service.app.models import ActionDefinition, LinkType, ObjectType, Ontology, OntologyBranch
from backend.ontology_service.app.services.action_engine import validate_submission_criteria
from backend.ontology_service.app.services.derived_properties import validate_definition


def create_schema_snapshot(session: Session, ontology: Ontology) -> dict[str, Any]:
    object_types = session.scalars(
        select(ObjectType)
        .where(ObjectType.ontology_id == ontology.id)
        .options(selectinload(ObjectType.properties))
        .order_by(ObjectType.api_name)
    ).all()
    type_names = {object_type.id: object_type.api_name for object_type in object_types}
    links = session.scalars(
        select(LinkType).where(LinkType.ontology_id == ontology.id).order_by(LinkType.api_name)
    ).all()
    actions = session.scalars(
        select(ActionDefinition)
        .where(ActionDefinition.ontology_id == ontology.id)
        .order_by(ActionDefinition.api_name)
    ).all()
    return {
        "ontology_id": str(ontology.id),
        "revision": ontology.revision,
        "object_types": [
            {
                "api_name": item.api_name,
                "display_name": item.display_name,
                "plural_display_name": item.plural_display_name or item.display_name,
                "description": item.description,
                "primary_key_property": item.primary_key_property,
                "title_key_property": item.title_key_property,
                "aliases": item.aliases,
                "groups": item.groups,
                "icon": item.icon,
                "icon_color": item.icon_color,
                "properties": [
                    {
                        "api_name": prop.api_name,
                        "display_name": prop.display_name,
                        "data_type": prop.data_type,
                        "required": prop.required,
                        "editable": prop.editable,
                        "unique_value": prop.unique_value,
                        "sensitive": prop.sensitive,
                        "options": prop.options,
                    }
                    for prop in sorted(item.properties, key=lambda value: value.api_name)
                ],
            }
            for item in object_types
        ],
        "link_types": [
            {
                "api_name": item.api_name,
                "display_name": item.display_name,
                "description": item.description,
                "source_type_api_name": type_names.get(item.source_type_id),
                "target_type_api_name": type_names.get(item.target_type_id),
                "source_cardinality": item.source_cardinality,
                "target_cardinality": item.target_cardinality,
            }
            for item in links
        ],
        "actions": [
            {
                "api_name": item.api_name,
                "display_name": item.display_name,
                "object_type_api_name": type_names.get(item.object_type_id),
                "enabled": item.enabled,
                "parameters_schema": item.parameters_schema,
                "submission_criteria": item.submission_criteria,
                "allowed_properties": item.allowed_properties,
            }
            for item in actions
        ],
    }


def apply_schema_changes(snapshot: dict[str, Any], changes: list[dict[str, Any]]) -> tuple[dict, dict]:
    result = deepcopy(snapshot)
    errors: list[dict[str, str]] = []
    warnings: list[dict[str, str]] = []
    object_types = result.setdefault("object_types", [])
    link_types = result.setdefault("link_types", [])
    actions = result.setdefault("actions", [])

    for change in changes:
        operation = change.get("op")
        api_name = str(change.get("api_name", ""))
        if operation == "add_object_type":
            path = f"object_type:{api_name}"
            if any(item["api_name"] == api_name for item in object_types):
                errors.append({"path": path, "message": "对象类型 API 名已存在"})
                continue
            primary_key = change.get("primary_key_property", "id")
            object_types.append(
                {
                    "api_name": api_name,
                    "display_name": change["display_name"],
                    "plural_display_name": change.get("plural_display_name") or change["display_name"],
                    "description": change.get("description", ""),
                    "primary_key_property": primary_key,
                    "title_key_property": change.get("title_key_property") or primary_key,
                    "aliases": change.get("aliases", []),
                    "groups": change.get("groups", []),
                    "icon": change.get("icon", "object"),
                    "icon_color": change.get("icon_color", "#4F8067"),
                    "properties": [
                        {
                            "api_name": primary_key,
                            "display_name": "唯一标识",
                            "data_type": "string",
                            "required": True,
                            "editable": False,
                            "unique_value": True,
                            "sensitive": False,
                            "options": {},
                        }
                    ],
                }
            )
            if not change.get("description"):
                warnings.append({"path": path, "message": "建议补充对象类型说明"})
            continue

        if operation == "add_property":
            type_name = change["object_type_api_name"]
            path = f"property:{type_name}.{api_name}"
            object_type = next((item for item in object_types if item["api_name"] == type_name), None)
            if object_type is None:
                errors.append({"path": path, "message": "目标对象类型不存在"})
                continue
            if any(item["api_name"] == api_name for item in object_type["properties"]):
                errors.append({"path": path, "message": "属性 API 名已存在"})
                continue
            object_type["properties"].append(
                {
                    "api_name": api_name,
                    "display_name": change["display_name"],
                    "data_type": change["data_type"],
                    "required": change.get("required", False),
                    "editable": change.get("editable", True),
                    "unique_value": change.get("unique_value", False),
                    "sensitive": change.get("sensitive", False),
                    "options": change.get("options", {}),
                }
            )
            continue

        if operation == "update_object_type":
            path = f"object_type:{api_name}"
            object_type = next((item for item in object_types if item["api_name"] == api_name), None)
            if object_type is None:
                errors.append({"path": path, "message": "待修改的对象类型不存在"})
                continue
            for field in (
                "display_name",
                "plural_display_name",
                "description",
                "title_key_property",
                "aliases",
                "groups",
                "icon",
                "icon_color",
            ):
                if field in change:
                    object_type[field] = change[field]
            continue

        if operation == "update_property":
            type_name = change["object_type_api_name"]
            path = f"property:{type_name}.{api_name}"
            object_type = next((item for item in object_types if item["api_name"] == type_name), None)
            prop = next(
                (item for item in object_type["properties"] if item["api_name"] == api_name), None
            ) if object_type is not None else None
            if prop is None:
                errors.append({"path": path, "message": "待修改的属性不存在"})
                continue
            for field in (
                "display_name",
                "data_type",
                "required",
                "editable",
                "unique_value",
                "sensitive",
                "options",
            ):
                if field in change:
                    prop[field] = change[field]
            continue

        if operation == "add_link_type":
            path = f"link_type:{api_name}"
            source_name = change["source_type_api_name"]
            target_name = change["target_type_api_name"]
            if any(item["api_name"] == api_name for item in link_types):
                errors.append({"path": path, "message": "链接类型 API 名已存在"})
                continue
            known_types = {item["api_name"] for item in object_types}
            if source_name not in known_types or target_name not in known_types:
                errors.append({"path": path, "message": "链接类型的起点或终点对象类型不存在"})
                continue
            link_types.append(
                {
                    "api_name": api_name,
                    "display_name": change["display_name"],
                    "description": change.get("description", ""),
                    "source_type_api_name": source_name,
                    "target_type_api_name": target_name,
                    "source_cardinality": change.get("source_cardinality", "many"),
                    "target_cardinality": change.get("target_cardinality", "many"),
                }
            )
            continue

        if operation == "update_link_type":
            path = f"link_type:{api_name}"
            link = next((item for item in link_types if item["api_name"] == api_name), None)
            if link is None:
                errors.append({"path": path, "message": "待修改的链接类型不存在"})
                continue
            known_types = {item["api_name"] for item in object_types}
            source_name = change.get("source_type_api_name", link["source_type_api_name"])
            target_name = change.get("target_type_api_name", link["target_type_api_name"])
            if source_name not in known_types or target_name not in known_types:
                errors.append({"path": path, "message": "链接两端必须引用已定义对象类型"})
                continue
            for field in ("display_name", "description", "source_cardinality", "target_cardinality"):
                if field in change:
                    link[field] = change[field]
            link["source_type_api_name"] = source_name
            link["target_type_api_name"] = target_name
            continue

        if operation == "set_derived_property":
            object_type_name = change["object_type_api_name"]
            path = f"derived_property:{object_type_name}:{api_name}"
            object_type = next((item for item in object_types if item["api_name"] == object_type_name), None)
            if object_type is None:
                errors.append({"path": path, "message": "派生属性所属对象类型不存在"})
                continue
            existing = next((item for item in object_type["properties"] if item["api_name"] == api_name), None)
            if existing is not None and not existing.get("options", {}).get("derived_property"):
                errors.append({"path": path, "message": "该 API 名已被原生属性占用"})
                continue
            definition = {key: value for key, value in change.items() if key != "op"}
            errors.extend(validate_definition(result, definition))
            target = next(
                (item for item in result["object_types"] if item["api_name"] == _path_target_type(result, definition)),
                None,
            )
            terminal = next(
                (item for item in (target or {}).get("properties", []) if item["api_name"] == definition["terminal_property_api_name"]),
                None,
            )
            derived_property = {
                "api_name": api_name,
                "display_name": change["display_name"],
                "data_type": change["data_type"],
                "required": False,
                "editable": False,
                "unique_value": False,
                "sensitive": bool((terminal or {}).get("sensitive", False)),
                "options": {"derived_property": definition},
            }
            if existing is None:
                object_type["properties"].append(derived_property)
            else:
                object_type["properties"] = [
                    derived_property if item["api_name"] == api_name else item for item in object_type["properties"]
                ]
            continue

        if operation == "remove_derived_property":
            object_type = next((item for item in object_types if item["api_name"] == change["object_type_api_name"]), None)
            prop = next((item for item in (object_type or {}).get("properties", []) if item["api_name"] == api_name), None)
            path = f"derived_property:{change['object_type_api_name']}:{api_name}"
            if prop is None or not prop.get("options", {}).get("derived_property"):
                errors.append({"path": path, "message": "待删除的派生属性不存在"})
                continue
            object_type["properties"] = [item for item in object_type["properties"] if item["api_name"] != api_name]
            continue

        if operation == "add_action":
            path = f"action:{api_name}"
            object_type_name = change["object_type_api_name"]
            object_type = next((item for item in object_types if item["api_name"] == object_type_name), None)
            if any(item["api_name"] == api_name for item in actions):
                errors.append({"path": path, "message": "Action API 名已存在"})
                continue
            if object_type is None:
                errors.append({"path": path, "message": "Action 目标对象类型不存在"})
                continue
            property_names = {item["api_name"] for item in object_type["properties"]}
            allowed_properties = change.get("allowed_properties", [])
            unknown_properties = set(allowed_properties) - property_names
            if unknown_properties:
                errors.append({"path": path, "message": f"Action 引用了未定义属性：{', '.join(sorted(unknown_properties))}"})
                continue
            parameters_schema = change.get("parameters_schema", {})
            if not set(parameters_schema).issubset(set(allowed_properties)):
                errors.append({"path": path, "message": "Action 参数必须对应可修改的对象属性"})
                continue
            try:
                validate_submission_criteria(
                    change.get("submission_criteria", {}),
                    property_names=property_names,
                    parameter_names=set(parameters_schema) or set(allowed_properties),
                )
            except HTTPException as exc:
                errors.append({"path": path, "message": str(exc.detail)})
                continue
            actions.append(
                {
                    "api_name": api_name,
                    "display_name": change["display_name"],
                    "description": change.get("description", ""),
                    "object_type_api_name": object_type_name,
                    "allowed_properties": allowed_properties,
                    "parameters_schema": parameters_schema,
                    "submission_criteria": change.get("submission_criteria", {}),
                    "enabled": change.get("enabled", True),
                }
            )
            continue

        if operation == "update_action":
            path = f"action:{api_name}"
            action = next((item for item in actions if item["api_name"] == api_name), None)
            if action is None:
                errors.append({"path": path, "message": "待修改的 Action 不存在"})
                continue
            object_type_name = action["object_type_api_name"]
            if not any(item["api_name"] == object_type_name for item in object_types):
                errors.append({"path": path, "message": "Action 目标对象类型不存在"})
                continue
            for field in (
                "display_name",
                "description",
                "allowed_properties",
                "parameters_schema",
                "submission_criteria",
                "enabled",
            ):
                if field in change:
                    action[field] = change[field]
            continue

        errors.append({"path": "change", "message": f"不支持的本体变更类型：{operation}"})

    for object_type in object_types:
        property_names = {item["api_name"] for item in object_type.get("properties", [])}
        primary_key = object_type.get("primary_key_property")
        title_key = object_type.get("title_key_property", primary_key)
        if primary_key not in property_names:
            errors.append({"path": f"object_type:{object_type['api_name']}", "message": "主键必须引用已定义属性"})
        if title_key not in property_names:
            errors.append({"path": f"object_type:{object_type['api_name']}", "message": "标题键必须引用已定义属性"})

    object_type_by_name = {item["api_name"]: item for item in object_types}
    for action in actions:
        path = f"action:{action['api_name']}"
        object_type = object_type_by_name.get(action["object_type_api_name"])
        if object_type is None:
            errors.append({"path": path, "message": "Action 目标对象类型不存在"})
            continue
        property_names = {item["api_name"] for item in object_type["properties"]}
        allowed_properties = set(action["allowed_properties"])
        unknown_properties = allowed_properties - property_names
        if unknown_properties:
            errors.append({"path": path, "message": f"Action 引用了未定义属性：{', '.join(sorted(unknown_properties))}"})
        if not set(action["parameters_schema"]).issubset(allowed_properties):
            errors.append({"path": path, "message": "Action 参数必须对应可修改的对象属性"})
        try:
            validate_submission_criteria(
                action.get("submission_criteria", {}),
                property_names=property_names,
                parameter_names=set(action["parameters_schema"]) or allowed_properties,
            )
        except HTTPException as exc:
            errors.append({"path": path, "message": str(exc.detail)})

    return result, {"errors": errors, "warnings": warnings, "valid": not errors}


def resource_key_for_change(change: dict[str, Any]) -> str:
    operation = change.get("op")
    if operation == "add_object_type":
        return f"object_type:{change['api_name']}"
    if operation == "add_property":
        return f"property:{change['object_type_api_name']}.{change['api_name']}"
    if operation == "update_object_type":
        return f"object_type:{change['api_name']}"
    if operation == "update_property":
        return f"property:{change['object_type_api_name']}.{change['api_name']}"
    if operation == "add_link_type":
        return f"link_type:{change['api_name']}"
    if operation == "update_link_type":
        return f"link_type:{change['api_name']}"
    if operation == "add_action":
        return f"action:{change['api_name']}"
    if operation == "update_action":
        return f"action:{change['api_name']}"
    if operation in {"set_derived_property", "remove_derived_property"}:
        return f"derived_property:{change['object_type_api_name']}:{change['api_name']}"
    return f"resource:{change.get('api_name', 'unknown')}"


def _path_target_type(snapshot: dict[str, Any], definition: dict[str, Any]) -> str | None:
    links = {item["api_name"]: item for item in snapshot.get("link_types", [])}
    current = definition.get("object_type_api_name")
    for step in definition.get("path", []):
        link = links.get(step.get("link_api_name"))
        if link is None:
            return None
        current = link.get("target_type_api_name") if step.get("direction") == "outgoing" else link.get("source_type_api_name")
    return current


def require_branch(session: Session, branch_id: UUID, *, active: bool = False) -> OntologyBranch:
    branch = session.get(OntologyBranch, branch_id)
    if branch is None:
        raise HTTPException(status_code=404, detail="本体分支不存在")
    if active and branch.status != "active":
        raise HTTPException(status_code=409, detail="只有活动分支可以继续修改")
    return branch
