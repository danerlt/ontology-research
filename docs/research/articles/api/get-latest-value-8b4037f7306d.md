<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/time-series-value-bank-properties/get-latest-value -->
<!-- 研读状态：已完成 -->

# Get Latest Value • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/time-series-value-bank-properties/get-latest-value)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/v2/ontologies-v2-resources
- 相关性：direct；Ontology REST API v2 Value Bank 时间序列最新值接口
- 官方更新时间：2026-11-12T17:46:46.921Z
- 目录核对时间：2026-11-14T14:57:57Z
- 产品状态：本页未标注 Preview

## 英文原文短摘录（每个来源不超过 25 词）

> “Get the latest value of a property backed by a timeseries.”

## 摘录译文

获取由时间序列支持的属性最新值。

## 中文要点

- 端点：`GET /api/v2/ontologies/{ontology}/objects/{objectType}/{primaryKey}/timeseries/{propertyName}/latestValue`，读取对象 Value Bank 时间序列属性的最新条目。
- 若某个 geotime 集成同时连接历史与实时来源，接口优先采用实时来源。OAuth 读取范围为 `api:ontologies-read`；可选 SDK 包 RID、SDK 版本和分支，省略分支使用默认分支。
- 响应 `TimeseriesEntry` 包含 ISO 8601 `time` 与 `value`；值可为 enum 字符串、double 或 geopoint。它不仅是普通属性标量，还带观测时间。
- 这里的“latest”受数据源接入和可见性影响，文档未承诺采集延迟上限或数据新鲜度 SLA。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Value Bank | 值库 | 支持该类时间序列属性的底层能力名 |
| Latest value | 最新值 | 优先读取可用实时集成中的最近条目 |
| Geopoint | 地理点 | 时间序列值的一种空间类型 |
| TimeseriesEntry | 时间序列条目 | 时间戳与观测值组成的响应 |

## 疑问与待验证项

- 实时集成与历史集成冲突时，除实时优先外，缺值回退与重复采样消歧规则未说明。
- 属性路径使用 `propertyName`，与其他时间序列端点写作 `property`；代码生成需以具体 endpoint schema 为准。
- “最新”排序所用时间字段、空序列返回和数据新鲜度保证未给出。

## 复刻启示

- 为当前值面板返回 `(value, observedAt, source)`，并把实时优先策略写进连接器配置；不要静默隐藏观测来源和时间。
- 以专用查询接口读取高频序列值，不把全量时序装载进普通对象 JSON 或画布节点。
- 若 Agent 将最新值用于决策，应在工具结果中附带采样时间、来源及延迟提示，并在动作执行前重新验证关键值。
