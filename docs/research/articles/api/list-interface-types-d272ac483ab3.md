<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/ontology-interfaces/list-interface-types -->
<!-- 研读状态：已完成 -->

# List Interface Types • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/ontology-interfaces/list-interface-types)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/ontologies-v2-resources/ontology-interfaces
- 相关性：direct；Ontology REST API v2 参考
- 官方更新时间：2026-11-12T17:46:46.921Z
- 目录核对时间：2026-11-14T14:54:03Z
- 产品状态：Preview 兼容路由；调用需传 `preview=true`

## 英文原文短摘录（每个来源不超过 25 词）

> “Lists the interface types for the given Ontology.”

## 摘录译文

列出指定本体中的接口类型。

## 中文要点

该接口 API 的兼容路由用于分页列出本体中的接口类型，规范路由位于 `/api/v2/.../ontology-interfaces/list-interface-types`。请求需带 `preview=true`，分页通过 `pageToken` 和响应 `nextPageToken` 延续，默认页大小为 500；服务可以返回更小的页面，但有剩余结果时会至少返回一条。读取权限范围为 `api:ontologies-read`。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| `nextPageToken` | 下一页令牌 | 服务返回的分页位置，应传给后续 `pageToken` |
| `pageSize` | 页大小 | 默认 500，实际返回可更少 |
| Ontology | 本体 | 列表读取范围由 ontology API 名或 RID 指定 |
| Preview | 预览功能 | 需要请求参数显式启用 |

## 疑问与待验证项

- 文档没有说明列表响应是否提供并发修改期间的一致性快照；须在同步器设计中允许增量变更与重扫。
- 分支能力标为实验性，不能推断默认分支与任意分支的接口集合完全一致。

## 复刻启示

- 多项目画布的接口发现应按项目授权范围列举，不要将一个本体的接口缓存跨租户复用。
- 增量同步器要存游标与版本/时间戳，分页期间失效时能重启本体级扫描并保持图谱一致性。
