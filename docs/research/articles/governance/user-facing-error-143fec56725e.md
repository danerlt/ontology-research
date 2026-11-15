<!-- 页面 URL：https://www.palantir.com/docs/zh/foundry/functions/user-facing-error -->
<!-- 研读状态：已完成 -->

# 函数 • Ontology edits • 抛出用户界面错误 • Palantir

- 英文来源：[现行英文原文](https://www.palantir.com/docs/foundry/functions/user-facing-error)
- 官方中文来源：[官方中文页（AIP 机器翻译，准确性未独立验证）](https://www.palantir.com/docs/zh/foundry/functions/user-facing-error)
- 页面语言：中文（官方 AIP 机器翻译，需与英文原文交叉核对）
- 主题栏目：functions
- 相关性：direct；本体函数文档
- 官方更新时间：2026-11-12T17:46:46.935Z
- 目录核对时间：2026-11-14T14:59:48Z
- 产品状态：TypeScript v1/v2 与 Python 函数均可抛出 UserFacingError；在 Workshop Action 或导出等宿主中，该消息会显示给用户。

## 原文短摘录与翻译

> “throw a UserFacingError to show users a specific message that explains what went wrong and how to fix it.”

## 摘录译文

抛出 `UserFacingError`，向用户显示具体说明错误原因及修复方式的消息。

## 中文要点

- UserFacingError 将可操作的业务错误转成用户可见消息；函数作者应说明发生了什么以及用户可采取的修复步骤。
- 文档示例在参数数量不符合要求时展示实际与期望值，并可由 Workshop function-backed Action 或 function-backed export 显示错误。
- TSv1、TSv2 与 Python 的导入/使用语法不同，但面向用户的异常意图一致。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| `UserFacingError` | 用户可见错误 | 在应用界面展示给终端用户的函数错误类型 |
| actionable message | 可执行的错误提示 | 告诉用户如何修正输入或状态的错误信息 |
| function-backed export | 函数支持的导出 | 由函数生成导出数据并呈现失败反馈的入口 |

## 疑问与待验证项

- 错误字符串来自函数作者；应避免在其中返回 SQL、内部 stack trace、秘密或无权访问字段的存在信息。
- 用户可见错误与系统异常/服务不可用应区别处理：前者提供输入纠正提示，后者需保留诊断上下文并返回通用错误。

## 复刻启示

- 错误协议区分业务校验、权限拒绝、外部连接失败和内部异常；业务消息可操作，审计日志保留 request ID 与原因码。
- Agent 工具反馈错误时把修正要求返回给规划器，但不把内部调试细节或凭据传回模型上下文。
- 对 Action 提交前做字段级校验并展示具体问题，减少用户执行后才遇到难以理解的失败。
