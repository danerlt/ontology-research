<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/time-series-value-bank-properties/stream-values -->
<!-- 研读状态：已完成 -->

# Stream Values • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/time-series-value-bank-properties/stream-values)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/ontologies-v2-resources/time-series-value-bank-properties
- 相关性：direct；Ontology REST API v2 参考
- 官方更新时间：2026-11-12T17:46:46.921Z
- 目录核对时间：2026-11-14T14:54:38Z
- 产品状态：页面未标注 Beta/Preview；流式响应编码与分页策略应以客户端/环境验证

## 英文原文短摘录（每个来源不超过 25 词）

> “Stream all of the points of a time series property (this includes geotime series references).”

## 摘录译文

流式读取时间序列属性的全部数据点（包括 geotime series 引用）。

## 中文要点

- `POST /api/v2/ontologies/{ontology}/objects/{objectType}/{primaryKey}/timeseries/{property}/streamValues` 用于流式读取指定对象上时序属性的全部点。
- 请求体可选 `range`，支持绝对或相对时间范围；官方示例使用相对时间窗口。可选 SDK package RID、SDK 版本和分支参数，OAuth2 第三方客户端需要 `api:ontologies-read`。
- 文档将成功响应描述为原始 `body` 字符串，并未在该页展开流分块、内容类型、背压、断点续读或最大结果限制。需要依赖客户端生成代码/实际响应确认线协议。
- 该接口特别声明包括 geotime series 引用；它与仅按普通点序列读取的 `Stream Points` 页面不是可互换的契约。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| stream values | 流式读取时序值 | 从时序属性读取数据点的操作 |
| range | 时间范围 | 限定查询窗口，可为绝对或相对范围 |
| geotime series reference | 地理时序引用 | 此接口声明会包含的引用类型 |
| raw body | 原始响应体 | 文档对成功响应的简略描述，未细化编码格式 |

## 疑问与待验证项

- 页面没有说明 `body` 的实际媒体类型、点记录编码、如何表示 geotime 引用，也没有分块/游标协议示例；工程接入前应保存原始响应样本并核对 SDK。
- 未说明不传 range 时查询的历史跨度、服务端截断和限流策略。
- 相对时间范围的时区/基准时间和边界开闭规则未在本页定义。

## 复刻启示

- 设计流接口时明确内容类型、分块边界、范围上限、取消与背压行为；UI 允许指定绝对/相对窗口并展示加载状态。
- 对 geotime 值保留空间引用和时间点的联合语义，图表视图可在折线与地图轨迹间切换，并让导出结果保留时间戳。
- 派生属性的时间窗计算应使用声明式 `range` 和确定的聚合规则；解释面板列出命中的点数、范围与数据源版本，避免把大流量原始点无审计地交给 Agent。
