<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/time-series-properties -->
<!-- 研读状态：已完成 -->

# Time Series Property basics • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/time-series-properties)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/v2/ontologies-v2-resources
- 相关性：direct；Ontology REST API v2 Time Series API 分组入口
- 官方更新时间：2026-11-12T17:46:46.921Z
- 目录核对时间：2026-11-14T14:57:52Z
- 产品状态：分组入口未标注 Preview；流式端点状态以子页为准

## 英文原文短摘录（每个来源不超过 25 词）

> “Time Series Properties”

## 摘录译文

时间序列属性。

## 中文要点

- 这是 v2 时间序列属性分组页，分组路由未能独立读取正文。官方导航列出属性基础、获取首点、获取末点和流式读取点等页面。
- 基础页将其定义为包含一系列时间序列数据点的属性；首末点返回单条 `time/value`，Stream Points 用于读取一段序列。
- 时间序列属性是对象相关的时态数据接口，不能等同于对象当前标量值，也不是本体对象之间的静态链接。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Time Series Property | 时间序列属性 | 对象上的时间化数据点序列 |
| First point | 首点 | 序列中的第一个采样点 |
| Last point | 末点 | 序列中的最后一个采样点 |
| Stream points | 流式读取数据点 | 分页/流式读取序列数据 |

## 疑问与待验证项

- 分组页正文信息依据官方[v2 Ontology API 导航](https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources)；具体采样单位、保留期、排序和分页协议需逐个端点核对。
- `Time Series Property` 与 `Time Series Value Bank Property` 是不同分组，数据来源和实时优先规则不能互相套用。
- 本体图只展示静态 schema 时，应通过时序属性标记提醒操作者数据值随观测时间变化。

## 复刻启示

- 类型目录支持时序专用属性标记，并给出采样时间、单位、来源和读取能力；对象详情区提供时间轴/图表，而非把整段序列塞进属性表。
- 推理引擎如使用时序值，应把窗口、聚合方式、数据新鲜度和路径来源写入可解释结果；它是时态计算而非普通链接跳转。
- 超大序列使用服务端流/分页和时间窗约束，避免画布加载时拉取完整历史。
