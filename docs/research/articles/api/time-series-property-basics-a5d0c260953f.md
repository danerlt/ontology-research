<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/time-series-properties/time-series-property-basics -->
<!-- 研读状态：已完成 -->

# Time Series Property basics • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/time-series-properties/time-series-property-basics)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/v2/ontologies-v2-resources
- 相关性：direct；本体时间序列属性基础定义
- 官方更新时间：2026-11-12T17:46:46.921Z
- 目录核对时间：2026-11-14T14:57:57Z
- 产品状态：基础概念页未标注 Preview

## 英文原文短摘录（每个来源不超过 25 词）

> “A Time Series property is a property that contains a time series of data points.”

## 摘录译文

时间序列属性是一种包含一系列时间数据点的属性。

## 中文要点

- 本体时间序列属性不是单值字段，而是与对象关联的一系列数据点；端点响应常以 `time` 与 `value` 表示一个点。
- v2 API 为首点、末点、流式序列读取提供专用操作；另有 Time Series Value Bank 属性与最新值接口，不能把两个分组看成完全相同的存储/读取契约。
- 基础定义没有规定采样间隔、时区、单位、聚合、完整性或保留期，这些需要按具体源集成和读取 API 确定。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Time Series | 时间序列 | 随时间变化的数据点集合 |
| Data point | 数据点 | 具有观测时间和值的单项记录 |
| Time | 时间戳 | 点在序列中的时间标识 |
| Value | 值 | 点的数值/枚举内容，需按类型解释 |

## 疑问与待验证项

- 时间戳采用 UTC、是否保留原始时区以及相同时间点的排序/去重规则未在此页说明。
- 空数据、迟到数据和历史回填如何影响“首点/末点/最新值”需要具体 API 与集成确认。
- 是否能在派生属性中直接引用或聚合时间序列，需与 Derived Property 功能文档对照，不能只凭这一定义假设。

## 复刻启示

- 时序数据建模为单独的时间索引属性，并把单位、采样来源与精度元数据纳入 schema/连接器契约。
- 在推理试算中展示时间窗和最新采样时间；如派生结果使用时序聚合，应明确聚合函数与缺失点处理。
- 普通属性面板保留概要统计和打开时间序列视图的入口，按需读取历史数据以控制性能。
