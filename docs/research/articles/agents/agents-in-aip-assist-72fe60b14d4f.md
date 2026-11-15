<!-- 页面 URL：https://www.palantir.com/docs/foundry/assist/agents-in-aip-assist -->
<!-- 研读状态：已完成 -->

# AIP Assist • Power AIP Assist with custom content sources • Deploy custom source-backed AIP Chatbots • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/assist/agents-in-aip-assist)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/assist/agents-in-aip-assist)（配对状态：matched）
- 页面语言：英文
- 主题栏目：assist
- 相关性：direct；AIP Assist Agent 文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:04:36Z
- 产品状态：AIP Chatbot Studio/AIP Assist 流程；功能可能因 enrollment 配置而不可用。

## 英文原文短摘录（每个来源不超过 25 词）

> “AIP Chatbots: Interactive, LLM-powered assistants equipped with enterprise-specific information and tools.”

## 摘录译文

AIP Chatbot：配备企业专属信息与工具、由 LLM 驱动的交互式助手。

## 中文要点

- 本教程将 Notepad 文档（推荐）或代码仓库中的 Markdown 自定义文档注册为 AIP Assist 可检索内容，再在 Chatbot Studio 创建和部署专用 AIP Chatbot。
- 注册内容源本身只让内容可被发现，不会自动改变 AIP Assist 行为；仍须创建并发布使用该内容源的 Agent。内容发现有延迟，功能也不保证在所有 enrollment 开放。
- Agent 作为文件系统资源受保存位置权限控制；访问用户还须能读取内容源。用户无权访问指定模型时会回退到环境默认模型；首次发布版本为 1.0，后续修改需发布新版本。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| custom content source | 自定义内容源 | Notepad 文档或文档仓库中的 Markdown 检索材料。 |
| AIP Assist Agent | AIP Assist Agent | 使用自定义内容源的专用助手。 |
| enrollment | 注册环境 | 决定功能开关与可用性的 Foundry 环境。 |
| publish | 发布 | 将 Agent 版本提供给用户使用。 |

## 疑问与待验证项

- 英文页同时提到本体上下文与 Functions 工具；官方中文配对页将自定义源称为“唯一搜索上下文”，可能指 RAG 检索范围而非全部 Agent 上下文，需核对语义。
- 内容注册、Agent 位置和用户模型权限是三层独立访问条件；跨组织 OSDK 部署的详细授权规则需查相关页面。

## 复刻启示

- 把内容源导入/索引、Agent 配置、发布版本和用户权限做成连续但独立的流程；注册内容后提示还需部署 Agent。
- 对每次回答记录检索源、对象/工具调用、模型版本和用户访问决策；Agent 只使用调用者有权访问的内容源。
- 把版本发布和内容源更新纳入审阅流程，支持确定的版本快照及权限复核。
