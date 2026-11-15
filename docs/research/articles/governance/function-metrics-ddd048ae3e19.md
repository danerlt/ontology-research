<!-- 页面 URL：https://www.palantir.com/docs/foundry/functions/function-metrics -->
<!-- 研读状态：已完成 -->

# Functions • 函数指标 • Function metrics • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/functions/function-metrics)
- 官方中文来源：尚未确认（配对状态：needs_review）
- 页面语言：英文
- 主题栏目：functions
- 相关性：direct；本体函数文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:02:33Z
- 产品状态：函数指标近实时覆盖最近 30 天成功/失败计数与 P95 时长，运行历史覆盖 7 天。

## 英文原文短摘录（每个来源不超过 25 词）

> “Function metrics display the near real-time usage of a function type over the last 30 days.”

## 摘录译文

函数指标近实时展示函数类型最近 30 天的使用情况。

## 中文要点

- 可从 Ontology Manager 的函数类型总览或 Workflow Lineage 的函数节点查看指标，适合从具体工作流追到函数执行健康。
- 指标包括成功/失败数和 P95 执行时长；执行历史能查看过去 7 天的完整调用记录。
- 失败类型区分运行时、资源限制、用户错误、无效输入/输出、数据加载禁止、未声明类型编辑、结构化错误、部署错误和一致快照错误。
- Foundry Telemetry Service 近实时刷新数据；可嵌入 Workshop Observability Chart，告警支持 P95 时长和时间窗失败数；查看者需有函数 Viewer 权限。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| P95 duration | P95 时长 | 95 百分位的函数执行时间 |
| Run history | 运行历史 | 近期逐次函数执行记录 |
| Undeclared object type edited | 编辑未声明对象类型 | 函数实际写入类型超出函数规格声明的失败 |

## 疑问与待验证项

- 指标窗口为近 30 天且运行历史仅 7 天；需要长期取证时应使用独立遥测/审计保留。
- 资源限制分类文本中“对象类型数量”默认通常 10,000 的具体限额对象需结合官方错误规格复核。

## 复刻启示

- 函数监控按函数版本、分支、调用方和本体资源关联调用数、成功率、P95 延迟与分类失败。
- 把未声明编辑与权限失败单独告警，并支持从 Workflow Lineage 下钻到一次执行及其引用对象。
