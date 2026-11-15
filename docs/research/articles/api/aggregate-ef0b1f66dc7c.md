<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/ontology-resources/objects/aggregate -->
<!-- 研读状态：已完成 -->

# Aggregate Objects Details • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/ontology-resources/objects/aggregate)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/ontology-resources/objects
- 相关性：direct；Ontology API v1 聚合契约参考
- 官方更新时间：2026-11-12T17:46:46.922Z
- 目录核对时间：2026-11-14T14:54:58Z
- 产品状态：接口详情页；兼容性参考

## 英文原文短摘录（每个来源不超过 25 词）

> “Null values are ignored in aggregations.”

## 摘录译文

聚合计算会忽略空值。

## 中文要点

- 本页展开 `POST /api/v1/ontologies/{ontologyRid}/objects/{objectType}/aggregate` 的可用聚合与分组语义：`count`、`max`、`min`、`sum`、`avg`、`approximateDistinct`；分组支持 `exact`、`fixedWidth`、`ranges`、`duration`。
- 可组合多个聚合和多个 groupBy，并以 query 子句先筛选对象。响应逐组给出 metrics 与 group；超过分组上限时可用 `excludedItems` 观察被排除数量。
- Null 不进入聚合或分组，因此不会产生 null 指标或 null 组。`exact` 的 `maxGroupCount` 默认 10,000；ranges 左闭右开；duration 用 ISO 8601，日期只按天分组，timestamp 还支持小时、分钟、秒。
- `approximateDistinct` 是近似计数，不能作为精确唯一性约束或财务对账依据。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| aggregation | 聚合 | 对对象属性计算统计指标 |
| groupBy | 分组 | 按属性值、区间或时间间隔拆分结果 |
| approximateDistinct | 近似去重计数 | 估算不同属性值数量 |
| excludedItems | 被排除条目数 | 因分组上限未纳入输出的对象数量 |
| half-open interval | 左闭右开区间 | 范围包含起点 `gte`，不包含终点 `lt` |

## 疑问与待验证项

- 聚合结果的排序、跨页一致性以及多个分组维度的总基数上限应结合基础 endpoint 文档/环境验证。
- 近似 distinct 的误差范围和具体算法未在本页承诺；不可自行宣称精度保证。
- 对 null 的忽略语义可能导致分组计数之和小于筛选对象总数，UI 应明确提示。

## 复刻启示

- 聚合 DSL 采用类型化操作符和字段 schema 校验；发布前验证属性类型是否支持该聚合/分组策略。
- 对近似统计标注估算，对范围和时间桶展示边界规则；把 null 忽略、最大组数和排除计数作为结果元数据。
- 这类聚合可作为派生属性中的多对象计算节点，但试算解释必须列出过滤条件、分组维度、排除对象数及精确/近似性质。
