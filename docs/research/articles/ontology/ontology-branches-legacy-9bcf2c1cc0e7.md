<!-- 页面 URL：https://www.palantir.com/docs/foundry/ontologies/ontology-branches-legacy -->
<!-- 研读状态：已完成 -->

# Ontologies • Branching the ontology • Ontology branches [Legacy] • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/ontologies/ontology-branches-legacy)
- 官方中文来源：无精确对应页面；参照英文原文
- 页面语言：英文
- 主题栏目：ontologies
- 相关性：direct；本体管理与治理文档
- 官方更新时间：页面未提供
- 目录核对时间：2026-11-15
- 产品状态：Legacy；启用 Global Branching 后不能再创建旧版本体分支，应使用全局分支。

## 英文原文短摘录（每个来源不超过 25 词）

> “Ontology branches (formerly known as ontology proposals) are being sunset.”

## 摘录译文

本体分支（以前称为本体提案）正在退役。

## 中文要点

- 旧提案把一组本体资源编辑放在从 Main 派生的隔离分支，自动创建 proposal 记录标题、描述和评审；旧工作流包括建分支、请求评审、审核和发布。
- 每个修改的本体实体作为独立任务评审，支持逐任务批准/拒绝和评论；旧权限体系下审阅者名单只是协作记录，不足以保护资源。
- 迁移到 Global Branching 后，数据源和本体变更可在统一分支工作流中管理，能在支持的下游应用验证。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| legacy branch | 遗留分支 | 已退役路线中的本体专用分支。 |
| proposal | 提案 | 旧机制中承载一组本体变更评审的记录。 |
| task-level review | 任务级评审 | 按受影响的单个资源审批变更。 |

## 疑问与待验证项

- 该页面同时包含旧流程细节；如与当前 Global Branching 文档冲突，应以当前分支文档为准。
- Reviewer 名单不等于权限保护；真正的编辑权和合并权限必须由资源授权及分支策略校验。

## 复刻启示

- 实现可移植的分支、proposal、资源级任务、评论与审核状态，但对外标识当前工作流而非复刻已退役标签。
- 发布检查要求授权、资源依赖、冲突、风险确认和审计全部通过；审批人列表不能替代访问控制。
