<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/v2/sql-queries-v2-resources/sql-queries/execute-ontology-sql-query -->
<!-- 研读状态：已完成 -->

# Execute Ontology Sql Query • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/v2/sql-queries-v2-resources/sql-queries/execute-ontology-sql-query)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/v2/sql-queries-v2-resources
- 相关性：direct；Ontology SQL 同步执行接口
- 官方更新时间：2026-11-12T17:46:46.922Z
- 目录核对时间：2026-11-14T14:58:00Z
- 产品状态：Preview；请求需 `preview=true`，可能修改或移除

## 英文原文短摘录（每个来源不超过 25 词）

> “Results are returned synchronously in Apache Arrow format.”

## 摘录译文

结果以 Apache Arrow 格式同步返回。

## 中文要点

- 端点：`POST /api/v2/sqlQueries/executeOntology`。这是直接对本体执行只读 SQL 的同步 API，需 `preview=true`；第三方 OAuth 需要 `api:sql-queries-execute` 和 `api:ontologies-read`。
- 请求体包括必填 SQL `query`；可选参数可为具名映射或位置参数，`rowLimit` 控制返回行数，`dryRun` 默认 false、为 true 时只解析和校验；`branch` 默认 main，`scenarioRid` 可指定场景。
- 可选 `ontologyIdentifier` 接受本体 RID 或 API 名。`tableProviders` 可为 SQL 表名绑定 ObjectSet，但必须同时提供 `ontologyIdentifier`。
- 官方用户文档补充：Ontology SQL 只支持 Object Storage v2，最多返回 10,000 行，执行超时 20 秒；只读，不支持 INSERT/UPDATE/DELETE 与 schema DDL。API 搜索结果将版本化目录项解析到未版本化 URL，但契约内容一致。
- 典型错误包括 SQL 解析失败、OSv1 对象/链接不兼容、嵌套对象集过大、字符串单元格超限、对象类型不存在/不可见及权限拒绝。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Ontology SQL | 本体 SQL | 面向本体对象、链接和接口执行的只读查询 |
| Dry run | 试运行 | 解析和校验而不实际执行 |
| Table provider | 表提供器 | 将 SQL 表名映射到本体 ObjectSet |
| Apache Arrow | Apache Arrow | 同步查询结果格式 |
| Preview | 预览功能 | 此 API 可能随时变更或移除 |

## 疑问与待验证项

- API 页响应 schema 写作 `body: string`，而说明和用户文档称 Arrow 输出；具体 HTTP Content-Type、Arrow IPC 变体及客户端解码方式需核对 OpenAPI/SDK。
- `dryRun` 是否会使用与正式执行相同的权限和资源计划验证，文档未细分。
- 10,000 行上限、20 秒超时来自 Ontology SQL 使用文档；部署或调用客户端是否还有更严限制需另行确认。

## 复刻启示

- 将本体 SQL 作为单独只读查询通道，使用解析校验、行数限制、执行超时、授权检查和审计；不要借 SQL 通道绕过 Action 写入治理。
- 画布/推理可把 SQL 查询节点作为分析能力展示，但它与派生属性计算的确定性对象路径应分开建模，并保留 SQL 文本、参数、branch/scenario 上下文和结果版本。
- Preview 与 Arrow 契约应显式放进客户端能力矩阵；本地复刻应发布稳定版本的媒体类型和分页/结果截断约定。
