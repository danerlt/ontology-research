<!-- 页面 URL：https://www.palantir.com/docs/zh/foundry/ontology-manager/save-changes -->
<!-- 研读状态：已完成 -->

# 本体管理器 • Change management • 保存对Ontology的更改 • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/ontology-manager/save-changes)
- 官方中文来源：[https://www.palantir.com/docs/zh/foundry/ontology-manager/save-changes](https://www.palantir.com/docs/zh/foundry/ontology-manager/save-changes)
- 页面语言：中文
- 主题栏目：ontology-manager
- 相关性：direct；本体管理器文档
- 官方更新时间：2026-11-12T17:46:46.935Z
- 目录核对时间：2026-11-15
- 产品状态：官方中文页提示其为未经验证的 AIP 机器翻译；已对照英文原文。

## 英文原文短摘录（每个来源不超过 25 词）

> “For these Ontology changes to be available for others and reflected in user-facing applications, you must save your changes.”

## 摘录译文

若要让他人可用并让更改反映到面向用户的应用中，必须保存本体更改。

## 中文要点

- 编辑先保存在本地工作状态，完成资源级审阅并保存后才对他人和应用生效。
- 审阅对话框汇总错误与警告：错误阻止保存，警告可提示风险但不一定阻止保存；资源可单独丢弃，也可整体丢弃。
- 如果他人先保存了更新，需要同步并合并对方更改；冲突时选择保留新主版本或采用当前工作改动。破坏性变更可能要求显式确认影响。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| work-in-progress | 进行中工作状态 | 尚未发布给其他用户的编辑状态。 |
| review edits | 审阅更改 | 在提交前查看资源变更、错误与警告的步骤。 |
| merge conflict | 合并冲突 | 并行修改无法自动合并时需要人工决策的情况。 |

## 疑问与待验证项

- 文档区分阻塞错误和非阻塞警告，但具体哪些属性/链接变化属破坏性变化由单独规则定义。
- 该页保存工作流与当前 Global Branching 联动的细节需结合分支文档，不应只实现一个无审核的“保存”按钮。

## 复刻启示

- 以资源为单位呈现待发布差异和错误；先校验引用、主键、授权和删除影响，再允许提交评审。
- 支持草稿、评审、冲突解决、拒绝、合并、丢弃和审计历史；发布时保留版本基准，避免覆盖他人新版本。
