<!-- 页面 URL：https://www.palantir.com/docs/foundry/action-types/function-actions-overview -->
<!-- 研读状态：已完成 -->

# 动作类型 • 函数支持的动作概述 • Function-backed actions • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/action-types/function-actions-overview)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/action-types/function-actions-overview)（配对状态：matched）
- 页面语言：英文
- 主题栏目：action-types
- 相关性：direct；本体动作文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:02:02Z
- 产品状态：复杂多对象编辑可交由本体函数实现，但仍受动作和函数运行限制。

## 英文原文短摘录（每个来源不超过 25 词）

> “Although function-backed actions are very flexible, they are subject to both action type limits and function execution limits.”

## 摘录译文

函数支持的动作虽然灵活，仍受 Action 类型限制和函数执行限制约束。

## 中文要点

- 简单规则适合直接创建/修改/删除对象与链接；复杂场景包括修改多个相连对象、跨对象读取后计算属性，以及创建多种对象并建立关系。
- 函数承载的逻辑可读取多个对象并产生本体编辑，复杂程度不再局限于单条属性映射。
- 实现依然受 Action 类型上限与函数执行上限约束；调用函数不会绕过系统的规模、安全和运行时限制。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Function-backed action | 函数支持的动作 | 使用函数定义对象变更逻辑的 Action |
| Ontology edit function | 本体编辑函数 | 读取对象并生成本体编辑的函数 |
| Execution limit | 执行限制 | 函数运行时的资源和编辑约束 |

## 疑问与待验证项

- 跨对象逻辑应通过函数实现，但函数的依赖版本、可改对象集合和外部调用风险需要另行评审。
- 选择函数动作前需比较声明式规则与自定义逻辑的可解释性、事务边界和运行上限。

## 复刻启示

- 保留规则动作与函数动作两条路径：简单编辑保持声明式，复杂变更将读集、写集和函数版本纳入评审。
- 运行时把函数产生的对象/链接编辑转成统一差异预览，并应用同一权限和提交条件检查。
