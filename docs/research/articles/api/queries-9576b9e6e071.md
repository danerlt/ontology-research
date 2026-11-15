<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/ontology-resources/queries -->
<!-- 研读状态：已完成 -->

# Query basics (v1) • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/ontology-resources/queries)
- 官方中文来源：尚未确认（配对状态：needs_review）
- 页面语言：英文
- 主题栏目：api/ontology-resources/queries
- 相关性：direct；Ontology API v1 查询概念参考，保留兼容性对照并优先关注 v2
- 官方更新时间：2026-11-12T17:46:46.923Z
- 目录核对时间：2026-11-14T14:55:22Z
- 产品状态：基础概念页；Query Type 由 Query Functions 创建

## 英文原文短摘录（每个来源不超过 25 词）

> “A query type represents a logic that can be run in the Ontology.”

## 摘录译文

Query Type 表示一段可在本体中运行的逻辑。

## 中文要点

- v1 查询基础页把 Query Type 定义为可在本体中运行的逻辑，并指出 Query Type 可用 Query Functions 创建。
- 概念页没有给出执行参数或输出 schema；列表/详情 API 提供命名、描述、输入参数、输出类型、RID 和版本等元数据，Execute Query 负责提交运行请求。
- Query Type 是查询逻辑定义，不等同于通用对象搜索过滤语法；它可以封装可复用的业务查询，并以稳定 API 名供应用调用。
- 当前页面是查询分组基础概念说明；详细的 Query Type 资源接口和运行流程应结合其相邻页面研读。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Query Type | 查询类型 | 可执行逻辑的本体资源 |
| Query Function | 查询函数 | 创建 Query Type 的逻辑实现方式 |
| Execute Query | 执行查询 | 以输入参数运行已定义的查询类型 |
| query schema | 查询契约 | 参数与输出类型定义 |

## 疑问与待验证项

- 基础页没有说明 Query Function 如何构建、部署或验证；需查看函数文档与 Ontology Manager 流程。
- v1/v2 Query Type 版本绑定和预发布版本选择策略需以各自 API 页面为准。
- 查询运行的超时、缓存与成本不在此概念页中说明。

## 复刻启示

- 将查询逻辑作为独立资源登记，存储参数/输出 schema、函数实现版本、发布状态和权限；Agent 按 schema 生成受约束工具调用。
- 本体画布中可视化 Query Type 的输入对象集、过滤依赖和输出类型，并支持对样例对象执行只读预览。
- 记录实际调用版本和参数摘要，使查询结果可复现且可纳入审计。
