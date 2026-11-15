<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/query-types/list-query-types -->
<!-- 研读状态：已完成 -->

# List Query Types (v2, latest) • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/query-types/list-query-types)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/v2/ontologies-v2-resources
- 相关性：direct；Ontology REST API v2 参考
- 官方更新时间：2026-11-12T17:46:46.922Z
- 目录核对时间：2026-11-14T14:57:51Z
- 产品状态：常规 v2 列表接口；可选 branch 为实验性功能。

## 英文原文短摘录（每个来源不超过 25 词）

> “Lists the query types for the given Ontology.”

## 摘录译文

列出给定 Ontology 中的 Query Type。

## 中文要点

- GET `/api/v2/ontologies/{ontology}/queryTypes` 列出本体查询类型；OAuth 需要 `api:ontologies-read`，默认 `pageSize` 为 100，使用 `pageToken` 分页。
- 列表中的每个查询类型都返回最近发布版本，该版本可能是预发布版；实际页可小于请求值，但有更多结果时至少返回一项。
- 可选 branch 指定分支列表，分支为实验性功能。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| pageSize | 页大小 | 希望每页返回的类型数，默认 100。 |
| pageToken | 分页令牌 | 继续读取列表的游标。 |
| latest version | 最新版本 | 最近发布的版本，可能是预发布版。 |

## 疑问与待验证项

- 分页列表在发布变化期间是否提供稳定快照，本页没有说明。
- 默认 latest 可能带来预发布版本；Agent 工具目录是否过滤预发布定义需单独设计。

## 复刻启示

- 目录卡片明确显示版本与预发布标记；分页按 nextPageToken 完整遍历。
- 将 Query Type 与对象类型、函数和 Agent 工具引用连到统一的本体画布，便于追踪数据逻辑和发布状态。
