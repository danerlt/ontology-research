<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/time-series-properties/get-first-point -->
<!-- 研读状态：已完成 -->

# Get First Point • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/time-series-properties/get-first-point)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/ontologies-v2-resources/time-series-properties
- 相关性：direct；Ontology REST API v2 参考
- 官方更新时间：2026-11-12T17:46:46.921Z
- 目录核对时间：2026-11-14T14:54:34Z
- 产品状态：v2 只读首点端点；第三方 OAuth2 使用 `api:ontologies-read`

## 英文原文短摘录（每个来源不超过 25 词）

> “Get the first point of a time series property.”

## 摘录译文

读取指定对象时间序列属性的首个数据点。

## 中文要点

- 端点为 `GET /api/v2/ontologies/{ontology}/objects/{objectType}/{primaryKey}/timeseries/{property}/firstPoint`，按本体 API 名/RID、对象类型 API 名、对象主键及时间序列属性 API 名定位序列。
- 成功响应为 `TimeSeriesPoint` 对象，包含 ISO 8601 时间戳 `time` 与 `value`；值可以是枚举字符串或 double。可附带 SDK package RID/version 元数据。
- 第三方 OAuth2 客户端需要 `api:ontologies-read` 操作范围。首点查询是单点读取，与 `streamPoints` 的区间批量流式响应不同。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| `firstPoint` | 首个数据点 | 读取时序属性的首点端点。 |
| `TimeSeriesPoint.time` | 数据点时间 | ISO 8601 格式的时间戳字符串。 |
| `TimeSeriesPoint.value` | 数据点值 | 本页列举为枚举字符串或双精度数值。 |
| `primaryKey` | 对象主键 | 标识拥有该时间序列属性的对象。 |

## 疑问与待验证项

- 文档没有说明首点按事件时间、同步顺序还是其他排序规则确定，也没有详细规定空序列/缺失属性的错误响应。
- 若序列数据有权限标记或对象属性限制，访问要求需结合时序数据源权限文档校验；`api:ontologies-read` 只是第三方 API 操作范围。

## 复刻启示

- 时间序列查询工具应返回统一 `{time, value}` 类型并保留单位、值类型及数据源授权上下文。
- 在对象检查器中增加“首点/末点/时间窗”专用操作，不把序列指针当成可直接排序的普通字符串。
- Agent 工具参数应包含对象主键与时序属性 API 名，并在无数据时返回明确的空结果语义，而不是伪造默认值。
