<!-- 页面 URL：https://www.palantir.com/docs/foundry/action-types/submission-criteria -->
<!-- 研读状态：已完成 -->

# Action types • Submission criteria • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/action-types/submission-criteria)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/action-types/submission-criteria)（配对状态：matched）
- 页面语言：英文
- 主题栏目：action-types
- 相关性：direct；动作提交治理文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:01:58Z
- 产品状态：旧称 validations；支持用户、参数及 Scenario 执行上下文条件。

## 英文原文短摘录（每个来源不超过 25 词）

> “Submission criteria are the conditions that determine whether an action can be submitted.”

## 摘录译文

提交标准是决定一个动作是否可以提交的一组条件。

## 中文要点

- 提交标准将业务规则编码到动作提交权限和数据质量治理中；条件可读取提交者、用户组/Multipass 属性、动作参数、对象及关系信息，并通过嵌套逻辑运算符组合。每个 Action Type 各自拥有独立标准，且不等同于“谁能编辑动作定义”。
- 条件模板包括 Current user、Parameter 和 Execution context。执行上下文可判断动作是否在任意 Ontology Scenario 中运行，但不识别具体哪个 Scenario；附件和对象集参数不受支持。
- 可以配置 all/any/none 等逻辑组合和失败消息，向用户解释动作被阻止的原因；Ontology Manager test run 可用指定参数试算条件。
- 文档特别警告：不要对组、marking 或 organization membership 使用 NOT。Scoped token 可能不包含相应属性，导致否定条件意外通过并扩大授权。更换参数后，使用该参数的所有条件需要重新配置。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| submission criteria | 提交标准 | 决定动作能否提交的一组可组合条件。 |
| execution context | 执行上下文 | 条件可识别动作是否在某个 Ontology Scenario 中运行。 |
| scoped token | 范围受限令牌 | 可能只携带用户部分权限属性的令牌。 |
| test run | 试运行 | 在 Ontology Manager 用给定参数检查条件结果。 |

## 疑问与待验证项

- Criteria 使用的用户属性与参数值在提交时的可见性、脱敏和失败原因暴露范围需要结合权限文档验证。
- Scenario 上下文只回答“是否在 Scenario 中”，不能表达具体 Scenario 身份；若业务需要按 Scenario 逐项授权，应通过其他建模方式补足。

## 复刻启示

- 将条件编辑器实现为可版本化表达式树，支持当前用户、组、对象/关系参数、执行上下文、比较器和嵌套逻辑；发布前做类型检查、范围授权检查与静态 NOT 风险检测。
- 让用户可用参数试算并查看逐条件通过/拒绝路径，但提交时在服务端重新评估，不能信任前端预览结果。
- 为每个根条件配置稳定、可理解的失败说明；表达式参数类型改变时列出受影响节点并强制重新验证。
