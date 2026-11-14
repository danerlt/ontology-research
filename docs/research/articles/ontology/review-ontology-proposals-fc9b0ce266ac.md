<!-- 页面 URL：https://www.palantir.com/docs/foundry/ontologies/review-ontology-proposals -->
<!-- 研读状态：已完成 -->

# Ontologies • Branching the ontology • Review ontology proposals • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/ontologies/review-ontology-proposals)
- 官方中文来源：尚未确认（配对状态：ambiguous）
- 页面语言：英文
- 主题栏目：ontologies
- 相关性：direct；本体管理与治理文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:01:36Z
- 产品状态：Global Branching 与 Legacy ontology branches 流程不同；旧分支条目标记为 Legacy；核对日期 2026-11-14

## 英文原文短摘录（每个来源不超过 25 词）

> “An ontology proposal is analogous to a Pull Request in a version control system.”

## 摘录译文

Ontology proposal 类似于版本控制系统中的 Pull Request。

## 中文要点

Proposal 用于审查和批准分支中的变更，再将它们合入 `main`。页面将提案分为我创建的、分配给我、审查中、已合并和已关闭等列表，并提供提案概览、预览状态、变更审查与变更日志。审查人可逐项或批量批准/拒绝任务，并评论和查看索引状态。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Ontology proposal | 本体提案 | 评审并合并分支本体资源变更的对象 |
| Task | 评审任务 | 对应一个需要处理的本体资源变更 |
| Preview status | 预览状态 | 显示对象类型索引进度和是否可预览 |
| Changelog | 变更日志 | 按作者和资源展开的变更历史 |
| Approval policy | 审批策略 | 决定谁可以批准受保护资源的规则 |

## 疑问与待验证项

- 新的 Global Branching proposal 与 Legacy ontology branch 的创建和合并规则不同；旧流程中可合并的角色边界更宽，实施时应按当前主流程设计。
- 本页说明默认批准人是资源 Editor/Owner；迁移至受保护项目后按项目策略审批，具体审批策略配置需另查。

## 复刻启示

- 把分支和提案建模为独立实体，关联变更任务、审阅者、状态、预览索引结果与完整变更日志。
- 只允许在满足资源/项目审批规则后把提案合入主版本；拒绝、关闭、重开和批量审批都留审计记录。
- 提供差异视图、任务级评论、预览状态和按资源定位的变更日志，降低审查者的上下文切换。
