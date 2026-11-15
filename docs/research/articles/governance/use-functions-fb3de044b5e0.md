<!-- 页面 URL：https://www.palantir.com/docs/foundry/functions/use-functions -->
<!-- 研读状态：已完成 -->

# Functions • Function consumption • Use functions in the platform • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/functions/use-functions)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/functions/use-functions)（配对状态：matched）
- 页面语言：英文
- 主题栏目：functions
- 相关性：direct；本体函数文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:02:33Z
- 产品状态：页面当前未标注特定 Beta/预览/弃用状态；关联功能状态按引用子页复核。

## 英文原文短摘录（每个来源不超过 25 词）

> “Function-backed variables cache results for identical inputs instead of recomputing them.”

## 摘录译文

由函数支持的变量会缓存相同输入的结果，而不是重复计算。

## 中文要点

- 函数可嵌入多类产品行为：Workshop 变量计算值/对象集、对象表派生列、图表聚合；Action 中承载复杂对象编辑与通知/webhook 参数计算。
- Workshop 的函数变量会对相同输入缓存结果，并可设置依赖变量变化时的重算方式，或由事件显式触发重算。
- Slate、Quiver 和 Automate 也能消费函数，但各自数据语义不同；Automate 函数异步运行，最长可运行 4 小时。返回 Ontology edits 的普通函数效果不会自动应用这些编辑，写操作应使用 Function-backed Action。
- 该页是消费入口索引而非单一运行时规范；函数支持的输入输出类型、权限、版本和副作用还需按具体宿主应用核对。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| function-backed variable | 函数支持的变量 | 用函数计算并供 Workshop 模块复用的变量。 |
| function-backed column | 函数支持的列 | 按对象计算展示值的表格派生列。 |
| function aggregation | 函数聚合 | 在图表或对象集分析中计算聚合指标。 |
| function effect | 函数效果 | Automate 中执行函数的自动化效果。 |

## 疑问与待验证项

- 缓存键、缓存时长、主动失效规则由宿主应用的变量配置决定，不能假设跨应用共享同一函数缓存。
- 不同应用对函数返回 Ontology edits 的处理并不一致，必须把只读计算与写入 Action 分开设计。

## 复刻启示

- 以统一函数定义连接画布、本体对象表、看板和 Agent 工具；在每个调用点保存输入、调用版本、权限主体和结果引用。
- 对缓存、重算、异步任务和写入副作用做显式配置，UI 显示数据新鲜度和结果来源。
