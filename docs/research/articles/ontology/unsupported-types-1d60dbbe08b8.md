<!-- 页面 URL：https://www.palantir.com/docs/foundry/ontology-sdk/unsupported-types -->
<!-- 研读状态：已完成 -->

# Ontology SDK • Unsupported types for OSDK • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/ontology-sdk/unsupported-types)
- 官方中文来源：[官方中文页面（AIP 机器翻译）](https://www.palantir.com/docs/zh/foundry/ontology-sdk/unsupported-types)（目录配对状态：matched）
- 页面语言：英文
- 主题栏目：ontology-sdk
- 相关性：direct；SDK 生成兼容性和跨语言能力差异
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:04:47Z
- 产品状态：生成器对 unsupported object property 与 Action/Function 类型采用不同失败策略

## 英文原文短摘录（不超过 25 词）

> “Not all data types are currently available in the OSDK.”

## 摘录译文

目前并非所有数据类型都可在 OSDK 中使用。

## 中文要点

- OSDK generator 为 TypeScript、Python、Java 生成对象、Action 和 Function 客户端代码；支持矩阵按 SDK 语言区分。
- 对象属性若为不支持类型，生成器会跳过该属性并记录错误；TypeScript 列出 Cipher、Marking、Vectors，Python 列出 Cipher、Marking、Media、Struct（Python functions 的 Beta Struct 支持例外）和 Vector，Java 列出 TimeSeries、Cipher、Vector。
- Action 参数含不支持类型时无法生成应用 SDK，需要先从 SDK 应用选择范围中移除该 Action；使用 OAuth 2.0 的 webhook Action 也不支持。
- Function 输入/输出类型也可能使包生成失败，例如 Python 的 ObjectSet、TimeSeries、Group、User、OntologyEdit 等；不能只检查对象属性 schema。
- OpenAPI specification 作为其它语言客户端路线，需单独确认其对具体特殊类型的表达能力。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| SDK generation | SDK 生成 | 将 Ontology 资源和类型转换为语言客户端包 |
| property type support | 属性类型支持 | SDK 能否表达对象字段的值类型 |
| webhook Action | Webhook 动作 | 含 OAuth 2.0 出站调用的 Action |
| OpenAPI Specification | OpenAPI 规范 | OSDK 未直接覆盖语言的生成式客户端替代路线 |

## 疑问与待验证项

- 当前列表未承诺 OpenAPI 对每种不支持类型均能无损生成，接入前需核对 schema 表达能力。
- Python Struct 属于 Beta 例外，表示特定 Python functions 场景，不应扩展解释为通用 OSDK 完整 Struct 支持。
- 属性跳过可能造成客户端类型与服务端对象实际字段不同步；需关注生成日志和应用行为。

## 复刻启示

- 多语言 SDK 从共享 Ontology schema 生成时，先按语言能力矩阵校验 schema，再决定字段省略或阻止生成。
- 报错区分属性级警告和 Action/Function 导致的包级失败，显示造成影响的资源依赖链。
- 生成包固定记录目标语言、schema 版本、生成器版本与能力表版本，便于追踪兼容变更。