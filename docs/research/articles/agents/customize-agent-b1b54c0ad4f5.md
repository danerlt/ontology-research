<!-- 页面 URL：https://www.palantir.com/docs/foundry/agent-sdk/customize-agent -->
<!-- 研读状态：已完成 -->

# Agent SDK • Customize agents • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/agent-sdk/customize-agent)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：agent-sdk
- 相关性：direct；Agent SDK 文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:04:32Z
- 产品状态：Agent SDK 入门定制指南；涉及的 provider 与 SDK 行为以当前文档为准。

## 英文原文短摘录（每个来源不超过 25 词）

> “An Agent SDK definition combines a model, a system prompt, and tools.”

## 摘录译文

Agent SDK 定义由模型、系统提示词和工具组合而成。

## 中文要点

- Agent SDK 的 Agent 定义包含模型、系统提示词和工具，并在持久化会话中响应消息。
- 工具由名称、描述、参数 schema 和 execute 函数组成；工具结果以 context item 返回给模型。页面示例通过 OSDK 读取对象、调用 Function，并把结果写入上下文。
- Agent state 与 session 创建参数采用强类型 schema；工具、Ontology 交互、模型和提示词均可在代码定义中组合。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| system prompt | 系统提示词 | 控制 Agent 回答行为的指令文本。 |
| tool | 工具 | 模型可请求执行的函数或动作。 |
| context item | 上下文项 | 工具向下一轮模型请求提供的数据。 |
| durable session | 持久会话 | 跨消息保留会话状态的 Agent 会话。 |

## 疑问与待验证项

- 工具执行回传 context item，页面没有规定内容脱敏、字段权限裁剪或敏感值审计的统一策略。
- 本页示例包含读取和 Function；写操作如何确认、重试和回滚需结合 Action 及人机审批文档。

## 复刻启示

- 把本体 Function/对象读取包装为有类型工具；限制可读字段并把来源对象 RID、查询参数及结果摘要附在上下文证据中。
- 区分查询型工具与会修改本体数据的 Action 工具；写操作需参数校验、权限检查和用户确认。
- 持久会话保存 Agent 版本、状态 schema 版本和上下文证据，便于重放与审计。
