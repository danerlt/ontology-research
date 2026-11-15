<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/aip-agents-v2-resources/agent-versions/agent-version-basics -->
<!-- 研读状态：已完成 -->

# Chatbot Studio Agent Version basics • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/aip-agents-v2-resources/agent-versions/agent-version-basics)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/aip-agents-v2-resources/agent-versions
- 相关性：direct；Agent REST API v2 参考
- 官方更新时间：2026-11-12T17:46:46.917Z
- 目录核对时间：2026-11-14T14:53:22Z
- 产品状态：按页面现行表述整理；若标注 Preview，相关 API 可能变化。

## 英文原文短摘录（每个来源不超过 25 词）

> “A version of a Chatbot Studio Agent.”

## 摘录译文

Chatbot Studio Agent 的一个版本。

## 中文要点

- 该 API 基础页只定义 Agent Version 是 Chatbot Studio Agent 的一个版本，没有展开字段结构或生命周期。
- 字段与读取方式由具体的获取版本、列举版本端点规定；不能从基础页推断版本可写、可删除或可回滚。
- 上下文中的名称沿用 API 资源模型，产品术语已从 AIP Agent / Agent Studio 演进到 Chatbot Studio。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Agent Version | Agent 版本 | Chatbot Studio Agent 的版本资源。 |
| Chatbot Studio | 聊天机器人工作室 | 当前文档中的产品命名；旧 API 保留兼容术语。 |
| resource schema | 资源结构 | API 端点请求/响应中定义的字段。 |

## 疑问与待验证项

- 这张基础页几乎没有版本字段信息；版本的可读字段、分页和 preview 边界必须分别以具体端点页为准。
- 文档中的产品更名与 API 路径是否完全同步，需要按现行 API reference 逐端点确认。

## 复刻启示

- 为 Agent 发布版本建模独立不可变快照，避免将 Agent 当前草稿直接覆盖运行中的版本。
- API 兼容层需要区分产品展示名、历史资源名与内部稳定 ID，并显式记录 preview 能力标记。
