<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/attachments/upload-attachment -->
<!-- 研读状态：已完成 -->

# Upload Attachment (v2, latest) • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/attachments/upload-attachment)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/ontologies-v2-resources/attachments
- 相关性：direct；Ontology REST API v2 参考
- 官方更新时间：2026-11-12T17:46:46.922Z
- 目录核对时间：2026-11-14T14:53:39Z
- 产品状态：目录页按版本化 API 规范页核对；涉及 Preview 的端点可能变化。

## 英文原文短摘录（每个来源不超过 25 词）

> “Any attachment which has not been linked to an object via an action within one hour after upload will be removed.”

## 摘录译文

上传后 1 小时内未通过 Action 关联到对象的附件会被删除。

## 中文要点

- POST `/api/v2/ontologies/attachments/upload` 上传二进制文件，Content-Type 必须为 `application/octet-stream`，文件名通过 filename 查询参数给出。
- 成功返回 AttachmentV2 元数据。上传后 1 小时内未通过 Action 关联到对象的文件会被移除；已映射但不再关联任何对象的附件每两周清理一次。
- 第三方 OAuth 客户端需要 `api:ontologies-write`。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| application/octet-stream | 二进制内容类型 | 上传正文所需的 Content-Type。 |
| filename | 文件名参数 | 上传请求的文件名查询参数。 |
| orphan cleanup | 孤立附件清理 | 清理未被对象关联的临时或遗留附件。 |

## 疑问与待验证项

- 文档没有给出上传大小限制或可接受 MIME 白名单。
- 两种清理周期不同：新临时文件 1 小时，已映射孤立附件双周；业务应允许附件关联 Action 延迟失败后的恢复处理。

## 复刻启示

- 客户端上传后立即保存 RID，Action 提交时用该 RID 作为附件参数，并显示 1 小时有效期。
- 设置项目级文件大小、MIME 和扫描策略；清理任务要考虑正在评审的草稿引用。
