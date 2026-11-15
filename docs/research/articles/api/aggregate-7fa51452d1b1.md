<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/v1/ontology-resources/objects/aggregate -->
<!-- 研读状态：已完成 -->

# Aggregate Objects Details • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/v1/ontology-resources/objects/aggregate)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/v1/ontology-resources
- 相关性：direct；Ontology API v1 聚合契约详情，保留兼容性对照并优先关注 v2
- 官方更新时间：2026-11-12T17:46:46.923Z
- 目录核对时间：2026-11-14T14:55:46Z
- 产品状态：接口详细说明；近似计数无精度保证

## 英文原文短摘录（每个来源不超过 25 词）

> “Null values are ignored in aggregations.”

## 摘录译文

聚合计算忽略空值。

## 中文要点

- `POST /api/v1/ontologies/{ontologyRid}/objects/{objectType}/aggregate` 的 aggregation 可用 count/max/min/sum/avg/approximateDistinct；分组类型有 exact、fixedWidth、ranges 和 duration。
- `exact.maxGroupCount` 默认 10,000；ranges 起点包含、终点不含；duration 采用 ISO 8601。日期只支持日区间，时间戳还可按小时、分钟和秒分组。
- 空值会从 aggregation 与 groupBy 中排除，不形成空值组或 null metric；有较多分组被截断时 `excludedItems` 表示被排除对象数。
- `approximateDistinct` 是估算不同值数量，并非精确 distinct。聚合可多项组合，多个 groupBy 按定义顺序参与结果结构。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| approximateDistinct | 近似去重计数 | 属性不同值数量的估算 |
| fixedWidth | 固定宽度分组 | 按数值区间宽度生成分组 |
| ranges | 显式范围分组 | 按 `gte`/`lt` 边界分类 |
| duration | 时间间隔分组 | 按 ISO 8601 时间跨度分桶 |
| excludedItems | 被排除条目数 | 受分组上限影响而未进入结果的对象数 |

## 疑问与待验证项

- ApproximateDistinct 的误差范围/算法未承诺，不能用于精确去重校验。
- `maxGroupCount` 超限时保留哪些组的规则未说明；需要将 `excludedItems` 呈现给调用者。
- Null 被排除可能造成分组/指标总数不等于输入对象数；API 未返回被忽略 null 的计数。

## 复刻启示

- 聚合 schema 要根据属性类型动态生成合法操作符，并在预览中展示 null 排除、区间边界和截断条数。
- 对近似统计标注估算，不与精确值混用；业务合规或金额核算应要求精确语义。
- 将过滤、聚合、分组编译成可解释计划，记录输入对象集、schema 版本、字段权限和输出定义，便于复核派生属性。
