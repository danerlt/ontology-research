<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/attachment-properties/list-property-attachments -->
<!-- 研读状态：已完成 -->

# List Property Attachments • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/attachment-properties/list-property-attachments)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/ontologies-v2-resources/attachment-properties
- 相关性：direct；Ontology REST API v2 参考
- 官方更新时间：2026-11-12T17:46:46.921Z
- 目录核对时间：2026-11-14T14:53:37Z
- 产品状态：按当前 API 参考整理；批量与分支能力以页面限制为准。

## 英文原文短摘录（每个来源不超过 25 词）

> “Get the metadata of attachments parented to the given object.”

## 摘录译文

获取隶属于指定对象的附件元数据。

## 中文要点

- GET 路径以 Ontology、对象类型、主键和附件属性定位该对象字段，返回所关联附件的元数据。
- 响应是 union：单附件以 `single` 表示，多附件以 `multiple` 表示；示例显示单附件包含 RID、文件名、大小和媒体类型。
- 需要 `api:ontologies-read`；可选 SDK 版本和 branch。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| single | 单附件 | 响应中表示属性只关联一个附件的分支。 |
| multiple | 多附件 | 响应中表示属性关联附件集合的分支。 |
| AttachmentMetadataResponse | 附件元数据响应 | 以 union 表示单附件或多附件结构。 |

## 疑问与待验证项

- 页面没有展示 multiple 分支的完整子字段，序列化结构应按目标 API schema 验证。
- 零附件属性的返回形态未在本页说明。

## 复刻启示

- 前端按 union 判别式渲染附件卡片/列表，不依赖附件数量推断响应结构。
- 将文件名、RID、大小与媒体类型放在元数据列表；内容读取独立授权。
