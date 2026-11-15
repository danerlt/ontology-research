<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/v1/ontology-resources/queries/execute-query -->
<!-- 研读状态：已完成 -->

# Execute Query (v1) • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/v1/ontology-resources/queries/execute-query)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/v1/ontology-resources
- 相关性：direct；Ontology API v1 查询执行端点，保留兼容性对照并优先关注 v2
- 官方更新时间：2026-11-12T17:46:46.923Z
- 目录核对时间：2026-11-14T14:55:59Z
- 产品状态：页面未标注 Preview；v1 未暴露分支/版本参数

## 英文原文短摘录（每个来源不超过 25 词）

> “Optional parameters do not need to be supplied.”

## 摘录译文

可选参数无需提供。

## 中文要点

- `POST /api/v1/ontologies/{ontologyRid}/queries/{queryApiName}/execute` 以本体 RID 和 Query API 名运行查询；请求体 `parameters` 是参数 ID 到 `DataValue` 的映射，required=false 的输入可省略。
- 响应 `value` 为 any，可表示嵌套数组、结构体、对象集、对象引用、聚合、附件、时序引用等类型，各类型 JSON 编码不同。
- OAuth2 第三方客户端需要 `api:ontologies-read`。此 v1 端点不列 version、branch、transaction 或 scenario 参数；更完整的运行上下文在 v2 API 中提供。
- 由于返回字段不具备固定静态类型，调用方需结合 Query Type output schema 解码，不能只依据示例中的数组输出。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| ExecuteQueryRequest | 查询执行请求 | 参数映射封装 |
| DataValue | 本体数据值 | 按类型采用不同 JSON 表示，支持嵌套 |
| ExecuteQueryResponse | 查询执行响应 | `value` 可能是任意受支持本体值 |
| Query API name | 查询 API 名 | 标识运行的查询逻辑 |

## 疑问与待验证项

- `value: any` 的具体 schema 应从 Get Query Type 读取；本页未说缺少 output 定义时的运行行为。
- v1 同步执行的超时、缓存、限流、取消能力和超大对象集如何编码未说明。
- 同一路径在旧/新 REST 文档版的 DataValue 类型映射可能存在差异，应使用版本化 SDK 检查。

## 复刻启示

- 运行 API 必须绑定已审核发布的 Query Type 版本，并按 output schema 做结果校验和渲染。
- Agent 工具定义从参数 schema 生成，运行后记录调用用户、版本、参数摘要、耗时和来源对象集。
- 对象集等大返回类型需提供分页/摘要策略，避免将未知体量的 `any` 直接塞入模型上下文。
