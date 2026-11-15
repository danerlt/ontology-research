from typing import Any


NUMERIC_TYPES = {"integer", "number"}
AGGREGATIONS = {"count", "sum", "average", "minimum", "maximum", "collect_list", "collect_set"}


def validate_definition(snapshot: dict[str, Any], definition: dict[str, Any]) -> list[dict[str, str]]:
    """Validate a declarative 1–3 hop path against a branch schema snapshot."""
    object_types = {item["api_name"]: item for item in snapshot.get("object_types", [])}
    links = {item["api_name"]: item for item in snapshot.get("link_types", [])}
    api_name = definition.get("api_name", "unknown")
    errors: list[dict[str, str]] = []
    object_type_name = definition.get("object_type_api_name")
    source_type = object_types.get(object_type_name)
    if source_type is None:
        return [{"path": f"derived_property:{object_type_name}:{api_name}", "message": "起始对象类型不存在"}]

    path = definition.get("path") or []
    resource_path = f"derived_property:{object_type_name}:{api_name}"
    if not 1 <= len(path) <= 3:
        errors.append({"path": resource_path, "message": "推理路径必须包含 1 到 3 个链接步骤"})
        return errors

    current_type = object_type_name
    requires_aggregation = False
    for index, step in enumerate(path, start=1):
        link = links.get(step.get("link_api_name"))
        if link is None:
            errors.append({"path": f"{resource_path}.path[{index}]", "message": "链接类型不存在"})
            return errors
        direction = step.get("direction")
        if direction == "outgoing":
            if link.get("source_type_api_name") != current_type:
                errors.append({"path": f"{resource_path}.path[{index}]", "message": "出向链接起点与上一步对象类型不连续"})
                return errors
            current_type = link.get("target_type_api_name")
            cardinality = link.get("source_cardinality", "many")
        elif direction == "incoming":
            if link.get("target_type_api_name") != current_type:
                errors.append({"path": f"{resource_path}.path[{index}]", "message": "入向链接终点与上一步对象类型不连续"})
                return errors
            current_type = link.get("source_type_api_name")
            cardinality = link.get("target_cardinality", "many")
        else:
            errors.append({"path": f"{resource_path}.path[{index}]", "message": "链接遍历方向无效"})
            return errors
        requires_aggregation |= cardinality == "many"

    target_type = object_types.get(current_type)
    terminal = next(
        (item for item in (target_type or {}).get("properties", []) if item.get("api_name") == definition.get("terminal_property_api_name")),
        None,
    )
    if terminal is None:
        errors.append({"path": resource_path, "message": "终点对象不存在指定原生属性"})
        return errors
    if terminal.get("options", {}).get("derived_property"):
        errors.append({"path": resource_path, "message": "首版推理路径的终点必须是原生属性"})

    aggregation = definition.get("aggregation")
    result_type = definition.get("data_type")
    if requires_aggregation and aggregation is None:
        errors.append({"path": resource_path, "message": "路径存在多对象链接，必须选择聚合器"})
    if aggregation not in AGGREGATIONS and aggregation is not None:
        errors.append({"path": resource_path, "message": "不支持此聚合器"})
    if aggregation == "count" and result_type != "integer":
        errors.append({"path": resource_path, "message": "count 的结果类型必须是 integer"})
    elif aggregation in {"sum", "average", "minimum", "maximum"}:
        if terminal.get("data_type") not in NUMERIC_TYPES:
            errors.append({"path": resource_path, "message": "数值聚合器只能用于 integer 或 number 属性"})
        if result_type != "number":
            errors.append({"path": resource_path, "message": "数值聚合器的结果类型必须是 number"})
    elif aggregation in {"collect_list", "collect_set"} and result_type != "json":
        errors.append({"path": resource_path, "message": "集合聚合器的结果类型必须是 json"})
    elif aggregation is None and result_type != terminal.get("data_type"):
        errors.append({"path": resource_path, "message": "未使用聚合器时，结果类型必须与终点属性类型一致"})

    return errors
