<!-- 页面 URL：https://www.palantir.com/docs/foundry/agent-sdk/advanced-customization -->
<!-- 研读状态：已完成 -->

# Agent SDK • Advanced customization • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/agent-sdk/advanced-customization)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：agent-sdk
- 相关性：direct；Agent SDK 文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:04:33Z
- 产品状态：Agent SDK 高级扩展指南；页面未标注 Preview。

## 英文原文短摘录（每个来源不超过 25 词）

> “In the Agent SDK, an agent is a state machine, processing queued events deterministically and updating its state.”

## 摘录译文

在 Agent SDK 中，Agent 是一个状态机，以确定性的方式处理排队事件并更新自身状态。

## 中文要点

- 高级扩展覆盖动态系统提示词、模型选择/自定义、上下文项、工具以及状态机事件/效果。
- 上下文项使用强类型数据和 render 函数提供模型上下文；异步加载时可先呈现 pending，完成后再继续生成。
- 事件按队列顺序确定性处理状态与上下文；Effects 在事件处理器之外执行异步工作，并在完成时派发事件。工具可随 Agent 状态变化，长任务可显示进度，也可通过人机交互事件等待用户答复。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Context item | 上下文项 | 类型化的会话数据及面向模型的呈现形式。 |
| Event | 事件 | 触发状态或上下文变化的有类型消息。 |
| Effect | 效果 | 在状态机外执行的异步工作。 |
| Agent state machine | Agent 状态机 | 按队列处理事件并更新会话状态的执行模型。 |

## 疑问与待验证项

- 该指南未承诺异步 Effect 的重试、超时、 恰好一次执行保证或外部副作用回滚语义。
- 自定义模型适配器如何继承 Foundry 的模型权限、审计与速率限制，需要结合运行环境核验。

## 复刻启示

- 把 Agent 会话建模为强类型状态、事件和 Effect 队列；对外部调用保留可观测状态和失败恢复信息。
- 用于本体写入的工具先进入待确认上下文，用户确认后再派发执行事件；把审批与模型文本生成解耦。
- 工具可根据项目权限和当前状态动态暴露；界面显示工具参数、进度事件、结果上下文和审计链。
