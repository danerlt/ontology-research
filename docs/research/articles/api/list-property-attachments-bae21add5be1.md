<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/attachment-properties/list-property-attachments -->
<!-- 研读状态：已完成 -->

# List Property Attachments • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/attachment-properties/list-property-attachments)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/v2/ontologies-v2-resources
- 相关性：direct；Ontology REST API v2 附件属性元数据列表接口
- 官方更新时间：2026-11-12T17:46:46.921Z
- 目录核对时间：2026-11-14T14:56:22Z
- 产品状态：本页未标注 Preview

## 英文原文短摘录（每个来源不超过 25 词）

> “Get the metadata of attachments parented to the given object.”

## 摘录译文

获取隶属于给定对象的附件元数据。

## 中文要点

- 端点：`GET /api/v2/ontologies/{ontology}/objects/{objectType}/{primaryKey}/attachments/{property}`，按本体、对象类型、主键和附件属性列出关联附件；OAuth 读取范围为 `api:ontologies-read`。
- ontology 可使用 API 名或 RID；对象类型和属性使用 API 名。可选 `branch` 默认为默认分支，也可附带 SDK 包 RID 与版本。
- 返回 `AttachmentMetadataResponse` 联合，文档列出 `single` 和 `multiple` 两个分支。示例展示 `single`，其元数据含 `rid`、`filename`、`sizeBytes`、`mediaType`。
- `sizeBytes` 在子字段 schema 中标为字符串，示例 JSON 却为数字；`multiple` 子结构也未在本页示例中展开，客户端需依赖实际 schema 而非猜测。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Parent object | 父对象/所属对象 | 持有附件属性的本体对象 |
| Single | 单附件结果 | 联合响应中的单项表示 |
| Multiple | 多附件结果 | 联合响应中的多项表示 |
| Attachment metadata | 附件元数据 | RID、文件名、大小和媒体类型等 |

## 疑问与待验证项

- `multiple` 的字段结构、是否保序以及空列表表示方式应从生成的 API schema 或 SDK 类型确认。
- 单附件/多附件联合的判定依据和属性基数规则未在页面解释。
- 页内分页与文件数量上限没有出现；不应把通用列表 API 的分页机制自行套用到此端点。

## 复刻启示

- 前端可以将单个和多个附件响应归一成数组供列表组件展示，同时保留原始联合类型用于契约校验。
- 对象属性元数据与文件内容走两步：先展示列表和元数据，再由用户动作读取选定 RID 的内容；列表接口不应暗中下载全部文件。
- 固定 OpenAPI 生成流程并测试 schema 与真实 JSON 示例类型差异，尤其是字节数和 union 分支。
