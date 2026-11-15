<!-- 页面 URL：https://www.palantir.com/docs/foundry/palantir-mcp/example-mcp-workflows -->
<!-- 研读状态：已完成 -->

# Palantir MCP • Example MCP workflows • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/palantir-mcp/example-mcp-workflows)
- 官方中文来源：目录中未发现对应中文页面
- 页面语言：英文
- 主题栏目：palantir-mcp
- 相关性：direct；Palantir MCP 文档
- 官方更新时间：页面未提供
- 目录核对时间：2026-11-15
- 产品状态：Palantir MCP 开发者工作流示例；结构编辑须经 proposal 评审。

## 英文原文短摘录（每个来源不超过 25 词）

> “The Palantir MCP is able to provide ontology and code-snippet context to your agent loop.”

## 摘录译文

Palantir MCP 能为 Agent 循环提供本体与代码片段上下文。

## 中文要点

- Palantir MCP 可为 IDE Agent 提供代码库、Foundry 项目、本体资源和 SDK 上下文，帮助导航代码和平台资源。
- 工具可搜索数据集、执行 SQL 并创建样例数据集，但文档说明它不能覆盖已有数据集。
- 本体探索可搜索对象类型、动作和函数；模型结构更改可创建 proposal 并修改本体，但要经 proposal review 才成为持久更改。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Palantir MCP | Palantir MCP | 面向本体构建者/IDE Agent 的平台开发工具服务。 |
| proposal review | 提案评审 | 将本体结构修改纳入正式版本前的人审流程。 |
| ontology structure | 本体结构 | 对象类型、链接类型和动作等定义层资源。 |

## 疑问与待验证项

- Palantir MCP 和 Ontology MCP 分工不同：前者构建/编辑结构与开发资源，后者供外部 Agent 查询/执行本体应用工具。
- 不能把创建示例数据集当成生产写回能力；对任意外部系统的动作也需单独连接器与授权策略。

## 复刻启示

- 将“建模/发布 Agent”和“Agent 运行时消费本体”拆成不同权限面与工具服务器。
- Agent 自动提议模式变更时先生成结构化差异与影响分析，阻止直接写主版本，并要求通过资源级评审再部署。
