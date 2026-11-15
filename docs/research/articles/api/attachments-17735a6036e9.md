<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/attachments -->
<!-- 研读状态：已完成 -->

# Attachment basics (v2, latest) • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/attachments)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/ontologies-v2-resources/attachments
- 相关性：direct；Ontology REST API v2 参考
- 官方更新时间：2026-11-12T17:46:46.922Z
- 目录核对时间：2026-11-14T14:53:37Z
- 产品状态：目录页按版本化 API 规范页核对；涉及 Preview 的端点可能变化。

## 英文原文短摘录（每个来源不超过 25 词）

> “An Attachment is a file that acts like a parameter of an object.”

## 摘录译文

Attachment 是作为对象参数存在的文件。

## 中文要点

- 该目录路由重定向到 `/api/v2/.../attachments/attachment-basics` 规范页。
- 规范页说明附件先作为临时文件上传，再通过 Action 关联到对象，且在 Ontology Manager 配置。
- 附件 API 分别提供临时上传、RID 元数据读取和文件内容读取。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| temporary upload | 临时上传 | 尚未由 Action 关联至对象的上传文件。 |
| Attachment RID | 附件 RID | 后续元数据/内容请求使用的资源标识。 |

## 疑问与待验证项

- 目录页链接到用户文档的 Upload attachments 工作流；API 与用户文档的步骤/限制应互相核对。

## 复刻启示

- 将附件做成与对象关联的资源生命周期，不当作普通 URL 文本字段。
- 上传后显示“待挂载”，应用 Action 后才进入对象附件列表。
