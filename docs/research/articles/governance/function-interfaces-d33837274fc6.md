<!-- 页面 URL：https://www.palantir.com/docs/foundry/functions/function-interfaces -->
<!-- 研读状态：已完成 -->

# Functions • 函数接口 • Function interfaces • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/functions/function-interfaces)
- 官方中文来源：尚未确认（配对状态：needs_review）
- 页面语言：英文
- 主题栏目：functions
- 相关性：direct；本体函数文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:03:18Z
- 产品状态：函数接口定义输入、输出与错误契约，使平台应用能发现并专门调用符合契约的用户实现。

## 英文原文短摘录（每个来源不超过 25 词）

> “Function interfaces define how an application or user should interact with a function.”

## 摘录译文

函数接口定义应用或用户应如何与函数交互。

## 中文要点

- 函数接口只定义签名契约（输入、输出、错误），它本身不是可执行函数，而是由实际函数实现。
- Foundry 应用可按接口发现兼容函数并提供专门行为；用户可实现某些接口，平台仍可使用原生集成。
- ChatCompletion 接口用于多轮/多用户对话，AIP Logic 的 Use LLM block 可从平台模型或注册模型中选择实现。
- 接口兼容需匹配结构与输入约束；如接口所有输入字段可选，自定义类型仍须至少共享一个可选字段。页面还提示 AIP Logic 按位置校验参数名。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Function interface | 函数接口 | 输入/输出/错误契约与应用集成边界 |
| Interface implementation | 接口实现 | 满足函数接口签名的具体用户函数 |
| ChatCompletion | 对话补全接口 | 可由自定义 LLM 函数实现的对话能力契约 |

## 疑问与待验证项

- 官方列出 Pipeline Builder 支持“即将推出”，这是时点敏感的产品状态，使用时需重新核验。
- 接口兼容除静态类型外还包含参数名/顺序和错误语义，注册前应使用平台验证结果而非只看类型子集。

## 复刻启示

- Agent/LLM 能力通过注册接口提供标准签名，再由 AIP Logic/应用发现实现，避免把模型调用写死在单一供应商适配器。
- 接口注册保留能力描述、输入/输出类型、错误结构和运行授权，并提供实现者兼容性验证。
