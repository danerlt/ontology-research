import json
import math
from datetime import date, datetime
from typing import Any
from uuid import UUID

from fastapi import HTTPException
from sqlalchemy import String, cast, select
from sqlalchemy.orm import Session

from backend.ontology_service.app.models import ActionDefinition, ObjectRecord, ObjectType, PropertyDefinition
from backend.ontology_service.app.security import Actor
from backend.ontology_service.app.services.audit import record_audit


def validate_record_properties(
    session: Session,
    object_type: ObjectType,
    values: dict[str, Any],
    *,
    existing_object_id: UUID | None = None,
) -> dict[str, Any]:
    definitions = session.scalars(
        select(PropertyDefinition).where(PropertyDefinition.object_type_id == object_type.id)
    ).all()
    definitions_by_name = {definition.api_name: definition for definition in definitions}
    unknown_properties = set(values) - set(definitions_by_name)
    if unknown_properties:
        names = ", ".join(sorted(unknown_properties))
        raise HTTPException(status_code=422, detail=f"对象类型未定义这些属性：{names}")

    validated: dict[str, Any] = {}
    for definition in definitions:
        if definition.api_name not in values:
            if definition.required:
                raise HTTPException(
                    status_code=422,
                    detail=f"缺少必填属性：{definition.display_name}",
                )
            continue
        value = values[definition.api_name]
        if value is None:
            if definition.required:
                raise HTTPException(
                    status_code=422,
                    detail=f"必填属性不能为空：{definition.display_name}",
                )
            validated[definition.api_name] = None
            continue
        _validate_value(definition, value)
        if definition.unique_value:
            _ensure_unique_value(
                session,
                object_type,
                definition,
                value,
                existing_object_id=existing_object_id,
            )
        validated[definition.api_name] = value
    return validated


def execute_action(
    session: Session,
    action: ActionDefinition,
    object_record: ObjectRecord,
    parameters: dict[str, Any],
    *,
    expected_version: int,
    actor: Actor,
) -> ObjectRecord:
    if not action.enabled:
        raise HTTPException(status_code=409, detail="此 Action 已停用")
    if object_record.object_type_id != action.object_type_id:
        raise HTTPException(status_code=422, detail="Action 与对象类型不匹配")
    if object_record.version != expected_version:
        raise HTTPException(status_code=409, detail="对象已被其他操作更新，请刷新后重试")

    allowed = set(action.allowed_properties or [])
    supplied = set(parameters)
    if not supplied:
        raise HTTPException(status_code=422, detail="至少需要提供一个 Action 参数")
    if not supplied.issubset(allowed):
        names = ", ".join(sorted(supplied - allowed))
        raise HTTPException(status_code=422, detail=f"Action 不允许修改这些属性：{names}")

    parameter_schema = action.parameters_schema or {}
    if parameter_schema and not supplied.issubset(parameter_schema):
        names = ", ".join(sorted(supplied - set(parameter_schema)))
        raise HTTPException(status_code=422, detail=f"Action 未声明这些参数：{names}")
    missing_required = [
        name
        for name, definition in parameter_schema.items()
        if definition.get("required", False) and name not in parameters
    ]
    if missing_required:
        raise HTTPException(status_code=422, detail=f"缺少必填 Action 参数：{', '.join(missing_required)}")

    definitions = session.scalars(
        select(PropertyDefinition).where(PropertyDefinition.object_type_id == object_record.object_type_id)
    ).all()
    definitions_by_name = {definition.api_name: definition for definition in definitions}
    changes: dict[str, dict[str, Any]] = {}
    next_properties = dict(object_record.properties)
    for name, value in parameters.items():
        definition = definitions_by_name.get(name)
        if definition is None:
            raise HTTPException(status_code=422, detail=f"对象类型未定义属性：{name}")
        if not definition.editable:
            raise HTTPException(status_code=403, detail=f"属性不可编辑：{definition.display_name}")
        if value is None and definition.required:
            raise HTTPException(status_code=422, detail=f"必填属性不能为空：{definition.display_name}")
        if value is not None:
            _validate_value(definition, value)
            if definition.unique_value:
                _ensure_unique_value(
                    session,
                    object_record.object_type,
                    definition,
                    value,
                    existing_object_id=object_record.id,
                )
        if definition.sensitive:
            changes[name] = {"redacted": True}
        else:
            changes[name] = {"before": next_properties.get(name), "after": value}
        next_properties[name] = value

    try:
        with session.begin_nested():
            object_record.properties = next_properties
            object_record.version += 1
            record_audit(
                session,
                actor_id=actor.id,
                event_type="action.executed",
                resource_type="object",
                resource_id=object_record.id,
                details={
                    "action_api_name": action.api_name,
                    "changes": changes,
                    "version": object_record.version,
                },
            )
            session.flush()
    except HTTPException:
        raise
    session.commit()
    session.refresh(object_record)
    return object_record


def _validate_value(definition: PropertyDefinition, value: Any) -> None:
    data_type = definition.data_type
    valid = False
    if data_type == "string":
        valid = isinstance(value, str)
    elif data_type == "integer":
        valid = isinstance(value, int) and not isinstance(value, bool)
    elif data_type == "number":
        valid = isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(value)
    elif data_type == "boolean":
        valid = isinstance(value, bool)
    elif data_type == "date":
        if isinstance(value, str):
            try:
                date.fromisoformat(value)
                valid = True
            except ValueError:
                valid = False
    elif data_type == "datetime":
        if isinstance(value, str):
            try:
                datetime.fromisoformat(value.replace("Z", "+00:00"))
                valid = True
            except ValueError:
                valid = False
    elif data_type == "enum":
        choices = definition.options.get("choices", [])
        valid = isinstance(value, str) and value in choices
    elif data_type == "json":
        try:
            json.dumps(value, allow_nan=False)
            valid = True
        except (TypeError, ValueError):
            valid = False
    if not valid:
        raise HTTPException(status_code=422, detail=f"属性“{definition.display_name}”值类型不正确")


def _ensure_unique_value(
    session: Session,
    object_type: ObjectType,
    definition: PropertyDefinition,
    value: Any,
    *,
    existing_object_id: UUID | None,
) -> None:
    if isinstance(value, (dict, list)):
        raise HTTPException(status_code=422, detail="唯一属性只能使用简单值")
    property_value = cast(ObjectRecord.properties[definition.api_name].as_string(), String)
    statement = select(ObjectRecord.id).where(
        ObjectRecord.object_type_id == object_type.id,
        property_value == str(value),
    )
    if existing_object_id is not None:
        statement = statement.where(ObjectRecord.id != existing_object_id)
    if session.scalar(statement) is not None:
        raise HTTPException(status_code=409, detail=f"属性值必须唯一：{definition.display_name}")
