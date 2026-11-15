<!-- 页面 URL：https://www.palantir.com/docs/zh/foundry/ontology-sdk/how-to-add-to-existing-typescript -->
<!-- 研读状态：已完成 -->

# OSDK • 将 Ontology SDK 包添加到现有应用程序中 • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/developer-console/how-to-add-to-existing-typescript)（同主题不同栏目路由）
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/ontology-sdk/how-to-add-to-existing-typescript)（页面注明机器翻译未经验证）
- 页面语言：中文
- 主题栏目：ontology-sdk
- 相关性：direct；Ontology SDK 文档
- 官方更新时间：2026-11-12T17:46:46.932Z
- 目录核对时间：2026-11-14T15:00:45Z
- 产品状态：待核对 Beta、预览、弃用或更名信息

## 原文短摘录与翻译

> “TypeScript SDK 需要 Node 18 或更高版本才能工作。”

## 摘录译文

将 OSDK 接入现有 TypeScript 应用需要 Node.js 18 或更高版本。

## 中文要点

- 中文页引导现有 React/TypeScript 应用接入 OSDK：建立 Developer Console 应用、在本地配置 token 和 npm registry、安装生成 SDK 及 OAuth/client 包，并初始化 Foundry 客户端。
- 页面适用公共 OAuth 前端；个人 token 仅用于本地开发且不得提交。Node 最低版本为 18；React 可使用类型化 hooks、共享缓存与预构建的本体组件。
- 该页面由 AIP 从英文机器翻译且准确性未经验证。英文页说明服务用户后端应使用单独的后端引导流程；中文示例的注释不应取代原始 API 定义。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| 本地开发令牌 | local development token | 用于从 Foundry 私有 registry 安装 SDK 的本地凭据。 |
| 公共 OAuth 客户端 | public OAuth client | 交互式浏览器应用采用的认证方式。 |
| Ontology RID | 本体 RID | 客户端初始化时指定要访问的本体。 |

## 疑问与待验证项

- 机器翻译中的示例注释和类型提示应与实际 SDK 版本核对；本页未覆盖服务身份后端的凭据托管。
- React 组件包是可选项，不应成为 REST 服务或其他前端框架的依赖要求。

## 复刻启示

- 按开发者、服务身份和终端用户区分 OAuth 主体，不能把个人开发令牌复用为服务凭据。
- 提供可选生成式 React hooks/组件，同时保持独立 API 契约，确保 Vue 等前端也能通过稳定服务接口访问本体。
