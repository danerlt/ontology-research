<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/attachment-properties/get-attachment-property-content -->
<!-- 研读状态：已完成 -->

# Get Attachment Property Content • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/attachment-properties/get-attachment-property-content)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/v2/ontologies-v2-resources
- 相关性：direct；Ontology REST API v2 按对象附件属性读取内容接口
- 官方更新时间：2026-11-12T17:46:46.921Z
- 目录核对时间：2026-11-14T14:56:21Z
- 产品状态：本页未标注 Preview

## 英文原文短摘录（每个来源不超过 25 词）

> “Get the content of an attachment.”

## 摘录译文

获取一个附件的内容。

## 中文要点

- 端点：`GET /api/v2/ontologies/{ontology}/objects/{objectType}/{primaryKey}/attachments/{property}/content`。它按对象和属性读取附件内容，没有显式接收 `attachmentRid`。
- 路径中的 ontology 接受本体 API 名或 RID；对象类型和附件属性使用 API 名；主键定位拥有该附件的对象。OAuth 读取范围为 `api:ontologies-read`。
- 可选参数包括生成 SDK 的 `sdkPackageRid`、`sdkVersion` 和 `branch`；省略分支时使用默认分支。
- 文档把成功响应描述为 `body: string`，但没有在本页说明文件字节如何编码、响应 `Content-Type`、文件名头或大文件传输方式。因此不能从类型标注直接推断它一定是 JSON 字符串或流式响应。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Attachment content | 附件内容 | 附件文件本体，而非附件元数据 |
| Attachment property | 附件属性 | 对象上的附件引用字段 |
| Response body | 响应体 | 文档标作字符串，传输细节未展开 |
| Default branch | 默认分支 | 未传 `branch` 时采用的读取上下文 |

## 疑问与待验证项

- 单个属性下有多个附件时，不含 RID 的内容接口选择哪个附件？页面没有描述选择顺序或是否仅适用于单附件属性。
- `body` 字符串与实际二进制响应之间的编码/传输约定需通过 OpenAPI 与实际响应确认。
- 错误码、缓存、内容大小限制和下载权限策略不在本页说明范围内。

## 复刻启示

- 对象属性读取和二进制下载应分开处理；下载端点可以返回文件响应，而对象查询仍只返回可控的附件引用/元数据。
- 多附件属性应优先走明确列出附件再按 RID 获取内容的流程；在产品实现中拒绝含糊的“取第一个”规则，直到契约明确。
- 评审设计时应把文件内容权限、对象权限和分支上下文一起记录；具体授权模型仍需依据本地需求设计，不能冒充此页已规定。
