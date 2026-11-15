<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/attachment-properties/get-attachment-property-content -->
<!-- 研读状态：已完成 -->

# Get Attachment Property Content • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/attachment-properties/get-attachment-property-content)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/ontologies-v2-resources/attachment-properties
- 相关性：direct；Ontology REST API v2 参考
- 官方更新时间：2026-11-12T17:46:46.921Z
- 目录核对时间：2026-11-14T14:53:37Z
- 产品状态：按当前 API 参考整理；批量与分支能力以页面限制为准。

## 英文原文短摘录（每个来源不超过 25 词）

> “Get the content of an attachment.”

## 摘录译文

获取附件内容。

## 中文要点

- GET `/objects/{objectType}/{primaryKey}/attachments/{property}/content` 读取指定对象属性关联的附件内容。
- 响应正文为字符串形式的 content；需要 `api:ontologies-read`，可指定 SDK 版本或读取 branch。
- 此路由不带 attachmentRid；对于单附件/多附件属性的适用差异需结合属性 schema 和另一条按 RID 读取内容的端点确认。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| attachment content | 附件内容 | 附件文件本体数据。 |
| attachment property | 附件属性 | 定义该对象上附件的属性。 |
| branch | 分支 | 可选的本体读取上下文。 |

## 疑问与待验证项

- 响应正文的字符串编码/二进制传输约定没有在摘录页展开。
- 本页未说明多附件列表中选择哪一项；不要假定它等同于按 RID 的内容端点。

## 复刻启示

- 前后端分离元数据接口与内容流式读取，避免把大文件编码进对象 JSON。
- 对多附件读取要求明确 attachment RID，提供下载进度、MIME 和授权检查。
