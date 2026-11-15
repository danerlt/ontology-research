<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/v1/ontology-resources/attachments/attachment-basics -->
<!-- 研读状态：已完成 -->

# Attachment basics (v1) • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/v1/ontology-resources/attachments/attachment-basics)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/v1/ontology-resources
- 相关性：direct；Ontology API v1 附件概念参考，保留兼容性对照并优先关注 v2
- 官方更新时间：2026-11-12T17:46:46.923Z
- 目录核对时间：2026-11-14T14:55:38Z
- 产品状态：概念页；未标注 Preview

## 英文原文短摘录（每个来源不超过 25 词）

> “Attachments are uploaded as temporary files and attached to objects via actions.”

## 摘录译文

附件先作为临时文件上传，再通过动作附加到对象。

## 中文要点

- Attachment 是作用于对象的文件参数；用户先上传临时资源，再由 Action 将其绑定到对象附件属性，绑定后才能像对象属性一样访问。
- 配置入口在 Ontology Manager；配套 API 分别承担上传、元数据读取和内容读取，本页作为概念介绍不展开各 endpoint schema。
- 临时附件与对象绑定后的持久引用应区分。失败/取消的清理周期、大小上限和格式处理规则需阅读 API 及用户操作文档。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| temporary file | 临时文件 | 还未通过对象动作持久关联的上传附件 |
| attach via action | 通过动作关联 | 将附件 RID 写入对象附件属性的操作 |
| attachment property | 附件属性 | 对象类型上保存附件引用的属性 |
| persisted attachment | 已持久化附件 | 完成对象关联后可按属性访问的附件 |

## 疑问与待验证项

- 本页没有说明临时文件保留多久，也没有列出对象被删除/属性移除后的清理行为。
- 附件是否可同时绑定多个对象、权限是否完全随对象属性继承，应以对应 API/上传操作专题核验。

## 复刻启示

- 以附件 RID 引用外部二进制存储，数据库只保留元数据和对象关系；通过 Action 审计绑定变更。
- 临时上传资源设置短期 TTL，成功绑定后继承对象授权；未绑定/解绑资源进入异步清理队列。
- 本体画布中的附件属性节点展示基数、媒体类型限制与上传 Action，不在关系图中把文件误画为普通业务对象。
