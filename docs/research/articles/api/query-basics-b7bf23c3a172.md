<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/queries/query-basics -->
<!-- 研读状态：已完成 -->

# Query basics (v2, latest) • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/queries/query-basics)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/ontologies-v2-resources/queries
- 相关性：direct；Ontology REST API v2 参考
- 官方更新时间：2026-11-12T17:46:46.922Z
- 目录核对时间：2026-11-14T14:54:25Z
- 产品状态：Ontology REST API v2 概念页；正文与同主题父路由重复

## 英文原文短摘录（每个来源不超过 25 词）

> “Query types can be created using Query Functions.”

## 摘录译文

Query Type 可通过 Query Functions 创建。

## 中文要点

- 本页与 `/queries` 父路由内容相同，解释 Query Type 是本体中可运行的逻辑，并由 Query Functions 创建。
- 该说明把查询能力定位为 Ontology 中可发布、可执行的业务逻辑资源，而非任意用户编写的临时查询文本。参数、输出形状和发布版本可进一步通过 Query Type 元数据端点查询。
- 本页本身没有运行接口、版本参数和响应定义；具体契约应看 Execute Query API，避免把简短概念页误作完整技术规范。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| `Query Type` | 查询类型 | Query Function 生成并可在本体中运行的逻辑接口。 |
| `Query Function` | 查询函数 | 创建查询逻辑与参数/返回值定义的函数资源。 |
| `API name` | API 名称 | 调用端点和 SDK 中用于稳定识别查询的名称。 |
| `Published version` | 已发布版本 | Execute Query 默认选取的最近发布版本。 |

## 疑问与待验证项

- 该卡记录的是重复路由的页面正文；它不增加父页面之外的独立接口行为。
- 创建 Query Function 的运行环境、发布流程、缓存/一致性和执行成本未在本页说明，需结合专门文档。

## 复刻启示

- 查询编辑器中明确展示逻辑定义、参数、返回类型和发布版本，使可执行查询与对象类型/属性 schema 有清晰边界。
- 对有相同内容的导航 URL 使用 canonical 页面/主题关联以减少维护重复，同时在资料目录中保留每个官方入口的逐篇研读卡。
- Agent 生成调用计划时只能调用已登记 Query Type，先读取类型描述再构造参数，不直接拼接未经校验的接口请求。
