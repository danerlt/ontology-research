<!-- 页面 URL：https://www.palantir.com/docs/foundry/ontology-sdk/generate-osdk-for-other-languages -->
<!-- 研读状态：已完成 -->

# Ontology SDK • Generate OSDK for other languages • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/ontology-sdk/generate-osdk-for-other-languages)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/ontology-sdk/generate-osdk-for-other-languages)（配对状态：matched）
- 页面语言：英文
- 主题栏目：ontology-sdk
- 相关性：direct；Ontology SDK 文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:04:44Z
- 产品状态：常规 Developer Console 功能；其他语言客户端以导出的 OpenAPI schema 和外部生成器构建。

## 英文原文短摘录（每个来源不超过 25 词）

> “Developer Console also supports exporting APIs in the industry-standard OpenAPI format.”

## 摘录译文

Developer Console 还支持以标准 OpenAPI 格式导出接口。

## 中文要点

- Developer Console 为其他语言的 OSDK 使用场景提供 OpenAPI 出口：在应用的 API 页面进入 SDK generation，选择 Other languages，再导出 OpenAPI 文件。
- 下载的规范可交给开源生成器创建客户端和服务端。导出内容包含应用 SDK 所选资源的名称与描述，因此这些元数据不得包含敏感信息。
- 英文页说内置 Java、Python、TypeScript 支持，其他语言走 OpenAPI；语言支持需按当前 SDK 指南核验，生成的客户端能力不自动等于各语言官方 SDK 能力完全一致。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| OpenAPI | 开放 API 规范 | 描述应用 API 的可下载接口格式。 |
| client generator | 客户端生成器 | 根据 OpenAPI 规范生成语言客户端的外部工具。 |
| resource description | 资源描述 | 可能写入导出文档的资源元数据，应避免包含敏感信息。 |

## 疑问与待验证项

- 规范包含所选 API 资源的元数据；即使没有业务对象数据，接口命名也可能泄露内部术语。
- 此页未声明外部生成客户端具备官方 TS/Python/Java SDK 的相同特性、版本兼容或支持等级。

## 复刻启示

- 本体系统可从 OpenAPI schema 派生其他语言客户端，但必须将生成器版本、schema 版本和本体资源快照一起锁定。
- 将 API 描述纳入发布前敏感信息扫描；面向 Agent 的工具清单也要从受限资源集合生成，避免泄漏不该暴露的 Ontology 名称。
