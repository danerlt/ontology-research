import json
import math
import re
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


def preview_action(
    session: Session,
    action: ActionDefinition,
    object_record: ObjectRecord,
    parameters: dict[str, Any],
    *,
    expected_version: int,
    actor: Actor,
) -> dict[str, Any]:
    _next_properties, _audit_changes, property_changes = _prepare_action(
        session,
        action,
        object_record,
        parameters,
        expected_version=expected_version,
        actor=actor,
    )
    return {
        "action_api_name": action.api_name,
        "object_id": object_record.id,
        "current_version": object_record.version,
        "next_version": object_record.version + 1,
        "property_changes": property_changes,
    }


def execute_action(
    session: Session,
    action: ActionDefinition,
    object_record: ObjectRecord,
    parameters: dict[str, Any],
    *,
    expected_version: int,
    actor: Actor,
) -> ObjectRecord:
    next_properties, audit_changes, _property_changes = _prepare_action(
        session,
        action,
        object_record,
        parameters,
        expected_version=expected_version,
        actor=actor,
    )
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
                    "changes": audit_changes,
                    "version": object_record.version,
                },
            )
            session.flush()
    except HTTPException:
        raise
    session.commit()
    session.refresh(object_record)
    return object_record


def _prepare_action(
    session: Session,
    action: ActionDefinition,
    object_record: ObjectRecord,
    parameters: dict[str, Any],
    *,
    expected_version: int,
    actor: Actor,
) -> tuple[dict[str, Any], dict[str, Any], list[dict[str, Any]]]:
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
    validate_submission_criteria(
        action.submission_criteria or {},
        property_names=set(definitions_by_name),
        parameter_names=set(parameter_schema) or allowed,
    )
    validated_parameters: dict[str, Any] = {}
    for name, value in parameters.items():
        definition = definitions_by_name.get(name)
        if definition is None:
            raise HTTPException(status_code=422, detail=f"对象类型未定义属性：{name}")
        if not definition.editable:
            raise HTTPException(status_code=403, detail=f"属性不可编辑：{definition.display_name}")
        if value is None:
            if definition.required:
                raise HTTPException(status_code=422, detail=f"必填属性不能为空：{definition.display_name}")
        else:
            schema = parameter_schema.get(name, {})
            _validate_parameter(name, value, schema)
            _validate_value(definition, value)
            if definition.unique_value:
                _ensure_unique_value(
                    session,
                    object_record.object_type,
                    definition,
                    value,
                    existing_object_id=object_record.id,
                )
        validated_parameters[name] = value

    if not _evaluate_submission_criteria(action.submission_criteria or {}, object_record, validated_parameters, actor):
        raise HTTPException(status_code=409, detail="未满足 Action 提交条件")

    audit_changes: dict[str, dict[str, Any]] = {}
    property_changes: list[dict[str, Any]] = []
    next_properties = dict(object_record.properties)
    for name, value in validated_parameters.items():
        definition = definitions_by_name.get(name)
        if definition.sensitive:
            audit_changes[name] = {"redacted": True}
            property_changes.append({"property": name, "before": "已隐藏", "after": "已隐藏", "sensitive": True})
        else:
            before = next_properties.get(name)
            audit_changes[name] = {"before": before, "after": value}
            property_changes.append({"property": name, "before": before, "after": value, "sensitive": False})
        next_properties[name] = value
    return next_properties, audit_changes, property_changes


def _validate_parameter(name: str, value: Any, schema: dict[str, Any]) -> None:
    expected_type = schema.get("type")
    type_checks = {
        "string": lambda item: isinstance(item, str),
        "integer": lambda item: isinstance(item, int) and not isinstance(item, bool),
        "number": lambda item: isinstance(item, (int, float)) and not isinstance(item, bool) and math.isfinite(item),
        "boolean": lambda item: isinstance(item, bool),
        "array": lambda item: isinstance(item, list),
        "object": lambda item: isinstance(item, dict),
    }
    if expected_type is not None and expected_type not in type_checks:
        raise HTTPException(status_code=422, detail=f"Action 参数配置了不支持的数据类型：{name}")
    if expected_type is not None and not type_checks[expected_type](value):
        raise HTTPException(status_code=422, detail=f"Action 参数类型不正确：{name}")
    if "enum" in schema and value not in schema["enum"]:
        raise HTTPException(status_code=422, detail=f"Action 参数不满足枚举约束：{name}")
    if "minimum" in schema or "maximum" in schema:
        if not isinstance(value, (int, float)) or isinstance(value, bool) or not math.isfinite(value):
            raise HTTPException(status_code=422, detail=f"Action 参数不满足数值约束：{name}")
        if "minimum" in schema and value < schema["minimum"]:
            raise HTTPException(status_code=422, detail=f"Action 参数小于最小值：{name}")
        if "maximum" in schema and value > schema["maximum"]:
            raise HTTPException(status_code=422, detail=f"Action 参数大于最大值：{name}")
    if "min_length" in schema or "max_length" in schema:
        if not isinstance(value, (str, list, dict)):
            raise HTTPException(status_code=422, detail=f"Action 参数不满足长度约束：{name}")
        if "min_length" in schema and len(value) < schema["min_length"]:
            raise HTTPException(status_code=422, detail=f"Action 参数短于最小长度：{name}")
        if "max_length" in schema and len(value) > schema["max_length"]:
            raise HTTPException(status_code=422, detail=f"Action 参数超过最大长度：{name}")
    if "pattern" in schema:
        if not isinstance(value, str):
            raise HTTPException(status_code=422, detail=f"Action 参数不满足格式约束：{name}")
        try:
            if re.fullmatch(schema["pattern"], value) is None:
                raise HTTPException(status_code=422, detail=f"Action 参数不满足格式约束：{name}")
        except re.error as exc:
            raise HTTPException(status_code=422, detail=f"Action 参数格式规则无效：{name}") from exc


