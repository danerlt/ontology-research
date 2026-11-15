<!-- 页面 URL：https://www.palantir.com/docs/foundry/action-types/function-actions-batched-execution -->
<!-- 研读状态：已完成 -->

# 动作类型 • 函数支持的动作批量执行 • Batched execution • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/action-types/function-actions-batched-execution)
- 官方中文来源：尚未确认（配对状态：ambiguous）
- 页面语言：英文
- 主题栏目：action-types
- 相关性：direct；本体动作文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:02:03Z
- 产品状态：函数动作可选择逐条处理批次，或把整个调用列表交给一次函数执行。

## 英文原文短摘录（每个来源不超过 25 词）

> “A batched action call will invoke a single function execution with several entries in the list input parameter.”

## 摘录译文

批量 Action 调用会以列表输入的多个条目触发一次函数执行。

## 中文要点

- 常规批量触发通常按请求顺序逐次调用函数，全部编辑在 Action 调用末尾应用；可改为一次接收整个请求批次，以降低开销或处理编辑冲突。
- 批量模式要求函数接收一个列表参数，列表元素为 struct/map/dictionary；单次 Action 也作为一个元素进入同一函数执行。
- 启用后，批量中的多项输入由一次函数执行处理，函数需显式遍历条目并规划各自编辑。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Batched execution | 批量执行 | 将一次批量 Action 的所有条目交给一次函数运行 |
| List parameter | 列表参数 | 承载批量调用项的单一函数输入 |
| Atomic application | 原子应用 | 文档所述 Action 调用结束时统一应用编辑 |

## 疑问与待验证项

- 页面称“编辑在调用末尾原子应用”，需区分这一动作提交语义与跨外部副作用、批次超限或函数异常时的失败行为。
- 多条输入作用于同一对象时如何排序或冲突检测，文档未在该页给出完整矩阵。

## 复刻启示

- 执行引擎可提供逐项与整批两种函数调用策略，并以列表载荷、最大批次、单次执行审计和冲突策略显式配置。
- 试算时按实际函数批次边界展示所有目标对象的编辑集合，避免把“单次执行”误解为“所有副作用可回滚”。
