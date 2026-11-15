<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/v2/aip-agents-v2-resources/agent-versions -->
<!-- 研读状态：已完成 -->

# Chatbot Studio Agent Version basics • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/v2/aip-agents-v2-resources/agent-versions)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/v2/aip-agents-v2-resources
- 相关性：direct；Agent REST API v2 参考
- 官方更新时间：2026-11-12T17:46:46.917Z
- 目录核对时间：2026-11-14T14:56:01Z
- 产品状态：Chatbot Studio Agent Version 概念页；本页未标注 Preview。

## 英文原文短摘录（每个来源不超过 25 词）

> “A version of a Chatbot Studio Agent.”

## 摘录译文

Chatbot Studio Agent 的一个版本。

## 中文要点

- 该 API 概念页把 Agent Version 定义为 Chatbot Studio Agent 的一个版本。
- 本页没有解释版本号格式、发布状态、版本内容差异或回滚语义；需要继续阅读 List/Get Agent Version 等端点。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Agent Version | Agent 版本 | Agent 定义的一个已编号版本。 |
| Chatbot Studio Agent | Chatbot Studio Agent | 版本所归属的 Agent 定义资源。 |

## 疑问与待验证项

- 该概念页未说明 draft、预发布和正式版本的区别。
- Agent 的系统提示词、工具和模型在版本间如何快照与兼容，需要结合版本读取接口核验。

## 复刻启示

- 分离 Agent 主资源与不可变版本快照，版本列表展示发布时间、发布者和内容差异。
- 执行会话固定 Agent RID 与版本，避免 Agent 更新后旧会话行为无记录地变化。
