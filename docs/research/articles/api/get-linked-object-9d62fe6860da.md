<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/linked-objects/get-linked-object -->
<!-- 研读状态：已完成 -->

# Get Linked Object (v2, latest) • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/linked-objects/get-linked-object)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/v2/ontologies-v2-resources
- 相关性：direct；Ontology REST API v2 参考
- 官方更新时间：2026-11-12T17:46:46.921Z
- 目录核对时间：2026-11-14T14:56:50Z
- 产品状态：常规读取接口；可选分支与 OTDP 字段有实验性限制。

## 英文原文短摘录（每个来源不超过 25 词）

> “Get a specific linked object that originates from another object.”

## 摘录译文

获取一个从另一对象通过链接到达的指定对象。

## 中文要点

- GET `/api/v2/ontologies/{ontology}/objects/{objectType}/{primaryKey}/links/{linkType}/{linkedObjectPrimaryKey}` 从指定起点、按 Link Type 定位一个目标对象；OAuth 需要 `api:ontologies-read`。
- 若两对象之间不存在该链接，接口抛出 `LinkedObjectNotFound`。可选择返回属性，也可排除 RID；后者在 OSv2 对象上可能改善性能。
- 响应可请求 OTDP，但派生属性尚未普遍开放；分支和事务上下文也有实验性限制。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| linkType | 链接类型 | 标识起点与目标对象之间的关系。 |
| linkedObjectPrimaryKey | 目标对象主键 | 待取回链接对象的主键。 |
| LinkedObjectNotFound | 链接对象不存在 | 两对象无指定链接时的错误。 |
| OTDP | Ontology 定义派生属性 | 当前实验性的对象属性计算能力。 |

## 疑问与待验证项

- 错误是否区分目标对象不存在与关系不存在，需进一步核对错误 API 和权限行为。
- OTDP 的计算路径及其在单对象读取响应中的呈现没有在本页说明。

## 复刻启示

- 实现按起点—关系—目标主键的可追溯读取，并把“对象存在但没有此边”作为独立业务错误。
- 对象检查器可在同一屏展示属性和来源关系；OTDP 字段应注明实验/本地实现状态及计算路径。
