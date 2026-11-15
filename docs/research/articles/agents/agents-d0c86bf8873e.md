<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/v2/aip-agents-v2-resources/agents -->
<!-- 研读状态：已完成 -->

# Chatbot Studio Agent basics • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/v2/aip-agents-v2-resources/agents)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/v2/aip-agents-v2-resources
- 相关性：direct；Agent REST API v2 参考
- 官方更新时间：2026-11-12T17:46:46.917Z
- 目录核对时间：2026-11-14T14:56:06Z
- 产品状态：当前产品名称为 AIP Chatbot Studio / AIP Chatbot；API 保留 Agent 术语以维持向后兼容。

## 英文原文短摘录（每个来源不超过 25 词）

> “An Agent represents an AIP Chatbot (formerly an AIP Agent) created in AIP Chatbot Studio (formerly AIP Agent Studio).”

## 摘录译文

Agent 表示在 AIP Chatbot Studio（原 AIP Agent Studio）中创建的 AIP Chatbot（原称 AIP Agent）。

## 中文要点

- 这张 API 基础页只定义资源身份：API 中的 Agent 对应 Chatbot Studio 创建的 AIP Chatbot。
- Palantir 已调整产品命名，但接口继续使用 Agent 作为兼容术语；阅读其他旧文档时应将其映射到当前产品。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Agent | Agent 资源 | API 中用于兼容旧命名的资源称呼。 |
| AIP Chatbot | AIP Chatbot | 当前 Chatbot Studio 中创建的聊天助手。 |
| AIP Agent Studio | AIP Agent Studio | 旧产品名称。 |

## 疑问与待验证项

- 本页没有说明旧 Agent RID、API 名称与新 Chatbot 资源标识之间的迁移规则。
- 该基础页未提供 Agent 的配置 schema、发布和授权细节。

## 复刻启示

- 内部领域模型使用清晰的 Agent 与版本实体，同时为 API/导入器保留兼容别名和产品显示名称。
- 目录与画布保存资源来源和命名变更历史，避免把旧 Agent Studio 文档误认为不同的产品实体。
