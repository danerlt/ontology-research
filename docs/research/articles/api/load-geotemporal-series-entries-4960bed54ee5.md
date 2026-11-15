<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/geotemporal-series-properties/load-geotemporal-series-entries -->
<!-- 研读状态：已完成 -->

# Load Geotemporal Series Entries • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/geotemporal-series-properties/load-geotemporal-series-entries)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/ontologies-v2-resources/geotemporal-series-properties
- 相关性：direct；Ontology REST API v2 参考
- 官方更新时间：2026-11-12T17:46:46.921Z
- 目录核对时间：2026-11-14T14:53:43Z
- 产品状态：目录页按版本化 API 规范页核对；涉及 Preview 的端点可能变化。

## 英文原文短摘录（每个来源不超过 25 词）

> “The range field is required and restricts results to a specific time window.”

## 摘录译文

range 字段是必填项，用于限制具体时间窗口。

## 中文要点

- POST `/api/v2/ontologies/{ontology}/objects/{objectType}/{primaryKey}/geotemporalSeries/{property}/loadEntries` 在指定时间区间加载条目；端点处于 Preview，需 `preview=true`。
- range 必须同时包含 startTime 与 endTime，起点包含、终点不包含；条目总是含 time 与 position，可选择额外属性。
- 返回 data 与 nextPageToken；使用 pageToken 分页。仅启用 cold storage 的时空集成不支持此端点。OAuth scope 为 `api:ontologies-read`。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| range | 时间范围 | ISO 8601 起止时间；左闭右开。 |
| additionalProperties | 附加属性 | 在 time/position 外选择要返回的字段。 |
| cold storage | 冷存储 | 此预览端点不支持仅冷存储的集成。 |

## 疑问与待验证项

- Preview 端点可能变化；纯冷存储限制可能影响历史轨迹的完整性。
- additionalProperties 中若字段不适用于集成会被省略，调用方不能假设每条记录字段完全相同。

## 复刻启示

- 地图组件用左闭右开区间定义时间筛选，并以游标持续加载轨迹点。
- 对预览和存储集成能力做运行前检查；字段缺失按可选值处理，不能误报为零。
