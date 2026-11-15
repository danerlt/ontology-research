<!-- 页面 URL：https://www.palantir.com/docs/foundry/developer-console/ontology-mcp -->
<!-- 研读状态：已完成 -->

# Developer Console • Core concepts • Ontology MCP • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/developer-console/ontology-mcp)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：developer-console
- 相关性：direct；Ontology MCP 文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:05:02Z
- 产品状态：Developer Console 中的本体 MCP 能力；资源筛选与客户端配置详见关联文档。

## 英文原文短摘录（每个来源不超过 25 词）

> “Ontology MCP is a Developer Console feature that exposes your application's ontology resources as Model Context Protocol (MCP) tools.”

## 摘录译文

Ontology MCP 是 Developer Console 的一项功能，可将应用程序的本体资源作为 Model Context Protocol（MCP）工具开放。

## 中文要点

- Ontology MCP（OMCP）把某个应用的 Ontology 资源暴露为 MCP tools，让外部 AI Agent/系统以 MCP client 连接该应用。
- 本页指向架构示例但没有列出可暴露资源、应用限制、权限传播或写入确认机制；进一步的 [Ontology MCP 概览](https://www.palantir.com/docs/foundry/ontology-mcp) 区分了两类 MCP：OMCP 面向本体消费者、受应用限制的对象读取/预定义 Action/Query；Palantir MCP 面向开发者工具，可修改本体结构而非生产本体数据。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Ontology MCP (OMCP) | 本体 MCP | 把应用本体资源封装成外部 Agent 可调用的工具。 |
| MCP server | MCP 服务端 | 向 Agent 提供工具能力的服务器。 |
| MCP client | MCP 客户端 | 连接 OMCP 并调用工具的 Agent/外部系统。 |
| application restrictions | 应用限制 | 控制外部工具能暴露哪些本体资源的边界。 |

## 疑问与待验证项

- 本页没有展开连接身份、令牌委托、工具白名单、操作审批及审计字段，应结合 OMCP Getting Started 与权限页阅读。
- 外部模型连接 OMCP 时，本体数据会进入外部客户端上下文；数据治理和留存边界需要在系统设计中说明。

## 复刻启示

- 将开发者本体管理工具与生产运行时本体工具拆成不同 MCP server/权限域；外部 Agent 默认只能读取授权类型、调用白名单 Query/Action。
- 每个项目可独立配置 MCP endpoint、资源列表、Action/Query 白名单、身份绑定、速率限制和审计。
- 画布展示 Agent 到对象类型/Query/Action 的实际工具授权边，支持管理员审核暴露面。
