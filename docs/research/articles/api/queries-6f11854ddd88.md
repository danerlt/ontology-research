<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/queries -->
<!-- 研读状态：已完成 -->

# Query basics (v2, latest) • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/queries)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/ontologies-v2-resources/queries
- 相关性：direct；Ontology REST API v2 参考
- 官方更新时间：2026-11-12T17:46:46.922Z
- 目录核对时间：2026-11-14T14:54:25Z
- 产品状态：Ontology REST API v2 概念页；执行和元数据端点另有独立契约

## 英文原文短摘录（每个来源不超过 25 词）

> “A query type represents a logic that can be run in the Ontology.”

## 摘录译文

查询类型表示可在本体中运行的一段逻辑。

## 中文要点

- 本页说明 Query Type 是可在 Ontology 中运行的逻辑定义，可由 Query Functions 创建。
- 该页面是 REST API 查询主题的基础概念，不定义任意 SQL/搜索语句；具体运行方式由按 API 名调用的 Execute Query 端点承担，类型/参数信息由 Query Type 元数据端点描述。
- API 导航将查询与 Query Types 分列，说明“可执行查询逻辑”和“该逻辑的接口类型描述”是相互关联但职责不同的资源。
- 本路由与 `/queries/query-basics` 子路由展示相同的基础定义，属于内容重复的目录页；应保留两条目录入口，但设计说明可集中指向同一语义。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| `Query type` | 查询类型 | 在本体中可运行的逻辑及其输入/输出契约。 |
| `Query Function` | 查询函数 | 创建 Query Type 的一种 Foundry 函数资源。 |
| `Execute Query` | 执行查询 | 通过 API 名和参数执行已发布查询的端点。 |
| `Query Type metadata` | 查询类型元数据 | 描述 API 名、参数、输出类型及版本的资源信息。 |

## 疑问与待验证项

- 基础页没有定义 Query Function 的构建、测试、发布和依赖管理流程；需要结合 Query Functions 用户指南阅读。
- 路由重复但对应目录项各自计入本次 676 篇直接相关页面；避免把两个 URL 误认为两套不同的运行语义。

## 复刻启示

- 系统中将查询定义建模为有版本的可执行资源，并将参数 schema、输出 schema、实现函数 RID 和版本关联起来。
- 画布应以查询节点表达可复用业务逻辑，连线表示输入对象集/参数和输出类型；允许 Agent 调用前由工具目录读取该接口契约。
- 区分查询定义、查询执行实例、执行结果和查询类型元数据，避免把运行结果当作可编辑本体 schema。
