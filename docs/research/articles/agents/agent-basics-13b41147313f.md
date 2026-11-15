<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/aip-agents-v2-resources/agents/agent-basics -->
<!-- 研读状态：已完成 -->

# Chatbot Studio Agent basics • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/aip-agents-v2-resources/agents/agent-basics)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/aip-agents-v2-resources/agents
- 相关性：direct；Agent REST API v2 参考
- 官方更新时间：2026-11-12T17:46:46.917Z
- 目录核对时间：2026-11-14T14:53:23Z
- 产品状态：按页面现行表述整理；若标注 Preview，相关 API 可能变化。

## 英文原文短摘录（每个来源不超过 25 词）

> “An Agent represents an AIP Chatbot (formerly an AIP Agent) created in AIP Chatbot Studio.”

## 摘录译文

Agent 表示在 AIP Chatbot Studio 中创建的 AIP Chatbot（旧称 AIP Agent）。

## 中文要点

- 该页解释 Agent API 资源的命名兼容背景：资源表示 Chatbot Studio 中创建的 AIP Chatbot，API 继续使用 Agent 一词以保持向后兼容。
- 这是术语说明而非完整数据模型；资源字段应以 Get Agent 和相关端点定义为准。
- 产品名称、文档导航标题和 API 路径可能使用不同代际的术语，阅读时需先识别其兼容关系。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| AIP Chatbot | AIP 聊天机器人 | 当前产品表述之一。 |
| AIP Agent | AIP Agent | 旧产品名，仍出现在兼容文档中。 |
| backwards compatibility | 向后兼容 | 保留旧 API 命名以避免破坏既有集成。 |

## 疑问与待验证项

- 此页未规定 Agent 草稿、发布版本和会话之间的数据关系，应结合具体 API 端点判断。
- Palantir 后续是否将 API resource path 迁移到 Chatbot 命名，本页未作承诺。

## 复刻启示

- 业务界面使用统一、当前的中文产品名；API 适配层保留旧字段和路由映射，避免把兼容术语扩散到领域模型。
- Agent、发布版本、运行会话应是独立对象，API 的“Agent”不能简单映射为单个可变配置记录。
