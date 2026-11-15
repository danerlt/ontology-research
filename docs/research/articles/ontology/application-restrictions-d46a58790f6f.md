<!-- 页面 URL：https://www.palantir.com/docs/foundry/developer-console/application-restrictions -->
<!-- 研读状态：已完成 -->

# Developer Console • Core concepts • Application restrictions • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/developer-console/application-restrictions)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：developer-console
- 相关性：direct；Developer Console OAuth 应用授权治理
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:05:01Z
- 产品状态：核心安全概念页；未标注 Preview

## 英文原文短摘录（每个来源不超过 25 词）

> “Every Developer Console application corresponds to an OAuth client that is responsible for handling Foundry authorization.”

## 摘录译文

每个 Developer Console 应用都对应一个负责处理 Foundry 授权的 OAuth 客户端。

## 中文要点

- 有效 token 权限由三项取交集：授权码流程中的用户权限（或客户端凭证流程中的服务用户权限）、Developer Console 应用配置的最大资源/操作限制、代码在 token 请求中申请的 operation scope。
- 应用默认受限，开发者控制台规定应用最多可请求哪些资源和操作。切换为 unrestricted 会移除现有项目与操作限制配置；受限/不受限切换可能导致已有应用失效。
- 每个 token 必须在 OAuth client 限制或授权时 scope 至少受一处约束；完全没有范围限制的 token 请求会得到无权限 token。
- `api:...` operation scope 只声明客户端可请求的操作范围，不会越过用户/服务用户本身的资源授权。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| OAuth client | OAuth 客户端 | 代表应用执行 Foundry 授权的身份配置 |
| Application restrictions | 应用限制 | 限定应用可访问资源与可请求操作的最大范围 |
| Operation scope | 操作范围 | token 请求时申请的 API 操作权限 |
| Unrestricted application | 不受限应用 | 不设置最大资源/操作约束的客户端配置 |

## 疑问与待验证项

- 本页描述 OAuth 范围交集，但没有给出所有 OSDK/服务应用授权流程和用户/服务用户的完整选择条件；需结合认证授权专题核验。
- 应用限制变更导致已签发 token 如何失效、何时重新授权，没有在本文说明。
- unrestricted 应用的审批、治理审计和安全使用条件需结合组织策略确认。

## 复刻启示

- 每个集成应用具有显式资源白名单与操作白名单，用户 token 权限取“用户/服务身份授权 ∩ 应用最大权限 ∩ 本次调用 scope”。
- UI 默认建立受限应用；扩大范围时提供差异预览、审批和审计，禁止用“无限制”解决普通集成问题。
- Agent 工具清单应绑定应用身份和 resource/action scopes；工具可用不代表当前用户有权执行，授权需在每次执行时检查。
