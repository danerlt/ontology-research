<!-- 页面 URL：https://www.palantir.com/docs/foundry/ontology-mcp/example-mcp-workflows -->
<!-- 研读状态：已完成 -->

# Ontology MCP • Example MCP workflows • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/ontology-mcp/example-mcp-workflows)
- 官方中文来源：目录中未发现对应中文页面
- 页面语言：英文
- 主题栏目：ontology-mcp
- 相关性：direct；Ontology MCP 文档
- 官方更新时间：页面未提供
- 目录核对时间：2026-11-15
- 产品状态：OMCP 使用模式说明；包含桌面 Agent、第三方 Agent 框架和无头 Agent。

## 英文原文短摘录（每个来源不超过 25 词）

> “Ontology MCP can serve as the memory and tracking layer for headless agent workflows.”

## 摘录译文

Ontology MCP 可作为无界面 Agent 工作流的记忆与跟踪层。

## 中文要点

- 桌面助手可通过 OMCP 连接组织本体，读取共享事实、执行受治理操作，让用户和 Agent 在同一数据/逻辑/动作基础上协作。
- ADK、Microsoft Agent Framework、OpenAI SDK 等外部 Agent 可以把 OMCP 当成标准 MCP 系统接入，并与其他 MCP Server 组合。
- 无头 Agent 可响应本体变化或定时运行；通过 OMCP 读写业务对象后，执行和状态会进入组织本体，从而可追踪和审计。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| desktop agent | 桌面 Agent | 在用户桌面或协作产品中调用本体工具的 Agent。 |
| headless agent | 无头 Agent | 不提供交互界面、由事件或计划触发运行的 Agent。 |
| source of truth | 事实来源 | 组织业务事实与工作状态的权威数据层。 |

## 疑问与待验证项

- 示例强调执行留痕，但无头自动运行仍需要限频、异常处理、幂等和人工升级策略，细节由具体系统决定。
- “把本体作为 Agent memory”是工作流模式，不代表向通用长期记忆自动写入所有 prompt 对话。

## 复刻启示

- 将 Agent 会话、任务、结果和行动引用建模为可审计业务数据；记录由哪个 Agent/用户在何种事件下发起。
- 支持桌面人工协作和无头定时/事件工作流两种触发方式，并复用相同的对象、动作授权与审计管道。
