<!-- 页面 URL：https://www.palantir.com/docs/zh/foundry/action-types/parameter-overview -->
<!-- 研读状态：已完成 -->

# 动作类型 • Parameters • 概述 • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/action-types/parameter-overview)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/action-types/parameter-overview)
- 页面语言：中文
- 主题栏目：action-types
- 相关性：direct；本体动作文档
- 官方更新时间：2026-11-12T17:46:46.935Z
- 目录核对时间：2026-11-14T14:58:19Z
- 产品状态：官方中文页标注为未经验证的 AIP 机器翻译；英文原文为核对依据。

## 英文原文短摘录（每个来源不超过 25 词）

> “Parameters are the inputs of an action type.”

## 摘录译文

参数是操作类型的输入项。

## 中文要点

- 参数具有类型，类型限定可传值的范围；除类型外，还可配置是否显示在表单中、用户能否更改，以及其它参数行为。
- 规则可读取参数值以写入对象/链接或触发副作用；提交条件可引用参数，参数也能读取动作修改前对象属性的当前值。
- Value Type 可将通用约束复用于多个动作/应用；参数覆盖还可影响后续参数配置。
- 页面英文正文定义参数为跨动作规则与应用的输入契约；中文路由译文未校验准确性。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Action parameter | 操作参数 | 动作类型接收的、有类型约束的输入。 |
| Value type | 值类型 | 可复用的属性类型及验证约束。 |
| Parameter override | 参数覆盖 | 根据上下文动态修改参数设置。 |

## 疑问与待验证项

- 复杂类型、集合、对象引用和空值等参数类型的边界应查看类型参考和各专页。
- 参数“不可更改”与“隐藏”是否一致影响服务端校验，需明确其只是表单展示配置还是授权规则。

## 复刻启示

- 以版本化 schema 保存参数的 API 名、显示名称、类型、必填/可见/只读状态、默认值和约束。
- 参数 schema 同时驱动表单生成、规则类型检查、API 输入校验和 SDK 类型生成，避免各消费端定义漂移。
