<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/ontology-resources/objects/get-object -->
<!-- 研读状态：已完成 -->

# Get Object (v1) • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/ontology-resources/objects/get-object)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/ontology-resources/objects
- 相关性：direct；Ontology API v1 端点参考，保留兼容性对照并优先关注 v2
- 官方更新时间：2026-11-12T17:46:46.922Z
- 目录核对时间：2026-11-14T14:54:59Z
- 产品状态：页面未标注 Preview；Object Storage v1/v2 的兼容行为需结合数据源验证

## 英文原文短摘录（每个来源不超过 25 词）

> “Gets a specific object with the given primary key.”

## 摘录译文

按给定主键获取一个指定对象。

## 中文要点

- `GET /api/v1/ontologies/{ontologyRid}/objects/{objectType}/{primaryKey}` 按本体 RID、对象类型 API 名和主键读取单个对象；OAuth2 第三方应用需要 `api:ontologies-read`。
- 可选 `properties` 参数选择响应中要包含的属性，省略时读取全部属性。响应 `OntologyObject` 包含对象 RID 与属性映射。
- v1 路径使用 Ontology RID；v2 采用统一 `{ontology}` 标识形式并调整字段结构。迁移时要检查返回的对象属性包裹方式和 SDK 映射，不要只替换 URL。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| primary key | 主键 | 定位单个对象实例的键值 |
| properties | 属性选择 | 可选读取的对象属性集合 |
| OntologyObject | 本体对象 | 返回对象的 RID 与属性映射 |
| object type | 对象类型 | 解析主键及属性 schema 的类型定义 |

## 疑问与待验证项

- 当请求的主键不存在时的具体错误码/状态结构未在本页摘要说明，应查错误参考。
- 文档没有说明属性投影是否支持派生属性、权限裁剪后的字段缺省规则，以及读取期间与动作写入并发的快照语义。
- 主键的序列化格式依对象类型而定，客户端应使用 Get Object Type 的主键 schema 验证。

## 复刻启示

- 读取 API 先按项目/本体授权，再按对象类型主键 schema 做解析；属性投影应验证字段并支持安全的默认全量读取。
- 返回对象 ID 与业务属性分层保存，便于对象图 canvas 以稳定标识连接关系而不依赖可变显示名。
- 兼容 API 版本时集中处理 RID/API 名和 response shape 差异，避免污染推理与领域模型。
