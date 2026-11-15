<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/geotemporal-series-properties/load-geotemporal-series-entries -->
<!-- 研读状态：已完成 -->

# Load Geotemporal Series Entries • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/geotemporal-series-properties/load-geotemporal-series-entries)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/v2/ontologies-v2-resources
- 相关性：direct；Ontology REST API v2 时空序列窗口加载接口
- 官方更新时间：2026-11-12T17:46:46.921Z
- 目录核对时间：2026-11-14T14:56:50Z
- 产品状态：Preview；调用需附 `preview=true`，功能可能修改或移除

## 英文原文短摘录（每个来源不超过 25 词）

> “Results are paginated. Use the `nextPageToken` from the response to retrieve subsequent pages.”

## 摘录译文

结果采用分页；使用响应中的 `nextPageToken` 获取后续页面。

## 中文要点

- 端点：`POST /api/v2/ontologies/{ontology}/objects/{objectType}/{primaryKey}/geotemporalSeries/{property}/loadEntries`。它读取对象时空序列属性在指定时间范围内的条目；OAuth 读取范围为 `api:ontologies-read`。
- 必须添加 `preview=true`。仅启用冷存储的时空集成不受支持。
- 请求体 `range` 必填，`startTime` 与 `endTime` 都必填；开始时间包含在范围内，结束时间不包含。`additionalProperties` 可选请求 `speed`、`heading` 等字段；`time` 与 `position` 始终返回，底层集成缺少的字段会省略。
- `pageToken` 首次省略、后续传入上次响应的 `nextPageToken`；可指定 `pageSize`。返回 `data` 列表与可选下一页令牌。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Half-open time range | 半开时间范围 | 开始时间包含、结束时间不包含 |
| Additional properties | 附加属性 | 可请求速度、航向等观测字段 |
| Page token | 分页令牌 | 在多页时间序列读取中继续查询 |
| Cold storage | 冷存储 | 仅冷存储集成当前不支持此端点 |

## 疑问与待验证项

- 预览端点未来可能变更；调用者需要核验文档/部署状态，并为升级或移除准备替代读取路径。
- 多页读取是否基于固定快照、条目按哪个时间字段排序以及同一时间戳如何处理未说明。
- API 页说条目类似 `OntologyObjectV2` 的属性映射，地图字段详细 geometry schema 应由实际集成和 schema 核实。

## 复刻启示

- 时间序列浏览器应把半开时间范围、游标分页、附加列选择和“底层字段未提供”的缺省表现做成明确控件。
- 批量读取允许逐页加载，并对 Preview 能力加标记；不能把冷存储数据缺失误报为“该对象没有位置历史”。
- 路径解释和结果引用应包含对象、属性、时间窗、样本时间和地理位置，以便操作者复核时空过滤是否正确。
