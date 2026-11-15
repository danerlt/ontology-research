<!-- 页面 URL：https://www.palantir.com/docs/foundry/developer-console/how-to-bootstrapping-typescript -->
<!-- 研读状态：已完成 -->

# Developer Console • How-to guides • Bootstrap a TypeScript application • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/developer-console/how-to-bootstrapping-typescript)
- 官方中文来源：[中文候选（多页近似匹配，目录配对为 ambiguous）](https://www.palantir.com/docs/zh/foundry/ontology-sdk/how-to-bootstrapping-typescript)
- 页面语言：英文
- 主题栏目：developer-console
- 相关性：direct；客户端 TypeScript OSDK 应用脚手架
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:05:10Z
- 产品状态：新应用默认使用 TypeScript OSDK 2.0 generator；Node.js 至少为 18

## 英文原文短摘录（不超过 25 词）

> “The Typescript SDK requires Node 18 or higher to work.”

## 摘录译文

TypeScript SDK 需要 Node 18 或更高版本才能运行。

## 中文要点

- 创建 Developer Console 应用并在本地设置个人 token 后，用 `@osdk/create-app` 根据应用 RID、Foundry URL、托管子域、client ID 和 SDK 包地址生成客户端项目。
- CLI 让开发者指定项目名和前端框架；然后安装依赖并运行开发服务器。
- 脚手架生成客户端与应用 SDK 的 generator 版本匹配；新应用默认用 OSDK 2.0 的 `createClient` 和 `createPublicOauthClient`。
- 若应用 SDK 用 1.x generator，生成代码会出现已弃用的 `FoundryClient`、`PublicClientAuth`；需重新生成 OSDK 2.0 并重跑脚手架或升级包。
- React 项目可选使用 `@osdk/react` 和 `@osdk/react-components`。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| `@osdk/create-app` | OSDK 应用生成器 | 根据 Developer Console 应用参数创建客户端项目 |
| public OAuth client | 公共 OAuth 客户端 | 浏览器应用所用客户端，不保存机密 secret |
| OSDK generator | OSDK 生成器 | 决定生成 SDK/客户端代码版本的工具 |
| `createPublicOauthClient` | 公共 OAuth 客户端工厂 | OSDK 2.0 客户端认证初始化方法 |

## 疑问与待验证项

- 文档给出 Node 18 最低版本，但当前可用版本应结合代码仓库运行时指南确认。
- 应用 RID、redirect URL 与托管地址必须与目标环境相符；跨环境安装后依赖 Marketplace 的参数映射能力。
- TypeScript 客户端面向浏览器，不可复用服务端 confidential client 的凭据配置。

## 复刻启示

- 创建向导应先配置本体资源及 OAuth 模式，再生成与 SDK generator 对应的项目脚手架。
- 明确区分 public client 和 confidential client，静态扫描阻止 secret 进入客户端 bundle。
- 报告旧生成器带来的 API 兼容性问题，并将升级指引链接到逐项迁移清单。