<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/attachment-properties/attachment-property-basics -->
<!-- 研读状态：已完成 -->

# Attachment Property basics • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/attachment-properties/attachment-property-basics)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/v2/ontologies-v2-resources
- 相关性：direct；Ontology REST API v2 附件属性概念
- 官方更新时间：2026-11-12T17:46:46.921Z
- 目录核对时间：2026-11-14T14:56:21Z
- 产品状态：基础概念页未标注 Preview

## 英文原文短摘录（每个来源不超过 25 词）

> “An Attachment Property is a property that references a file attachment.”

## 摘录译文

附件属性是一种引用文件附件的属性。

## 中文要点

- 页面只给出一句定义：Attachment Property 属于对象属性的一种，其值语义是引用文件附件。
- 这与把二进制内容直接当成普通字符串/数组属性不同。读写“属性关联”和读写“附件内容”是不同概念，具体的列表、RID 查询和内容 API 需看同组端点卡。
- 本页没有说明可接受文件类型、大小、单个属性关联数量、文件名/媒体类型等元数据形态，也没有描述创建、替换或删除附件的完整生命周期。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Attachment Property | 附件属性 | 指向文件附件引用的对象属性 |
| File attachment | 文件附件 | 该属性所引用的文件资源 |
| Reference | 引用 | 属性指向附件，而非内嵌文件字节 |

## 疑问与待验证项

- “references”没有解释引用基数、对象属性值中保存的标识符格式，也没有说明附件解绑是否会删除文件。
- 未说明是否支持一个属性对应多个附件、排序、同一附件跨对象复用或替换时的原子性。
- 权限是否同时受对象可见性与附件内容权限控制，需要从内容读取和写入 API 实测；不能只凭本页定义推断。

## 复刻启示

- 领域模型中使用专门的 `AttachmentRef`/附件关联表，保存对象类型、对象主键、属性 API 名、附件 RID 与创建信息；把文件二进制存储在受控 blob 存储中。
- 将属性更新和上传文件拆成可审计的操作，并定义孤儿清理、重复引用、解绑与删除策略；这些是为复刻补齐的产品规则，公开定义页没有给出。
- 对象详情和画布节点可以展示附件计数/预览入口，但请求文件内容时另行校验权限和下载策略，避免把内容直接暴露在对象图数据查询中。
