<!-- 页面 URL：https://www.palantir.com/docs/foundry/action-types/function-actions-getting-started -->
<!-- 研读状态：已完成 -->

# 动作类型 • 函数支持的动作入门 • Function-backed actions: Getting started • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/action-types/function-actions-getting-started)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/action-types/function-actions-getting-started)（配对状态：matched）
- 页面语言：英文
- 主题栏目：action-types
- 相关性：direct；本体动作文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:02:03Z
- 产品状态：函数支持的 Action 通过单条 Function 规则映射已发布函数，并提供自动升级与来源兼容控制。

## 英文原文短摘录（每个来源不超过 25 词）

> “A function rule cannot be combined with other Ontology rules.”

## 摘录译文

Function 规则不能与其他 Ontology 规则组合使用。

## 中文要点

- 在 Rules 中添加唯一的 Function 规则，选择已发布函数的版本，并把函数输入映射到 Action 参数；该规则不能与其他本体规则同时存在。
- Auto upgrade 将选定最低版本之后的向后兼容 minor/patch 版本纳入依赖范围；0.y.z 开发版本不支持自动升级。
- 自动升级允许仅有函数编辑权限的人改变 Action 的运行行为，即使其无 Action 编辑权限；坏版本可导致执行失败。
- Action provenance 由最低版本的函数来源确定，目前仅覆盖运行时可编辑对象类型；新版本若写出来源范围外类型会失败。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Function rule | 函数规则 | Action 中唯一且不可与其他本体规则组合的规则 |
| Auto upgrade | 自动升级 | 允许依赖后续兼容版本的函数配置 |
| Provenance | 来源范围 | Action 声明的运行时可编辑对象类型范围 |

## 疑问与待验证项

- 函数与 Action 的权限如何在具体部署中配置，需要结合 Function permissions 页面和服务身份授权复核。
- 向后兼容版本范围不等于行为语义兼容；上线前仍应评估副作用、对象范围和回滚路径。

## 复刻启示

- 将 Action 权限与其依赖函数权限联动审查；自动升级默认应受发布审批、版本范围和兼容检查保护。
- 发布校验需比较函数实际可能写入的对象类型与 Action provenance，并阻止越界变更进入运行态。
