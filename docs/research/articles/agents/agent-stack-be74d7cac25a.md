<!-- 页面 URL：https://www.palantir.com/docs/foundry/aip/agent-stack -->
<!-- 研读状态：已完成 -->

# Overview • AIP • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/aip/agent-stack)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：aip
- 相关性：direct；AIP Agent 平台文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T14:53:18Z
- 产品状态：Agent in OSDK 与 AIP Logic sessions 在文档中标为 coming soon；核对日期 2026-11-14

## 英文原文短摘录（每个来源不超过 25 词）

> “The Agent Stack models each task as a session.”

## 摘录译文

Agent Stack 将每项任务建模为一个 session（会话）。

## 中文要点

Agent Stack 将工作状态放在可持久会话中：Context items 是带类型的信息单元，Events 承载用户、工具或应用输入，状态机和事件处理器决定如何修改上下文、启动新工作或转入等待审核。会话可跨应用和参与者持续，Agent Builder 用低代码方式配置，Agent SDK 用代码自定义运行逻辑，Agent Manager 负责查看和调试。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Session | 会话 | Agent 针对单项任务的状态、上下文和事件历史 |
| Context item | 上下文项 | 带类型的消息、工具结果、建议或决策 |
| Event | 事件 | 把用户/工具/应用输入送入会话 |
| State transition | 状态转换 | 事件处理器根据当前状态决定后续步骤 |
| Agent Manager | Agent 管理器 | 查看已发布 Agent 和跨应用会话的工具 |

## 疑问与待验证项

- 文档称会话可无限期保留上下文；具体保留期限、归档、删除和敏感上下文清理政策仍需验证。
- Agents in OSDK、AIP Logic 中的会话集成标为 coming soon，不能当成当前可用能力。

## 复刻启示

- 把 Agent 会话实现为持久状态实体，保存版本、状态、输入、类型化上下文项、事件序列和可追踪的转换记录。
- 事件处理使用幂等键和状态版本，避免消息重放造成重复动作；将等待审核、失败和恢复建为显式状态。
- 允许 Workshop、Automate 和 Agent Manager 接入统一的创建会话/发送事件 API，并独立检查会话级权限。
