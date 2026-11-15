<!-- 页面 URL：https://www.palantir.com/docs/foundry/functions/types-reference -->
<!-- 研读状态：已完成 -->

# Functions • Types reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/functions/types-reference)
- 官方中文来源：尚未确认（配对状态：ambiguous）
- 页面语言：英文
- 主题栏目：functions
- 相关性：direct；本体函数文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:02:26Z
- 产品状态：未见本页声明 Beta/预览/弃用；以页面当前说明为准。

## 英文原文短摘录（每个来源不超过 25 词）
> “a TypeScript function must have explicit type annotations on all input parameters and specify an explicit return type.”

## 摘录译文
TypeScript 函数的所有输入参数必须显式标注类型，并指定显式返回类型。

## 中文要点
- 页面提供 Function Registry 类型与 TypeScript v1、TypeScript v2、Python 类型之间的映射表，覆盖标量、集合、Ontology、媒体、用户/组和几何类型。
- TypeScript 函数进入 registry 前，所有输入参数和返回类型都需显式声明；映射表显示同一 Registry 类型在不同 SDK 版本/语言中的类型名可能不同。
- Pipeline Builder Python UDF 按行执行，函数应返回每行的新标量值，而非 DataFrame；需要区分普通函数和批处理/数据帧语义。

## 术语对照
| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Function Registry type | 函数注册表类型 | 平台用于声明函数输入输出的规范类型。 |
| TypeScript v1 / v2 | TypeScript v1 / v2 | 不同函数运行时/API 版本的语言类型映射。 |
| Python UDF | Python 用户定义函数 | 在 Pipeline Builder 逐行运行并产生新列值的函数。 |

## 疑问与待验证项
- 完整映射表随平台版本扩展；本地复刻需定义兼容矩阵并对未知类型快速报错。
- 页面中某些类型在特定语言标注为不支持，需结合当前函数运行时版本而不是只检查语言名称。

## 复刻启示
- 建立集中、版本化的 schema 类型注册表，负责校验、序列化和跨语言 SDK 代码生成。
- 对函数输入/输出做静态 schema 校验；将 UDF 的逐行标量语义与批量数据管道接口分开。
