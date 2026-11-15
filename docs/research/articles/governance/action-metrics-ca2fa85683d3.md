<!-- 页面 URL：https://www.palantir.com/docs/foundry/action-types/action-metrics -->
<!-- 研读状态：已完成 -->

# Action types • Action metrics • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/action-types/action-metrics)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/action-types/action-metrics)（配对状态：matched）
- 页面语言：英文
- 主题栏目：action-types
- 相关性：direct；本体动作运行监控文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:02:20Z
- 产品状态：英文现行页未标 Beta；与中文页的 Beta 标记和指标说明有版本差异。

## 英文原文短摘录（每个来源不超过 25 词）

> “Action metrics display the near real-time usage of an action type over the last 30 days.”

## 摘录译文

动作指标展示某个动作类型在最近 30 天的近实时使用情况。

## 中文要点

- Ontology Manager 动作类型概览页和 Workflow Lineage 的动作节点都可查看指标；核心指标为成功/失败数量和 P95 执行时长，数据来自 Foundry Telemetry Service，近实时更新。
- 指标窗口为 30 天；单个动作的 run history 提供最近 7 天的执行记录。Workshop 可通过 Observability Chart widget 把指标嵌入运维应用。
- 指标用于健康与性能观察，失败分类在中文页中仍标为 Beta 且称在积极开发；英文现行页未出现相同 Beta 状态说明，应该按具体环境和页面版本核对。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| action metrics | 动作指标 | 观察动作类型调用量、成功失败和性能。 |
| P95 duration | P95 执行时长 | 95 分位执行耗时，用于观察慢请求尾部。 |
| run history | 运行历史 | 单个动作最近七天的执行记录。 |
| Workflow Lineage | 工作流沿袭 | 在某次执行图中查看对应动作节点与指标。 |

## 疑问与待验证项

- 英文页与中文页状态、内容颗粒度不同：中文页列出失败原因类别并标 Beta，英文页重点是 30 天聚合指标和七天运行历史；不能假设两种视图的数据保留范围相同。
- 页面未说明指标采样、迟到数据校正、项目/空间过滤方式或 Telemetry 服务不可用时的 SLA，需要结合平台观测文档核验。

## 复刻启示

- 为每种动作保留成功率、失败数和 P95 时长的时间序列，并把聚合视图与逐次运行记录分开；界面明确各自时间窗口和数据新鲜度。
- 在 Workflow Lineage 和本体画布的 Action 节点展示调用健康、耗时和失败入口，让操作审计日志与运行指标通过 action ID 关联但职责分离。
- 指标分类采用可演进的维度；对 Beta 或未稳定分类标注来源版本，不将某一页列出的错误类别固化为完整错误全集。
