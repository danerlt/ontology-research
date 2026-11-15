<!-- 页面 URL：https://www.palantir.com/docs/zh/foundry/action-types/overview -->
<!-- 研读状态：已完成 -->

# 动作类型 • 概述 • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/action-types/overview)
- 官方中文来源：尚未确认（配对状态：not_applicable）
- 页面语言：中文
- 主题栏目：action-types
- 相关性：direct；本体动作文档
- 官方更新时间：2026-11-12T17:46:46.935Z
- 目录核对时间：2026-11-14T14:58:19Z
- 产品状态：官方中文页标注为未经验证的 AIP 机器翻译；英文原文为核对依据。

## 原文短摘录与翻译

> 英文原文：An action is a single transaction that changes the properties of one or more objects, based on a user-defined logic.

> 中文译文：Action 是一个基于用户定义逻辑、用于更改一个或多个对象属性的单一事务。

## 摘录译文

以上为英文短摘录及中文译文。官方中文页面为 AIP 机器翻译，准确性未经验证。

## 中文要点

- Action 让业务用户以目标为中心提交对象、属性和链接的变更；Action Type 则定义可执行的变更集合、参数、规则和提交后的副作用。
- 规则可在提交时修改属性、创建/修改链接或创建对象；参数为规则提供外部输入，提交条件决定当前提交是否有效。
- Action Type 可包含通知等副作用，也可与 Workshop、Object Views、Object Explorer 等消费端集成。
- 英文文档是功能语义的依据；官方中文版本页明确提示 AIP 机器翻译未经准确性验证。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Action | 操作 | 一次应用本体变更的事务性执行。 |
| Action type | 操作类型 | 描述动作输入、规则、允许变更和副作用的定义。 |
| Side effect | 副作用 | 随动作提交触发的通知或其他外部行为。 |

## 疑问与待验证项

- “单一事务”对跨多个对象写入的原子性与外部副作用顺序需结合具体动作实现/存储后端文档核验。
- 预验证、权限检查和最终写入在各执行路径上是否采用相同快照，需要与隔离级别文档交叉确认。

## 复刻启示

- 把操作类型作为一等本体资源建模：参数、规则、提交条件、读写集合、副作用、权限及发布版本均可独立追踪。
- 把 Action 执行界定为校验、授权、持久写入与副作用阶段，并为每阶段记录状态、失败原因和可恢复策略。
