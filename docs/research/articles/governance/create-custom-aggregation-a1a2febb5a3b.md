<!-- 页面 URL：https://www.palantir.com/docs/zh/foundry/functions/create-custom-aggregation -->
<!-- 研读状态：已完成 -->

# 函数 • Functions on objects • 创建自定义聚合 • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/functions/create-custom-aggregation)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/functions/create-custom-aggregation)
- 页面语言：中文
- 主题栏目：functions
- 相关性：direct；本体函数文档
- 官方更新时间：2026-11-12T17:46:46.935Z
- 目录核对时间：2026-11-14T14:59:08Z
- 产品状态：待核对 Beta、预览、弃用或更名信息

## 英文原文短摘录（每个来源不超过 25 词）

> “Functions can be used to compute custom aggregations based on data in the ontology, which can then be surfaced in a chart widget in Workshop.”

## 摘录译文

函数可根据 Ontology 中的数据计算自定义聚合结果，并将结果呈现在 Workshop 图表组件中。

## 中文要点

- 中文官方页展示 TypeScript v1 的自定义聚合流程：对象搜索与聚合、变换嵌套桶、返回三维聚合给 Workshop 图表。
- 页面明确提示中文内容由 AIP 从英文机器翻译，准确性未经验证；因此将中文页作为辅助对照，关键 API 语义以英文原页复核。
- 示例先按部门分组、按日期月份分段，对费用求和，再把最近月份的值复制到未来六个月，明确这只是简单的估算示范。中文页说明日期范围的 `max` 不包含端点。
- 中文页在示例中出现 `.byMonths()`，英文原文写 `.byMonth()`；API 方法名可能受文档翻译或 SDK 版本影响，需以目标版本的 OSDK 类型为准。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| 自定义聚合 | custom aggregation | 将本体聚合结果交给函数继续投影或变换。 |
| 桶（bucket） | bucket | 按分组与分段构成的聚合结果单元。 |
| Workshop | Workshop | 可使用该函数返回值的应用和图表构建环境。 |

## 疑问与待验证项

- 中文示例的日期分段方法名与英文版不一致，应检查文档所对应的 SDK 版本；两个页面均未在此处标注方法差异的原因。
- 该简单外推不是内置推理能力，复刻系统应要求预测逻辑明确说明假设与数据窗口。

## 复刻启示

- 自定义派生值需保留函数代码版本、输入聚合定义、分桶转换和返回类型，让审阅者追踪输出如何形成。
- 对用户呈现“历史观测”与“函数生成估值”的不同来源，并把日期范围端点约定纳入字段级说明。
