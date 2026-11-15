<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/v1/ontology-resources/attachments/get-attachment -->
<!-- 研读状态：已完成 -->

# Get Attachment (v1) • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/v1/ontology-resources/attachments/get-attachment)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/v1/ontology-resources
- 相关性：direct；Ontology API v1 元数据端点，保留兼容性对照并优先关注 v2
- 官方更新时间：2026-11-12T17:46:46.923Z
- 目录核对时间：2026-11-14T14:55:38Z
- 产品状态：页面未标注 Preview；元数据类型细节按部署核验

## 英文原文短摘录（每个来源不超过 25 词）

> “Get the metadata of an attachment.”

## 摘录译文

获取附件元数据。

## 中文要点

- `GET /api/v1/attachments/{attachmentRid}` 按 RID 获取附件元数据，不返回实际文件内容；OAuth2 第三方应用需要 `api:ontologies-read`。
- 响应字段包括 `rid`、`filename`、`sizeBytes` 和 `mediaType`。文件内容由单独的 `/content` endpoint 获取。
- v1 样例把 `sizeBytes` 表示为 JSON 数字，但结构说明写成 `string`；这是 schema 与示例类型不一致，接入时应检查生成 SDK/OpenAPI 和真实响应。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| attachmentRid | 附件 RID | 请求路径中的附件资源标识 |
| filename | 文件名 | 文件名元数据 |
| sizeBytes | 文件字节数 | 文件大小字段，页面类型声明与示例有差异 |
| mediaType | 媒体类型 | 文件 MIME 类型 |

## 疑问与待验证项

- 附件元数据可见性与对象属性权限的继承规则本页未解释，需要结合对象安全模型核对。
- 资源不存在、已清理或无权限时返回什么错误码需参照通用 Errors 文档。
- `sizeBytes` 声明和 JSON 示例冲突，生成代码可能采用其中之一。

## 复刻启示

- 元数据读取与内容下载分离，下载前先检查文件类型/大小并重新执行授权。
- API schema、示例与 SDK 类型从同一规范生成，避免出现数值/字符串不一致。
- 附件资源需要独立的授权与访问审计，关联对象后还需校验调用者对对象和附件属性的权限。
