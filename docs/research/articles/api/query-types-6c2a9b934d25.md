<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/v1/ontology-resources/query-types -->
<!-- 研读状态：已完成 -->

# Query Type basics (v1) • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/v1/ontology-resources/query-types)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/v1/ontology-resources
- 相关性：direct；Ontology API v1 查询类型基础页，保留兼容性对照并优先关注 v2
- 官方更新时间：2026-11-12T17:46:46.923Z
- 目录核对时间：2026-11-14T14:55:59Z
- 产品状态：概念页；与 Query Type basics 子页重复

## 英文原文短摘录（每个来源不超过 25 词）

> “A query type represents a logic that can be run in the Ontology.”

## 摘录译文

Query Type 表示一段可在本体中运行的逻辑。

## 中文要点

- Query Type 是可在本体运行的查询逻辑；通过 Query Functions 创建。该页面不提供单独的 REST 方法或参数 schema。
- v1 查询类型详情与列表 API 分别获取某个查询的参数/输出定义和一组查询类型；Execute Query 对目标 Query Type 执行。
- 本页与 `/query-types/query-type-basics` 子路由及其他版本路由的基础描述一致；按目录保留 URL，语义统一归为 Query Type 基础知识。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Query Type | 查询类型 | 可运行的命名查询逻辑 |
| Query Functions | 查询函数 | 构建 Query Type 的实现方式 |
| API name | API 名 | 从 REST/SDK 定位查询类型 |

## 疑问与待验证项

- 页面未说明函数发布与 Query Type 发布是否使用相同事务/版本号。
- 基础说明未涉及分支、稳定版选择、权限和调用审计，需对照各端点文档。

## 复刻启示

- 用统一查询定义 schema 管理多个路由/SDK 对接，支持 Query Type 名称、参数、输出、函数 RID、版本和权限。
- 同一语义文档可合并展示；每个原始来源仍单独存档，方便比较不同 API 版文档更新。
- 在可视化画布里，查询逻辑节点显示输入、输出与函数依赖，支持评审和试算。
