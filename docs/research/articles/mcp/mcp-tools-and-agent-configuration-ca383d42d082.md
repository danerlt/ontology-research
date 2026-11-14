<!-- 页面 URL：https://www.palantir.com/docs/foundry/ontology-mcp/mcp-tools-and-agent-configuration -->
<!-- 研读状态：已完成 -->

# Ontology MCP • MCP tools and agent configuration • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/ontology-mcp/mcp-tools-and-agent-configuration)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：ontology-mcp
- 相关性：direct；Ontology MCP 文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:04:50Z
- 产品状态：待核对 Beta、预览、弃用或更名信息

## 英文原文短摘录（每个来源不超过 25 词）

> “Use the Agent tool description field in the Ontology Manager application to update the description the agent sees when using the action as a tool.”

## 摘录译文

“在 Ontology Manager 中设置 Agent 工具描述，提供 Agent 调用该 Action 工具时可见的说明。”

## 中文要点

本页说明 Agent 工具不只依靠 API 名：Action 可有面向 Agent 的工具说明，解释何时调用、如何取得输入。组合多个工具时，可用可复用的 skill 写出先搜索、检查匹配、必要时再创建的步骤，避免重复数据。该页还展示通过 OAuth bearer token 连接 MCP，并将结构化本体结果用 Adaptive Cards 呈现。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Agent tool description | Agent 工具说明 | 给 Agent 的 Action 用法提示和参数准备指引 |
| Skill | 工作流指令 | 约束多步工具使用顺序的可复用指令集 |
| Bearer token | 持有者令牌 | MCP 客户端请求携带的访问 token |
| Adaptive Card | 自适应卡片 | 将结构化工具结果呈现为图卡的 UI 格式 |

## 疑问与待验证项

- 工具说明是帮助模型正确选择/使用能力的上下文，不是服务端安全边界；仍需 OAuth、应用限制和底层授权强制校验。
- 示例涉及多个客户端生态集成；token 放置、redirect 和模型数据流需按具体客户端另行确认。

## 复刻启示

- Action 定义应带有用户可读说明、参数 schema、可见权限和副作用提示；Agent 指令可声明“先检索再创建”的业务流程。
- 当前原型有 Agent allowlist 和 Action 参数 schema，但尚未设置每个 Action 的 agent-facing description、工作流技能或结构化卡片输出；服务端 allowlist 不可被说明文本替代。
