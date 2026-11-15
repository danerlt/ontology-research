<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/v1/ontology-resources/objects/search-objects -->
<!-- 研读状态：已完成 -->

# Search Objects (v1) • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/v1/ontology-resources/objects/search-objects)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/v1/ontology-resources
- 相关性：direct；Ontology API v1 搜索端点，保留兼容性对照并优先关注 v2
- 官方更新时间：2026-11-12T17:46:46.923Z
- 目录核对时间：2026-11-14T14:55:53Z
- 产品状态：页面未标注 Preview；短页由内存上限导致也可继续翻页

## 英文原文短摘录（每个来源不超过 25 词）

> “As long as the response contains a `nextPageToken`, the remaining objects can be retrieved.”

## 摘录译文

只要响应包含 `nextPageToken`，就可以继续读取剩余对象。

## 中文要点

- `POST /api/v1/ontologies/{ontologyRid}/objects/{objectType}/search` 在 JSON 请求体中按 `query` 搜索；可选排序、页大小、页令牌和 `fields` 投影。响应返回对象页、总数和可选 `nextPageToken`。
- `pageSize` 是最大值；如果对象较大而达到服务端内存限制，当前页可以少于请求数但仍有后续数据。翻页时应保持查询与 pageSize 不变，并看令牌判断是否结束。
- OAuth2 第三方调用需 `api:ontologies-read`。支持的 query grammar 见 Search Objects Details；查询页与 List Objects 的 URL query filter 是不同请求形态。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| SearchObjectsRequest | 搜索请求体 | query、排序、分页与字段选择 |
| fields | 字段投影 | 指定返回的对象属性 API 名 |
| nextPageToken | 下一页令牌 | 继续查询其余结果的游标 |
| memory limit | 内存上限 | 对象页过大时服务端缩小实际响应数 |

## 疑问与待验证项

- 此 v1 搜索页没有明确说明默认 pageSize；应从共享分页参考/实际 SDK schema 核对。
- 总数计算与分页读取是否在同一时点，本页没有承诺一致性。
- v1 页面未描述快照参数；高并发更新期间需按可用后端行为验收是否出现重复/遗漏。

## 复刻启示

- 遵循分页令牌进行续读，不以 `data.length < pageSize` 当作结束；服务端可以因内存约束动态缩页。
- 查询 AST 和 cursor 指纹关联，禁止中途改变筛选/排序复用分页令牌。
- Agent 分页必须限制每页返回字段和最大条数，并将总数和分页不一致风险暴露为工具元数据。
