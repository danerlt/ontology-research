<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/v1/ontology-resources/object-types/get-object-type -->
<!-- 研读状态：已完成 -->

# Get Object Type (v1) • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/v1/ontology-resources/object-types/get-object-type)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/v1/ontology-resources
- 相关性：direct；Ontology API v1 端点参考；保留作兼容性对照，并优先关注 v2
- 官方更新时间：2026-11-12T17:46:46.922Z
- 目录核对时间：2026-11-14T14:55:41Z
- 产品状态：正式 API（页面未标注 Preview）

## 英文原文短摘录（每个来源不超过 25 词）

> “Gets a specific object type with the given API name.”

## 摘录译文

按 API 名称获取指定对象类型。

## 中文要点

- v1 路径使用 ontology RID 与对象类型 API 名称读取对象类型。
- 响应包含 API 名称、名称/描述、发布状态、建议可见性、属性映射、RID；`primaryKey` 是属性 API 名称列表。
- 响应还包含 `legacyObjectTypeId`，官方明确称其为旧标识且不建议新应用使用。此 v1 页面没有 branch、titleProperty 或 includeDatasources 参数。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Legacy object type ID | 旧对象类型 ID | 兼容字段，官方不建议新应用依赖 |
| Primary key | 主键 | v1 响应为属性名列表 |
| Properties map | 属性映射 | 对象类型公开的属性定义 |
| Status | 发布状态 | ACTIVE、ENDORSED、EXPERIMENTAL、DEPRECATED |

## 疑问与待验证项

- v1 的主键列表是否兼容复合主键，字段结构支持列表但编码限制未在此页说明。
- v1 API 没有单独返回 `titleProperty`，应用是否要自行选择展示属性需结合 SDK 和本体 UI 文档核实。

## 复刻启示

- 保留 v1 作为兼容读取路径，但内部域模型以 RID/API name 等稳定资源标识为主，不把 legacyObjectTypeId 用作新外键。
- 适配器需将 v1 主键列表与 v2 主键字段规范化为内部表示，同时保留来源 API 版本，避免丢失语义。
