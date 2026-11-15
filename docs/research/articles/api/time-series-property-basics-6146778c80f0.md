<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/time-series-properties/time-series-property-basics -->
<!-- 研读状态：已完成 -->

# Time Series Property basics • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/time-series-properties/time-series-property-basics)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/ontologies-v2-resources/time-series-properties
- 相关性：direct；Ontology REST API v2 参考
- 官方更新时间：2026-11-12T17:46:46.921Z
- 目录核对时间：2026-11-14T14:54:34Z
- 产品状态：Ontology REST API v2 的稳定概念定义页；具体读取行为由各时间序列端点规定

## 英文原文短摘录（每个来源不超过 25 词）

> “A Time Series property is a property that contains a time series of data points.”

## 摘录译文

时间序列属性是一种包含时间序列数据点的属性。

## 中文要点

- 本页将 Time Series property 定义为对象属性中的时序引用/序列能力：字段关联一系列带时间和值的数据点，而不是单一静态字段值。
- 与普通对象属性相比，它需要专门的数据接口支持按时间范围读取、取首末点或流式消费；调用参数仍通过 Ontology、对象类型、对象主键和属性 API 名定位。
- 这是极简概念页，不定义数据源绑定、单位、插值、权限、时间范围格式或空序列语义；这些由配置指南和相应 API 文档补充。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| `Time Series property` | 时间序列属性 | 在 Ontology 对象上表示一系列时序数据点的属性。 |
| `TimeSeriesPoint` | 时间序列数据点 | API 返回的 `time` 与 `value` 组成的单点结构。 |
| `Series ID` | 序列标识符 | 指向外部或同步时间序列数据流的标识；此概念页未规定其配置方式。 |
| `Time range` | 时间范围 | 读取时间序列点时限定数据窗口的参数。 |

## 疑问与待验证项

- 概念页没有说明每个对象是否允许多条序列、属性如何绑定同步资源或时间值是否可空，需结合 Ontology Manager 配置指南确认。
- 不应仅从“property”一词推导出数据点物化在对象行内；实际 API 使用独立时间序列服务端点。

## 复刻启示

- 对象属性类型模型要区分标量属性与时序引用，并提供独立的时间范围、采样和流式读取接口。
- 画布属性检查器应展示底层序列标识、关联来源、单位/插值和默认序列配置；时间序列点不能误画成普通 Object 节点。
- 派生属性引擎需要明确普通链接推理与时间序列运算的计算边界，避免未经确认将时间窗聚合混入 1–3 跳对象链接规则。
