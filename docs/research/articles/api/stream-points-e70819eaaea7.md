<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/time-series-properties/stream-points -->
<!-- 研读状态：已完成 -->

# Stream Points • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/time-series-properties/stream-points)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/ontologies-v2-resources/time-series-properties
- 相关性：direct；Ontology REST API v2 参考
- 官方更新时间：2026-11-12T17:46:46.921Z
- 目录核对时间：2026-11-14T14:54:34Z
- 产品状态：v2 只读流式 API；支持 JSON/Arrow 序列化和绝对/相对时间范围

## 英文原文短摘录（每个来源不超过 25 词）

> “ARROW is more efficient than JSON at streaming a large sized response.”

## 摘录译文

大响应流式传输时，Arrow 比 JSON 更高效。

## 中文要点

- 端点为 `POST /api/v2/ontologies/{ontology}/objects/{objectType}/{primaryKey}/timeseries/{property}/streamPoints`，读取对象某个时间序列属性的全部或限定范围数据点。
- 请求体可选 `range`，支持绝对或相对时间窗口；可选 `aggregate` 汇总数据。输出格式参数 `format` 默认 `JSON`，也可用 `ARROW`，文档建议大响应使用 Arrow 提高流式效率。
- 响应正文是序列化的流式 body，而不是分页 JSON 对象；第三方 OAuth2 应用需 `api:ontologies-read`。路径资源仍由对象主键和时序属性 API 名唯一确定。
- 此端点只读取 time series points；另有 Time Series Value Bank/Geotemporal 路径负责时间序列值或地理时间值，不能把 endpoint 的输出对象和这些 API 混为一谈。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| `streamPoints` | 流式读取数据点 | 按可选范围和聚合读取时序点的 POST 端点。 |
| `range` | 时间范围 | 限定读取数据的绝对或相对时间窗口。 |
| `aggregate` | 聚合设置 | 可选的时间序列聚合请求配置。 |
| `JSON` / `ARROW` | JSON / Arrow | 序列化输出格式；大响应可选 Arrow。 |
| `api:ontologies-read` | 本体读取范围 | 第三方 OAuth2 应用所需的操作范围。 |

## 疑问与待验证项

- 页面没有给出响应流中的分块格式、背压行为、最大时间窗和聚合参数完整结构；实现前需查看版本化 OpenAPI schema 与性能限制。
- 该 API 的值类型本页未在响应结构中展开；应与对象类型/属性定义配合解码，避免把时间序列枚举值默认转成浮点数。
- 不同 serialization format 的客户端兼容性应核对生成 SDK/调用方是否支持 Arrow，而不能只因服务端提供就默认可解码。

## 复刻启示

- 为大时间序列提供真正的流式服务边界、按需时间窗和可选聚合；当 Arrow 可用时将其作为高吞吐传输选项，并提供格式能力协商。
- 推理画布可把时间范围、采样/聚合和输出字段串成可解释管线，保存表达式版本及执行窗口；本次确认的 1–3 跳对象链接推理与时序窗口聚合需分开命名和限权。
- 查询过程应暴露流量、延迟、点数和聚合方式等可观测字段，支持对昂贵的大窗口查询做资源预算。
