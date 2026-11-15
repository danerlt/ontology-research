<!-- 页面 URL：https://www.palantir.com/docs/zh/foundry/ontology-sdk/unsupported-types -->
<!-- 研读状态：已完成 -->

# OSDK • Ontology SDK 不支持的类型 • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/ontology-sdk/unsupported-types)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/ontology-sdk/unsupported-types)
- 页面语言：中文（译文准确性需与现行英文页核对）
- 主题栏目：ontology-sdk
- 相关性：direct；OSDK 生成时的属性、Action 与 Function 类型约束
- 官方更新时间：2026-11-12T17:46:46.932Z
- 目录核对时间：2026-11-14T15:01:03Z
- 产品状态：不同语言 SDK 的不支持类型集合不同；生成失败和跳过属性的后果不同

## 英文原文短摘录（不超过 25 词）

> “the code generator will skip that property and log the error.”

## 摘录译文

代码生成器会跳过该属性并记录错误。

## 中文要点

- OSDK 为 TypeScript、Python、Java 生成对象、Action 和 Function 客户端代码，但类型支持存在语言差异。
- 对象属性层面：TypeScript 不支持 Cipher、Marking、Vectors；Python 不支持 Cipher、Marking、Media、Vector，以及除 Beta 函数支持以外的 Struct；Java 不支持 TimeSeries、Cipher、Vector。
- Action 参数不支持的类型可能导致整个 SDK 包无法生成，而不是只跳过参数；有些需暂时将相关 Action 从 SDK 应用范围移除。
- 使用 OAuth 2.0 webhook 的 Action 不支持 OSDK；Function 输入/输出另有按语言区分的不支持类型集合。
- 文档中的代码生成错误行为区分“跳过属性并记录”与“包生成失败”，不能统一看成隐藏字段。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| unsupported property type | 不支持的属性类型 | 生成客户端时无法映射的对象字段类型 |
| unsupported action parameter | 不支持的 Action 参数 | 会阻止 SDK 包生成的 Action 输入类型 |
| unsupported function I/O type | 不支持的 Function 输入/输出类型 | 生成函数客户端时无法表达的类型 |
| code generation skip | 代码生成跳过 | 属性被忽略并输出错误日志的行为 |

## 疑问与待验证项

- 中文卡片对应源页面可能为官方机翻，也存在目录配对状态差异；最终应以英文路由当前列表为基准。
- 支持类型清单可能随 SDK 生成器版本变化，文档没有在每种类型旁列出最低可用版本。
- 若属性被跳过，运行时数据如何通过 REST/OpenAPI 读取要看其它客户端/API 能力，不能由类型清单推断。

## 复刻启示

- OSDK generator 应有语言能力矩阵，逐项标记对象字段、Action 参数、Function 输入/输出与附件支持状态。
- 生成前做静态兼容检查，给出资源名、属性名、类型、受影响语言和“字段跳过/包失败”的具体影响。
- 语言 SDK 的类型兼容应作为有版本号的能力数据，不以统一模型强行假设所有语言同构。