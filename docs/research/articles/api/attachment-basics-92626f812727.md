<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/attachments/attachment-basics -->
<!-- 研读状态：已完成 -->

# Attachment basics (v2, latest) • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/attachments/attachment-basics)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/ontologies-v2-resources/attachments
- 相关性：direct；Ontology REST API v2 参考
- 官方更新时间：2026-11-12T17:46:46.922Z
- 目录核对时间：2026-11-14T14:53:38Z
- 产品状态：按当前 API 参考整理；批量与分支能力以页面限制为准。

## 英文原文短摘录（每个来源不超过 25 词）

> “An Attachment is a file that acts like a parameter of an object.”

## 摘录译文

Attachment 是作为对象参数存在的文件。

## 中文要点

- Attachment 是对象关联的文件资源；文件先上传为临时文件，再通过 Action 挂载到对象。
- 附件在 Ontology Manager 中配置；因此附件具有对象上下文，不等同于只存一个下载 URL 的普通属性。
- 基础页给出概念与工作流概览，上传、挂载和下载端点分别处理具体动作。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| temporary file | 临时文件 | 上传后尚未挂载到对象的文件。 |
| attach via action | 通过 Action 挂载 | 用本体动作把文件关联到对象。 |
| object parameter | 对象参数 | Attachment 作为对象关联的数据输入。 |

## 疑问与待验证项

- 文件在临时上传与 Action 挂载之间的保留时间没有说明。
- 上传后被 Action 拒绝或取消时临时文件何时清理，需查上传文档。

## 复刻启示

- 附件流程采用临时上传→Action 校验/挂载→对象关系持久化→按权限读取，界面展示明确的生命周期状态。
- 保留附件 RID、父对象、属性、上传者、MIME、大小与挂载动作的审计关联。
