<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/v1/ontology-resources/attachments/get-attachment-content -->
<!-- 研读状态：已完成 -->

# Get Attachment Content (v1) • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/v1/ontology-resources/attachments/get-attachment-content)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/v1/ontology-resources
- 相关性：direct；Ontology API v1 内容端点，保留兼容性对照并优先关注 v2
- 官方更新时间：2026-11-12T17:46:46.923Z
- 目录核对时间：2026-11-14T14:55:39Z
- 产品状态：页面未标注 Preview；媒体类型/流式行为需客户端实测

## 英文原文短摘录（每个来源不超过 25 词）

> “Get the content of an attachment.”

## 摘录译文

获取附件内容。

## 中文要点

- `GET /api/v1/attachments/{attachmentRid}/content` 通过附件 RID 下载文件内容；OAuth2 第三方应用需要 `api:ontologies-read`。
- 成功响应简写为 `body: string`，页面没有声明该内容一定是文本，也没有说明 HTTP `Content-Type`、分块下载或 Range 支持。
- 结合 Get Attachment 读取元数据；内容 API 独立于文件名、大小、媒体类型等元信息。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| attachment content | 附件内容 | 文件实际数据 |
| attachment RID | 附件 RID | 作为路径参数的资源标识 |
| response body | 响应体 | 成功结果中的文件载荷 |
| media type | 媒体类型 | 应从元数据端点读取/确认的文件类型 |

## 疑问与待验证项

- 对大文件的真实传输方式、内容类型、文件名 header、Range/断点续传支持未说明。
- 需确认未关联对象的暂存附件是否可以通过此 endpoint 下载，以及上传者权限限制。

## 复刻启示

- 内容下载使用流式输出与范围请求，支持中断和资源配额；普通对象读取只返回附件 RID/元数据。
- 采用允许列表/沙箱预览，防止不可信附件被浏览器直接执行。
- 下载审计记录附件与对象的关联、请求用户、媒体类型、响应字节数和时间。
