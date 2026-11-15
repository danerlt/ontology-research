<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/v1/ontology-resources/objects/get-object -->
<!-- 研读状态：已完成 -->

# Get Object (v1) • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/v1/ontology-resources/objects/get-object)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/v1/ontology-resources
- 相关性：direct；Ontology API v1 对象端点，保留兼容性对照并优先关注 v2
- 官方更新时间：2026-11-12T17:46:46.923Z
- 目录核对时间：2026-11-14T14:55:47Z
- 产品状态：页面未标注 Preview；返回结构以 v1 为准

## 英文原文短摘录（每个来源不超过 25 词）

> “Gets a specific object with the given primary key.”

## 摘录译文

按给定主键获取指定对象。

## 中文要点

- `GET /api/v1/ontologies/{ontologyRid}/objects/{objectType}/{primaryKey}` 读取单个对象；主键值按该对象类型 schema 编码，OAuth2 第三方调用需要 `api:ontologies-read`。
- 可选 `properties` 参数指定返回字段；省略时返回对象的全部属性。响应为 `OntologyObject`，包含对象 RID 和 `properties` 映射。
- v1 以 ontology RID 作路径标识；输出中属性位于 map 下，与业务字段本身、对象 RID 分开。v2 响应结构和参数命名有差异，应使用版本映射层。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| primaryKey | 主键 | 目标对象实例的唯一键值 |
| properties | 属性投影 | 通过 query 参数选择的属性集合 |
| OntologyObject | 本体对象 | RID 与属性映射构成的响应 |
| ontologyRid | 本体 RID | v1 的本体标识参数 |

## 疑问与待验证项

- 无匹配主键时的错误响应、返回字段的权限裁剪和 null 属性表示方式未在本页解释。
- 页面没有说明属性投影能否包括派生属性或链接对象字段；不要从普通字段投影外推此能力。

## 复刻启示

- 按项目/本体授权后再解析类型与主键；对象 RID 作为稳定资源标识，主键保持业务键语义。
- 详情检查器支持字段选择，但区分未请求、无权限、null 和不存在，避免把缺失字段解读为业务空值。
- API 版本适配器将 map 包裹结构规整为内部 ObjectRecord，同时保留原始 response shape 用于兼容。
