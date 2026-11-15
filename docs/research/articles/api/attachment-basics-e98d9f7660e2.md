<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/ontology-resources/attachments/attachment-basics -->
<!-- 研读状态：已完成 -->

# Attachment basics (v1) • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/ontology-resources/attachments/attachment-basics)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/ontology-resources/attachments
- 相关性：direct；Ontology API v1 参考，保留兼容性对照并优先关注 v2
- 官方更新时间：2026-11-12T17:46:46.923Z
- 目录核对时间：2026-11-14T14:55:02Z
- 产品状态：基础概念页；未发现可确认的 Preview 或弃用标记

## 英文原文短摘录（每个来源不超过 25 词）

> “Attachments are uploaded as temporary files and attached to objects via actions.”

## 摘录译文

附件先以临时文件形式上传，再通过动作附加到对象。

## 中文要点

- Attachment 是一种作用于对象的文件参数；Ontology Manager 中负责配置附件属性，Action 将暂存文件关联到目标对象。
- 生命周期可分为临时上传、动作提交关联、对象属性读取三步。API 对附件元数据与二进制内容分别提供读取端点，避免把二者混成一个响应。
- 该基础页指向用户文档中的 Upload attachments 操作说明，但本页自身未定义所有端点参数、清理周期或文件大小限制。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Attachment | 附件 | 作为对象参数的文件资源 |
| temporary file | 临时文件 | 完成对象关联前的上传状态 |
| attach to object | 附加到对象 | 经 Action 将附件设置到对象属性 |
| attachment property | 附件属性 | 对象类型中承载附件引用的属性 |

## 疑问与待验证项

- 临时文件何时过期、动作取消或校验失败时如何清理，不在本页展开。
- 页面未标出文件大小、MIME 白名单、恶意文件扫描或多对象复用策略；需查上传附件、读取内容和权限说明。

## 复刻启示

- 定义显式附件状态机（待上传、暂存、已关联、孤立待清理、已删除），关联行为由 Action/事务审计。
- 文件读取权限继承对象访问约束，同时内容下载应单独校验属性和附件资源的授权。
- 实例检查器展示文件名、大小、媒体类型与对象引用，二进制使用受控流式下载，不返回在普通对象属性响应里。
