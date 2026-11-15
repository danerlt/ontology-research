<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/attachments/get-attachment -->
<!-- 研读状态：已完成 -->

# Get Attachment (v2, latest) • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/attachments/get-attachment)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/ontologies-v2-resources/attachments
- 相关性：direct；Ontology REST API v2 参考
- 官方更新时间：2026-11-12T17:46:46.922Z
- 目录核对时间：2026-11-14T14:53:38Z
- 产品状态：目录页按版本化 API 规范页核对；涉及 Preview 的端点可能变化。

## 英文原文短摘录（每个来源不超过 25 词）

> “Get the metadata of an attachment.”

## 摘录译文

获取附件元数据。

## 中文要点

- GET `/api/v2/ontologies/attachments/{attachmentRid}` 按附件 RID 读取通用附件元数据，不需要在此路径重传对象类型或属性。
- 响应类型为 AttachmentV2；旁边的 Upload Attachment 示例显示其元数据包含 RID、文件名、字节大小和媒体类型。
- 第三方 OAuth 客户端需 `api:ontologies-read`。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| attachmentRid | 附件 RID | 指定待查询的附件。 |
| AttachmentV2 | 附件资源结构 | 附件元数据响应类型。 |
| mediaType | 媒体类型 | 文件 MIME 类型。 |

## 疑问与待验证项

- 此接口文档未在正文给出完整错误矩阵。
- 可通过 RID 读取元数据不应被解释为绕过父对象授权。

## 复刻启示

- 先检查当前用户对父对象和附件的权限，再向 UI 暴露元数据。
- 将附件资源 ID、文件属性和对象挂载关系分开保存。
