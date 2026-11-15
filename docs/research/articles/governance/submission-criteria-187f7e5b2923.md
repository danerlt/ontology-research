<!-- 页面 URL：https://www.palantir.com/docs/zh/foundry/action-types/submission-criteria -->
<!-- 研读状态：已完成 -->

# 动作类型 • 提交标准 • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/action-types/submission-criteria)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/action-types/submission-criteria)（已直接核验；页面声明未经验证的机器翻译）
- 页面语言：中文
- 主题栏目：action-types
- 相关性：direct；动作提交治理文档
- 官方更新时间：2026-11-12T17:46:46.935Z
- 目录核对时间：2026-11-14T14:58:29Z
- 产品状态：中文页面是 AIP 机器翻译且未验证；其条件模板说明比英文页少。

## 原文短摘录与翻译

> “只有当所有提交标准都满足时，操作才能提交。”

**对应英文：** “Actions can only be submitted if all the submission criteria are met.”

## 摘录译文

配置的全部提交标准都必须通过，动作才能提交。

## 中文要点

- 条件由用户、参数和静态值的比较组成，可读取用户 ID、组成员资格、Multipass 属性或对象参数中的属性；多个条件可按 all/any/none 逻辑嵌套。
- 提交标准是每个动作独立的运行资格判断，不等于编辑动作定义的权限。失败消息可显示阻止原因，Ontology Manager 提供指定参数的试运行。
- 中文页列举 Current user 与 Parameter 条件模板，但英文现行页还说明 Execution context，可判断动作是否在 Scenario 中执行；英文页也明确附件和 Object Set 参数不支持，以及 scoped token 下对组/标记/组织使用 NOT 的风险。
- 本页提示译文未经 AIP 验证，不能以中文页未列出某能力就推断英文现行页不支持。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| 条件模板 | condition template | 配置用户属性或动作参数比较上下文。 |
| 逻辑运算符 | logical operator | 组合多个条件并可嵌套。 |
| 失败消息 | failure message | 向用户解释未通过标准的原因。 |

## 疑问与待验证项

- 中文内容未覆盖英文当前的执行上下文、附件/Object Set 参数限制与 scoped token 风险；当前实现路线需以英文页面和实际产品能力为准。
- 中文页没有解释逻辑否定在有限权限属性下的安全问题，需避免从翻译遗漏中引入错误配置。

## 复刻启示

- 中文产品文案应跟随能力版本更新；设计条件节点时为用户上下文、参数、Scenario 上下文提供明确标签和类型提示。
- 对权限判定采用 fail-closed 设计；如果表达式所需属性对当前调用主体不可见或缺失，返回拒绝并给管理员可诊断的解释。
