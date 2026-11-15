<!-- 页面 URL：https://www.palantir.com/docs/foundry/developer-console/how-to-bootstrapping-server-side-typescript -->
<!-- 研读状态：已完成 -->

# Developer Console • How-to guides • Bootstrap a back-end TypeScript application • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/developer-console/how-to-bootstrapping-server-side-typescript)
- 官方中文来源：[中文候选（同主题多页，目录配对为 ambiguous）](https://www.palantir.com/docs/zh/foundry/ontology-sdk/how-to-bootstrapping-server-side-typescript)
- 页面语言：英文
- 主题栏目：developer-console
- 相关性：direct；后端 TypeScript、服务用户与 confidential OAuth
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:05:11Z
- 产品状态：后端示例使用服务用户；密钥仅在创建时显示一次，轮换会影响旧凭据应用

## 英文原文短摘录（不超过 25 词）

> “Service user authentication is done through a confidential OAuth client.”

## 摘录译文

服务用户认证通过 confidential OAuth client 完成。

## 中文要点

- 在 Developer Console 创建 Backend service 类型应用，选择应用权限、Ontology、对象类型和 Action 类型，然后生成 OSDK。
- Developer Console 按应用创建服务用户；除读取所选对象的权限外，还需满足 Action submission criteria。
- 新建应用时复制一次性 client secret 并安全保存；轮换密钥会让仍使用旧密钥的现有服务中断，Marketplace 目标环境需重新生成目标 secret。
- 服务端使用 `createConfidentialOauthClient` 和环境变量中的 client ID、secret、Foundry URL 创建 OSDK client；文档使用 Next.js 服务端渲染演示，避免把 secret 放进浏览器。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Backend service application | 后端服务应用 | 使用机密 OAuth 客户端的 Developer Console 应用类型 |
| service user | 服务用户 | 该应用在 Foundry 中执行数据访问的身份 |
| confidential OAuth client | 机密 OAuth 客户端 | 服务端以 client secret 换取授权的客户端 |
| client secret | 客户端密钥 | 必须在服务端保管的 OAuth 凭据 |

## 疑问与待验证项

- 文档示例负责读对象；写入受 Action 权限与提交条件约束，需结合 Action 文档确认完整行为。
- 本体一旦选定后 SDK 绑定关系如何迁移，需要新建版本/应用还是有原位迁移方式，本文没有说明。
- 密钥轮换造成旧应用中断，文档没有说明双密钥并行或无停机切换机制。

## 复刻启示

- 机密 OAuth 仅用于后端运行时，密钥由密钥服务注入；浏览器 token 与服务端身份必须分离。
- 服务身份的本体权限、Action 提交条件和项目成员可见性分别配置并记录。
- 密钥轮换流程展示依赖服务、切换窗口和失效时间，保留版本化审计。