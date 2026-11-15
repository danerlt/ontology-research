<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/attachments -->
<!-- 研读状态：已完成 -->

# Attachment basics (v2, latest) • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/attachments)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/v2/ontologies-v2-resources
- 相关性：direct；Ontology REST API v2 附件资源分组入口
- 官方更新时间：2026-11-12T17:46:46.922Z
- 目录核对时间：2026-11-14T14:56:25Z
- 产品状态：分组入口未标注 Preview；各操作页状态以子页为准

## 英文原文短摘录（每个来源不超过 25 词）

> “Attachment basics”

## 摘录译文

附件基础

## 中文要点

- 该 URL 是 Ontology REST API v2 中通用附件资源的分组入口，但页面正文无法独立读取。官方本体 API 导航将附件分组下的操作列为上传附件、按 RID 读取元数据、按 RID 读取内容；用户文档另说明附件先上传为临时文件，再通过 Action 关联对象。
- 这组接口面向附件资源本身；“Attachment Properties”分组则通过对象类型、主键和属性访问某对象所关联的附件。两种路径分别适合全局附件 RID 读取与对象属性上下文读取。
- 本卡只记录分组结构。上传参数、暂存期限、内容响应格式和授权边界须分别以具体端点页为准。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Attachments | 附件 | 文件资源及其相关 API 操作的分组 |
| Attachment RID | 附件 RID | 附件资源的唯一标识符 |
| Attachment property | 附件属性 | 对象上关联附件的属性，属于另一 API 分组 |
| Temporary upload | 临时上传 | 文件尚未通过 Action 绑定对象的阶段 |

## 疑问与待验证项

- 分组入口 URL 无可读正文，导航信息来自[官方 v2 Ontology API 页面](https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources)；目前能核实的元数据和内容行为分别见子页。
- 上传端点的暂存清理时限、临时 RID 授权、重试及失败清理需查看 Upload Attachment 与上传用户指南。
- 通用 RID 接口是否仍要求调用者具备源对象可见权限，分组目录没有说明。

## 复刻启示

- 按资源分组组织后端路由和权限策略：附件资源 API 与对象属性关联 API 分开；调用日志中同时记录附件 RID 和对象关联上下文（若有）。
- UI 将“对象属性附件列表”与“附件资源管理”分开展示，避免用户误以为全局附件列表等同于本体对象关系。
- 上传临时态与关联态应显式建模，并在目录、审计和存储生命周期中可追踪；具体过期策略由复刻系统自行定义。
