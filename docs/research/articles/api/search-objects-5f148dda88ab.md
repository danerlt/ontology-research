<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/ontology-resources/objects/search-objects -->
<!-- 研读状态：已完成 -->

# Search Objects (v1) • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/ontology-resources/objects/search-objects)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/ontology-resources/objects
- 相关性：direct；Ontology API v1 端点参考；保留兼容性对照并优先关注 v2
- 官方更新时间：2026-11-12T17:46:46.923Z
- 目录核对时间：2026-11-14T14:55:19Z
- 产品状态：页面未标注 Preview；分词匹配规则可能变化

## 英文原文短摘录（每个来源不超过 25 词）

> “The request body is used to filter objects based on the specified query.”

## 摘录译文

请求体用于按指定查询筛选对象。

## 中文要点

- `POST /api/v1/ontologies/{ontologyRid}/objects/{objectType}/search` 在请求体中提交 query，可选 `orderBy`、`pageSize`、`pageToken` 和返回字段 `fields`；返回对象页、下一页令牌和跨页总数。
- `pageSize` 是最大目标值；对象体积触及内部内存限制时实际页可更小。只要响应带 `nextPageToken`，就仍可继续读取；翻页时应保持 pageSize 和查询条件不变。
- 查询操作符和类型表由 Search Objects Details 展开，包括比较、数组包含、null、布尔组合和文本词项搜索。OAuth2 第三方应用需要 `api:ontologies-read`。
- v1 的 search endpoint 用 POST JSON 表达复杂查询；与 List Objects 的 URL 查询参数过滤形式不同，适合用同一 AST 生成不同接口载荷。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| SearchObjectsRequest | 对象搜索请求 | 包含查询、排序、分页和字段投影的请求体 |
| fields | 返回字段 | 指定响应中的对象属性 |
| nextPageToken | 下一页令牌 | 标识可继续读取的游标 |
| orderBy | 排序条件 | 由字段和升降序构成的排序定义 |

## 疑问与待验证项

- 请求 schema 只描述 `pageSize` 为端点入参，没有在搜索摘要中给出默认值；需从分页通用规范/生成 SDK 确认。
- 分页是否快照一致、多个请求间的数据变更如何体现，本页没有承诺一致性。
- `totalCount` 的计算成本与是否受查询复杂度影响未说明。

## 复刻启示

- 统一查询 AST，分别编译成 REST JSON 和 UI 查询计划；分页游标必须绑定查询指纹，拒绝跨条件复用。
- 对超大对象页提供动态缩页但保留令牌继续读取；不要把“当前页不足 pageSize”当作末页。
- 在 Agent 工具 schema 中限制查询深度和字段权限，令牌与排序作为受服务端管理的分页状态。
