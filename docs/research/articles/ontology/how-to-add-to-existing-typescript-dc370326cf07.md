<!-- 页面 URL：https://www.palantir.com/docs/foundry/developer-console/how-to-add-to-existing-typescript -->
<!-- 研读状态：已完成 -->

# Developer Console • How-to guides • Add OSDK to an existing application • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/developer-console/how-to-add-to-existing-typescript)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/ontology-sdk/how-to-add-to-existing-typescript)（同主题不同栏目路由；中文页为机器翻译）
- 页面语言：英文
- 主题栏目：developer-console
- 相关性：direct；开发者控制台与本体集成文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:05:11Z
- 产品状态：待核对 Beta、预览、弃用或更名信息

## 英文原文短摘录（每个来源不超过 25 词）

> “The Typescript SDK requires Node 18 or higher to work.”

## 摘录译文

TypeScript SDK 要求使用 Node.js 18 或更高版本。

## 中文要点

- 本指南为已有 React/TypeScript 客户端应用补入 OSDK；前置条件是已创建 Developer Console 应用、拿到本地 token，并使用 Node.js 18 或更高版本。此流程适用于使用公共 OAuth 的面向客户端应用；服务用户后端应走另一套模板。
- 在 `.npmrc` 配置应用专属 Foundry registry 与 `FOUNDRY_TOKEN`，安装生成的 SDK 包、`@osdk/client` 和 `@osdk/oauth`，再用 OAuth client、Foundry URL 与 Ontology RID 创建客户端。
- React 项目可选装 `@osdk/react` 以用类型化 hooks、共享缓存、Actions/Functions；`@osdk/react-components` 提供预构建的 Ontology-aware UI 组件。
- 个人访问令牌不可提交到源码；404 安装错误常见原因是全局或上层 `.npmrc` 覆盖 Foundry registry。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| public OAuth | 公共 OAuth | 浏览器客户端使用的用户授权流程。 |
| Foundry registry | Foundry 包注册表 | 提供应用生成 SDK 包的私有 npm registry。 |
| `@osdk/react` | OSDK React 集成 | 提供 React hooks、缓存和本体操作/函数调用能力。 |
| `@osdk/react-components` | OSDK React 组件 | 基于 `@osdk/react` 的预构建本体感知 UI。 |

## 疑问与待验证项

- 该教程只覆盖公共 OAuth 客户端；服务身份、后端 token 保存与跨服务调用需遵循 service user 指南。
- `@latest` 安装方式便于入门，生产系统需要锁定兼容版本，避免生成 SDK 与运行客户端不匹配。

## 复刻启示

- 本地系统可生成 React 类型化对象 hooks 与通用组件，但访问 token 只放在服务端或受控 OAuth 流程中；浏览器持有的身份必须映射到细粒度资源权限。
- 让 SDK 版本与 schema 发布绑定，并在 CI 对客户端和后端 API 版本兼容性做门禁。
