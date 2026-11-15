<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/v1/ontology-resources/query-types/list-query-types -->
<!-- 研读状态：已完成 -->

# List Query Types (v1) • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/v1/ontology-resources/query-types/list-query-types)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/v1/ontology-resources
- 相关性：direct；Ontology API v1 查询类型分页列表接口；保留作兼容性对照，并优先关注 v2
- 官方更新时间：2026-11-12T17:46:46.923Z
- 目录核对时间：2026-11-14T14:56:00Z
- 产品状态：待核对 Beta、预览、弃用或更名信息；本页未标注 Preview

## 英文原文短摘录（每个来源不超过 25 词）

> “Each page may be smaller than the requested page size.”

## 摘录译文

每一页实际返回的项目数可能少于请求的页大小。

## 中文要点

- 端点：`GET /api/v1/ontologies/{ontologyRid}/queryTypes`，以本体 RID 为范围列出查询类型；OAuth 第三方客户端需要 `api:ontologies-read`。
- 可选 `pageSize` 默认 100；可选 `pageToken` 首次请求省略，后续用响应的 `nextPageToken` 请求下一页。
- 响应 `data` 是 `QueryType` 列表，`nextPageToken` 可选。即使返回页短于指定大小，只要还有后续结果，服务保证本页至少返回一个结果；因此不能用“本页数量不足 pageSize”判断已到末页，应检查令牌。
- 页内 QueryType 字段与单条 Get Query Type 契约一致，可用 `apiName`、描述、参数、输出、Function RID 和版本组织索引。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Page size | 页大小 | 请求希望每页返回的数量，默认 100 |
| Page token | 分页令牌 | 指示下一页读取位置的游标 |
| Next page token | 下一页令牌 | 响应中供下一次请求继续读取的游标 |
| QueryType | 查询类型 | 列表中的查询契约元数据对象 |

## 疑问与待验证项

- 文档没有承诺分页期间定义发生变化时的快照一致性；不能假设多页枚举看到同一时点的目录。
- `data` 在 schema 中标为可选；需要依据实际 SDK/服务行为核对无结果时是空数组、省略字段还是其他响应形态。
- 分页令牌是否短期有效、是否绑定调用者或本体版本，本页没有说明。

## 复刻启示

- 目录 API 采用不透明游标分页，客户端只转交 `nextPageToken`，不可自行解析或从页大小推导终止。
- 前端查询目录要保留加载中、下一页可用和空目录状态；如果目录要用于发布评审，需额外定义稳定快照或修订号，不能把普通分页当成事务快照。
- 列表只负责发现元数据，详情页应通过单项接口加载完整契约；避免一次性拉取所有参数 schema 和执行历史。
