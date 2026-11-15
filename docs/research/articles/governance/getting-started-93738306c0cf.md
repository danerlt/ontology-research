<!-- 页面 URL：https://www.palantir.com/docs/zh/foundry/action-types/getting-started -->
<!-- 研读状态：已完成 -->

# 动作类型 • 入门 • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/action-types/getting-started)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/action-types/getting-started)
- 页面语言：中文
- 主题栏目：action-types
- 相关性：direct；本体动作文档
- 官方更新时间：2026-11-12T17:46:46.935Z
- 目录核对时间：2026-11-14T14:58:16Z
- 产品状态：官方中文页标注为未经验证的 AIP 机器翻译；英文原文为核对依据。

## 英文原文短摘录（每个来源不超过 25 词）

> “In this guide, we will create a simple action type for changing the priority on a ticket.”

## 摘录译文

本指南将创建一个简单的操作类型，用来更改工单优先级。

## 中文要点

- 教程从 Demo Ticket 对象类型创建修改 Priority 的 Action Type，用多选参数将值限制为 P0/P1/P2，再以提交条件限制仅处理 Open 工单。
- 应用侧可将当前对象作为参数默认值并隐藏该字段，防止用户把动作目标切换为别的工单；动作可放入对象视图供用户执行。
- 执行写入之前仍需配置存储后端：OSv2 用户需启用编辑；OSv1 则依赖 writeback dataset，且原文标注 OSv1 计划弃用。
- 教程还指出用户编辑与数据源更新可能冲突，默认策略应用用户编辑，另有有限测试版策略应用最近值；中文译文未验证。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Submission criteria | 提交条件 | 决定操作是否允许提交的条件表达式。 |
| Default value | 默认值 | 预填动作参数的值，可绑定当前对象。 |
| Writeback dataset | 回写数据集 | OSv1 写入用户编辑的后端配置。 |

## 疑问与待验证项

- 冲突策略的“有限测试版”适用范围和生效顺序应查看当前 Object 编辑文档，不应直接以旧教程推断为 GA。
- 对象存储版本迁移后，写入启用开关、权限和冲突策略需要逐租户核验。

## 复刻启示

- 将动作定义拆成目标对象、规则/写集、参数、校验和 UI 消费配置；预览时显示提交条件失败原因。
- 目标对象可由当前视图上下文锁定；数据源写入与人工修改冲突策略需可审计且显式展示。
