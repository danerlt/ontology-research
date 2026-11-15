<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/attachments/get-attachment-content -->
<!-- 研读状态：已完成 -->

# Get Attachment Content (v2, latest) • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/attachments/get-attachment-content)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/ontologies-v2-resources/attachments
- 相关性：direct；Ontology REST API v2 参考
- 官方更新时间：2026-11-12T17:46:46.922Z
- 目录核对时间：2026-11-14T14:53:39Z
- 产品状态：目录页按版本化 API 规范页核对；涉及 Preview 的端点可能变化。

## 英文原文短摘录（每个来源不超过 25 词）

> “Get the content of an attachment.”

## 摘录译文

获取附件内容。

## 中文要点

- GET `/api/v2/ontologies/attachments/{attachmentRid}/content` 按 RID 读取上传/挂载附件的文件内容。
- 响应正文为内容字符串；第三方 OAuth 客户端需 `api:ontologies-read`。
- 它与 `Get Attachment` 的职责不同：一个取元数据，一个取文件本体。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| attachment content | 附件内容 | 附件文件本体数据。 |
| metadata | 元数据 | RID、文件名、大小、媒体类型等描述。 |

## 疑问与待验证项

- 页面未说明大文件的范围请求、流式响应或字符编码策略。
- 附件 RID 可读性与挂载对象的授权关系需在目标环境验证。

## 复刻启示

- 使用独立下载端点并按文件大小选择流式传输，避免把二进制内容塞入对象响应。
- 下载记录关联用户、对象、附件和时间，方便审计敏感文件访问。
