<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/ontology-objects/list-objects -->
<!-- 研读状态：已完成 -->

# List Objects (v2, latest) • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/ontology-objects/list-objects)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/v2/ontologies-v2-resources
- 相关性：direct；Ontology REST API v2 参考
- 官方更新时间：2026-11-12T17:46:46.921Z
- 目录核对时间：2026-11-14T14:57:25Z
- 产品状态：常规分页读取接口；OTDP、分支等选项有实验性限制。

## 英文原文短摘录（每个来源不超过 25 词）

> “Lists the objects for the given Ontology and object type.”

## 摘录译文

列出给定 Ontology 和对象类型中的对象。

## 中文要点

- GET `/api/v2/ontologies/{ontology}/objects/{objectType}` 支持 `pageToken` 分页，`pageSize` 默认 1,000；实际页可以小于或大于请求值，有更多数据时保证至少返回一项。
- 默认不保证跨页一致性，数据变更可能导致重复或漏项；`snapshot=true` 可按分页开始前的快照读取。对象存储 v1 最多返回 10,000 个对象，v2 无此上限；null 属性不会返回。
- 可投影属性并请求 OTDP；派生属性默认加载，但只在未显式选择属性时适用，且当前仍属实验性、尚未普遍开放。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| pageToken | 分页令牌 | 从上页的 nextPageToken 继续读取。 |
| snapshot | 快照一致性 | 可减少分页过程中的重复或漏项。 |
| ObjectsExceededLimit | 对象数超限 | 对象存储 v1 超过 10,000 条后的分页错误。 |
| OTDP | Ontology 定义派生属性 | 该列表接口可返回的实验性派生字段。 |

## 疑问与待验证项

- 默认非快照分页适用于持续读取最新数据，但不适合需要唯一完整遍历的同步任务。
- 对象存储 v1 与 v2 的规模上限不同，部署前需把存储后端类型纳入分页策略。
- 页面未保证快照模式下所有属性派生值的计算快照与对象记录快照完全同一时点。

## 复刻启示

- 对象浏览器提供游标分页和可选快照模式；同步/导出流程默认请求快照并按 nextPageToken 结束。
- API 明示 OSv1 10,000 条限制；本地多系统适配器按数据源能力返回分页一致性和规模上限。
- OTDP 列表能力标为实验性，先作为本地可解释派生属性路线实现，并避免宣传为 Palantir 已 GA 的同等能力。
