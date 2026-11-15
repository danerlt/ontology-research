<!-- 页面 URL：https://www.palantir.com/docs/foundry/functions/overview -->
<!-- 研读状态：已完成 -->

# Functions • Overview • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/functions/overview)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/functions/overview)（配对状态：matched）
- 页面语言：英文
- 主题栏目：functions
- 相关性：direct；本体函数文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T14:53:14Z
- 产品状态：按页面现行表述整理；若标注 Preview，相关 API 可能变化。

## 英文原文短摘录（每个来源不超过 25 词）

> “Functions include first-class support for authoring logic based on the Ontology.”

## 摘录译文

Functions 原生支持围绕 Ontology 编写逻辑。

## 中文要点

- Functions 在服务端隔离环境中执行，面向仪表盘、应用等需要快速返回结果的业务交互。
- 它可读取多类对象属性、遍历链接并执行本体编辑；常见用法包括对象集/变量返回、派生表列、聚合图表和函数支持的 Action。
- Functions 还能调用外部系统丰富对象、为语言模型逐步流式返回结果；文档列出的语言是 TypeScript 与 Python。
- 这里的“Ontology 逻辑”范围比派生属性宽，包含查询、编辑及外部调用；不能把所有 Function 都当作属性求值器。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| server-side execution | 服务端执行 | 业务逻辑在隔离服务端环境运行。 |
| function-backed action | 函数支持的动作 | 由函数表达可批量更新多个本体对象的复杂编辑。 |
| external function | 外部函数 | 查询外部系统并将结果用于本体对象丰富。 |

## 疑问与待验证项

- 不同语言版本的具体功能支持和版本限制需查看语言支持矩阵及各语言指南。
- 概述未承诺函数与派生属性的缓存、事务或延迟语义。

## 复刻启示

- 将派生属性、查询函数、写操作函数和外部集成按不同能力建模；表达式画布只暴露与该属性类型兼容的纯读取子集。
- 函数运行应记录输入对象、读取路径、调用的外部系统、写入 Action 和执行耗时，便于解释和审计。
