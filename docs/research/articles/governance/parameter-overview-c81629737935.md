<!-- 页面 URL：https://www.palantir.com/docs/foundry/action-types/parameter-overview -->
<!-- 研读状态：已完成 -->

# 动作类型 • 参数概述 • Parameters • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/action-types/parameter-overview)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/action-types/parameter-overview)（配对状态：matched）
- 页面语言：英文
- 主题栏目：action-types
- 相关性：direct；本体动作文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:01:54Z
- 产品状态：参数连接 Action 表单、规则、提交条件和副作用，是运行时输入而非对象属性本身。

## 英文原文短摘录（每个来源不超过 25 词）

> “Parameters are the inputs of an action type.”

## 摘录译文

参数是 Action 类型的输入。

## 中文要点

- 参数有类型，配置其是否在表单中显示、是否允许用户修改；也可以复用值类型约束。
- 规则可读取参数来写对象、链接或副作用；提交条件可验证参数；默认值和覆盖可读取之前参数或对象属性。
- 宿主应用可把变量传入隐藏参数，以在动作写入前保留对象旧值；新值和旧值随后都可传给规则。
- 示例以 Ticket 对象参数和 Status 字符串参数分别承载目标对象与未来状态。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Action parameter | Action 参数 | 动作调用输入 schema 中的一个值 |
| Host application | 宿主应用 | Workshop、Slate、Object Views 等 Action 消费方 |
| Hidden parameter | 隐藏参数 | 接收上下文输入但不让用户直接编辑的参数 |

## 疑问与待验证项

- 同一 Action 在不同宿主应用注入参数时的来源优先级应查看应用侧文档。
- 参数类型约束与值类型验证是否在所有宿主端保持一致，需测试跨应用的表单渲染。

## 复刻启示

- Action 参数模型应与本体属性分离，并可被规则、校验、默认值、覆盖和副作用按引用消费。
- 调用 API 要显式区分用户可编辑输入、宿主上下文及对象现值快照，保存其来源便于审计。
