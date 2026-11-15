from copy import deepcopy
from typing import Any
from uuid import UUID

from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session, selectinload

from backend.ontology_service.app.models import ActionDefinition, LinkType, ObjectType, Ontology, OntologyBranch


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
                "description": item.description,
                "primary_key_property": item.primary_key_property,
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
                    "description": change.get("description", ""),
                    "primary_key_property": primary_key,
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
                }
            )
            continue

        errors.append({"path": "change", "message": f"不支持的本体变更类型：{operation}"})

    return result, {"errors": errors, "warnings": warnings, "valid": not errors}


def resource_key_for_change(change: dict[str, Any]) -> str:
    operation = change.get("op")
    if operation == "add_object_type":
        return f"object_type:{change['api_name']}"
    if operation == "add_property":
        return f"property:{change['object_type_api_name']}.{change['api_name']}"
    if operation == "add_link_type":
        return f"link_type:{change['api_name']}"
    return f"resource:{change.get('api_name', 'unknown')}"


def require_branch(session: Session, branch_id: UUID, *, active: bool = False) -> OntologyBranch:
    branch = session.get(OntologyBranch, branch_id)
    if branch is None:
        raise HTTPException(status_code=404, detail="本体分支不存在")
    if active and branch.status != "active":
        raise HTTPException(status_code=409, detail="只有活动分支可以继续修改")
    return branch
