<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/ontology-resources/queries/query-basics -->
<!-- 研读状态：已完成 -->

# Query basics (v1) • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/ontology-resources/queries/query-basics)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/ontology-resources/queries
- 相关性：direct；Ontology API v1 概念参考，保留兼容性对照并优先关注 v2
- 官方更新时间：2026-11-12T17:46:46.923Z
- 目录核对时间：2026-11-14T14:55:22Z
- 产品状态：基础概念页；定义与同组 Query Type 页面一致

## 英文原文短摘录（每个来源不超过 25 词）

> “Query types can be created using Query Functions.”

## 摘录译文

Query Type 可以通过 Query Function 创建。

## 中文要点

- Query Type 表示一段可在本体中运行的逻辑，创建入口是 Query Functions。它为可复用查询逻辑提供命名资源和参数/输出契约。
- 本页是概念说明，不包含具体执行 endpoint；按名称读取其 schema 用 Get Query Type，枚举用 List Query Types，带参数执行用 Execute Query。
- 概念页未说明 Query Function 的实现和部署过程，也不表示任意函数都会自动成为对外可执行查询；需依相邻函数与 Ontology Manager 文档核实。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Query Type | 查询类型 | 可在本体中执行的逻辑资源 |
| Query Function | 查询函数 | 创建 Query Type 的函数实现入口 |
| query logic | 查询逻辑 | 对外可复用的业务查询行为 |
| parameter contract | 参数契约 | 调用逻辑所需输入参数的 schema |

## 疑问与待验证项

- 页面没有描述 Query Function 的运行环境、权限、版本晋升与失败重试；需结合 Function 文档和运行 API 查看。
- “可以通过 Query Functions 创建”没有界定可用函数类型或复杂度限制。

## 复刻启示

- 区分查询定义、实现函数和执行记录三类资源；建立绑定关系并对定义版本进行不可变发布。
- 画布展示 Query Type 的输入参数、所依赖的对象/链接和输出节点，便于人审和 Agent 选用。
- 对外工具注册只暴露已发布且授权的 Query Type，Agent 不应直接获得任意数据库查询能力。
