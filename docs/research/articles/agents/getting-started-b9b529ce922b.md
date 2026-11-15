<!-- 页面 URL：https://www.palantir.com/docs/foundry/agent-sdk/getting-started -->
<!-- 研读状态：已完成 -->

# Agent SDK • Getting started • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/agent-sdk/getting-started)
- 官方中文来源：尚未确认（配对状态：ambiguous）
- 页面语言：英文
- 主题栏目：agent-sdk
- 相关性：direct；Agent SDK 文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T14:53:18Z
- 产品状态：按页面现行表述整理；若标注 Preview，相关 API 可能变化。

## 英文原文短摘录（每个来源不超过 25 词）

> “Agent API names must be unique within an Ontology.”

## 摘录译文

Agent 的 API 名称在同一个 Ontology 中必须唯一。

## 中文要点

- 入门流程是在项目中创建 TypeScript Agent 代码仓库，仓库承担 Agent 定义与版本化；发布后的 Agent 可在 Agent Manager 中运行。
- Ontology 绑定是可选项；绑定后才能通过 Ontology 与 Platform SDK 在代码中使用该 Agent，且 API 名称在该 Ontology 内唯一。
- 定义包含模型、工具、Agent 状态 schema、会话参数 schema、会话初始化逻辑及上下文项定义；示例同时区分发布定位符和面向 Ontology 的 API 名称。
- 提交后检查构建状态，通过仓库 Tag 选择语义版本发布；Agent Manager 会话可检查消息、事件和 context items。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Ontology binding | 本体绑定 | 把 Agent 注册到本体，使 SDK 可按 API 名称调用。 |
| agentStateSchema | Agent 状态结构 | 定义 Agent 会话状态的数据结构。 |
| context item | 上下文项 | 作为会话上下文暴露的结构化数据。 |

## 疑问与待验证项

- 该指南以 TypeScript 和特定 Agent SDK 版本为例；不同模型供应商、运行时和授权的细节需要读定制章节。
- 文档没有在本页承诺发布审批规则或运行期权限的完整矩阵。

## 复刻启示

- 在本系统中把 Agent 资源与代码仓库、Ontology 绑定、API 名称、模型/工具配置、状态 schema 和发布版本分开持久化。
- 发布走校验、版本标记和环境发布的治理链；运行会话必须保留可检视的消息/事件/上下文轨迹。
