<!-- 页面 URL：https://www.palantir.com/docs/foundry/action-types/inline-edits -->
<!-- 研读状态：已完成 -->

# 动作类型 • 行内编辑 • Inline edits • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/action-types/inline-edits)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/action-types/inline-edits)（配对状态：matched）
- 页面语言：英文
- 主题栏目：action-types
- 相关性：direct；本体动作文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:02:13Z
- 产品状态：行内编辑把对象现值作为参数默认值，并以批量提交语义运行，具有严格的动作兼容限制。

## 英文原文短摘录（每个来源不超过 25 词）

> “every parameter is optional and defaults to the existing value of the object”

## 摘录译文

每个参数都是可选的，并默认取对象当前值。

## 中文要点

- 对象浏览器行内编辑在 Ontology Manager 的对象属性交互设置中绑定 Action；每个属性只能绑定一种行内编辑 Action，但多个属性可共用动作。
- 对象浏览器/对象视图的动作只能修改单个对象的单一类型，必须启用默认值且从对象引用参数取值；不能靠静态值、Current User/Time 映射编辑属性，也不能启用通知或 webhook。
- Workshop 行内编辑会批量校验与提交；同一批不能重复写同一对象、创建同一链接或依赖聚合一致性。读取可能被其他动作写入的数据也可能导致错误。
- Scenario 中的行内编辑改为非确定顺序逐个应用；文档不建议应用依赖此差异。连接表链接以及引用共享/链接对象的提交条件不兼容。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Inline edit | 行内编辑 | 直接从表格或对象视图改单一字段的 Action 入口 |
| Existing value default | 现值默认 | 未改参数以目标对象当前值补齐 |
| Bulk submission | 批量提交 | 多个行内变更一起校验和提交的模式 |

## 疑问与待验证项

- 页面区分 Workshop 与 Object Explorer 的行为和配置；跨场景一致性需要逐个应用验证，特别是 Scenario 的非确定顺序。
- 聚合值一致性约束由哪些提交条件/函数触发，页面未给出可静态判定的完整规则。

## 复刻启示

- 行内编辑绑定前执行单对象/单类型/默认值/副作用兼容校验；批量队列按对象和关系冲突去重。
- 服务端应将所有参数基于每个目标对象现值补齐后逐项评估授权与条件，再按明确的冲突策略提交。
