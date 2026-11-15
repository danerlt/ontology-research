<!-- 页面 URL：https://www.palantir.com/docs/foundry/functions/monitoring -->
<!-- 研读状态：已完成 -->

# Functions • Function management • Function monitoring • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/functions/monitoring)
- 官方中文来源：尚未确认（配对状态：ambiguous）
- 页面语言：英文
- 主题栏目：functions
- 相关性：direct；本体函数文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:02:31Z
- 产品状态：未见本页声明 Beta/预览/弃用；以页面当前说明为准。

## 英文原文短摘录（每个来源不超过 25 词）
> “Functions in Foundry can be monitored to track performance and reliability.”

## 摘录译文
Foundry 函数可通过监控跟踪性能和可靠性。

## 中文要点
- 函数监控支持 P95 执行时长、指定时间窗内全部失败、面向用户失败和非面向用户失败等规则；可按阈值触发告警。
- 失败分类用于区分预期的用户输入错误与基础设施/系统错误；不能将它们合并成单一失败率，否则告警噪声和排障方向都会变差。
- 动态范围支持 Workflow Lineage、Workshop 和 OSDK 应用：系统跟踪范围内使用的函数，并随调用依赖增删更新。
- Ontology Manager 还能查看成功/失败计数和 P95 等近实时指标；这是运维观测能力，不等于对函数语义正确性的验证。

## 术语对照
| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| P95 duration | P95 执行时长 | 95 分位执行耗时，用于观察尾延迟。 |
| user-facing failure | 面向用户的失败 | 函数代码显式报告给调用用户的错误。 |
| dynamic scope | 动态范围 | 跟随指定应用/工作流实际调用函数变化的监控范围。 |

## 疑问与待验证项
- 页面说明规则类型和动态范围，但具体指标留存期、采样延迟、告警重复抑制与不同环境的可用性需查监控规则规范。
- P95 阈值要结合函数调用频率和业务 SLO 设置，低频函数单独看窗口指标可能不稳定。

## 复刻启示
- 为派生属性、Action 和 Agent 工具调用分别记录耗时、结果状态、权限拒绝、输入校验和基础设施错误。
- 监控可按项目、Ontology、应用和函数依赖动态聚合，并在图画布上把异常节点与上游/下游关系关联。
