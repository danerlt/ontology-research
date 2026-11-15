<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/v1/ontology-resources/queries/query-basics -->
<!-- 研读状态：已完成 -->

# Query basics (v1) • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/v1/ontology-resources/queries/query-basics)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/v1/ontology-resources
- 相关性：direct；Ontology API v1 查询概念参考，保留兼容性对照并优先关注 v2
- 官方更新时间：2026-11-12T17:46:46.923Z
- 目录核对时间：2026-11-14T14:55:59Z
- 产品状态：基础概念页；查询逻辑通过 Query Functions 创建

## 英文原文短摘录（每个来源不超过 25 词）

> “Query types can be created using Query Functions.”

## 摘录译文

Query Type 可以通过 Query Function 创建。

## 中文要点

- Query Type 表示在本体中执行的一段逻辑，创建入口为 Query Functions。
- 基础页没有展开 Query Function 的编辑、验证、发布与版本过程；相邻 REST API 将 Query Type 作为具有参数、输出和版本的可调用资源。
- 与 `/api/v1/ontology-resources/queries` 根路径内容一致；页面目录保留独立子页地址，但概念不应重复建模。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Query Function | 查询函数 | 创建可执行 Query Type 的函数入口 |
| Query Type | 查询类型 | 查询逻辑的命名/调用契约 |
| Query Function output | 查询函数输出 | 逻辑运行结果的类型定义 |

## 疑问与待验证项

- Query Function 的输入/输出类型支持集与部署约束需要函数文档补充。
- 此基础页没有说明查询成本/缓存；运行成本应通过平台查询用量文档和实际服务测量确认。

## 复刻启示

- 管理器从 Function 定义产生 Query Type，但在发布时验证契约兼容、授权和依赖图，保存发布快照。
- Agent 的可调用目录只纳入明确授权的查询类型，不暴露底层任意 Function。
- 同一查询的函数实现和外部 Query API 名分层保存并做版本绑定，便于升级与回滚。
