<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/ontology-resources/objects/get-linked-object -->
<!-- 研读状态：已完成 -->

# Get Linked Object (v1) • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/ontology-resources/objects/get-linked-object)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/ontology-resources/objects
- 相关性：direct；Ontology API v1 端点参考；保留作兼容性对照，并优先关注 v2
- 官方更新时间：2026-11-12T17:46:46.923Z
- 目录核对时间：2026-11-14T14:55:13Z
- 产品状态：v1 Get Linked Object 兼容路由，OAuth2 读取范围为 `api:ontologies-read`

## 英文原文短摘录（每个来源不超过 25 词）

> “Get a specific linked object that originates from another object.”

## 摘录译文

获取一个从另一对象链接而来的指定对象。

## 中文要点

该兼容入口通过来源对象类型/主键、link API 名和目标主键读取单个目标对象；若两对象间无链接会抛出 `LinkedObjectNotFound`。`properties` 可限制返回字段，省略则取全部。OAuth2 需 `api:ontologies-read`。canonical 路由为 `/api/v1/ontology-resources/objects/get-linked-object`。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| `primaryKey` | 来源主键 | 标识关系起点对象 |
| `linkType` | 链接类型 | 按类型 API 名定位来源至目标的关联 |
| `LinkedObjectNotFound` | 链接对象不存在 | 指定连接不存在时的异常 |
| Canonical URL | 规范地址 | 本文档对应的显式 v1 操作页面 |

## 疑问与待验证项

- 此路由为 v1 兼容入口，并非与显式 `/api/v1/` 页面不同的接口。
- 单次 GET 不提供遍历路径或多跳聚合结果，需用其他读取端点组合。

## 复刻启示

- 运行图采用主键与 link API 名构造单步边查询，结果保留目标对象 RID 与投影字段。
- 多跳派生属性执行器需要反复解析受授权关系，单步 API 的错误不可静默当作空集合。
