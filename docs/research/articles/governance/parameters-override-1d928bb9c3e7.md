<!-- 页面 URL：https://www.palantir.com/docs/zh/foundry/action-types/parameters-override -->
<!-- 研读状态：已完成 -->

# 动作类型 • Parameters • 覆盖 • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/action-types/parameters-override)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/action-types/parameters-override)
- 页面语言：中文
- 主题栏目：action-types
- 相关性：direct；本体动作文档
- 官方更新时间：2026-11-12T17:46:46.935Z
- 目录核对时间：2026-11-14T14:58:25Z
- 产品状态：官方中文页标注为未经验证的 AIP 机器翻译；英文原文为核对依据。

## 英文原文短摘录（每个来源不超过 25 词）

> “Overrides are used to change a parameter's behavior and configuration under specific circumstances.”

## 摘录译文

在特定情况下，覆盖项用于更改参数的行为和配置。

## 中文要点

- 覆盖块由 If 条件和 Then 配置组成；Then 可一起更改参数约束、可见性、必填状态与默认值。
- 一个参数可配置多个覆盖块；若同时满足多个条件，只执行排序最前的一个，覆盖块顺序因此属于业务语义。
- 覆盖条件只能引用表单层级中位于当前参数之前的参数；这使参数顺序决定条件可访问范围。
- 中文官方页属于未经准确性验证的 AIP 机器翻译。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Override block | 覆盖块 | 条件与对应参数配置变更的组合。 |
| Requiredness | 必填性 | 参数是否必须提供有效值。 |
| Form hierarchy | 表单层级 | 决定参数顺序及覆盖可引用参数范围的结构。 |

## 疑问与待验证项

- 覆盖块的顺序编辑是否支持拖动、条件重叠如何诊断以及优先级变更如何审计需在 UI/配置 API 中确认。
- 动态隐藏或可选参数是否仍参与提交条件，需对照提交条件规范测试。

## 复刻启示

- 覆盖规则应支持有序、可解释的 if/then 块，并在设计器中检测遮蔽/永远不可达条件。
- 预览面板应展示给定参数上下文下最终生效的默认值、约束、可见与必填状态，并解释来源块。
