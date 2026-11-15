<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/time-series-properties/get-first-point -->
<!-- 研读状态：已完成 -->

# Get First Point • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/time-series-properties/get-first-point)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/v2/ontologies-v2-resources
- 相关性：direct；Ontology REST API v2 时间序列首点查询
- 官方更新时间：2026-11-12T17:46:46.921Z
- 目录核对时间：2026-11-14T14:57:52Z
- 产品状态：本页未标注 Preview

## 英文原文短摘录（每个来源不超过 25 词）

> “Get the first point of a time series property.”

## 摘录译文

获取时间序列属性的第一个数据点。

## 中文要点

- 端点：`GET /api/v2/ontologies/{ontology}/objects/{objectType}/{primaryKey}/timeseries/{property}/firstPoint`，以本体、对象类型、主键及时间序列属性名定位。
- 第三方 OAuth 读取范围为 `api:ontologies-read`。可选 `sdkPackageRid` 与 `sdkVersion` 用于生成 SDK 上下文。
- 响应 `TimeSeriesPoint` 含 `time`（ISO 8601 时间戳）和 `value`；值的文档类型为 enum 字符串或 double 数字。
- 该接口只读序列中的首个点，不提供时间范围、多个采样点、统计聚合或游标分页。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| First point | 首点 | 时间序列中的第一个数据点 |
| TimeSeriesPoint | 时间序列数据点 | 时间戳与一个值组成的响应 |
| ISO 8601 | ISO 8601 时间格式 | `time` 的时间戳格式 |
| Property API name | 属性 API 名 | 路径中标识序列属性的名称 |

## 疑问与待验证项

- “第一个”按数据源的时间正序还是写入顺序选取，本页未额外解释。
- 空序列时的状态码/空值响应以及多类型序列的实际 JSON 表达需核对 SDK 与运行结果。
- 数值只描述 enum 字符串或 double，复杂测量值和单位约定未说明。

## 复刻启示

- 对首末点 API 采用明确的单条响应类型，时间戳用时区明确的标准格式，值类型以 schema 判别而非通用字符串化。
- 首点适合时间范围摘要卡或异常检测基线；若需要完整时序或窗口聚合，应调用专门序列查询能力，而不是通过本接口多次遍历对象图。
- 画布和推理结果需标记采样时间，避免把历史首点当作对象当前状态。
