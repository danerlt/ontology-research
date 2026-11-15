<!-- 页面 URL：https://www.palantir.com/docs/zh/foundry/action-types/side-effects-overview -->
<!-- 研读状态：已完成 -->

# 动作类型 • Side effects • 概述 • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/action-types/side-effects-overview)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/action-types/side-effects-overview)
- 页面语言：中文
- 主题栏目：action-types
- 相关性：direct；本体动作文档
- 官方更新时间：2026-11-12T17:46:46.935Z
- 目录核对时间：2026-11-14T14:58:28Z
- 产品状态：官方中文页标注为未经验证的 AIP 机器翻译；英文原文为核对依据。

## 英文原文短摘录（每个来源不超过 25 词）

> “Action types are designed to support the full range of decision-making processes within an organization.”

## 摘录译文

Action 类型旨在支持组织内各种决策流程。

## 中文要点

- 当本体承载决策流程记录时，规则负责修改本体；通知让用户对实时变化采取行动，webhook 则连接已有外部系统并将数据/决策写回。
- 页面把通知和 Webhook 作为两类主要副作用：通知面向平台用户；Webhook 可调用 REST API、ERP 或消息系统。
- 副作用解决本体内决策与组织既有系统协同问题，意味着动作不只改变图内对象，也可能触发外部影响。
- 官方中文页为未经验证的 AIP 机器翻译。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Side effect | 副作用 | 动作本体写入以外的通知或外部系统调用。 |
| Decision orchestration | 决策编排 | 本体决策与组织内外部系统之间的流程集成。 |
| Source system | 来源系统 | 组织中原本掌握某类数据或流程的系统。 |

## 疑问与待验证项

- 副作用是否重试、幂等、可撤销，以及与对象写入的提交次序应分别查 Webhook/Notification 专页。
- 不能假设所有副作用失败都能回滚已经完成的对象编辑，需为跨系统补偿建立业务约束。

## 复刻启示

- 将本体事务和外部副作用分成独立可观察阶段，并支持 outbox、幂等键、重试队列与人工补偿。
- 多系统本体工作流应能建模哪些系统为记录源、哪些系统接收决策写回，并可追踪跨系统变更。
