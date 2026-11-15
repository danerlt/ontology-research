<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/attachment-properties/get-attachment-property-by-rid -->
<!-- 研读状态：已完成 -->

# Get Attachment Property By Rid • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/attachment-properties/get-attachment-property-by-rid)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/ontologies-v2-resources/attachment-properties
- 相关性：direct；Ontology REST API v2 参考
- 官方更新时间：2026-11-12T17:46:46.921Z
- 目录核对时间：2026-11-14T14:53:35Z
- 产品状态：按当前 API 参考整理；批量与分支能力以页面限制为准。

## 英文原文短摘录（每个来源不超过 25 词）

> “Get the metadata of a particular attachment in an attachment list.”

## 摘录译文

获取附件列表中特定附件的元数据。

## 中文要点

- GET 路径包含 Ontology、对象类型、对象主键、Attachment Property API 名称和 attachment RID，用于读取对象附件列表中的某一个附件元数据。
- 返回 RID、文件名、字节大小和媒体类型；需要 `api:ontologies-read`，可选 SDK 版本及 branch。
- 该 API 定位的是已挂载在对象属性上的附件，不是通用文件检索接口。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| attachmentRid | 附件 RID | 某个附件的资源标识。 |
| mediaType | 媒体类型 | 文件 MIME 类型，例如 image/jpeg。 |
| primaryKey | 主键 | 定位持有该附件的本体对象。 |

## 疑问与待验证项

- 路径限定到对象和属性，页面未说明 RID 全局唯一性及跨对象访问的行为。
- 仅有读本体 scope 时，底层文件资源是否还需额外权限需结合实际授权验证。

## 复刻启示

- 在附件详情组件中展示文件名、大小、类型和 RID；读附件元数据前先验证对象与属性读取权。
- 内部 API 以对象主键和属性约束附件的父子关系，拒绝跨对象拼接 RID 的访问。
