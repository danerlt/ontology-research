<!-- 页面 URL：https://www.palantir.com/docs/foundry/functions/create-custom-aggregation -->
<!-- 研读状态：已完成 -->

# Functions • Functions on objects • Create a custom aggregation (TSv1) • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/functions/create-custom-aggregation)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/functions/create-custom-aggregation)（配对状态：matched）
- 页面语言：英文
- 主题栏目：functions
- 相关性：direct；本体函数文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:03:13Z
- 产品状态：本文明确为 TypeScript v1 教程；同页指向 Python 与 TypeScript v2 参考和迁移指南，不等同于 v2 聚合 API 说明。

## 英文原文短摘录（每个来源不超过 25 词）

> “Functions can be used to compute custom aggregations based on data in the ontology”

## 摘录译文

函数可基于本体数据计算自定义聚合。

## 中文要点

- TypeScript v1 教程演示：先从 `Objects.search()` 按部门分组、按日期分段并求和，再对返回桶进行业务逻辑变换，最后返回可供 Workshop 图表消费的三维聚合结果。
- 示例将最近一个月的费用值延展为未来六个月预测；这是演示投影的简化假设，不是平台自动进行预测。日期桶的结束边界为排他的 `max`。
- v1 使用嵌套 `buckets`；TypeScript v2 的 `.aggregate()` 返回扁平行，若消费方需要三维结构，函数需自行重建嵌套。返回类型在 v1、v2 和 Python 间保持兼容，但内部构造方式不同。
- v1 的聚合指标只接受标记为 searchable 的属性。字符串分桶上限分别为 `topValues()` 1,000 个、`exactValues()` 10,000 个，超过能力边界时会出现近似/性能取舍。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| groupBy | 分组 | 建立聚合结果的外层分桶。 |
| segmentBy | 分段 | 在分组内按日期等维度继续分段。 |
| ThreeDimensionalAggregation | 三维聚合 | 此处为“部门 × 日期 × 数值”的嵌套结构。 |
| searchable property | 可搜索属性 | 本页说明 v1 聚合指标只能基于已标记为 searchable 的属性。 |

## 疑问与待验证项

- 示例预测规则只是“沿用最近一个月”，真实业务需定义缺失月份、季节性、部分月份和币种等语义。
- 中文配对页示例代码在方法名（`byMonths()` 与英文页 `byMonth()`）上存在差异；实现应以对应 SDK 版本的类型定义与迁移文档核验，不能直接复制示例。

## 复刻启示

- 允许用户在本体聚合结果上追加受控投影函数，但在 UI 中区分“确定性派生计算”和“预测假设”；展示完整分桶结构、时间边界和函数版本。
- v1/v2/Python 共用图表消费协议时，服务边界应提供聚合结构适配器，并在迁移评审中检查桶形状与属性可搜索性。
