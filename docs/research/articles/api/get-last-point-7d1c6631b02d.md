<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/time-series-properties/get-last-point -->
<!-- 研读状态：已完成 -->

# Get Last Point • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/time-series-properties/get-last-point)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/ontologies-v2-resources/time-series-properties
- 相关性：direct；Ontology REST API v2 参考
- 官方更新时间：2026-11-12T17:46:46.921Z
- 目录核对时间：2026-11-14T14:54:34Z
- 产品状态：v2 只读末点端点；第三方 OAuth2 使用 `api:ontologies-read`

## 英文原文短摘录（每个来源不超过 25 词）

> “Get the last point of a time series property.”

## 摘录译文

读取指定对象时间序列属性的末个数据点。

## 中文要点

- 端点为 `GET /api/v2/ontologies/{ontology}/objects/{objectType}/{primaryKey}/timeseries/{property}/lastPoint`，根据本体、对象类型、主键和时序属性 API 名读取末点。
- 响应为 `TimeSeriesPoint`，含 ISO 8601 `time` 和 `value`；该值可以是枚举字符串或 double。可传 SDK package RID 和版本以标识生成客户端。
- OAuth2 第三方应用需要 `api:ontologies-read`。除“末点”语义外，其参数和响应结构与首点 API 相同。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| `lastPoint` | 末个数据点 | 读取时序属性的末点端点。 |
| `TimeSeriesPoint` | 时间序列数据点 | 时间戳和值组成的时序 API 响应。 |
| `ISO 8601` | ISO 8601 | API 使用的时间戳字符串格式。 |
| `api:ontologies-read` | 本体读取范围 | 第三方 OAuth2 客户端读取此数据所需范围。 |

## 疑问与待验证项

- 文档没有明确末点如何处理乱序事件、同时间戳多个值、迟到数据和空序列；应查看时序同步/存储语义。
- “末点”不必然等于最新接收值；序列以事件时间排序时需在产品交互中标明采用的时间语义。

## 复刻启示

- 首末点计算要统一按明确的事件时间字段排序，并在数据写入/回补后刷新缓存，避免将到达顺序混作业务时间。
- 画布可将首值、末值、首末时间差作为只读查询/推理运算节点；如进一步提供派生属性，应作为独立算子并标注数据源与计算时间窗。
- 对象详情页为高频展示的末点考虑短时缓存，但需明确刷新时机和来源时间戳。
