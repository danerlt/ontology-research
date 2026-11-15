<!-- 页面 URL：https://www.palantir.com/docs/foundry/developer-console/overview -->
<!-- 研读状态：已完成 -->

# Developer Console • Overview • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/developer-console/overview)
- 官方中文来源：尚未确认（配对状态：ambiguous）
- 页面语言：英文
- 主题栏目：developer-console
- 相关性：direct；开发者控制台与本体集成文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:04:57Z
- 产品状态：待核对 Beta、预览、弃用或更名信息

## 英文原文短摘录（每个来源不超过 25 词）

> “Use Developer Console to build and manage Custom Applications and their associated authorization clients and SDKs.”

## 摘录译文

Developer Console 用于构建和管理自定义应用及其授权客户端与 SDK。

## 中文要点

- Developer Console 管理自定义应用的 OAuth 客户端、资源生成的 SDK、应用级/用户级权限、自动生成的 SDK 文档、指标、可选网站托管、代码仓库和 Marketplace 分发。
- 它可把本体资源作为可供外部 Agent 调用的 MCP 工具公开；只有被选入应用的对象类型、Action 和查询函数才能按该应用配置暴露。
- 与 UI 驱动的 Developer Console 相对，SuperRepo 把 Ontology 定义、Functions 和前端放在代码单仓库中，由本地生成 SDK 并通过 Marketplace/CI 部署到多个 enrollment。
- 应用默认最多 1,000 个数据资源和资源限制项；OAuth client 是仅含授权客户端的旧式原语，文档建议以应用取代它。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| custom application | 自定义应用 | 扩展 Foundry 的应用实体，包含 SDK、权限、指标等功能。 |
| application restrictions | 应用资源限制 | 控制应用与 token 可访问的本体资源和操作。 |
| SuperRepo | SuperRepo 单仓库 | 以代码管理 Ontology、Functions 与前端的开发方式。 |
| enrollment | Foundry enrollment | Marketplace/CI 部署目标环境。 |
| MCP server | MCP 服务端 | 将应用允许的本体资源作为 Agent 工具提供。 |

## 疑问与待验证项

- Developer Console 的 1,000 项默认限制具体如何统计不同资源与限制项，要结合应用限制页面确认。
- 应用可以选择 Unrestricted；跨环境发布与外部 MCP 暴露需继续遵守各 enrollment 的 OAuth 和资源授权。

## 复刻启示

- 把“应用”建模为 Ontology 资源集合、用户/服务身份、OAuth 配置、权限约束、SDK版本、指标、托管和Agent工具清单的治理容器。
- Agent 工具只从受限应用资源清单生成，并继承相同的身份和操作 scope；跨多个项目部署需按环境分别配置与审计，避免单个全局客户端越权。
