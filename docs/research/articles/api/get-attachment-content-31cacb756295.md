<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/attachments/get-attachment-content -->
<!-- 研读状态：已完成 -->

# Get Attachment Content (v2, latest) • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/attachments/get-attachment-content)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/v2/ontologies-v2-resources
- 相关性：direct；Ontology REST API v2 按附件 RID 读取文件内容
- 官方更新时间：2026-11-12T17:46:46.922Z
- 目录核对时间：2026-11-14T14:56:44Z
- 产品状态：本页未标注 Preview

## 英文原文短摘录（每个来源不超过 25 词）

> “Get the content of an attachment.”

## 摘录译文

获取一个附件的内容。

## 中文要点

- 端点：`GET /api/v2/ontologies/attachments/{attachmentRid}/content`，只需附件 RID，即可请求该附件内容；第三方 OAuth 范围为 `api:ontologies-read`。
- 与 `GET /api/v2/ontologies/attachments/{attachmentRid}` 元数据接口分离。内容端点成功响应在 schema 中标成 `body: string`，但页面未说明二进制编码、Content-Type 或下载头。
- 本端点没有对象主键和属性上下文，也没有文档化的 `branch` 查询参数。它与按对象属性读取内容的端点使用不同路径和上下文。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Content endpoint | 内容端点 | 读取附件文件本体 |
| Attachment RID | 附件 RID | 指定文件资源的标识符 |
| Metadata endpoint | 元数据端点 | 返回描述文件的信息，不返回内容本体 |
| Response body | 响应体 | schema 标记为字符串，传输格式待核实 |

## 疑问与待验证项

- `body: string` 不能说明实际 REST 传输是原始字节、文本、Base64 还是 SDK 包装对象；需查 OpenAPI 原始 schema 或实测。
- 仅有 RID 时服务端是否根据项目/对象关联权限作访问判定，本页没有解释。
- 大文件是否支持范围请求、流式下载、缓存控制以及大小上限也未说明。

## 复刻启示

- 元数据和二进制内容采用不同 API 与存储路径，避免对象查询响应携带大文件。
- 独立 RID 下载接口易于提供可审计的下载事件；本地实现仍应基于资源归属和授权上下文校验，而不能把 RID 等同于访问令牌。
- 明确文件响应的 Content-Type、Content-Disposition、流式传输和范围请求契约，填补该页面未提供的协议细节。
