<!-- 页面 URL：https://www.palantir.com/docs/zh/foundry/action-types/function-actions-overview -->
<!-- 研读状态：已完成 -->

# 动作类型 • 函数支持的动作概述 • Function-backed actions • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/action-types/function-actions-overview)
- 官方中文来源：尚未确认（配对状态：not_applicable）
- 页面语言：中文
- 主题栏目：action-types
- 相关性：direct；本体动作文档
- 官方更新时间：2026-11-12T17:46:46.935Z
- 目录核对时间：2026-11-14T14:58:13Z
- 产品状态：函数支持的 Action 用于表达结构化规则无法覆盖的多对象逻辑，且受 Action/Function 执行限制。

## 原文短摘录与翻译

> 【待研读：摘录中文原文】

## 摘录译文

【待填写】

## 中文要点

【用自己的话概括本页解决的问题、对象和关键操作。】

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| 【待填写】 | 【待填写】 | 【待填写】 |

## 疑问与待验证项

- 【记录文档未说明之处、与其他页面的差异，以及需要验证的假设。】

## 复刻启示

- 【写出对本体管理系统的数据模型、治理流程、权限或 Agent 接入的具体启示。】
## 英文原文短摘录（每个来源不超过 25 词）

> “Many action types can be defined using simple rules which allow you to create, modify, and delete objects”

## 摘录译文

许多 Action 类型可以用简单规则创建、修改和删除对象。

## 中文要点

- 简单规则可以处理常见对象属性和链接编辑；当逻辑要同时修改互相关联对象、跨对象计算属性，或创建多种对象并建立链接时，可调用函数。
- Function-backed action 的函数负责定义对象如何变化，可以读取多个对象并产生写入编辑。
- 灵活性仍受 Action 类型限制与函数执行限制约束；函数不等于无上限、任意外部代码执行环境。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Function-backed action | 函数支持的动作 | 由函数定义复杂本体变更逻辑的 Action |
| Ontology edit | 本体编辑 | 函数返回或提交的对象/链接变更 |
| Execution limit | 执行限制 | Action 与函数运行时的资源/规模边界 |

## 疑问与待验证项

- 复杂函数动作的对象数、编辑数、运行时长与副作用限制应以各限制页和目标租户配置为准。
- 函数从外部系统读取数据时的身份传播、超时及重试语义并非本概览的范围。

## 复刻启示

- 简单字段写入优先采用声明式规则；只在多对象事务逻辑确有需要时升级到函数动作，便于审查和预测差异。
- 函数动作需要依赖图、允许变更对象类型清单、运行上限和可追踪的编辑结果。
