<!-- 页面 URL：https://www.palantir.com/docs/foundry/developer-console/create-application -->
<!-- 研读状态：已完成 -->

# Developer Console • How-to guides • Create a new application • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/developer-console/create-application)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：developer-console
- 相关性：direct；开发者控制台与本体集成文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:05:10Z
- 产品状态：待核对 Beta、预览、弃用或更名信息

## 英文原文短摘录（每个来源不超过 25 词）

> “restricted by default to the set of entities selected.”

## 摘录译文

通过 OAuth 2.0 流程获得的令牌默认也受限于所选资源集合。

## 中文要点

- 创建向导让操作者配置应用图标和类型、OAuth 回调 URL/CORS、目标 Ontology、SDK 资源、Platform API 操作和首个 SDK 版本；后端服务可选择 service-user 类型而不是 client-facing 类型。
- 生成的类型绑定与应用内 API 文档由所选对象类型、Action 等资源决定；OAuth 令牌默认也受限于同一资源集合。Platform API 资源必须单独加到 Platform SDK 页。
- 应用默认以 Restricted 模式创建；需要超出项目的广泛平台访问时，创建后才可显式切为 Unrestricted。Ontology 生成后不能更换绑定本体。
- 应用级 API 文档覆盖 TS、Python 和 cURL，并可按语言切换；可直接复制对象、Action 与 Function 的代码示例。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| client-facing application | 面向客户端的应用 | 使用交互式授权码流程的前端应用。 |
| backend service | 后端服务 | 以服务用户运行的服务端应用。 |
| Restricted | 受限 | 应用只能访问明确配置的资源和操作。 |
| CORS | 跨域资源共享 | 控制浏览器开发应用可访问 Foundry 的来源策略。 |
| application-specific SDK | 应用专属 SDK | 绑定指定 Ontology 与资源清单生成的客户端包。 |

## 疑问与待验证项

- redirect URL 与 CORS 示例是本地开发参数；生产域名、凭据和部署方式需由 OAuth/托管文档决定。
- 中文配对页缺少英文页中 Restricted 默认值、Ontology 生成后不可变以及后端应用类型等更新，应优先依据英文页治理权限。

## 复刻启示

- 每个前端或服务应用绑定一个本体与精确资源白名单，令牌按此白名单最小授权；跨系统连接通过独立 Platform API scope 配置。
- 向导预先选择应用运行模式、身份方式、回调地址和资源清单，并对 Unrestricted、跨项目访问与服务用户授权加入单独审批/审计。
