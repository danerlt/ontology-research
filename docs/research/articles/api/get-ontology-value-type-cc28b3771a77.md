<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/ontology-value-types/get-ontology-value-type -->
<!-- 研读状态：已完成 -->

# Get Ontology Value Type • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/ontology-value-types/get-ontology-value-type)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/v2/ontologies-v2-resources
- 相关性：direct；Ontology REST API v2 参考
- 官方更新时间：2026-11-12T17:46:46.922Z
- 目录核对时间：2026-11-14T14:57:38Z
- 产品状态：预览（Preview；请求需显式启用 `preview=true`）

## 英文原文短摘录（每个来源不超过 25 词）

> “Gets a specific value type with the given API name.”

## 摘录译文

按 API 名称获取指定值类型。

## 中文要点

- 端点按本体与值类型 API 名称读取自定义 Ontology Value Type，返回 API 名称、显示名、描述、RID、状态、字段类型、版本和约束。
- 状态目前列出 ACTIVE 与 DEPRECATED；`fieldType` 为联合类型，`constraints` 可表达具体取值限制。
- 此端点处于 Preview，必须显式 `preview=true`；第三方 OAuth 应用需要 `api:ontologies-read`。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Value type | 值类型 | 自定义本体字段类型定义 |
| Field type | 字段类型 | 值类型基础数据类型的联合定义 |
| Constraint | 约束 | 对字段取值施加的限制 |
| Deprecated | 已弃用 | 不宜作为新字段定义的状态 |

## 疑问与待验证项

- 字段约束的种类、组合语义和版本兼容策略要继续看 ValueTypeConstraint 的子结构与用户指南。
- 当旧版本值类型改为 DEPRECATED 后，既有对象值如何解释和迁移，API 页未说明。

## 复刻启示

- 若本地支持自定义字段类型，应把 `fieldType` 与约束作为版本化 Schema 资源，并在画布属性节点展示约束摘要。
- Preview API 外置在适配层，定义评审时校验值类型版本与已有属性/数据的兼容性。
