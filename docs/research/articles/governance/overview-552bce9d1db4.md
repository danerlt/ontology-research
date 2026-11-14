<!-- 页面 URL：https://www.palantir.com/docs/foundry/action-types/overview -->
<!-- 研读状态：已完成 -->

# Action types • Overview • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/action-types/overview)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/action-types/overview)（配对状态：matched）
- 页面语言：英文
- 主题栏目：action-types
- 相关性：direct；本体动作文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T14:53:14Z
- 产品状态：本页未标记 Beta 或弃用状态；核对日期 2026-11-14

## 英文原文短摘录（每个来源不超过 25 词）

> “An action is a single transaction that changes the properties of one or more objects, based on a user-defined logic.”

## 摘录译文

动作是根据用户定义的逻辑，对一个或多个对象属性进行更改的单个事务。

## 中文要点

Action Type 是一组可一次执行的对象、属性值和链接变更定义，也可包含提交后的副作用。它可以声明参数、规则和授权校验，并在多个用户应用间复用。只有用户提交动作后变更才写入 Ontology；统一动作定义让不同应用执行同一套业务校验。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Action | 动作 | 一次事务式业务变更 |
| Action type | 动作类型 | 定义变更内容、参数、规则与提交副作用 |
| Parameter | 参数 | 提交时由用户或调用方提供的标准化输入 |
| Side effect | 副作用 | 动作提交后触发的通知等操作 |
| Writeback dataset | 回写数据集 | 记录包含用户编辑后的对象数据 |

## 疑问与待验证项

- 页面没有在概览中说明对外部系统副作用与对象写入如何保证原子性；需阅读 consistency/isolation 与副作用专题。
- 权限校验、提交审批和冲突处理分别由哪些层完成，需结合 Action 权限与授权文档核实。

## 复刻启示

- 将动作声明建模为可版本化资源：输入参数、对象变更、规则、授权条件、副作用、回滚策略均可审查。
- 执行时先校验权限、参数和业务规则，再事务性写入对象变更，并单独记录通知/Webhook 等副作用状态。
- Agent 工具应调用预定义动作类型，不能直接拼接任意数据库更新语句。
