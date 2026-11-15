<!-- 页面 URL：https://www.palantir.com/docs/foundry/functions/typescript-error-types -->
<!-- 研读状态：已完成 -->

# Functions • TypeScript v1 • Error types • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/functions/typescript-error-types)
- 官方中文来源：尚未确认（配对状态：ambiguous）
- 页面语言：英文
- 主题栏目：functions
- 相关性：direct；本体函数文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:03:05Z
- 产品状态：TSv1 专属语法；TSv2 的函数类型与错误处理方式不同。

## 英文原文短摘录（每个来源不超过 25 词）

> “In addition to declaring an output type on your TypeScript function, you can also declare an error type.”

## 摘录译文

TypeScript 函数除了声明输出类型，也可以声明错误类型。

## 中文要点

- 通过 `FunctionsError<name, value>` 定义具名错误及可选载荷，并用 `FunctionsResult<Output, Error>` 表达成功或业务错误的联合返回。
- 函数用 `FunctionsResult.ok/err` 构造结果；若作为跨仓库 Query 调用，返回 Result，调用者通过 `isOk/isErr` 分支并读取错误名和载荷。
- 默认 Result 也可能携带 CPU 超时、墙钟超时、内存不足或运行时失败等执行基础设施错误。
- 本页特别强调 typed error 在 TSv1 Query 间传播；不能将可预期业务错误与异常/执行故障混为一类。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| FunctionsError | 函数错误类型 | 含稳定错误名与可选值载荷的业务错误契约。 |
| FunctionsResult | 函数结果类型 | 组合函数输出与具名错误的联合返回。 |
| isOk / isErr | 结果类型守卫 | 判断 Query 返回成功还是错误。 |

## 疑问与待验证项

- 错误载荷可包含对象/对象集，跨边界时需核查序列化、权限和错误信息泄露风险。
- 该类型模式限定于 TSv1；迁移 TSv2 前应核对错误契约对应的替代机制。

## 复刻启示

- Agent 工具和派生属性预览采用稳定的结构化错误码/载荷；展示给用户的文本和内部诊断分开。
- 调用链将 Query 的业务错误作为可分支结果传递，运行时超时则标为基础设施失败。
