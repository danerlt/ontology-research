<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/attachment-properties -->
<!-- 研读状态：已完成 -->

# Attachment Property basics • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/attachment-properties)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/v2/ontologies-v2-resources
- 相关性：direct；Ontology REST API v2 附件属性分组入口
- 官方更新时间：2026-11-12T17:46:46.921Z
- 目录核对时间：2026-11-14T14:56:19Z
- 产品状态：分组入口未标注 Preview；所含操作状态需以各子页为准

## 英文原文短摘录（每个来源不超过 25 词）

> “Attachment Properties”

## 摘录译文

附件属性。

## 中文要点

- 这是 REST API v2 文档中的附件属性分组入口。该 URL 未能独立读取正文；官方 v2 API 导航显示本组列出四类操作：列出对象属性的附件、按 RID 读取附件属性、读取附件属性内容、按 RID 读取附件属性内容。
- 同一 API 导航把“Attachment Properties”和“Attachments”分成不同资源组。结合 Attachment Property basics 子页，属性是对文件附件的引用；元数据/属性读取与二进制内容读取因此应作为相关但不同的请求处理。
- 本卡仅总结目录结构和可读取的基础定义，不把子页参数、权限、二进制响应或错误码推断到这个分组页面上。分组的正式短摘录取自[官方 v2 API 导航](https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources)，基础定义见[Attachment Property basics](https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/attachment-properties/attachment-property-basics)。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Attachment Property | 附件属性 | 在对象属性上引用文件附件的特殊属性 |
| Attachment | 附件 | 可读取或上传内容的文件资源；与属性引用分组不同 |
| Property attachment | 属性附件 | 通过某对象的某附件属性关联的附件项 |
| Content endpoint | 内容端点 | 获取附件二进制内容的接口类别 |

## 疑问与待验证项

- 该分组入口本身没有正文，四个操作的路径参数、分页、权限、内容类型和状态码须逐页研读对应端点卡。
- 当前导航中分组名为复数，单项概念页标题为 Attachment Property；目录中文件名或旧版路径可能不同，需以 canonical URL 区分，避免将历史路由误当成当前 v2 页面。
- 仅凭“references a file attachment”不能断言附件存储、保留期、病毒扫描或下载授权策略；需要附件基础、上传和内容端点共同核实。

## 复刻启示

- schema 中可提供 Attachment Property 类型，但对象记录中宜存附件引用/元数据关联，不要将任意大文件字节塞入普通 JSON 属性。
- 后端 API 把关联查询、引用元数据和内容流分层；下载权限在服务端检查，并为内容流设计大小限制、审计和安全扫描策略。这些是本地复刻的工程建议，非该页面直接承诺的 Palantir 机制。
- 画布可将附件属性显示为对象节点上的专用属性标记，连到附件资源/内容面板；不要把它画成两个业务对象之间的普通关系边。
