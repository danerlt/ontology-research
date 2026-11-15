<!-- 页面 URL：https://www.palantir.com/docs/foundry/agents/create-agent -->
<!-- 研读状态：已完成 -->

# Pro-code agents • How-to guides • Build a pro-code agent in Foundry • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/agents/create-agent)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：agents
- 相关性：direct；Agent 文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:05:32Z
- 产品状态：向导覆盖选择模板、配置本体绑定和 API 名称、实现 Agent、本地试跑/构建、打版本发布和调用；日志范围受权限和环境影响。

## 英文原文短摘录（每个来源不超过 25 词）

> “This guide walks you through building a pro-code agent, from creating the repository to publishing the agent as a Foundry function.”

## 摘录译文

本指南介绍如何从创建代码仓库开始，构建 pro-code Agent 并将其发布为 Foundry function。

## 中文要点

- 前置条件包括可读写的 Ontology 访问和创建代码仓库权限；创建时选择框架模板、仓库位置、本体绑定与 Agent API name。
- 生成仓库包含 OSDK、OMCP 和 Palantir MCP 配置；可传 JSON 参数本地试跑，发布前运行 build。
- 发布版本后由 CI 部署成异步 function；主线可通过仓库界面或 Git tag 发布，分支预发布应遵循 Global Branching 页面规定的仓库 UI 流程。
- Workflow Lineage 可关联执行日志；查看范围受运行身份、log access、markings 和 CBAC 等因素限制，日志应避免敏感信息。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| repository template | 仓库模板 | 初始化 Agent 代码与平台集成配置。 |
| Agent API name | Agent API 名称 | 注册为 function 后供调用方使用的名称。 |
| Workflow Lineage | 工作流血缘 | 查看异步执行的调用链与运行日志。 |

## 疑问与待验证项

- - 主线指南允许 Git tag，而分支指南要求仓库 UI 创建分支预发布；需按目标分支选择发布方式。
- - 本地 build 成功只说明代码构建完成，不替代线上权限、运行与结果回写验证。

## 复刻启示

- - 创建向导分步收集模板、项目/本体绑定、参数、工具和权限，之后进入构建、发布版本、异步运行与日志查看。
- - 发布前展示身份、异步/Void 语义、结果回写位置和日志可见范围；主线与分支走不同校验规则。
