<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/ontology-objects/aggregate-objects -->
<!-- 研读状态：已完成 -->

# Aggregate Objects (v2, latest) • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/ontology-objects/aggregate-objects)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/ontologies-v2-resources/ontology-objects
- 相关性：direct；Ontology REST API v2 参考
- 官方更新时间：2026-11-12T17:46:46.921Z
- 目录核对时间：2026-11-14T14:54:08Z
- 产品状态：常规 v2 读取接口；branch 参数属于实验性功能。

## 英文原文短摘录（每个来源不超过 25 词）

> “Perform functions on object fields in the specified ontology and object type.”

## 摘录译文

对指定 Ontology 和对象类型中的字段执行聚合函数。

## 中文要点

- POST `/api/v2/ontologies/{ontology}/objects/{objectType}/aggregate` 是按一个对象类型执行字段聚合的端点；请求可指定 `where`、`aggregation`、`groupBy` 与 `accuracy`，OAuth 应用需要 `api:ontologies-read`。
- 默认允许近似结果；若要求 `REQUIRE_ACCURATE` 但无法保证精确，接口会返回 `AggregationAccuracyNotSupported`。响应包含实际准确度、分组指标，可选返回排除项与 compute-seconds 用量。
- 与对象集合聚合端点相比，此路由把 `objectType` 固定在 URL 上，适合类型范围统计；集合端点允许通过 ObjectSet 定义更灵活的输入。branch 参数可切换读取分支，但当前仍为实验性功能。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| where | 过滤条件 | 聚合前约束对象范围。 |
| aggregation | 聚合算子 | 对属性计算 min、avg 等指标，并为结果命名。 |
| groupBy | 分组 | 按精确值或范围切分结果。 |
| computeUsage | 计算用量 | 以计算秒表示的耗用详情。 |

## 疑问与待验证项

- 示例说明分组可以按日期范围和城市精确值进行，但此页未展开每种字段类型支持的操作及 group count 限制。
- 接口对客户端标示结果准确度；消费端应保留该状态，不能将近似结果包装成确定值。

## 复刻启示

- 将过滤、分组和指标拆成画布上可检查的节点，并记录从对象类型到输出指标的依赖关系，便于解释多跳派生属性。
- 预览响应统一携带精度、排除记录数和成本字段；对 API 调用按只读权限授权，并显式区分类型聚合与任意集合聚合。
