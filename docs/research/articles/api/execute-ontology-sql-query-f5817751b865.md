<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/sql-queries-v2-resources/sql-queries/execute-ontology-sql-query -->
<!-- 研读状态：已完成 -->

# Execute Ontology Sql Query • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/sql-queries-v2-resources/sql-queries/execute-ontology-sql-query)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/sql-queries-v2-resources/sql-queries
- 相关性：direct；Ontology SQL API 参考
- 官方更新时间：2026-11-12T17:46:46.922Z
- 目录核对时间：2026-11-14T14:55:28Z
- 产品状态：Preview；端点可变更或移除，调用需 `preview=true`

## 英文原文短摘录（每个来源不超过 25 词）

> “This endpoint is in preview and may be modified or removed at any time.”

## 摘录译文

此端点处于 Preview 阶段，可能随时修改或移除。

## 中文要点

- `POST /api/v2/sqlQueries/executeOntology?preview=true` 同步执行面向 Ontology 的 SQL，结果以 Apache Arrow 格式返回。OAuth2 客户端需要 `api:sql-queries-execute` 与 `api:ontologies-read` 两个 scope。
- 请求体包含 SQL 字符串，可选参数支持位置参数或命名映射；`rowLimit` 限定返回行数，`dryRun=true` 只解析/校验不执行。
- 可选指定 branch、scenarioRid 和 ontologyIdentifier（RID 或 API 名）；使用 `tableProviders` 时必须同时提供 ontologyIdentifier。
- 文档列出关键限制与错误：查询涉及 OSv1 索引对象类型/链接时报不兼容错误；跨 join/链接/子查询对象集过大时报错；结果字符串单元格过长也会失败。故此接口存在明确执行边界。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Ontology SQL | 本体 SQL | 以本体对象类型/链接为语义层的数据查询 |
| Apache Arrow | Apache Arrow | 同步结果的数据交换格式 |
| dryRun | 试运行校验 | 仅解析和验证 SQL，不实际执行 |
| tableProviders | 表提供者映射 | 将 SQL 表名映射到对象集，需要 ontologyIdentifier |
| scenarioRid | 场景 RID | 指定查询读取的本体场景上下文 |

## 疑问与待验证项

- 接口仍为 Preview，语法、返回编码和限制可能变化，不适合在复刻版作为稳定兼容承诺。
- 响应文档只列 `body: string`，同时描述 Arrow 格式；需以实际 HTTP Content-Type/SDK 解码方式为准。
- rowLimit 的服务端默认、最大值、Arrow 大结果体积限制及 dryRun 可校验范围未在此页完整说明。

## 复刻启示

- SQL 查询应默认只读、受控解析并限制扫描量、join 扇出、行数与单元格大小；预览模式明确标识为不稳定能力。
- 分支、场景和本体标识应作为执行上下文写入审计；Agent 运行时只提供批准的 schema/查询入口，不让模型直接拼装无限制 SQL。
- 对画布派生推理与 SQL 分析分别呈现：前者可解释关系链，后者展示执行计划/数据范围和 Arrow 结果摘要。
