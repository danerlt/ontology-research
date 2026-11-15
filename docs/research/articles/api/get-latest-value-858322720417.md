<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/time-series-value-bank-properties/get-latest-value -->
<!-- 研读状态：已完成 -->

# Get Latest Value • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/time-series-value-bank-properties/get-latest-value)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/ontologies-v2-resources/time-series-value-bank-properties
- 相关性：direct；Ontology REST API v2 参考
- 官方更新时间：2026-11-12T17:46:46.921Z
- 目录核对时间：2026-11-14T14:54:35Z
- 产品状态：页面未标注 Beta/Preview；底层 geotime 集成行为需按部署验证

## 英文原文短摘录（每个来源不超过 25 词）

> “If a specific geotime series integration has both a history and a live integration, we will give precedence to the live integration.”

## 摘录译文

如果某个特定 geotime series 集成同时具有历史集成和实时集成，系统会优先采用实时集成。

## 中文要点

- `GET /api/v2/ontologies/{ontology}/objects/{objectType}/{primaryKey}/timeseries/{propertyName}/latestValue` 读取给定对象时序属性的最新值。
- 路径由本体、对象类型、对象主键和时序属性 API 名组成。可选参数包括生成 SDK 的 package RID、SDK 版本和读取分支；OAuth2 第三方客户端需 `api:ontologies-read`。
- 成功响应是 `TimeseriesEntry`，包含 ISO 8601 `time` 和 `value`；文档列出的 value 形态为枚举字符串、double 或 geopoint。
- 若同一 geotime series 集成同时配置了历史与实时来源，实时来源优先。这个优先级是特定集成语境，不能推广成所有数据源的统一新旧判定规则。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| latest value | 最新值 | 属性对应时序中的当前最新数据点 |
| TimeseriesEntry | 时序条目 | 含时间戳与值的成功响应对象 |
| geotime series integration | 地理时序集成 | 同时含历史/实时接入时以实时集成为优先 |
| primary key | 主键 | 定位拥有时序属性的对象实例 |

## 疑问与待验证项

- 页面没有说明“最新”的事件时间/摄取时间定义、迟到数据排序、同时间戳冲突和无数据时的错误/空值表现，需在接入实现中验证。
- `value: any` 的具体序列化结构仅被概述为三类；geopoint 的坐标系与字段细节应查对应值类型定义。
- SDK 参数与分支参数的兼容规则未在本页展开。

## 复刻启示

- 单点读取接口要同时返回值与事件时间，并携带对象、属性、数据源及查询时间等元数据，以便 UI 和 Agent 判断数据新鲜度。
- 推理试算若使用最新时序值，应在结果解释里记录实际采用的时间戳和实时/历史来源；同一逻辑重复运行时可追溯数据变化。
- 实时与历史集成冲突策略应配置化并显式展示，避免把某一来源优先级隐含在查询代码中。
