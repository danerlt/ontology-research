<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/time-series-value-bank-properties/time-series-value-bank-property-basics -->
<!-- 研读状态：已完成 -->

# Time Series Value Bank Property basics • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/time-series-value-bank-properties/time-series-value-bank-property-basics)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/ontologies-v2-resources/time-series-value-bank-properties
- 相关性：direct；Ontology REST API v2 参考
- 官方更新时间：2026-11-12T17:46:46.921Z
- 目录核对时间：2026-11-14T14:54:39Z
- 产品状态：基础概念页；没有可确认的 Preview 或弃用标记

## 英文原文短摘录（每个来源不超过 25 词）

> “A Time Series Value Bank property is a property that contains a series of time based data points.”

## 摘录译文

Time Series Value Bank 属性是一种包含一系列基于时间的数据点的属性。

## 中文要点

- 本页对 Value Bank 属性作概念定义：它承载按时间组织的一系列数据点。相邻 API 提供读最新值和按时间范围流式读取的操作。
- 它是对象属性层面对时序数据的引用/能力，不足以推断数据点物理存储、采样频率、保留周期等实现细节。
- 需与同组的 Time Series Property 基础页及 Value Bank API 区分；两者概念相近，但 API 分组和支持端点有差别。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Time Series Value Bank property | 时间序列值库属性 | 包含按时间组织数据点的对象属性 |
| time based data point | 基于时间的数据点 | 关联时间戳和值的单条时序记录 |
| time series | 时间序列 | 按时间排列的一组数据点 |

## 疑问与待验证项

- 页面没有定义内部存储、数据保留、采样/插值和时区语义，应查具体 Foundry 配置或下游时序服务文档。
- 与另一组 Time Series Property 的底层语义差异在基础页中没有解释，需通过对象类型配置和 API 实际行为比较。

## 复刻启示

- schema 应允许属性声明为时序绑定，并将时间序列引用与标量列分开存储；画布属性面板展示绑定类型、单位、默认时间序列等可验证元数据。
- 运行时至少提供最新点和时间窗读取两类能力；派生属性需要把时间范围/聚合方式纳入表达式与结果来源轨迹。
- 不依据概念页臆造采样或保留能力，先将这些设为数据源适配器提供的能力声明。
