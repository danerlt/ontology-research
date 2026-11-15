<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/ontology-resources/query-types/query-type-basics -->
<!-- 研读状态：已完成 -->

# Query Type basics (v1) • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/ontology-resources/query-types/query-type-basics)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/ontology-resources/query-types
- 相关性：direct；Ontology API v1 查询概念参考，保留兼容性对照并优先关注 v2
- 官方更新时间：2026-11-12T17:46:46.923Z
- 目录核对时间：2026-11-14T14:55:27Z
- 产品状态：基础概念页；与查询分组根页、显式 v1 路由内容重叠

## 英文原文短摘录（每个来源不超过 25 词）

> “A query type represents a logic that can be run in the Ontology.”

## 摘录译文

Query Type 表示一段可以在本体中运行的逻辑。

## 中文要点

- Query Type 是可在本体上执行的命名逻辑；页面补充可由 Query Functions 创建。
- 此 URL 不带显式 `/v1`，但页面标题标为 v1；另外两个路由也承载相同基础概念。对功能差异没有证据，故按重复文档路径而非三类能力处理。
- 参数/输出 schema、版本与运行结果不在基础概念页定义，需由 List/Get Query Type 和 Execute Query API 补充。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Query Type | 查询类型 | 可运行的本体查询逻辑资源 |
| Query Function | 查询函数 | 创建 Query Type 的函数入口 |
| query type basics | 查询类型基础 | 概念介绍而非运行端点契约 |

## 疑问与待验证项

- 页面极简，没有说明实现函数如何发布、哪些输入/输出类型受支持或权限如何绑定。
- `/api/ontology-resources` 与 `/api/v1/ontology-resources` 路径之间的 canonical 关系需后续核对。

## 复刻启示

- UI 不应仅展示 Query Type 名称，还要关联参数 schema、输出 schema、实现函数、授权与发布版本。
- 目录层可把重复路由聚合成一个概念条目，同时保留官方来源记录和 REST API 版本标签。
- Agent 只能调用被授权的已发布逻辑，查询参数由 schema 校验，执行行为写入审计。
