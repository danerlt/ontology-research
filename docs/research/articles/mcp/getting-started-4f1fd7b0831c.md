<!-- 页面 URL：https://www.palantir.com/docs/foundry/palantir-mcp/getting-started -->
<!-- 研读状态：已完成 -->

# Palantir MCP • Getting started • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/palantir-mcp/getting-started)
- 官方中文来源：尚未确认（配对状态：ambiguous）
- 页面语言：英文
- 主题栏目：palantir-mcp
- 相关性：direct；Palantir MCP 文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:04:54Z
- 产品状态：Palantir MCP 开发者工作流指南；页面称当前默认启用工具搜索。

## 英文原文短摘录（每个来源不超过 25 词）

> “If you need coding assistance, the Palantir MCP can help by searching the Palantir documentation or getting context about your current repository.”

## 摘录译文

需要编程协助时，Palantir MCP 可以搜索 Palantir 文档或读取当前代码仓库上下文。

## 中文要点

- 指南展示 Palantir MCP 的开发辅助用法：在 TypeScript OSDK 仓库查本体对象、在 Python transforms 仓库理解/改写代码、按 RID 分析数据集。
- 示例还提示为 OSDK 应用生成 notional 数据/对象并继续开发、创建 PR；这是开发工作流示例，不等同于对生产本体数据执行写入。
- 工具发现当前默认提供 `search_tools`，开发者可用自然语言询问某项任务的可用工具；完整工具目录和本地/Code Workspace 差异见 Available tools。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Palantir MCP | Palantir MCP | 面向 Foundry 开发与仓库工作流的 MCP 服务。 |
| search_tools | 工具搜索 | 根据任务发现并暴露适用工具。 |
| notional data | 示意数据 | 用于开发上下文的非正式示例数据。 |
| Code Workspace | 代码工作区 | Palantir MCP 可运行的 Foundry 开发环境之一。 |

## 疑问与待验证项

- 页面示例把创建示意数据与新本体对象、PR 放在同一开发流程中；真正的持久化目标和审批边界应通过具体工具 schema 核验。
- 工具搜索默认状态可能随客户端或文档版本变化；客户端需要支持刷新动态发现的工具列表。

## 复刻启示

- 把开发态 MCP 与生产态本体 Agent 连接器分开：开发 MCP 面向 schema/仓库构建，生产连接器只暴露获批的数据读取、Query 和 Action。
- 工具目录按用户权限动态发现，提供工具描述和参数 schema；审计触发者、项目、资源范围以及开发/生产环境。
- 对 notional 与真实数据操作显式区分环境、数据集和审批状态。
