<!-- 页面 URL：https://www.palantir.com/docs/foundry/functions/user-facing-error -->
<!-- 研读状态：已完成 -->

# Functions • Language-agnostic features • User-facing errors • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/functions/user-facing-error)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/functions/user-facing-error)（配对状态：matched）
- 页面语言：英文
- 主题栏目：functions
- 相关性：direct；本体函数文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:02:46Z
- 产品状态：页面当前未标注特定 Beta/预览/弃用状态；关联功能状态按引用子页复核。

## 英文原文短摘录（每个来源不超过 25 词）

> “Write messages that users can act on: state what was wrong and what to change.”

## 摘录译文

错误信息应让用户能够采取行动：说明问题是什么以及需要改什么。

## 中文要点

- 函数在 Workshop、Action 或函数支持导出中运行时，可以抛出 `UserFacingError`，将特定问题说明显示给终端用户。
- 错误文本应描述实际错误和可修正动作，示例会同时指出要求数量与收到数量；不是所有底层异常都适合原样呈现给用户。
- 不同语言/运行时使用各自的 UserFacingError 导入方式，但面向用户的语义一致；调用者可依据提示修改选择或输入后重试。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| UserFacingError | 用户可见错误 | 由函数作者提供、可展示给调用者的可行动错误信息。 |
| user-facing error | 面向用户的错误 | 用于解释输入或业务问题并指导修正的错误类别。 |
| function-backed export | 函数支持的导出 | 执行函数生成导出内容的宿主能力。 |

## 疑问与待验证项

- 页面着重于消息展示，没有将安全敏感字段脱敏作为自动行为；错误信息应避免包含对象机密或完整令牌。
- 如果业务问题无法由用户修正，应在错误类别中和基础设施失败区分，避免错误地鼓励重试。

## 复刻启示

- 统一结构化错误码、用户消息、开发者诊断信息与可重试标志；接口响应对终端用户只显示安全、具体且可操作的部分。
- 在本体画布试算和 Agent 调用中展示字段级验证错误与修复建议，并记录完整原因到受控审计日志。
