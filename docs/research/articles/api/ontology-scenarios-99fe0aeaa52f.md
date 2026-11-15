<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/ontology-scenarios -->
<!-- 研读状态：已完成 -->

# Ontology Scenario basics • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/ontology-scenarios)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/v2/ontologies-v2-resources
- 相关性：direct；Ontology REST API v2 参考
- 官方更新时间：2026-11-12T17:46:46.922Z
- 目录核对时间：2026-11-14T14:57:30Z
- 产品状态：基础概念页（无 Preview 标注）

## 英文原文短摘录（每个来源不超过 25 词）

> “An OntologyScenario represents a sandboxed data-fork of the ontology.”

## 摘录译文

Ontology Scenario 表示本体数据的隔离分叉。

## 中文要点

- 情景允许在不影响生产数据的隔离本体副本中进行模拟，并可在该副本上读写，之后将改动合并回本体。
- 这是 API 概念入口，没有定义冲突解决、权限审批、保留期限或合并粒度；这些要从其他端点和管理文档补齐。
- 场景“合并回本体”与“rebase 到 scenario base 的最新数据”是不同操作，不能在界面流程中合并为一个按钮。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Scenario | 情景 | 与生产数据隔离的本体副本 |
| Data fork | 数据分叉 | 在隔离副本上模拟对象数据变化 |
| Merge | 合并 | 将情景变更回写至本体 |

## 疑问与待验证项

- 合并是一次性提交还是支持按对象/类型选择变更，本文没有说明。
- 该概念页没有说明 scenario 是否覆盖本体定义变更；后续 API 示例更多体现对象和链接实例的模拟编辑。

## 复刻启示

- 把草稿情景视为隔离的数据变更分支，允许先查看、编辑、评估冲突再合并；合并授权和审批记录需由本地产品显式实现。
- 将情景生命周期、分支基线、冲突与对象数据差异分别建模，并在 UI 里区分 Rebase 与 Merge。
