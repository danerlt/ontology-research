<!-- 页面 URL：https://www.palantir.com/docs/zh/foundry/ontology-sdk/generate-osdk-for-other-languages -->
<!-- 研读状态：已完成 -->

# OSDK • 为其他语言生成 OSDK • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/ontology-sdk/generate-osdk-for-other-languages)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/ontology-sdk/generate-osdk-for-other-languages)
- 页面语言：中文
- 主题栏目：ontology-sdk
- 相关性：direct；Ontology SDK 文档
- 官方更新时间：2026-11-12T17:46:46.932Z
- 目录核对时间：2026-11-14T15:00:44Z
- 产品状态：待核对 Beta、预览、弃用或更名信息

## 英文原文短摘录（每个来源不超过 25 词）

> “The Developer Console has built-in Java, Python, and TypeScript support for code generation using both pip and Conda but is not limited to these languages.”

## 摘录译文

Developer Console 内置支持通过 pip 和 Conda 为 Java、Python 与 TypeScript 生成代码，但也支持其他语言。

## 中文要点

- 中文页说明：在 Developer Console 应用的 Application API 页面进入 SDK 生成，选择 Other languages 并导出 OpenAPI；之后用开源工具生成对应语言客户端和服务端。
- 导出的 OpenAPI 文件包含所选资源的名称和描述；应先清理敏感元数据，再分享或纳入代码仓库。
- 页面声明由 AIP 从英文机器翻译且准确性未验证。英文原文进一步明确此路线补足内置 SDK 语言之外的客户端生成，但没有承诺与官方 SDK 能力等价。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| OpenAPI 规范 | OpenAPI specification | 用于生成 API 客户端和服务端的接口描述文件。 |
| SDK 生成 | SDK generation | Developer Console 中导出本体应用客户端契约的流程。 |
| 敏感元数据 | sensitive metadata | 出现在 OpenAPI 资源名称和说明中的组织内部信息。 |

## 疑问与待验证项

- 中文机器翻译对内置 SDK 的语言描述易产生歧义；语言覆盖范围和生成器能力应核对英文版本及具体工具。
- 开源生成的客户端如何适配 OAuth、分页和本体资源授权，需要在目标语言里单独验证。

## 复刻启示

- 为多语言微服务生成客户端时，以版本化 OpenAPI schema 为边界，固定 ontology RID、资源白名单、认证配置和分页约定。
- 发布流水线扫描 API schema 中的命名与描述；Agent 工具生成不得绕过最小权限资源清单。
