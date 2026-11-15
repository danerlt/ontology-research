<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/ontology-resources/actions/action-basics -->
<!-- 研读状态：已完成 -->

# Action basics (v1) • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/ontology-resources/actions/action-basics)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/ontology-resources/actions
- 相关性：direct；Ontology API v1 端点参考；保留作兼容性对照，并优先关注 v2
- 官方更新时间：2026-11-12T17:46:46.923Z
- 目录核对时间：2026-11-14T14:54:58Z
- 产品状态：v1 Action 基础概念页兼容路由，canonical 页面无 Preview 标记

## 英文原文短摘录（每个来源不超过 25 词）

> “An Action represents one application of an action type.”

## 摘录译文

一个 Action 表示对某个 Action Type 的一次应用。

## 中文要点

本页把 Action 定义为 Action Type 的一次具体应用。API 中的 Action 调用用于向 Ontology 应用变更；因此 Action Type 是可复用的操作定义，而 Action 表示一次带具体参数的执行请求/执行记录。该路由为 `/api/ontology-resources/...` 兼容入口，目录 canonical 指向显式 `/api/v1/.../action-basics` 页面。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Action Type | 动作类型 | 定义可复用的变更及逻辑 |
| Action | 动作 | Action Type 的一次应用，用于请求修改本体 |
| API v1 | API v1 | 本卡所属的 Ontology REST API 版本 |

## 疑问与待验证项

- 基础页没有解释校验、权限、提交标准、异步通知和失败语义；需分别查 Apply Action、Validate Action 及治理文档。
- 文档把 Action 的用途说成“应用变更”，但没有说明此概念页中的 Action 是否指请求体、已提交事件或两者，需以具体操作端点为准。

## 复刻启示

- 画布将 Action Type 建模为操作/命令定义，运行时的 Action 执行单独记录参数、操作者、结果与审计事件。
- Agent 可发现 Action Type 作为工具，但执行前需进行参数验证与授权，并将副作用结果回写到本体。
