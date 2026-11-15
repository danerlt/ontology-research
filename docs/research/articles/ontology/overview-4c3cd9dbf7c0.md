<!-- 页面 URL：https://www.palantir.com/docs/foundry/ontology-sdk/overview -->
<!-- 研读状态：已完成 -->

# Ontology SDK • Overview • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/ontology-sdk/overview)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/ontology-sdk/overview)（配对状态：matched）
- 页面语言：英文
- 主题栏目：ontology-sdk
- 相关性：direct；Ontology SDK 文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:04:36Z
- 产品状态：待核对 Beta、预览、弃用或更名信息

## 英文原文短摘录（每个来源不超过 25 词）

> “The Ontology Software Development Kit (OSDK) allows you to access the full power of the Ontology directly from your development environment.”

## 摘录译文

Ontology SDK 可让开发者从开发环境直接访问 Ontology 的能力。

## 中文要点

- OSDK 将 Ontology 暴露给应用开发环境：TypeScript 使用 npm，Python 使用 pip 或 Conda，Java 使用 Maven；其他语言可从 OpenAPI 规范生成客户端。
- Foundry 可作为应用后端，提供高规模查询、写回能力与细粒度治理。OSDK 应用在 Developer Console 中创建和管理；本节主要索引各语言 SDK 参考。
- 因为 SDK 从 Ontology 资源生成类型绑定，客户端可获得对象、属性和函数等结构；资源选择、版本生成和权限仍由 Developer Console 管理，SDK 本身不是独立数据存储。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| OSDK | Ontology 软件开发工具包 | 在应用代码中访问本体查询与写入能力的生成式 SDK。 |
| generated SDK | 生成的 SDK | 与选定 Ontology 资源集合对应的类型化客户端。 |
| Developer Console | 开发者控制台 | 创建和管理使用 OSDK 的 Foundry 应用。 |
| OpenAPI specification | OpenAPI 规范 | 为其他语言生成客户端的接口描述。 |

## 疑问与待验证项

- 概览并未定义各语言 API 能力是否完全对齐；应针对 Functions/REST/OSDK 具体页面核验差异。
- SDK 所包含资源范围受 Developer Console 配置约束，客户端不应假定可以任意访问整个 Ontology。

## 复刻启示

- 复刻系统可生成版本化 TS/Python 客户端，并把资源授权范围作为部署元数据；更新 schema 后需重建 SDK 并在分支内验证。
- Agent 工具应使用和应用一致的类型化查询/Action 契约，避免另造一套与 Ontology schema 脱节的接口。
