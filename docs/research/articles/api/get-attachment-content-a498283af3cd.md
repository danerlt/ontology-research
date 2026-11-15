<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/ontology-resources/attachments/get-attachment-content -->
<!-- 研读状态：已完成 -->

# Get Attachment Content (v1) • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/ontology-resources/attachments/get-attachment-content)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/ontology-resources/attachments
- 相关性：direct；Ontology API v1 端点参考，保留兼容性对照并优先关注 v2
- 官方更新时间：2026-11-12T17:46:46.923Z
- 目录核对时间：2026-11-14T14:55:02Z
- 产品状态：页面未标注 Preview；响应媒体类型需在客户端核验

## 英文原文短摘录（每个来源不超过 25 词）

> “Get the content of an attachment.”

## 摘录译文

获取附件内容。

## 中文要点

- `GET /api/v1/attachments/{attachmentRid}/content` 按附件 RID 读取文件内容；OAuth2 第三方应用需要 `api:ontologies-read`。
- 文档把成功响应概述为 `body: string`，没有在本页给出媒体类型、下载头、范围请求或流式传输细节；不能把该 schema 简述当作内容必然是 JSON 文本。
- 与 `Get Attachment` 元数据端点搭配使用：先读文件名、大小、媒体类型，再请求内容字节。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| attachment content | 附件内容 | 附件对应的实际文件数据 |
| attachment RID | 附件 RID | 读取该文件资源的标识 |
| response body | 响应体 | 文档描述成功响应载荷的字段 |
| media type | 媒体类型 | 内容解释方式，需结合元数据端点读取 |

## 疑问与待验证项

- 需验证 HTTP 响应中的 `Content-Type`、二进制编码、下载文件名和大文件是否流式返回；参考页没有给出这些字段。
- 无权访问与 RID 不存在时的错误体/状态码未在本页说明。

## 复刻启示

- 附件元数据和文件内容分开读取；下载端点按 RID 重新授权，设置安全的 `Content-Disposition` 并支持流式传输。
- 客户端先校验 `mediaType` 和大小，再按允许类型预览或下载，避免将不可信文件直接以内联 HTML 渲染。
- 审计记录应包含用户、项目、对象关联、附件 RID 和下载时间，不记录文件明文内容。
