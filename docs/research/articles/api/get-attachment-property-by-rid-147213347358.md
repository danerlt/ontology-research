<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/attachment-properties/get-attachment-property-by-rid -->
<!-- 研读状态：已完成 -->

# Get Attachment Property By Rid • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/attachment-properties/get-attachment-property-by-rid)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/v2/ontologies-v2-resources
- 相关性：direct；Ontology REST API v2 附件元数据读取接口
- 官方更新时间：2026-11-12T17:46:46.921Z
- 目录核对时间：2026-11-14T14:56:21Z
- 产品状态：本页未标注 Preview

## 英文原文短摘录（每个来源不超过 25 词）

> “Get the metadata of a particular attachment in an attachment list.”

## 摘录译文

获取附件列表中某个附件的元数据。

## 中文要点

- 端点：`GET /api/v2/ontologies/{ontology}/objects/{objectType}/{primaryKey}/attachments/{property}/{attachmentRid}`。路径同时限定本体、对象类型、对象主键、附件属性和附件 RID。
- `ontology` 可传本体 API 名或 RID；`objectType` 和 `property` 使用 API 名；`primaryKey` 定位拥有附件的对象。第三方 OAuth 读取范围为 `api:ontologies-read`。
- 可选查询参数 `branch` 指定 Foundry 分支，省略时读取默认分支；还可携带生成 SDK 的 `sdkPackageRid` 与 `sdkVersion`。
- 响应是 `AttachmentV2` 元数据对象，含附件 RID、文件名、`sizeBytes` 和媒体类型。本页 schema 将 `sizeBytes` 标为字符串，但示例 JSON 给出数字 `393469`，类型表达不一致。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Attachment RID | 附件 RID | 单个附件资源的唯一标识符 |
| Primary key | 主键 | 拥有该附件的本体对象主键 |
| Media type | 媒体类型 | 如 `image/jpeg`、`application/pdf` |
| Branch | 分支 | 可选的本体读取上下文 |

## 疑问与待验证项

- `sizeBytes` 的 schema/示例 JSON 类型相冲突，生成客户端应以实际 OpenAPI 与服务响应复核，不要静默假设为整数或字符串。
- 路径带对象主键及属性，但页面没有解释附件 RID 不属于该列表时的具体错误码；应核对空引用、无权访问和 RID 不匹配的差异。
- 分支参数是否接受分支名、RID 或二者，页面示例只展示 RID；需结合分支通用规范确认。

## 复刻启示

- 元数据读取 API 按对象上下文和附件 RID 精确定位，可将附件预览、下载入口和审计对象关联到同一个 `AttachmentRef`。
- 在客户端统一做 OpenAPI/示例一致性检查；数字字段需明确规范化边界，避免 TS、Python 客户端生成不同类型。
- 读取路径应强制核对附件属于该对象属性，并在同一分支上下文读取；该归属校验是根据路径语义提出的复刻要求。
