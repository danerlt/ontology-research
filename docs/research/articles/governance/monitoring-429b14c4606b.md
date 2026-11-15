<!-- 页面 URL：https://www.palantir.com/docs/foundry/action-types/monitoring -->
<!-- 研读状态：已完成 -->

# Action types • Monitoring • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/action-types/monitoring)
- 官方中文来源：未找到确定的一对一官方中文页（配对状态：ambiguous）
- 页面语言：英文
- 主题栏目：action-types
- 相关性：direct；动作可靠性与告警文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:02:20Z
- 产品状态：基于平台 Monitoring views/rules 与告警订阅能力配置。

## 英文原文短摘录（每个来源不超过 25 词）

> “Action monitoring in Foundry supports two key rule types:”

## 摘录译文

Foundry 的动作监控支持两类主要规则。

## 中文要点

- 当前页面列出两类动作监控规则：P95 执行时长超过阈值告警，以及某时间窗口内动作失败数量超过阈值告警。
- 配置过程是创建 monitoring view、对动作或动作类型添加规则、设置阈值与严重级别，再配置告警订阅。
- 动作监控可使用 Workflow Lineage、Workshop 或 OSDK application 的动态范围；范围内引用的动作新增/移除后，监控对象会自动调整。
- 运行指标负责描述健康状态，监控规则把指标阈值变成可通知事件；操作日志记录成功决定的业务背景，不能把它们混为一个日志表。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| monitoring view | 监控视图 | 聚合并展示规则所需的被监控对象与指标。 |
| action duration p95 | 动作 P95 时长 | 用 95 分位执行耗时设置阈值。 |
| dynamic scope | 动态范围 | 自动跟踪应用/工作流依赖动作的增删变化。 |
| alert subscription | 告警订阅 | 设置告警向哪些接收方和渠道发送。 |

## 疑问与待验证项

- 文档只列出两种 Action 规则类型；通用 Monitoring 是否支持业务条件、按项目过滤和去重静默，需要查对应规则参考页。
- 告警延迟、评估频率、缺失指标处理和通知失败重试策略没有在本页展开。

## 复刻启示

- 在动作配置之外建立可复用监控定义，支持阈值、窗口、严重级别、动态 scope 和告警订阅；显示规则当前追踪的动作集合。
- 将运行指标、审计事件与告警事件用 action ID 关联，保留各自生命周期；可通过画布 Action 节点快速跳转指标、错误追踪和审计记录。
