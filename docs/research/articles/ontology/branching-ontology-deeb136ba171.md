<!-- 页面 URL：https://www.palantir.com/docs/foundry/ontologies/branching-ontology -->
<!-- 研读状态：已完成 -->

# Ontologies • Branching the ontology • Overview • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/ontologies/branching-ontology)
- 官方中文来源：未确认对应页
- 页面语言：英文
- 主题栏目：ontologies
- 相关性：direct；本体管理与治理文档
- 官方更新时间：页面未提供
- 目录核对时间：2026-11-15
- 产品状态：当前页面讲全局分支；旧版 ontology branches/proposals 已进入弃用迁移路线。

## 英文原文短摘录（每个来源不超过 25 词）

> “The ontology integrates with Global Branching to enable safe, isolated development of ontology resources.”

## 摘录译文

本体与全局分支集成，以便安全、隔离地开发本体资源。

## 中文要点

- 分支把本体变更与主版本隔离；本体变更进入 Global Branching proposal 后，会产生跟踪本体资源变更、评审信息和说明的 ontology proposal。
- 可从 Ontology Manager 创建分支，或通过保存对话框将当前改动另存为分支；文档说明本体分支基于 main。
- 工作流涵盖资源新增/修改、索引、rebase、冲突处理、评审和合并，并有资源保护及已知限制。旧版分支说明明确建议迁移到 Global Branching。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Global Branching | 全局分支 | 统一管理数据和本体变更的分支工作流。 |
| ontology proposal | 本体提案 | 跟踪分支中将合并的本体变更与评审元数据。 |
| rebase | 变基 | 将分支更新到新的主线基准并处理冲突。 |

## 疑问与待验证项

- 分支内哪些资源可以索引、哪些下游应用支持验证，受产品当前功能和部署环境限制，需要逐项核对。
- 本地复刻应把“评审记录”与“保护机制”分开设计；仅记录 reviewers 并不能阻止未授权发布。

## 复刻启示

- 为本体资源建立分支快照、变更集、冲突状态和评审决议；发布时校验主线版本是否已变化。
- 评审界面按资源列出新增/修改/删除及影响对象，采用明确的合并策略并记录操作者与时间。
