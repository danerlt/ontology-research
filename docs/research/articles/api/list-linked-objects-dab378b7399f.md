<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/v1/ontology-resources/objects/list-linked-objects -->
<!-- 研读状态：已完成 -->

# List Linked Objects (v1) • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/v1/ontology-resources/objects/list-linked-objects)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/v1/ontology-resources
- 相关性：direct；Ontology API v1 端点参考；保留作兼容性对照，并优先关注 v2
- 官方更新时间：2026-11-12T17:46:46.923Z
- 目录核对时间：2026-11-14T14:55:48Z
- 产品状态：v1 分页只读关系 API；跨页读取不保证一致性

## 英文原文短摘录（每个来源不超过 25 词）

> “Lists the linked objects for a specific object and the given link type.”

## 摘录译文

列出某个对象通过指定链接类型关联的对象。

## 中文要点

`GET /api/v1/ontologies/{ontologyRid}/objects/{objectType}/{primaryKey}/links/{linkType}` 分页列举来源对象沿某一 Link Type 到达的目标对象，可组合对象过滤条件。默认 `pageSize=1000`，通过 `nextPageToken` 延续；页面可能大于或小于请求数量，但若有后续数据保证至少返回一条。API 不保证跨页一致性，数据变更可能造成重复或遗漏。OSv1 对象最多 10,000 个，超限续页返回 `ObjectsExceededLimit`；OSv2 对象无此项数量上限。null 属性不返回，第三方 OAuth2 scope 是 `api:ontologies-read`。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| List Linked Objects | 列出链接对象 | 对来源对象按单种 Link Type 枚举目标 |
| `pageSize` | 页大小 | 默认 1,000；实际页面大小可有变化 |
| `nextPageToken` | 下一页令牌 | 用于继续分页的游标 |
| `ObjectsExceededLimit` | 对象数量超限 | OSv1 返回超过 10,000 对象后再取页时的错误 |

## 疑问与待验证项

- 文档明确不保证跨页一致性；并发新增/删除关系会造成列表不稳定，不能拿游标分页做强一致快照。
- OSv2 “无数量上限”不代表无分页、计算、响应大小或时延限制。

## 复刻启示

- 实例关系画布的邻居载入必须采用分页、重复去重和数据变化提示；关系定义画布则不依赖该实例接口。
- 多跳推理路径应把每一跳的Link Type、分页与一致性状态带入trace；有重复结果时基于稳定对象 RID 去重。
