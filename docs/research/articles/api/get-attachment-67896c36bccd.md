<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/ontology-resources/attachments/get-attachment -->
<!-- 研读状态：已完成 -->

# Get Attachment (v1) • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/ontology-resources/attachments/get-attachment)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/ontology-resources/attachments
- 相关性：direct；Ontology API v1 端点参考，保留兼容性对照并优先关注 v2
- 官方更新时间：2026-11-12T17:46:46.923Z
- 目录核对时间：2026-11-14T14:55:02Z
- 产品状态：页面未标注 Preview；具体权限行为需在部署中核验

## 英文原文短摘录（每个来源不超过 25 词）

> “Get the metadata of an attachment.”

## 摘录译文

获取附件的元数据。

## 中文要点

- `GET /api/v1/attachments/{attachmentRid}` 通过附件 RID 查询元数据；它不返回文件字节内容。
- 成功响应类型为 `Attachment`，包含 `rid`、`filename`、`sizeBytes` 和 `mediaType`。第三方 OAuth2 客户端需要 `api:ontologies-read` 范围。
- 文件内容应使用同组 `Get Attachment Content` 端点读取；将元数据查询和内容下载分开，便于先检查文件信息再请求大文件。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| attachment RID | 附件 RID | 全局定位附件的资源标识 |
| Attachment | 附件元数据对象 | 包含 RID、文件名、字节数与媒体类型 |
| sizeBytes | 字节数 | 文件大小字段；文档 schema 标为字符串 |
| mediaType | 媒体类型 | 文件的 MIME 类型 |

## 疑问与待验证项

- 文档 schema 将 `sizeBytes` 描述为字符串，示例 JSON 却显示未加引号的数字；调用时应按 API 实际响应/生成 SDK schema 处理这一表示差异。
- 本页未说明附件元数据可见性是否完全继承对象属性权限，需结合权限文档与内容端点确认。
- 未在本页定义附件不存在、无权访问或已孤立时的具体错误码。

## 复刻启示

- 为文件资源提供独立的元数据端点，并在下载前按 RID 重新做授权；元数据与下载流采用不同响应策略。
- OpenAPI 契约和示例需保持字段类型一致，尤其大小字段避免 schema 与样例类型冲突。
- UI 在附件卡片上先显示文件名、大小、MIME，再触发内容读取，并记录访问审计。
