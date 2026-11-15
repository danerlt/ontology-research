<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/ontology-resources/objects/list-linked-objects -->
<!-- 研读状态：已完成 -->

# List Linked Objects (v1) • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/ontology-resources/objects/list-linked-objects)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/ontology-resources/objects
- 相关性：direct；Ontology API v1 端点参考；保留作兼容性对照，并优先关注 v2
- 官方更新时间：2026-11-12T17:46:46.923Z
- 目录核对时间：2026-11-14T14:55:14Z
- 产品状态：v1 List Linked Objects 兼容路由；跨页不保证一致性

## 英文原文短摘录（每个来源不超过 25 词）

> “Lists the linked objects for a specific object and the given link type.”

## 摘录译文

列出某个对象通过指定链接类型关联的对象。

## 中文要点

此兼容路由对应 v1 的关系枚举 API：从本体、来源类型和主键出发，按 Link Type 分页读取目标对象。默认页大小 1,000；跨页不保证一致性，变化会导致重复/漏项。OSv1 最多返回 10,000 条，OSv2 没有此数量上限；null 属性不会返回。响应 `nextPageToken` 继续分页，OAuth2 读取 scope 为 `api:ontologies-read`。canonical URL 为 `/api/v1/ontology-resources/objects/list-linked-objects`。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Link Type | 链接类型 | 指定用于遍历来源对象关系的类型 |
| Inconsistent pagination | 非一致分页 | 数据变化可能导致跨页重复或遗漏 |
| Page token | 分页令牌 | 延续当前来源对象的相邻节点枚举 |
| Canonical URL | 规范地址 | 目录登记的显式 v1 API 路由 |

## 疑问与待验证项

- 读取不提供强一致快照；调用方应在持续变化的数据源上允许重扫和去重。
- 路由兼容不改变 OSv1 与 OSv2 后端存储限制之间的差异。

## 复刻启示

- 前端邻接图用加载更多而非一次拉完整图，管理分页状态、失败重试和节点去重。
- Agent 多跳检索工具记录每一跳关系定义与不一致读取限制，避免把遍历结果误当事务快照。