def _evaluate_submission_criteria(
    criteria: Any,
    object_record: ObjectRecord,
    parameters: dict[str, Any],
    actor: Actor,
) -> bool:
    if not criteria:
        return True
    if not isinstance(criteria, dict):
        raise HTTPException(status_code=422, detail="Action 提交条件配置必须是对象")
    if "all" in criteria:
        clauses = criteria["all"]
        return isinstance(clauses, list) and bool(clauses) and all(
            _evaluate_submission_criteria(item, object_record, parameters, actor) for item in clauses
        )
    if "any" in criteria:
        clauses = criteria["any"]
        return isinstance(clauses, list) and bool(clauses) and any(
            _evaluate_submission_criteria(item, object_record, parameters, actor) for item in clauses
        )
    if "not" in criteria:
        return not _evaluate_submission_criteria(criteria["not"], object_record, parameters, actor)

    if "property" in criteria:
        actual = object_record.properties.get(criteria["property"])
    elif "parameter" in criteria:
        actual = parameters.get(criteria["parameter"])
    elif criteria.get("subject") == "actor_role":
        actual = actor.role
    else:
        raise HTTPException(status_code=422, detail="Action 提交条件缺少可判断的对象属性或参数")

    expected = criteria.get("value")
    operator = criteria.get("operator", "equals")
    if operator == "equals":
        return actual == expected
    if operator == "not_equals":
        return actual != expected
    if operator == "in":
        return isinstance(expected, list) and actual in expected
    if operator == "not_in":
        return isinstance(expected, list) and actual not in expected
    if operator in {"greater_than", "greater_than_or_equal", "less_than", "less_than_or_equal"}:
        try:
            if operator == "greater_than":
                return actual > expected
            if operator == "greater_than_or_equal":
                return actual >= expected
            if operator == "less_than":
                return actual < expected
            return actual <= expected
        except TypeError:
            return False
    if operator == "is_empty":
        return actual is None or actual == "" or actual == [] or actual == {}
    if operator == "not_empty":
        return not (actual is None or actual == "" or actual == [] or actual == {})
    raise HTTPException(status_code=422, detail=f"Action 提交条件使用不支持的比较方式：{operator}")


def validate_submission_criteria(
    criteria: Any,
    *,
    property_names: set[str],
    parameter_names: set[str],
    depth: int = 0,
) -> None:
    if criteria is None or (criteria == {} and depth == 0):
        return
    if criteria == {}:
        raise HTTPException(status_code=422, detail="Action 提交条件不能包含空子条件")
    if depth > 20:
        raise HTTPException(status_code=422, detail="Action 提交条件嵌套层级过深")
    if not isinstance(criteria, dict):
        raise HTTPException(status_code=422, detail="Action 提交条件配置必须是对象")

    logical_fields = set(criteria).intersection({"all", "any", "not"})
    if logical_fields:
        if len(logical_fields) != 1 or set(criteria) != logical_fields:
            raise HTTPException(status_code=422, detail="Action 逻辑条件只能包含一种组合运算")
        operator = next(iter(logical_fields))
        clauses = criteria[operator]
        if operator == "not":
            validate_submission_criteria(
                clauses,
                property_names=property_names,
                parameter_names=parameter_names,
                depth=depth + 1,
            )
            return
        if not isinstance(clauses, list) or not clauses or len(clauses) > 50:
            raise HTTPException(status_code=422, detail="Action 逻辑条件需要 1 到 50 条子条件")
        for clause in clauses:
            validate_submission_criteria(
                clause,
                property_names=property_names,
                parameter_names=parameter_names,
                depth=depth + 1,
            )
        return

    selectors = set(criteria).intersection({"property", "parameter", "subject"})
    if len(selectors) != 1:
        raise HTTPException(status_code=422, detail="Action 条件必须指定一个属性、参数或执行者角色")
    selector = next(iter(selectors))
    name = criteria[selector]
    if selector == "property" and name not in property_names:
        raise HTTPException(status_code=422, detail=f"Action 提交条件引用未定义属性：{name}")
    if selector == "parameter" and name not in parameter_names:
        raise HTTPException(status_code=422, detail=f"Action 提交条件引用未定义参数：{name}")
    if selector == "subject" and name != "actor_role":
        raise HTTPException(status_code=422, detail=f"Action 提交条件使用不支持的执行者字段：{name}")

    permitted = {selector, "operator", "value"}
    if not set(criteria).issubset(permitted):
        raise HTTPException(status_code=422, detail="Action 条件包含不支持的配置字段")
    operator = criteria.get("operator", "equals")
    operators = {
        "equals", "not_equals", "in", "not_in", "greater_than",
        "greater_than_or_equal", "less_than", "less_than_or_equal", "is_empty", "not_empty",
    }
    if operator not in operators:
        raise HTTPException(status_code=422, detail=f"Action 提交条件使用不支持的比较方式：{operator}")
    if operator in {"in", "not_in"} and not isinstance(criteria.get("value"), list):
        raise HTTPException(status_code=422, detail="Action 集合条件的 value 必须是数组")
    if operator in {"greater_than", "greater_than_or_equal", "less_than", "less_than_or_equal"}:
        value = criteria.get("value")
        if not isinstance(value, (int, float)) or isinstance(value, bool) or not math.isfinite(value):
            raise HTTPException(status_code=422, detail="Action 数值条件需要有限数字")


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
