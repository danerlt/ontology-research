<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/queries/query-basics -->
<!-- 研读状态：已完成 -->

# Query basics (v2, latest) • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/queries/query-basics)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/v2/ontologies-v2-resources
- 相关性：direct；Ontology REST API v2 参考
- 官方更新时间：2026-11-12T17:46:46.922Z
- 目录核对时间：2026-11-14T14:57:48Z
- 产品状态：常规 v2 概念页；Query Function 是其创建入口。

## 英文原文短摘录（每个来源不超过 25 词）

> “A query type represents a logic that can be run in the Ontology.”

## 摘录译文

Query Type 表示一段可在 Ontology 中运行的逻辑。

## 中文要点

- Query Type 表示可在 Ontology 中运行的逻辑；该页指出通过 Query Functions 创建。
- 它是一个可被执行的查询/函数定义，不是对象类型，也不是 Action Type；具体参数和输出要查看 Query Type schema 与 Execute Query。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Query Type | 查询类型 | 可在本体中执行的逻辑定义。 |
| Query Function | 查询函数 | 创建 Query Type 的产品能力。 |
| Execute Query | 执行查询 | 按参数运行查询定义的 API。 |

## 疑问与待验证项

- 本页没有解释 Query Functions 与普通 Functions/Query Type 的版本或发布流程差别。
- 输入输出类型、权限上下文和执行限制需要对应 API 与用户文档确认。

## 复刻启示

- 把 Query Type 建模为单独的可版本化逻辑资源，并关联参数、输出类型及其引用的对象/接口。
- 画布将查询逻辑与数据结构节点区分；试算面板记录使用的版本和情景。
