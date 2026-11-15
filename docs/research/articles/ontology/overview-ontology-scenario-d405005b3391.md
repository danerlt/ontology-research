<!-- 页面 URL：https://www.palantir.com/docs/foundry/ontology/overview-ontology-scenario -->
<!-- 研读状态：已完成 -->

# Overview • Ontology • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/ontology/overview-ontology-scenario)
- 官方中文来源：尚未确认（配对状态：ambiguous）
- 页面语言：英文
- 主题栏目：ontology
- 相关性：direct；本体模型与治理文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:04:03Z
- 产品状态：当前页面的 Ontology scenarios 标注 Beta，提供用于 what-if 分析和动作/函数试算的隔离数据沙箱；不用于历史时点快照。

## 英文原文短摘录（每个来源不超过 25 词）

> “Scenarios are not data versioning tools.”

## 摘录译文

Scenario 不是数据版本管理工具。

## 中文要点

- Scenario 在主本体或全局分支数据上叠加由一个或多个 Action 产生的编辑，可比较策略、模拟业务过程、评估预测或 Agent。
- 默认 31 天后自动删除；每 10 分钟自动 rebase 到基线，不能任意手动 rebase 或配置周期。
- Scenario 与 Global Branching 用途不同：分支帮助 builder 隔离开发平台资源，scenario 让人/Agent 在不影响主数据的情况下测试业务变更并比较、合并结果。
- Action submission criteria 可区分 scenario 与 main 执行环境；合并另受 merge action 的条件控制。多数函数直接针对 scenario 状态读写，AIP Logic 需要启用 staged writes。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Ontology scenario | 本体场景 | 基于主本体或分支数据进行隔离业务试算的环境。 |
| auto-rebase | 自动变基 | 周期性把基线最新变化纳入活动场景。 |
| merge action | 合并 Action | 经独立提交条件批准后将场景编辑应用到主本体。 |

## 疑问与待验证项

- - 31 天和 10 分钟是文档当时的产品设定，需允许部署环境配置变化并标示实验 Beta 状态。
- - 场景合并受 Action 限制，且不代表创建了可追溯历史快照；需单独提供审计和过期策略。

## 复刻启示

- - 将“推理预览”与“可写 scenario”分成两级：预览只计算不写入，scenario 用于隔离地运行 Action/Function；两者都不应自动发布到生产。
- - 实现版本化基线、场景编辑日志、自动过期/冲突提示、执行上下文策略和独立合并审批；不要把 branch 与 scenario 做成同一个实体。
