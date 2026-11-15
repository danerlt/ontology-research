<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/linked-objects/list-linked-objects -->
<!-- 研读状态：已完成 -->

# List Linked Objects (v2, latest) • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/linked-objects/list-linked-objects)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/ontologies-v2-resources/linked-objects
- 相关性：direct；Ontology REST API v2 参考
- 官方更新时间：2026-11-12T17:46:46.921Z
- 目录核对时间：2026-11-14T14:53:49Z
- 产品状态：按当前 API 参考整理；列表一致性、分支和部分媒体能力有明确限制。

## 英文原文短摘录（每个来源不超过 25 词）

> “This endpoint does not guarantee consistency. Changes to the data could result in missing or repeated objects in the response pages.”

## 摘录译文

此端点不保证一致性；数据变化可能导致分页结果漏项或重复。

## 中文要点

- GET `/api/v2/ontologies/{ontology}/objects/{objectType}/{primaryKey}/links/{linkType}` 列出指定源对象按给定 Link Type 关联的对象；默认页大小 1,000，支持 cursor。
- 默认 snapshot=false，分页期间数据变化可能产生重复/缺失；设置 snapshot=true 可固定开始翻页前的视图。响应页大小可大于或小于请求值，但有后续结果时至少含一条；null 属性不返回。
- OSv1 关联对象最多返回 10,000 条，超过后继续翻页会报 `ObjectsExceededLimit`；OSv2 无此上限。
- 可用 select 选择字段；未指定字段时 OTDP 派生属性默认加载，但这是实验能力且尚未普遍可用。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| snapshot | 快照一致性 | 翻页时固定开始读取前的数据视图。 |
| pageToken | 分页令牌 | 继续读取后续链接对象的游标。 |
| OTDP | Ontology-defined derived property | 未显式选字段时默认加载的实验派生属性。 |

## 疑问与待验证项

- 默认非快照模式适合查看最新数据，但不可用于需要无重/无漏的批处理。
- OTDP 显示为默认 true 但受实验/可用性限制；项目需探测环境支持。

## 复刻启示

- 解释推理路径时为多对象集合读取启用 snapshot，保存请求窗口和成员对象 RID，避免分页变动导致结果路径漂移。
- 执行图谱遍历时尊重 OSv1 的 10,000 上限并对超限显示可操作提示。
