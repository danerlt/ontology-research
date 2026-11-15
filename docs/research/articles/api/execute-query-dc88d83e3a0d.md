<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/ontology-resources/queries/execute-query -->
<!-- 研读状态：已完成 -->

# Execute Query (v1) • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/ontology-resources/queries/execute-query)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/ontology-resources/queries
- 相关性：direct；Ontology API v1 执行端点，保留兼容性对照并优先关注 v2
- 官方更新时间：2026-11-12T17:46:46.923Z
- 目录核对时间：2026-11-14T14:55:22Z
- 产品状态：页面未标注 Preview；v2 增加的版本/分支/场景参数需单独评估

## 英文原文短摘录（每个来源不超过 25 词）

> “Executes a Query using the given parameters.”

## 摘录译文

使用给定参数执行查询。

## 中文要点

- `POST /api/v1/ontologies/{ontologyRid}/queries/{queryApiName}/execute` 按本体 RID 与查询 API 名执行 Query；可选参数可以省略，请求体 `parameters` 是参数名到 `DataValue` 的映射。
- 成功响应为 `ExecuteQueryResponse.value`，类型概括为 `any`，可包含嵌套数组或结构体；页面枚举多种 JSON 编码，包括对象集/对象引用、附件引用、聚合结构、时序引用、decimal/long 字符串等。
- OAuth2 第三方调用需要 `api:ontologies-read`。v1 endpoint 本身未列版本、分支、事务或场景参数；较新的 v2 执行 API 增加了这些上下文选项，且部分属于实验能力。
- 参数和返回值需依据 Query Type 元数据及 DataValue 编码解释，不能把所有 `value` 都当成普通对象数组。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Execute Query | 执行查询 | 运行已定义 Query Type 的 REST 操作 |
| parameters | 参数映射 | 参数 API 名到对应数据值的映射 |
| DataValue | 本体数据值 | 可嵌套且依类型采用不同 JSON 编码 |
| scenario reference | 场景引用 | 可由查询输出包含的本体场景资源引用 |

## 疑问与待验证项

- 返回值 schema 为 `any`；客户端应使用 Get Query Type 的 output contract 解析，且应验证 API 名大小写和可选参数缺省规则。
- v1 文档未说明同步查询超时、缓存、分页/大对象集输出及取消执行能力。
- v1 与 v2 对 Date、Decimal、Long、对象集和时序引用的序列化差异需通过生成 SDK/OpenAPI 对照确认。

## 复刻启示

- 把 Query Type schema 与执行载荷分离；运行时按版本化 output schema 解码值，并把解析错误作为结构化错误报告。
- Agent 调用时基于参数 schema 生成 JSON Schema 工具定义，限制可调用 Query Type 的范围并审计输入摘要、版本、分支/场景和耗时。
- 结果视图按输出类型渲染对象集、结构体、聚合或附件引用；不要对不透明 `any` 做猜测性转换。
