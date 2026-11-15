<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/time-series-value-bank-properties -->
<!-- 研读状态：已完成 -->

# Time Series Value Bank Property basics • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/time-series-value-bank-properties)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/v2/ontologies-v2-resources
- 相关性：direct；Ontology REST API v2 Value Bank 时间序列属性分组入口
- 官方更新时间：2026-11-12T17:46:46.921Z
- 目录核对时间：2026-11-14T14:57:57Z
- 产品状态：分组入口未标注 Preview；端点状态以子页为准

## 英文原文短摘录（每个来源不超过 25 词）

> “Time Series Value Bank Properties”

## 摘录译文

时间序列值库属性。

## 中文要点

- 此 URL 是 Value Bank 时间序列属性的 API 分组入口，页面正文未能独立读取。官方导航包含该属性基础、Get Latest Value 与 Stream Values。
- 基础概念页把此属性定义为包含按时间记录的数据点序列；最新值接口返回一个 `(time, value)` 条目，流式接口读取多个点。
- `Get Latest Value` 说明若某个 geotime 集成同时提供历史和实时来源，会优先选择实时来源。该策略属于具体最新值接口，不能扩大成所有时序端点的全局规则。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Value Bank property | 值库属性 | 使用 Value Bank 的时序属性类型 |
| Latest value | 最新值 | 单项最新观测及其时间 |
| Stream values | 流式值读取 | 读取时间序列中的多个点 |
| History integration | 历史集成 | 提供历史观测数据的源 |

## 疑问与待验证项

- 分组入口依据官方[v2 Ontology API 导航](https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources)；概念定义见[基础页](https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/time-series-value-bank-properties/time-series-value-bank-property-basics)。
- Value Bank 与普通 Time Series Property 的存储、聚合、频率与保留差异不能从分组页判断。
- 实时优先逻辑在历史缺失/实时延迟时是否回退到历史值，公开简述未说明。

## 复刻启示

- 同一时间序列抽象之下可声明数据源/后端能力类型，最新值选择策略应可配置并显示实际来源。
- 结果模型保留时间戳、值类型和来源；Agent 决策与派生属性应显示 freshness，不把观测值误当静态字段。
- 区分点读取与流式读取，并通过时间窗限制资源使用；别在属性详情自动拉取完整历史序列。
