<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/v2/aip-agents-v2-resources/agent-versions/agent-version-basics -->
<!-- 研读状态：已完成 -->

# Chatbot Studio Agent Version basics • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/v2/aip-agents-v2-resources/agent-versions/agent-version-basics)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/v2/aip-agents-v2-resources
- 相关性：direct；Agent REST API v2 参考
- 官方更新时间：2026-11-12T17:46:46.917Z
- 目录核对时间：2026-11-14T14:56:05Z
- 产品状态：API 基础概念页（无 Preview 标注）

## 英文原文短摘录（每个来源不超过 25 词）

> “A version of a Chatbot Studio Agent.”

## 摘录译文

Chatbot Studio Agent 的一个版本。

## 中文要点

- 本页只定义 Agent Version 这一 API 资源概念，没有列出版本生命周期、发布策略或兼容约束。
- 该资源由 Agent RID 与版本号共同标识；相关查询接口使用 `majorVersion.minorVersion` 形式。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Agent version | Agent 版本 | Chatbot Studio Agent 的已发布版本资源 |
| Semantic version | 语义化版本 | 此 API 使用主版本.次版本格式 |

## 疑问与待验证项

- 预发布草稿是否也使用同样版本号，以及发布后版本能否覆盖或撤回，本页没有说明。

## 复刻启示

- 存储 Agent 配置快照时以 agentRid + version 为复合身份，并保留每次发布的配置摘要。
- 版本历史用于部署和复现，但不应把版本列表误解为源码或完整提示词内容。
