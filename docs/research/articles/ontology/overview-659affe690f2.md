<!-- 页面 URL：https://www.palantir.com/docs/zh/foundry/ontology-sdk/overview -->
<!-- 研读状态：已完成 -->

# OSDK • Ontology SDK • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/ontology-sdk/overview)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/ontology-sdk/overview)
- 页面语言：中文
- 主题栏目：ontology-sdk
- 相关性：direct；Ontology SDK 文档
- 官方更新时间：2026-11-12T17:46:46.932Z
- 目录核对时间：2026-11-14T15:01:03Z
- 产品状态：待核对 Beta、预览、弃用或更名信息

## 英文原文短摘录（每个来源不超过 25 词）

> “The Ontology Software Development Kit (OSDK) allows you to access the full power of the Ontology directly from your development environment.”

## 摘录译文

Ontology Software Development Kit（OSDK）使你能在开发环境中直接使用 Ontology 的全部能力。

## 中文要点

- 官方中文概览介绍 OSDK 是面向应用开发的客户端，支持 TypeScript/npm、Python/pip 或 Conda、Java/Maven，其他语言可使用 OpenAPI 规范。
- 页面说明 Foundry 可作为后端，提供本体查询、数据写回及细粒度治理；OSDK 应用由 Developer Console 创建和管理。
- 该中文页声明由 AIP 从英文原文机器翻译且准确性尚未验证。本卡保留其译文原句，并以英文概览核实语言工具链和产品职责。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| OSDK | Ontology 软件开发工具包 | 为应用提供类型化本体客户端。 |
| 写回 | writeback | 应用通过本体 Action 或 SDK 写入业务对象。 |
| Developer Console | 开发者控制台 | 管理 OSDK 应用与 SDK 资源配置。 |

## 疑问与待验证项

- 概览没有详述各语言 SDK 的功能覆盖或部署方式；需沿对应语言文档核对。
- 生成客户端的资源授权边界应在具体权限参考中核对，不能只依据概览作安全配置。

## 复刻启示

- 对本体系统提供版本化、类型化 SDK，并将每个应用的资源范围和环境绑定在部署配置中。
- Agent 的工具定义应由 schema 生成或校验，减少接口、属性类型和权限范围漂移。
