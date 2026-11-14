<!-- 页面 URL：https://www.palantir.com/docs/foundry/ontology-mcp/authentication-and-authorization -->
<!-- 研读状态：已完成 -->

# Ontology MCP • Authentication and authorization • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/ontology-mcp/authentication-and-authorization)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：ontology-mcp
- 相关性：direct；Ontology MCP 文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:04:49Z
- 产品状态：待核对 Beta、预览、弃用或更名信息

## 英文原文短摘录（每个来源不超过 25 词）

> “Ontology MCP (OMCP) is built on top of the OAuth 2.0 configuration of the Developer Console application that exposes it.”

## 摘录译文

“Ontology MCP 基于暴露它的 Developer Console 应用中的 OAuth 2.0 配置。”

## 中文要点

MCP 连接复用 Developer Console 应用已经配置的 OAuth 客户端和授权服务器，不额外建立一套认证。应用限制、权限和 OAuth 设置继续约束 MCP 请求；token scope 限定暴露的操作与资源。授权码流程代表最终用户，按用户权限工作；客户端凭据流程代表服务用户。无论授权方式如何，请求用户/服务身份都必须具备底层对象、Action 和查询权限。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| OAuth 2.0 | OAuth 2.0 | 对 MCP 客户端签发受限制访问令牌的授权机制 |
| Authorization code grant | 授权码许可 | 交互式用户代表本人授权，沿用用户权限 |
| Client credentials grant | 客户端凭据许可 | 非交互式服务以服务身份访问 |
| Scope | 作用域 | 限定客户端 token 可执行的操作/访问的资源 |

## 疑问与待验证项

- 服务身份访问是为了后台集成，不能误用来绕过最终用户权限；机密 client 还必须安全保存密钥。
- 具体资源是否暴露还同时依赖 Developer Console 应用限制和底层 Foundry 权限，不是只检查 MCP 端工具列表。

## 复刻启示

- 将身份、OAuth 客户端 scope、资源许可和工具授权组合检查，并让授权码调用保留用户身份上下文。
- 当前原型把用户 JWT 传递至本体 API，Agent 配置与角色各自授权；未实现 OAuth、scope 或机密客户端生命周期，MCP 对接前必须补全。
