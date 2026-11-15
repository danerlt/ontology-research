<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/query-types/get-query-type -->
<!-- 研读状态：已完成 -->

# Get Query Type (v2, latest) • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/query-types/get-query-type)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/v2/ontologies-v2-resources
- 相关性：direct；Ontology REST API v2 参考
- 官方更新时间：2026-11-12T17:46:46.922Z
- 目录核对时间：2026-11-14T14:57:50Z
- 产品状态：常规 v2 读取接口；可选 branch 为实验性功能。

## 英文原文短摘录（每个来源不超过 25 词）

> “Gets a specific query type with the given API name.”

## 摘录译文

按给定 API 名称获取一个指定 Query Type。

## 中文要点

- GET `/api/v2/ontologies/{ontology}/queryTypes/{queryApiName}` 读取查询定义，OAuth 需要 `api:ontologies-read`；可按版本获取，默认最新发布版本（可能为预发布版）。
- `QueryTypeV2` 包含 API 名称、描述、显示名、参数、输出、RID、版本及类型引用；可选 branch 读取分支元数据但为实验性功能。
- 响应将 RID 描述为 Function 的唯一资源标识，说明 Query Type 与 Function 注册/版本模型存在紧密关联。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| QueryTypeV2 | Query Type v2 结构 | 查询定义的 API 响应模型。 |
| output | 输出类型 | 查询结果的类型描述。 |
| typeReferences | 类型引用 | Query Type 使用的外部类型描述映射。 |
| RID | 资源标识符 | 文档说明此处为 Function 的唯一标识。 |

## 疑问与待验证项

- API 路由名为 queryTypes，但 RID 字段说明指向 Function；跨 API 关联时要以响应和类型注册数据核实。
- latest 可能包含预发布版本，版本读取必须能显式指定并展示当前选择。

## 复刻启示

- 在元模型中同时保存业务层 Query Type 与底层 Function RID/版本关联，避免丢失 API 语义和运行标识。
- 详情页明确标示查询参数、输出 schema、预发布标签和类型引用，为画布与 Agent 工具审核提供依据。
