<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/v1/ontology-resources/query-types/get-query-type -->
<!-- 研读状态：已完成 -->

# Get Query Type (v1) • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/v1/ontology-resources/query-types/get-query-type)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/v1/ontology-resources
- 相关性：direct；Ontology API v1 查询类型元数据读取接口；保留作兼容性对照，并优先关注 v2
- 官方更新时间：2026-11-12T17:46:46.923Z
- 目录核对时间：2026-11-14T14:55:59Z
- 产品状态：待核对 Beta、预览、弃用或更名信息；本页未标注 Preview

## 英文原文短摘录（每个来源不超过 25 词）

> “Gets a specific query type with the given API name.”

## 摘录译文

按给定的 API 名称获取一个具体查询类型。

## 中文要点

- 端点：`GET /api/v1/ontologies/{ontologyRid}/queryTypes/{queryApiName}`。OAuth 第三方客户端需要 `api:ontologies-read`。
- 查询类型描述的是可执行查询的接口契约。响应可含 `apiName`、显示名、描述、参数映射、输出类型、Function `rid` 和 `version`；参数、描述、显示名和输出可选。
- `rid` 指向 Function，可供其他 Foundry API 使用；版本采用 `major.minor.patch`，可带 `-rc1` 等预发布标签。示例响应的 `output` 可以是 `Array<OntologyObject<Employee>>`，所以调用端不能只按标量处理。
- 查询 `ontologyRid` 可从本体列表接口取得；`queryApiName` 可从查询类型列表接口取得，或在 Ontology Manager 中查看。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Query type | 查询类型 | 暴露查询的名称、输入参数和输出契约 |
| Function RID | 函数资源标识符 | 与 Function 资源关联的唯一 RID |
| Output type | 输出类型 | 可能为原始类型、数组或本体对象 |
| Prerelease tag | 预发布标签 | 版本号中的可选 `-tag`，如 `-rc1` |

## 疑问与待验证项

- 页面只说明元数据读取，没有说明该版本与线上实际执行实现之间的发布、回滚或兼容性约束；需要结合 Query Type 发布与 Execute Query 文档验证。
- `parameters` 与 `output` 的嵌套结构应以 schema/OpenAPI 为准；手工实现时不能把示例 JSON 当成穷尽的联合类型清单。
- v1 路径不携带分支参数。需要在 v2 对照卡中核实分支、场景或版本上下文是否可查询。

## 复刻启示

- 将查询定义建模为带稳定 API 名称、语义版本、输入参数 schema、输出 schema 和实现引用的独立资产；不要把查询类型和某次执行记录合并。
- 元数据面板可同时展示“契约”和 Function RID，执行日志另存输入摘要、分支/版本、调用者、耗时及结果状态。
- 本地替代产品应显式处理数组、对象集和多态输出，并在更改参数/输出契约时提供兼容性检查。该设计启示是基于 API 字段的复刻推论，不是 Palantir 对内部实现的说明。
