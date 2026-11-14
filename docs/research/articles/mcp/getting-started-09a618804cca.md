<!-- 页面 URL：https://www.palantir.com/docs/foundry/ontology-mcp/getting-started -->
<!-- 研读状态：已完成 -->

# Ontology MCP • Getting started • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/ontology-mcp/getting-started)
- 官方中文来源：尚未确认（配对状态：ambiguous）
- 页面语言：英文
- 主题栏目：ontology-mcp
- 相关性：direct；Ontology MCP 文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:04:48Z
- 产品状态：待核对 Beta、预览、弃用或更名信息

## 英文原文短摘录（每个来源不超过 25 词）

> “Ensure your application has the appropriate application restrictions configured to control which ontology resources are accessible through MCP.”

## 摘录译文

“先配置应用限制，以控制 MCP 可访问哪些本体资源。”

## 中文要点

启用 OMCP 前，应先确保 Developer Console 应用的应用限制已经定义可访问本体资源。管理员在应用 MCP 页面启用服务器，再按所选 Agent 框架复制连接信息；外部 MCP 客户端用该 URL 连接。MCP Hub 可发现组织中已配置的 OMCP 服务器，并跳转回应用继续维护。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Developer Console | 开发者控制台 | 配置承载 MCP 服务的应用、限制和连接参数 |
| MCP Hub | MCP 中心 | 查找组织已配置 MCP 服务的入口 |
| MCP server URL | MCP 服务器地址 | 外部客户端连接某个已启用服务的 URL |

## 疑问与待验证项

- 页面未把连接地址视为完整安全配置；令牌、scope、资源授权和客户端兼容性需阅读 OAuth/认证页面并逐项验证。
- 实际页面 UI 和部署界面可能随产品版本变化，应以目标 Foundry 环境的 Developer Console 为准。

## 复刻启示

- 对外开放 Agent 前先形成显式的应用资源边界，再显示连接配置；不要默认将整个本体开放给客户端。
- 当前系统有工具 allowlist，但缺少以应用为单位的资源包、MCP Hub 注册和可复制客户端配置。
