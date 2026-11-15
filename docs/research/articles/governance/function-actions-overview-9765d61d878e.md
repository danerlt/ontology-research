<!-- 页面 URL：https://www.palantir.com/docs/zh/foundry/action-types/function-actions-overview -->
<!-- 研读状态：已完成 -->

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/action-types/function-actions-overview)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/action-types/function-actions-overview)
- 页面语言：中文
- 主题栏目：action-types
- 相关性：direct；本体动作文档
- 官方更新时间：2026-11-12T17:46:46.935Z
- 目录核对时间：2026-11-14T14:58:13Z
- 产品状态：函数支持的 Action 用于表达结构化规则无法覆盖的多对象逻辑，且受 Action/Function 执行限制。

## 英文原文短摘录（每个来源不超过 25 词）

> “In an action type, rules define the ways objects should change when the action is applied.”

## 摘录译文

在操作类型中，规则定义应用该操作时对象应发生哪些变化。

## 中文要点

- 简单规则适用于常见对象属性和链接编辑；当逻辑需要同时修改多个相关对象、跨对象计算属性或创建多种对象并建立链接时，可使用函数支持的 Action。
- 函数支持的 Action 通过 Ontology Edit 函数定义对象如何变化；函数可读取多个对象并返回本体编辑。
- 函数执行仍受 Action 类型和运行时资源限制，不能视为没有边界的任意代码环境。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Function-backed action | 函数支持的 Action | 由函数定义复杂本体变更逻辑的操作类型 |
| Ontology Edit function | 本体编辑函数 | 返回对象或链接变更的函数 |
| Ontology edit | 本体编辑 | 创建、修改或删除本体对象的变更 |

## 疑问与待验证项

- 多对象编辑是否在 Action 提交时作为同一事务执行，需结合具体函数与 Action 文档验证。
- 函数读取外部数据时的身份传播、超时和重试语义不属于本概览范围。

## 复刻启示

- 常见字段写入优先使用声明式规则；只有多对象或复杂业务逻辑确有需要时才调用函数，以便审查和预估变更。
- 函数动作应记录允许变更的对象类型、依赖路径、运行限制及逐项编辑结果，供评审和审计。
