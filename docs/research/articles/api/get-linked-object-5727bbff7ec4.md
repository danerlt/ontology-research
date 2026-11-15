<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/linked-objects/get-linked-object -->
<!-- 研读状态：已完成 -->

# Get Linked Object (v2, latest) • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/linked-objects/get-linked-object)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/ontologies-v2-resources/linked-objects
- 相关性：direct；Ontology REST API v2 参考
- 官方更新时间：2026-11-12T17:46:46.921Z
- 目录核对时间：2026-11-14T14:53:45Z
- 产品状态：按当前 API 参考整理；列表一致性、分支和部分媒体能力有明确限制。

## 英文原文短摘录（每个来源不超过 25 词）

> “If there is no link between the two objects, `LinkedObjectNotFound` is thrown.”

## 摘录译文

如果两个对象之间没有该链接，将抛出 `LinkedObjectNotFound`。

## 中文要点

- GET `/api/v2/ontologies/{ontology}/objects/{objectType}/{primaryKey}/links/{linkType}/{linkedObjectPrimaryKey}` 按源对象、链接类型和目标主键读取一条链接对象。
- 未存在该链接时返回明确的 `LinkedObjectNotFound`；可通过 select 限制目标对象字段，默认读取全部属性。
- 支持 branch，并可在 OSv2 上用 `excludeRid=true` 避免取回 `__rid` 以改善性能；OAuth scope 是 `api:ontologies-read`。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| linkedObjectPrimaryKey | 目标对象主键 | 指定链接另一端对象的主键。 |
| select | 字段选择 | 决定目标对象响应包含哪些属性。 |
| excludeRid | 排除 RID | OSv2 下可省略内部 __rid 字段以改善性能。 |

## 疑问与待验证项

- 端点只说明从某个源对象出发的链接方向，反向关系应通过对应 link type/源对象读取。
- branch 能力有实验支持边界。

## 复刻启示

- 链接详情面板应在未找到边时显示关系不存在，不以目标对象存在来推断边必然存在。
- 响应字段选择应用白名单，防止画布预览无意加载敏感属性。
