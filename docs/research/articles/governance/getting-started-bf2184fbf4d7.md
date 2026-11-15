<!-- 页面 URL：https://www.palantir.com/docs/foundry/action-types/getting-started -->
<!-- 研读状态：已完成 -->

# 动作类型 • 入门 • Getting started • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/action-types/getting-started)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/action-types/getting-started)（配对状态：matched）
- 页面语言：英文
- 主题栏目：action-types
- 相关性：direct；本体动作文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:01:49Z
- 产品状态：教程以工单优先级修改为例，展示 Action Type、参数、映射和提交条件的基本配置。

## 英文原文短摘录（每个来源不超过 25 词）

> “In this guide, we will create a simple action type for changing the priority on a ticket.”

## 摘录译文

本指南将创建一个用于修改工单优先级的简单 Action 类型。

## 中文要点

- 示例对象 Demo Ticket 有 Ticket ID、Title、Priority、Status 四个属性；教程选择修改对象动作并把 Priority 加入映射。
- 优先级参数被设为 P0/P1/P2 多选项；提交条件再检查目标工单 Status 是否为 Open，并可配置失败提示。
- 执行前仍需配置对象写入：Object Storage v2 要启用 edits；v1 需要 writeback dataset，文档将 v1 标作计划弃用。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Action type | 动作类型 | 封装对象编辑规则与用户提交流程 |
| Mapping | 属性映射 | 将动作参数写入目标对象属性 |
| Submission criteria | 提交条件 | 控制动作能否在当前对象/参数状态下执行 |

## 疑问与待验证项

- Object Storage v1 的计划弃用时间与租户迁移状态需根据更新文档复核。
- 教程样例只展示单对象的属性修改；多对象变更、链接及冲突需看各自专题。

## 复刻启示

- 把创建向导分成目标对象/动作、属性映射、输入参数、提交条件、权限和确认预览，并允许后续在规则页继续编辑。
- 提交前按实际对象状态重新检查条件，并把写入存储配置作为 Action 可用性的显式前置检查。
