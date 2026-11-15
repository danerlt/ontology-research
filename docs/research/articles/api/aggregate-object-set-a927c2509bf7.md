<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/ontology-object-sets/aggregate-object-set -->
<!-- 研读状态：已完成 -->

# Aggregate Object Set • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/ontology-object-sets/aggregate-object-set)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/ontologies-v2-resources/ontology-object-sets
- 相关性：direct；Ontology REST API v2 参考
- 官方更新时间：2026-11-12T17:46:46.922Z
- 目录核对时间：2026-11-14T14:54:05Z
- 产品状态：常规 v2 查询接口；分支与事务参数属于实验性功能。

## 英文原文短摘录（每个来源不超过 25 词）

> “Aggregates the ontology objects present in the `ObjectSet` from the provided object set definition.”

## 摘录译文

依据给定的 Object Set 定义，对集合中的 Ontology 对象执行聚合。

## 中文要点

- POST `/api/v2/ontologies/{ontology}/objectSets/aggregate` 将对象集合表达式作为聚合输入，适合对过滤、链接组合或其他集合定义统一分组与统计。
- 请求体支持 `aggregation`、`groupBy` 与 `accuracy`；准确度默认允许近似。选择 `REQUIRE_ACCURATE` 而引擎无法保证精确时，接口会以 `AggregationAccuracyNotSupported` 失败，而不是悄悄返回近似值。
- 请求可指定 branch、transaction 或 scenario；其中 branch 和 transaction 被标为实验性。`executeInMemoryOnly` 可让超出内存计算能力的请求快速失败。响应可返回准确度、分组指标、排除项数量和计算用量；后者只对 OSDK 应用开放且可能降低性能。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| objectSet | 对象集合定义 | 作为聚合输入的数据对象集合表达式。 |
| groupBy | 分组 | 决定结果按哪些字段或值范围拆分。 |
| accuracy | 准确度策略 | 选择只接受精确结果，或允许在不可精确时返回近似结果。 |
| executeInMemoryOnly | 仅内存执行 | 不能以内存方式执行时快速失败。 |

## 疑问与待验证项

- 文档未在此端点页逐项列明各聚合类型和字段类型的精确度边界；应结合聚合类型参考页确定能力矩阵。
- `includeComputeUsage` 会增加查询耗时，不应作为生产默认选项。

## 复刻启示

- 推理画布应允许聚合节点直接接收集合定义，而不把输入限制成单一对象类型；试算输出同时标出精确/近似、排除项和成本。
- 在用户选择“必须精确”时将能力不足呈现为明确错误；为多跳计算提供仅内存快速失败选项，避免运行预览意外触发昂贵计算。
