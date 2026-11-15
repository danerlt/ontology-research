<!-- 页面 URL：https://www.palantir.com/docs/foundry/ontology/temporary-scenario -->
<!-- 研读状态：已完成 -->

# Temporary scenarios • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/ontology/temporary-scenario)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：ontology
- 相关性：direct；本体模型与治理文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:04:03Z
- 产品状态：当前页面介绍 Workshop 中仅在会话内存在的临时 Scenario，以及用 Scenario Manager、对象表、摘要组件和 Action 做交互式 what-if 试算。

## 英文原文短摘录（每个来源不超过 25 词）

> “Temporary scenarios are created and used only within the current session.”

## 摘录译文

临时 Scenario 仅在当前会话中创建和使用。

## 中文要点

- 临时 Scenario 的元数据不写入平台持久存储；用户结束当前 session 后会删除，适合无需协作/分享的临时分析。
- Workshop 可通过 Scenario Manager 创建动态场景，将 Object Table 配成读取场景数据、Scenario Summary 预览变更，再把 Action 配置成应用到活动场景而不是本体主数据。
- 场景变量也可接入聚合和对象属性变量，让图表/指标反映场景修改；需要持久元数据时应改用 persisted scenario。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| temporary scenario | 临时场景 | 仅对当前会话可见、不持久保存元数据的 what-if 沙箱。 |
| Scenario Manager | 场景管理器 | 在 Workshop 中创建和切换临时场景的组件。 |
| Scenario Summary | 场景摘要 | 展示当前场景编辑结果的组件。 |

## 疑问与待验证项

- - 用户结束 session 后场景元数据被删除；页面未展开异常断开、浏览器刷新和多标签会话下的具体生命周期。
- - 临时场景不适用于多人协作和长期审计；业务批准结果应转成可审阅的持久化变更。

## 复刻启示

- - 画布中的“试算”可提供临时上下文，不持久化定义或数据修改，并清楚展示当前基线和差异。
- - 如需团队评审/恢复，应另建持久场景或分支提案，并增加到期提醒、所有者、分享权限和合并审批。
