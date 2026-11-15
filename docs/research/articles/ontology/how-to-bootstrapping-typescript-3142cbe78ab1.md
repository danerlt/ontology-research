<!-- 页面 URL：https://www.palantir.com/docs/zh/foundry/ontology-sdk/how-to-bootstrapping-typescript -->
<!-- 研读状态：已完成 -->

# OSDK • 引导启动一个新的 Ontology SDK TypeScript 应用程序 • Palantir

- 英文来源：[现行英文原文](https://www.palantir.com/docs/foundry/developer-console/how-to-bootstrapping-typescript)
- 官方中文来源：[官方中文页（AIP 机器翻译）](https://www.palantir.com/docs/zh/foundry/ontology-sdk/how-to-bootstrapping-typescript)
- 页面语言：中文（官方机器翻译，准确性未验证）
- 主题栏目：ontology-sdk
- 相关性：direct；TypeScript 客户端应用脚手架与 OSDK
- 官方更新时间：2026-11-12T17:46:46.932Z
- 目录核对时间：2026-11-14T15:00:52Z
- 产品状态：新建应用默认使用 TypeScript OSDK 2.0 generator；1.x 项目需按迁移指南核对

## 英文原文短摘录（不超过 25 词）

> “The Typescript SDK requires Node 18 or higher to work.”

## 摘录译文

TypeScript SDK 需要 Node 18 或更高版本才能运行。

## 中文要点

- 先创建 Developer Console 应用并将个人 token 放在本地环境变量，再运行 `@osdk/create-app` CLI；命令从应用 RID、Foundry URL、托管子域、client ID 与 SDK 包地址等应用专属配置生成项目。
- CLI 通过交互提示选择项目名和前端框架；生成后的项目安装依赖并启动本地开发服务器。
- 新应用默认使用 TypeScript OSDK 2.0 generator，生成代码调用 `createClient` 与 `createPublicOauthClient`；若应用 SDK 仍由 1.x generator 生成，会出现已弃用的 `FoundryClient`/`PublicClientAuth`。
- React 项目可选用 `@osdk/react` 的类型化 hooks、共享缓存、Action/Function 能力，或使用基于它的 `@osdk/react-components`。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| `@osdk/create-app` | OSDK 应用脚手架 CLI | 从应用配置生成前端项目 |
| generator version | 生成器版本 | 决定 SDK 与客户端代码所使用的 API 代际 |
| public OAuth client | 公共 OAuth 客户端 | 客户端应用使用的 OAuth 模式，不能持有机密 secret |
| application RID | 应用 RID | CLI 用于定位 Developer Console 应用的资源标识 |

## 疑问与待验证项

- 文档要求 Node 18+，但没有在本文固定推荐的具体 Node 主版本；应结合当前工作区镜像和 SDK 发布说明核验。
- CLI 参数中包含 `--corsProxy false`，本地调试与正式托管的 CORS/身份边界还需以 OAuth 和应用限制文档为准。
- 默认 generator 会随平台变化，不能依赖“新应用默认”作为长期兼容保证；项目应显式记录生成器版本。

## 复刻启示

- 启动向导应读取应用配置后生成可复现的命令与项目模板，明确 Node 版本、SDK 生成器版本、OAuth 模式和本体资源范围。
- 模板不能将 PAT、client secret 写入前端 bundle；公共客户端只持有公开配置，服务端凭据使用独立后端。
- 升级生成器作为显式迁移任务，提供 API 差异提示并保留回滚点。