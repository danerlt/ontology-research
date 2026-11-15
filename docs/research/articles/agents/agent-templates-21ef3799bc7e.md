<!-- 页面 URL：https://www.palantir.com/docs/foundry/agents/agent-templates -->
<!-- 研读状态：已完成 -->

# Pro-code agents • Core concepts • Pro-code agent templates • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/agents/agent-templates)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：agents
- 相关性：direct；Agent 文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:05:16Z
- 产品状态：当前模板覆盖 Claude Agent SDK、OpenAI Agents SDK 与 Google ADK，并提供 OSDK、OMCP、Palantir MCP 公共连接配置。

## 英文原文短摘录（每个来源不超过 25 词）

> “The template keeps your repository focused on agent logic rather than platform plumbing.”

## 摘录译文

模板让代码仓库专注于 Agent 逻辑，而不是平台接线工作。

## 中文要点

- 三类框架模板共享参数 schema、默认 MCP 配置和发布流程，但 Agent 循环与自定义工具写法各异。
- 仓库将入口及参数、system prompt、自定义工具、公共工具库、打包脚本分层；自定义 MCP 应放独立文件以减少模板升级冲突。
- Palantir MCP 默认使用 tool search 按需发现获准工具以节省上下文，也可改为启动时加载完整允许目录。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| agent template | Agent 模板 | 生成含运行入口、公共连接和发布脚本的代码仓库。 |
| AgentArguments | Agent 参数 schema | 定义每次调用接收的结构化输入。 |
| tool search | 工具搜索 | Agent 运行中按需发现可用工具的机制。 |

## 疑问与待验证项

- - 本页以 TypeScript 模板为主，未说明各运行环境的完整版本兼容策略；升级时应记录模板与 SDK 版本。
- - 可用工具受权限和连接配置影响，界面展示内容应来自服务端授权结果。

## 复刻启示

- - 将 Agent runtime adapter、本体工具和外部 MCP 工具分层；参数 schema 版本化并在发布时固化。
- - 提供按需搜索/完整目录两种工具加载模式，记录权限来源、参数、结果状态与耗时。
