<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/attachment-properties -->
<!-- 研读状态：已完成 -->

# Attachment Property basics • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/attachment-properties)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/ontologies-v2-resources/attachment-properties
- 相关性：direct；Ontology REST API v2 参考
- 官方更新时间：2026-11-12T17:46:46.921Z
- 目录核对时间：2026-11-14T14:53:34Z
- 产品状态：目录页按版本化 API 规范页核对；涉及 Preview 的端点可能变化。

## 英文原文短摘录（每个来源不超过 25 词）

> “An Attachment Property is a property that references a file attachment.”

## 摘录译文

Attachment Property 是引用文件附件的属性。

## 中文要点

- 该目录路由会重定向到 `/api/v2/.../attachment-properties/attachment-property-basics` 规范页，正文只有一句属性定义。
- 此卡保留 catalog 中独立收录的入口链接，语义与嵌套基础页相同；附件列表、元数据和文件内容由各端点定义。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Attachment Property | 附件属性 | 值引用文件附件的属性。 |
| canonical route | 规范路由 | 版本化 API 文档的最终地址。 |

## 疑问与待验证项

- 目录页没有补充单附件/多附件语义，需查看 list-property-attachments 的 union 响应。

## 复刻启示

- 把别名目录页和规范页关联起来，不重复创建一个属性类型。
- 画布属性检查器展示附件引用及其文件元数据/内容操作。
