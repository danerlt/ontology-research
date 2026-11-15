<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/v2/aip-agents-v2-resources/agents/agent-basics -->
<!-- 研读状态：已完成 -->

# Chatbot Studio Agent basics • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/v2/aip-agents-v2-resources/agents/agent-basics)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/v2/aip-agents-v2-resources
- 相关性：direct；Agent REST API v2 参考
- 官方更新时间：2026-11-12T17:46:46.917Z
- 目录核对时间：2026-11-14T14:56:06Z
- 产品状态：API 基础概念页（无 Preview 标注）

## 英文原文短摘录（每个来源不超过 25 词）

> “An Agent represents an AIP Chatbot created in AIP Chatbot Studio.”

## 摘录译文

Agent 表示在 AIP Chatbot Studio 中创建的聊天机器人。

## 中文要点

- API 中的 Agent 对象指 Chatbot Studio 创建的 AIP Chatbot；AIP Agent Studio 是其旧名称。
- 文档为向后兼容保留“Agent”这一 API 名称；概念名称更新不等于资源 RID 或接口路径立即变更。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| AIP Chatbot | AIP 聊天机器人 | 当前产品文档使用的产品名称 |
| AIP Agent Studio | AIP Agent Studio | 旧产品名称 |
| Backward compatibility | 向后兼容 | API 暂保留 Agent 术语 |

## 疑问与待验证项

- Agent API 与 Chatbot Studio 管理界面的发布、草稿和权限模型对应关系，需由其他页面补全。

## 复刻启示

- 本地领域模型可将 Chatbot/Agent 设为带 `displayName` 的 AgentDefinition，但外部兼容层保留原 API 名称。
- 产品文案使用当前名称，同时在导入映射中识别旧名，避免按展示名称推断资源类型。
