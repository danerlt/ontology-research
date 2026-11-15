<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/linked-objects/list-linked-objects -->
<!-- 研读状态：已完成 -->

# List Linked Objects (v2, latest) • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/linked-objects/list-linked-objects)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/v2/ontologies-v2-resources
- 相关性：direct；Ontology REST API v2 参考
- 官方更新时间：2026-11-12T17:46:46.921Z
- 目录核对时间：2026-11-14T14:56:50Z
- 产品状态：常规分页读取接口；OTDP 与分支等选项有实验性限制。

## 英文原文短摘录（每个来源不超过 25 词）

> “Lists the linked objects for a specific object and the given link type.”

## 摘录译文

列出指定对象经给定链接类型关联的对象。

## 中文要点

- GET `/api/v2/ontologies/{ontology}/objects/{objectType}/{primaryKey}/links/{linkType}` 列出起点在指定 Link Type 下的关联对象；默认 `pageSize` 为 1,000。
- 分页默认不保证一致性，可能重复或遗漏；可用 `snapshot=true` 获取一致视图。对象存储 v1 最多 10,000 条，v2 无此上限；空值属性不返回。
- 可投影属性、排序并请求 OTDP；派生属性默认加载但只适用于未显式选择属性时，且目前实验性、尚未普遍开放。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| snapshot | 快照一致性 | 固定分页开始时的结果视图。 |
| pageToken | 分页令牌 | 从上一页 nextPageToken 继续遍历。 |
| Link Type | 链接类型 | 限定从起点获取哪些关联对象。 |
| OTDP | Ontology 定义派生属性 | 该接口可返回的实验性派生字段。 |

## 疑问与待验证项

- 非快照分页下关系变化可能造成重复/遗漏，完整同步应选择快照并保留去重键。
- v1 的 10,000 条限制与 v2 不同，跨系统关系查询需显式暴露该限制。
- 派生属性在 links 查询中是否依赖查询深度或目标集规模，页面没有说明。

## 复刻启示

- 关系画布的对象详情支持按 Link Type 展开关联集合，并以快照游标浏览大量关系。
- 推理路径需区分链接边读取与派生属性计算；返回关系结果时保留对象身份与边的定义来源。
- 对实验性 OTDP 显示能力标记，并记录本地 1–3 跳推理的执行与权限规则。
