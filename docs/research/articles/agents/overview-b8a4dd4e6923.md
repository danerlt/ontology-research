<!-- 页面 URL：https://www.palantir.com/docs/foundry/agent-manager/overview -->
<!-- 研读状态：已完成 -->

# Agent Manager • Overview • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/agent-manager/overview)
- 官方中文来源：尚未确认（配对状态：ambiguous）
- 页面语言：英文
- 主题栏目：agent-manager
- 相关性：direct；Agent Manager 文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:04:28Z
- 产品状态：本页未标记 Beta 或弃用状态；核对日期 2026-11-14

## 英文原文短摘录（每个来源不超过 25 词）

> “Access to an agent does not automatically grant access to every session.”

## 摘录译文

拥有 Agent 的访问权限，并不自动意味着拥有每个会话的访问权限。

## 中文要点

Agent Manager 是发布后 Agent 的浏览、启动、会话监控与行为调查入口。用户能查看自己有权访问的 Agent、版本和元数据，启动会话、发送消息或其他事件，并按版本/来源筛选会话。详情可检查上下文项、事件、状态历史、trace 和日志。发布的 Agent 是 Compass 资源；会话另外受强制和自主访问条件约束。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Published agent | 已发布 Agent | 可启动会话的资源版本 |
| Session access | 会话访问权 | 独立于 Agent 本身访问权限的授权条件 |
| Mandatory control | 强制控制 | 组织或标记等不可由资源成员关系绕过的条件 |
| Session trace | 会话追踪 | 用于调查 Agent 执行步骤的运行记录 |

## 疑问与待验证项

- Agent 资源和会话权限独立；界面、API 和审计查询都必须对每个会话再授权，不能沿用 Agent 的可见性。
- 日志/trace 与上下文项可能包含用户输入或工具输出，保留和脱敏策略需要继续查安全文档。

## 复刻启示

- 将 Agent、AgentVersion 和 AgentSession 建模为不同资源；会话列表支持按来源应用和版本过滤。
- 会话详情应按时间展示输入、事件、上下文项、状态变化、工具调用与结果。
- 查看 Agent 的权限不能继承为会话访问权；会话内容执行单独的授权策略和审计。
