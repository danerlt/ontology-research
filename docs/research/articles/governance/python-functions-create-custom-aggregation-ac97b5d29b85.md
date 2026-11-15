<!-- 页面 URL：https://www.palantir.com/docs/foundry/functions/python-functions-create-custom-aggregation -->
<!-- 研读状态：已完成 -->

# Functions • Python • Create a custom aggregation • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/functions/python-functions-create-custom-aggregation)
- 官方中文来源：尚未确认（配对状态：ambiguous）
- 页面语言：英文
- 主题栏目：functions
- 相关性：direct；本体函数文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:02:57Z
- 产品状态：Python 函数聚合教程；`from_osdk()` 在 `TwoDimensionalAggregation` 与 `ThreeDimensionalAggregation` 上仅支持 Python OSDK v2。

## 英文原文短摘录（每个来源不超过 25 词）

> “Functions can be used to compute custom aggregations based on data in the ontology”

## 摘录译文

函数可使用 Ontology 数据计算自定义聚合。

## 中文要点

- 教程从 Python OSDK 读取并聚合费用对象，借助 `ThreeDimensionalAggregation.from_osdk(result, "departmentName", "date")` 将 API 的聚合响应重建为分组桶；`from_osdk()` 的此类转换只适用于 Python OSDK v2。
- 示例随后用 `NestedBucket`、`SingleBucket` 与 `Range` 建立未来六个月的桶，并把最近月份的费用值重复作为估算，最后返回 `ThreeDimensionalAggregation` 供 Workshop 图表使用。
- Python 示例中日期分组结果先作为 `YYYY-MM-DD` 字符串，再解析为 Date 并做月份运算；应用层要明确时区、缺失值和月末日期处理，不应把示例等同于自动预测。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| FoundryClient | Foundry 客户端 | Python 函数访问本体数据与 OSDK 的入口。 |
| NestedBucket | 嵌套桶 | 以外层部门键包裹内层日期桶。 |
| SingleBucket | 单层桶 | 表示一个日期范围和值。 |
| Range | 范围 | 在示例中表达月份起止日期。 |
| from_osdk | 从 OSDK 转换 | 将 OSDK 聚合结果转换成函数所需的嵌套聚合对象。 |

## 疑问与待验证项

- 月度估算直接复用最近一个观测值，文档未给出统计预测、置信区间或模型误差处理；这属于示例业务函数逻辑。
- 需要验证 Python OSDK 升级时返回桶键的运行时类型；教程显式按日期字符串解析。

## 复刻启示

- 为派生属性节点提供有类型的函数输入/输出契约和嵌套聚合 schema，并将投影生成的每个结果桶追溯到原始聚合桶。
- 试算面板显示函数版本、数据窗口及由最近月份复制的预测规则；限制 Agent 自动生成或修改的计算代码须先过静态类型、资源限制和人工分支评审。
