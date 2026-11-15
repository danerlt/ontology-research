<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/queries -->
<!-- 研读状态：已完成 -->

# Query basics (v2, latest) • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/queries)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/v2/ontologies-v2-resources
- 相关性：direct；Ontology REST API v2 查询资源分组入口
- 官方更新时间：2026-11-12T17:46:46.922Z
- 目录核对时间：2026-11-14T14:57:45Z
- 产品状态：分组入口未标注 Preview；查询执行状态以具体端点为准

## 英文原文短摘录（每个来源不超过 25 词）

> “Query basics”

## 摘录译文

查询基础

## 中文要点

- 该路由是 REST API v2 Queries 分组入口，正文不能独立读取。官方导航将 Query basics 和 Execute Query 编在此组，二者分别描述查询执行契约和实际执行端点。
- 在本体资源模型中，“查询定义/查询类型”和“某次查询执行”应区分：前者提供参数与结果 schema，后者带具体输入并返回一次结果。
- 本卡只概览路由分类；参数、输入/输出格式、分支/场景上下文和响应限制需以 Query basics 与 Execute Query 子页为准。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Query | 查询 | 执行一段本体查询逻辑的操作 |
| Query type | 查询类型 | 查询接口定义及参数/输出契约 |
| Execute Query | 执行查询 | 以输入参数运行查询并取结果 |
| Query result | 查询结果 | 某次执行返回的数据 |

## 疑问与待验证项

- 分组信息来自官方[v2 Ontology API 导航](https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources)；目录入口没有独立说明查询版本绑定与缓存语义。
- 查询是可复用的已发布定义还是临时表达式，要从各具体 Query API 页面区分。
- 执行结果是否保证快照一致性、分页/流式策略如何选择，不能从 `Queries` 分组本身推断。

## 复刻启示

- 将查询定义、输入参数、执行实例和结果分页分成不同资源，持久保存 schema 版本与执行上下文。
- Agent 工具应从查询契约生成参数表单/schema，而执行日志则独立记录参数摘要、用户、项目、本体版本和结果引用。
- 画布可把 Query 作为可执行工具节点连到对象集/对象类型，但不要将其画成本体 schema 边。
