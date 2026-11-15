<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/attachments/get-attachment -->
<!-- 研读状态：已完成 -->

# Get Attachment (v2, latest) • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/attachments/get-attachment)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/v2/ontologies-v2-resources
- 相关性：direct；Ontology REST API v2 按 RID 读取附件元数据
- 官方更新时间：2026-11-12T17:46:46.922Z
- 目录核对时间：2026-11-14T14:56:27Z
- 产品状态：本页未标注 Preview

## 英文原文短摘录（每个来源不超过 25 词）

> “Get the metadata of an attachment.”

## 摘录译文

获取一个附件的元数据。

## 中文要点

- 端点：`GET /api/v2/ontologies/attachments/{attachmentRid}`。只通过附件 RID 读取附件元数据，不需要在路径中传本体、对象类型、主键或附件属性。
- 第三方 OAuth 读取范围为 `api:ontologies-read`。响应 `AttachmentV2` 包含 `rid`、`filename`、`sizeBytes` 和 `mediaType`。
- `sizeBytes` 的 schema 类型是 `string`，但示例 JSON 返回数值 `393469`；与对象属性附件详情接口存在同样的 schema/示例类型不一致。
- 页面没有列出查询参数，因此此接口没有文档化的 branch 参数；不能把其他附件接口的分支参数自动套用到此端点。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Attachment metadata | 附件元数据 | 文件名、RID、大小、媒体类型 |
| Attachment RID | 附件 RID | 端点唯一的路径标识 |
| Filename | 文件名 | Foundry 文件名称 |
| Media type | 媒体类型 | MIME 类别，如 `image/jpeg` |

## 疑问与待验证项

- 路径不包含对象上下文，端点文档未解释是否会返回未关联对象的临时附件、以及由何种权限决定可见性。
- 页面列出的 OAuth scope 是 API 操作范围；具体数据层权限和内容访问控制需要结合部署授权机制确认。
- `sizeBytes` 类型差异、错误响应和 RID 不存在时的状态码需要以 OpenAPI/实际服务复核。

## 复刻启示

- 可将附件 RID 设计成稳定的独立资源标识，再由关联表维护它与本体对象/属性的关系；全局元数据查询仍应执行资源级授权。
- 元数据接口适合填充文件列表和预览卡片；内容下载应走独立端点，并在服务端校验租户、项目、关联关系和策略。
- schema 类型和示例冲突应纳入契约测试/客户端生成检查，但此卡属于文档研读，不执行系统测试。
