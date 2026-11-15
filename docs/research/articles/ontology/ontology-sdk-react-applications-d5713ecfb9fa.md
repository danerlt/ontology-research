<!-- 页面 URL：https://www.palantir.com/docs/zh/foundry/ontology-sdk-react-applications -->
<!-- 研读状态：已完成 -->

# 本体SDK React应用 • 概述 • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/ontology-sdk-react-applications/overview)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/ontology-sdk-react-applications)
- 页面语言：中文（官方机器翻译，准确性未验证）
- 主题栏目：ontology-sdk-react-applications
- 相关性：direct；Ontology SDK 应用开发文档
- 官方更新时间：2026-11-12T17:46:46.937Z
- 目录核对时间：2026-11-14T15:00:37Z
- 产品状态：OSDK React 应用指南；英文页面已迁移到 overview 子路由

<!-- 研读状态：已完成 -->
# 英文原文短摘录（每个来源不超过 25 词）

> “Developer Console enables application builders to build completely customizable user interfaces using React and powered by the Ontology Software Development Kit (OSDK).”

## 英文原文短摘录（每个来源不超过 25 词）

> “Developer Console enables application builders to build completely customizable user interfaces”

## 摘录译文

Developer Console 让应用构建者能够创建完全可定制的用户界面

## 中文要点

- OSDK React 应用以 Foundry 为后端，通过 Ontology 进行高规模查询和编辑，并复用平台治理能力；指南覆盖创建、开发/部署和故障排除。
- 官方 React 库包括 @osdk/react（类型化 hooks、共享缓存、Action、Function 和数据驱动界面）以及 @osdk/react-components（预制的 Ontology 感知组件）。
- OSDK 与前端框架无关：TypeScript 使用 NPM，Python 使用 Pip/Conda，Java 使用 Maven，其他语言可使用 OpenAPI 规范。
- React 是自定义前端开发路线之一；组件库不取代 OSDK 资源范围和服务端授权。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| @osdk/react | OSDK React hooks 库 | 本体查询、缓存、Action 和 Function 绑定 |
| @osdk/react-components | OSDK React 组件库 | 预构建的 Ontology 感知 UI 组件 |
| Data-driven interface | 数据驱动界面 | 根据本体对象和 schema 构建的应用界面 |
| Developer Console | 开发者控制台 | 创建应用、SDK、权限与部署配置的入口 |

## 疑问与待验证项

- 页面未限定 React 库精确版本、组件成熟度和浏览器支持范围，需以当前包版本核验。
- 中文旧路由对应新英文 overview 子路由；SDK API 以语言专属参考页为准。

## 复刻启示

- 前端通过类型化客户端调用本体 API，统一处理缓存、Action/Function 和 schema 感知组件。
- Vue 与 React 共用领域模型和服务 API；画布编辑、权限校验和服务端写入保持框架无关。