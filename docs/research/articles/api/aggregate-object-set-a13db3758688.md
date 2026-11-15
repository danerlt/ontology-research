<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/ontology-object-sets/aggregate-object-set -->
<!-- 研读状态：已完成 -->

# Aggregate Object Set • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/ontology-object-sets/aggregate-object-set)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/v2/ontologies-v2-resources
- 相关性：direct；Ontology REST API v2 参考
- 官方更新时间：2026-11-12T17:46:46.922Z
- 目录核对时间：2026-11-14T14:57:17Z
- 产品状态：常规 v2 查询接口；分支/事务为实验性选项。

## 英文原文短摘录（每个来源不超过 25 词）

> “Aggregates the ontology objects present in the `ObjectSet` from the provided object set definition.”

## 摘录译文

依据给定的 Object Set 定义，对集合中的 Ontology 对象执行聚合。

## 中文要点

- POST `/api/v2/ontologies/{ontology}/objectSets/aggregate` 直接对 Object Set 表达式中的对象聚合；请求包括 objectSet、aggregation、groupBy 与 accuracy。
- 准确度默认允许近似；要求 `REQUIRE_ACCURATE` 而系统无法保证精确时会报 `AggregationAccuracyNotSupported`。可选 `executeInMemoryOnly=true` 使不能以内存计算的请求快速失败。
- 可在本体情景或事务上下文执行；computeUsage 详情目前只对 OSDK 应用可用，且文档提示可能拖慢查询、不建议生产启用。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| objectSet | 对象集合定义 | 本次统计的对象集合表达式。 |
| accuracy | 准确度要求 | 选择精确结果或允许近似结果。 |
| executeInMemoryOnly | 仅内存执行 | 无法以内存计算时快速失败。 |
| computeUsage | 计算用量 | 可选计算耗用详情，当前受应用类型与性能限制。 |

## 疑问与待验证项

- 页面未承诺所有聚合函数、字段类型和数据源都有相同精确度能力。
- 性能开销较大的 computeUsage 不应默认用于线上请求。

## 复刻启示

- 把集合定义、过滤、分组和统计表达式作为一个可审阅推理节点；输出同时显示准确度与排除项。
- 提供仅内存快速失败和计算成本提示，帮助用户在 1–3 跳推理试算时控制范围。
