<!-- 页面 URL：https://www.palantir.com/docs/zh/foundry/functions/use-functions -->
<!-- 研读状态：已完成 -->

# 函数 • 在平台中使用函数 • Palantir

- 英文来源：[现行英文原文](https://www.palantir.com/docs/foundry/functions/use-functions)
- 官方中文来源：[官方中文页（AIP 机器翻译，准确性未独立验证）](https://www.palantir.com/docs/zh/foundry/functions/use-functions)
- 页面语言：中文（官方 AIP 机器翻译，需与英文原文交叉核对）
- 主题栏目：functions
- 相关性：direct；本体函数文档
- 官方更新时间：2026-11-12T17:46:46.935Z
- 目录核对时间：2026-11-14T14:59:47Z
- 产品状态：Foundry Functions 可在 Workshop、Actions、Slate、Quiver 和 Automate 中复用，分别用于变量/函数列/聚合、受控写入、分析及自动化任务。

## 原文短摘录与翻译

> “Function-backed variables cache results for identical inputs instead of recomputing them.”

## 摘录译文

由函数支持的变量会缓存相同输入的结果，不必重复计算。

## 中文要点

- Workshop 函数变量可由依赖输入触发重算，并缓存相同参数的结果；Object Table 可动态计算函数列，Chart 可按当前用户选择运行函数聚合。
- Action 通过函数定义复杂本体编辑逻辑和副作用参数；Webhook 可将用户提交的 Action 集成到外部系统。
- Slate 的自有 JavaScript snippets 与 Foundry Functions 是不同机制，后者可访问本体对象。
- Quiver 可复用函数对象集/分类/值/时序输出；Automate 允许在满足条件时异步执行固定版本函数，稳定语义版本可配置自动兼容升级。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Function-backed variable | 函数支持的变量 | 由函数计算并供应用其他组件使用的 Workshop 变量 |
| Function-backed column | 函数计算列 | 在对象表格中按对象计算的动态列 |
| Function-backed aggregation | 函数支持的聚合 | 基于函数输出或用户选择计算的图表汇总 |
| function-backed automation | 函数支持的自动化 | 由条件触发并异步运行函数的自动化任务 |

## 疑问与待验证项

- 页面罗列多种使用入口，但各宿主的变量缓存、重算触发、版本选择和超时策略不同，需要逐项查看宿主文档。
- Automate 的最长运行时和稳定版本自动升级规则可能随平台治理调整，应视为配置/文档快照。
- Slate 内部函数与 Foundry Functions 名称相似但本体集成能力不同，迁移时不能自动互换。

## 复刻启示

- 设计函数注册中心，让 Workshop 式应用变量、画布派生列、Action 写入和 Automate 触发复用同一逻辑版本并明确读写副作用。
- UI 展示每个函数在哪里被消费、依赖哪些应用和本体资源；版本升级显示影响范围与缓存失效策略。
- Agent 自动化优先调用只读 Query；需要对象写入时使用经授权的 Action，异步任务记录触发条件、函数版本和执行状态。
