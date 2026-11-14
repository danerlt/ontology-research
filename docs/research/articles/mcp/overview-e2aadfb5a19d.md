<!-- 页面 URL：https://www.palantir.com/docs/foundry/ontology-mcp/overview -->
<!-- 研读状态：已完成 -->

# Ontology MCP • Overview • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/ontology-mcp/overview)
- 官方中文来源：尚未确认（配对状态：ambiguous）
- 页面语言：英文
- 主题栏目：ontology-mcp
- 相关性：direct；Ontology MCP 文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:04:47Z
- 产品状态：待核对 Beta、预览、弃用或更名信息

## 英文原文短摘录（每个来源不超过 25 词）

> “Ontology MCP (OMCP) is a Developer Console feature that exposes your application's ontology resources as Model Context Protocol (MCP) tools.”

## 摘录译文

“Ontology MCP 将应用中的本体资源作为 MCP 工具对外提供。”

## 中文要点

Ontology MCP（OMCP）把 Developer Console 应用中已配置的对象类型、Action 类型和查询函数暴露为 MCP 工具，让外部 Agent 读取对象、查询数据并通过预定义 Action 写入业务数据。Palantir MCP（PMCP）解决的是开发者侧的本体构建工作，可修改对象/链接/Action 类型和其他平台资源，但不负责写业务对象数据。二者方向相反：OMCP 是本体消费者接口，PMCP 是本体开发接口。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Ontology MCP (OMCP) | 本体 MCP | 外部 Agent 受限访问本体业务数据与预定义写操作 |
| Palantir MCP (PMCP) | Palantir MCP | 开发者使用工具修改本体结构及平台资源 |
| MCP client / server | MCP 客户端 / 服务器 | Agent 侧连接工具的一方 / 暴露本体工具的一方 |
| Application restriction | 应用限制 | 限定应用经 MCP 可访问的本体资源与操作 |

## 疑问与待验证项

- “外部 Agent 可安全写入”依赖应用限制和已配置 Action；这不代表开放任意 SQL 或任意属性写入。
- 应逐项确认 MCP 服务所绑定的应用资源，以及外部模型提供商接收哪些工具输出。

## 复刻启示

- Agent 接入面要按读取业务数据/调用受限 Action 设计；开发面要把 schema 修改置于提案/审批流程。
- 当前系统有独立 Agent HTTP API，但没有 MCP 协议端点；需要先实现 OAuth 和应用级资源清单，再考虑接入外部 Agent。
