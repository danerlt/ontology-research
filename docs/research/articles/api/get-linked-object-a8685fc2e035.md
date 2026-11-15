<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/v1/ontology-resources/objects/get-linked-object -->
<!-- 研读状态：已完成 -->

# Get Linked Object (v1) • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/v1/ontology-resources/objects/get-linked-object)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/v1/ontology-resources
- 相关性：direct；Ontology API v1 端点参考；保留作兼容性对照，并优先关注 v2
- 官方更新时间：2026-11-12T17:46:46.923Z
- 目录核对时间：2026-11-14T14:55:46Z
- 产品状态：v1 只读关系 API；OAuth2 第三方应用需 `api:ontologies-read`

## 英文原文短摘录（每个来源不超过 25 词）

> “Get a specific linked object that originates from another object.”

## 摘录译文

获取一个从另一对象链接而来的指定对象。

## 中文要点

`GET /api/v1/ontologies/{ontologyRid}/objects/{objectType}/{primaryKey}/links/{linkType}/{linkedObjectPrimaryKey}` 根据来源对象、Link Type 和目标主键读取一条已链接对象。若两者之间没有该链接，则抛出 `LinkedObjectNotFound`。可用 `properties` 选择返回字段；省略时返回全部属性。响应包括目标对象 RID 与属性 map。OAuth2 scope 为 `api:ontologies-read`。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Source object | 来源对象 | 由 `objectType` 与 `primaryKey` 标识的链接起点 |
| `linkType` | 链接类型 | 连接来源与目标对象的类型 API 名 |
| `linkedObjectPrimaryKey` | 目标对象主键 | 请求目标对象的主键 |
| `LinkedObjectNotFound` | 链接对象不存在 | 不存在该来源到目标链接时的错误 |

## 疑问与待验证项

- 返回该对象失败可能来自目标记录不存在、链接不存在或授权不足；错误区分需查看统一错误响应文档。
- 页面只描述单条定向读取，不支持多跳或返回路径解释。

## 复刻启示

- 对画布关系边的 inspector 提供单步跳转：验证来源实例、link API 名、目标主键和响应对象 RID。
- 处理 not-found 时不把无链接与对象不存在混作空属性；错误返回需保留关系端点上下文。
