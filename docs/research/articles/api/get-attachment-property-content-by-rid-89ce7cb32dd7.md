<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/attachment-properties/get-attachment-property-content-by-rid -->
<!-- 研读状态：已完成 -->

# Get Attachment Property Content By Rid • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/attachment-properties/get-attachment-property-content-by-rid)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/v2/ontologies-v2-resources
- 相关性：direct；Ontology REST API v2 按附件 RID 读取内容接口
- 官方更新时间：2026-11-12T17:46:46.921Z
- 目录核对时间：2026-11-14T14:56:22Z
- 产品状态：本页未标注 Preview

## 英文原文短摘录（每个来源不超过 25 词）

> “The RID must exist in the attachment array of the property.”

## 摘录译文

该 RID 必须存在于此属性的附件数组中。

## 中文要点

- 端点：`GET /api/v2/ontologies/{ontology}/objects/{objectType}/{primaryKey}/attachments/{property}/{attachmentRid}/content`。与不带 RID 的内容端点相比，它显式定位某个附件。
- 服务要求 `attachmentRid` 属于该对象附件属性的数组；这明确了附件归属校验的范围，不能仅凭全局 RID 下载任意文件。
- ontology 可使用本体 API 名或 RID；对象类型和属性使用 API 名，主键指定对象。第三方 OAuth 读取范围为 `api:ontologies-read`。
- 可选 SDK 包 RID、SDK 版本和 `branch`；默认读取分支。成功响应仍被 schema 标为 `body: string`，二进制编码与内容类型未说明。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Attachment array | 附件数组 | 属性关联附件的集合 |
| Attachment RID | 附件 RID | 被精确读取的附件标识符 |
| Ownership validation | 归属校验 | 验证 RID 属于对象的指定附件属性 |
| Content endpoint | 内容端点 | 返回附件内容的接口 |

## 疑问与待验证项

- 文档未说明 RID 与属性附件数组不匹配时返回的具体 HTTP 状态/错误类型。
- 空属性、附件刚上传未关联对象、对象变更并发与分支切换场景下的可见性语义需要分别验证。
- 响应编码、下载文件名、大小上限和断点续传支持未在页面描述。

## 复刻启示

- 内容下载授权应把 `(project, ontology, branch, objectType, primaryKey, property, attachmentRid)` 作为完整资源路径进行校验，阻止只验证全局 RID 的越权下载。
- 前端先列附件并选择具体项，再以 RID 取内容；服务端再次校验该 RID 仍关联于当前对象与属性，避免陈旧列表造成错误访问。
- 对大文件采用流式存储和下载是本地架构建议，需由复刻系统定义自己的响应契约与限额。
