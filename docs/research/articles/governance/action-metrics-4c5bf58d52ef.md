<!-- 页面 URL：https://www.palantir.com/docs/zh/foundry/action-types/action-metrics -->
<!-- 研读状态：已完成 -->

# 动作类型 • 操作指标 [测试版] • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/action-types/action-metrics)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/action-types/action-metrics)
- 页面语言：中文
- 主题栏目：action-types
- 相关性：direct；本体动作运行监控文档
- 官方更新时间：2026-11-12T17:46:46.935Z
- 目录核对时间：2026-11-14T14:58:13Z
- 产品状态：中文页明确标为 Beta，并说明失败分类仍在积极开发；与英文现行页面状态不同。

## 英文原文短摘录（每个来源不超过 25 词）

> “Action metrics display the near real-time usage of an action type over the last 30 days.”

## 摘录译文

操作指标显示某操作类型在过去 30 天内的近实时使用情况。

## 中文要点

- 中文页描述 Ontology Manager 中操作类型的使用情况，并明确操作指标无需启用操作日志；它与操作日志的关键区别之一是指标会跟踪失败。
- 页面列举无效参数、规模限制、认证、side effect、函数以及未分类失败等类别；其中规模限制示例提到默认通常为 10,000 个受影响对象，实际限制需以目标环境设置为准。
- 该页提示是 AIP 自动翻译且未验证。英文现行页补充最近 30 天的近实时成功/失败与 P95 指标、最近 7 天运行历史；不同语言文档的 Beta 状态也不一致。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| invalid parameter failure | 参数无效失败 | 提交上下文中的参数不合法。 |
| scale limit failure | 规模限制失败 | 动作影响对象数量超过当前限制。 |
| side effect failure | 副作用失败 | Webhook 或配置错误导致动作执行失败。 |
| uncategorized failure | 未分类失败 | 不能归入已列出的失败原因类别。 |

## 疑问与待验证项

- 中文页的失败分类与 10,000 示例是否仍适用于各存储版本、动作写入模式和环境，需要实测；不要把该例值当作普遍硬上限。
- 该页的 Beta 标签与英文现行页的状态差异可能来自页面更新不同步或产品 enrollment，当前实际状态仍需查询环境。

## 复刻启示

- 失败记录要保留结构化类别和原始错误码；分类不可识别时使用可查询的兜底类别，同时允许运维人员查看脱敏后的执行轨迹。
- 对调用方展示动作日志与失败指标是两套机制；失败动作不应因“没有成功日志对象”而从运维视野消失。
