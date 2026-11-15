<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/time-series-value-bank-properties/time-series-value-bank-property-basics -->
<!-- 研读状态：已完成 -->

# Time Series Value Bank Property basics • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/time-series-value-bank-properties/time-series-value-bank-property-basics)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/v2/ontologies-v2-resources
- 相关性：direct；本体 Time Series Value Bank 属性基础定义
- 官方更新时间：2026-11-12T17:46:46.921Z
- 目录核对时间：2026-11-14T14:58:00Z
- 产品状态：基础概念页未标注 Preview

## 英文原文短摘录（每个来源不超过 25 词）

> “A Time Series Value Bank property is a property that contains a series of time based data points.”

## 摘录译文

Time Series Value Bank 属性是一种包含一系列时序数据点的属性。

## 中文要点

- 页面说明 Value Bank 属性保存一串按时间记录的数据点；它是本体对象上的特殊时间序列属性。
- 分组 API 提供 Get Latest Value 和 Stream Values：一个返回最新单点，一个流式读取多个点；两者都围绕对象与属性定位。
- 该概念页没有说明与一般 Time Series Property 的内部存储差别、采样精度或写入方式；不能仅凭名称假设它一定采用某种数据库/硬件。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Time Series Value Bank property | 时间序列值库属性 | 由 Value Bank 支持的时间化属性 |
| Data point | 数据点 | 时间序列中的单次观测 |
| Latest value | 最新值 | 读取接口返回的最近观测 |
| Stream Values | 流式值读取 | 多点读取接口 |

## 疑问与待验证项

- 属性是否带单位、质量标记、来源标签，及如何处理迟到/重复数据，本页未提及。
- Value Bank 与普通时间序列属性的功能差别需从集成与端点接口对照，而不是从基础定义推测。
- 对象加载是否将该序列投影为概要值，须检查具体对象读取参数和返回 schema。

## 复刻启示

- 在 schema 类型层区分普通标量、时序序列和 Value Bank 绑定，但将共用观测结构抽象为 timestamp/value/source。
- 对象详情默认展示最新观测摘要和查看历史入口；历史数据依用户指定窗口按需加载。
- 推理运行结果记录引用了哪个时序属性、采样时刻、聚合/选值规则，满足可复查和 AI 工具审计要求。
