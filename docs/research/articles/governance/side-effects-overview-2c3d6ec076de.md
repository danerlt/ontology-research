<!-- 页面 URL：https://www.palantir.com/docs/foundry/action-types/side-effects-overview -->
<!-- 研读状态：已完成 -->

# 动作类型 • 副作用概述 • Side effects • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/action-types/side-effects-overview)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/action-types/side-effects-overview)（配对状态：matched）
- 页面语言：英文
- 主题栏目：action-types
- 相关性：direct；本体动作文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:02:05Z
- 产品状态：副作用将本体决策连到通知和外部业务系统，适用于 Foundry 与其他系统共同参与的工作流。

## 英文原文短摘录（每个来源不超过 25 词）

> “Side effects in action types enable you to send data out of Foundry to integrate with existing organizational processes.”

## 摘录译文

Action 类型的副作用可以把数据从 Foundry 发出，以接入现有组织流程。

## 中文要点

- Ontology 可作为组织决策流程的记录系统；Action 规则表达对象变化，副作用则补齐通知与外部系统协同。
- 通知用于提醒平台用户，包括站内消息和邮件。
- Webhook 可连接 REST API、ERP 或其他已配置系统，向源系统写回数据/决策，也可接入消息系统。
- 副作用让本体动作可编排外部工作流，但不能把外部系统操作与本体事务视为同一个原子提交。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Side effect | 副作用 | Action 本体编辑之外的附加效果 |
| Decision orchestration | 决策编排 | 将本体决策与外部记录系统/业务流程连接 |
| Source system | 源系统 | 组织业务数据的外部权威系统 |

## 疑问与待验证项

- 每种副作用的执行时点、失败是否影响 Action、重试和幂等要求不同，必须查看通知/Webhook 各自语义。
- 并存的 Foundry 本体和源系统如何解决部分成功与数据对账，本概览未提供通用协议。

## 复刻启示

- 把本体编辑与外部副作用拆成有序的执行阶段，分别记录开始、成功、失败、重试和外部关联 ID。
- 对会修改源系统的 Webhook 提供幂等键、补偿/对账入口，且在提交预览标注外部影响。
