<!-- 页面 URL：https://www.palantir.com/docs/zh/foundry/ontology-sdk/navigation -->
<!-- 研读状态：已完成 -->

# OSDK • 导航 • Palantir

- 英文来源：[现行相关概述（旧导航页无一对一英文路由）](https://www.palantir.com/docs/foundry/developer-console)
- 官方中文来源：[官方中文页（AIP 机器翻译）](https://www.palantir.com/docs/zh/foundry/ontology-sdk/navigation)
- 页面语言：中文（官方机器翻译，准确性未验证）
- 主题栏目：ontology-sdk
- 相关性：direct；Developer Console 导航和应用管理入口
- 官方更新时间：2026-11-12T17:46:46.932Z
- 目录核对时间：2026-11-14T15:00:52Z
- 产品状态：旧 OSDK 导航页描述的控制台功能已迁入 Developer Console 文档体系；所引英文页为现行概述而非逐段对应译文

## 现行英文相关来源短摘录（不超过 25 词）

> “Use Developer Console to build and manage Custom Applications and their associated authorization clients and SDKs.”

## 摘录译文

使用 Developer Console 构建和管理自定义应用及其关联的授权客户端与 SDK。

## 中文要点

- 中文旧页描述如何启用 Developer Console：需在 Control Panel 的 Foundry Suite 中启用；随后可从 Application Portal 进入。首页按用户权限列出可访问的应用与 OAuth 客户端。
- 旧页还介绍应用概览、定制 API 文档、SDK 版本生成、OAuth 范围、共享和 token、Web 托管及应用指标入口。
- 现行 Developer Console 概述将能力拆成应用认证客户端、生成 SDK 与文档、权限、指标、可选托管、代码仓库、Marketplace 分发和可选 Ontology MCP。
- 旧页的 OAuth 客户端管理语境已变化：独立 OAuth 客户端在当前文档中标记为 Legacy，不能再新建；新建集成应使用 Developer Console custom application。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Developer Console | 开发者控制台 | 配置自定义应用、客户端和 SDK 的 Foundry 工具 |
| Application Portal | 应用程序门户 | 用户进入已授权应用的门户入口 |
| application restrictions | 应用限制 | 管控客户端可请求的资源和操作范围 |
| Ontology MCP | 本体 MCP | 将应用纳入的本体资源以 MCP 工具形式暴露给 Agent |

## 疑问与待验证项

- 旧页提及 Control Panel 启用和 Application Portal 入口；现行概述未完整复述启用步骤，具体租户权限和入口仍需对照权限与创建应用指南。
- 指标页面的可用性、Web Hosting 支持范围和 MCP 开关可能受 enrollment 与应用类型影响。
- 旧中文路由存在但英文直接对应页未找到，因此本文使用现行概述佐证功能范围，不视为逐字配对。

## 复刻启示

- 把 Developer Console 视作应用生命周期工作台：资源范围、OAuth、生成 SDK、权限、代码仓库、托管、指标和分发均属于同一应用实体。
- 首页按用户/组织权限列出资源；对旧集成展示迁移入口和兼容边界。
- Agent/MCP 接入必须引用具体应用授权边界与资源清单，不能只用“已连接”表示安全状态。