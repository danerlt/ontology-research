<!-- 页面 URL：https://www.palantir.com/docs/foundry/dynamic-scheduling/scheduling-ontology-primitives -->
<!-- 研读状态：已完成 -->

# Dynamic Scheduling • Ontology primitives • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/dynamic-scheduling/scheduling-ontology-primitives)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/dynamic-scheduling/scheduling-ontology-primitives)（目录配对状态：matched）
- 页面语言：英文
- 主题栏目：dynamic-scheduling
- 相关性：direct；本体对象/链接建模及图形排程界面
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:04:21Z
- 产品状态：Workshop Dynamic Scheduling 小组件要求配置 Schedule 与 Resource 对象类型

## 英文原文短摘录（不超过 25 词）

> “The Ontology primitives for dynamic scheduling are comprised of one `Schedule` object and one or more `Resource` objects.”

## 摘录译文

动态排程的本体原语由一个 Schedule 对象和一个或多个 Resource 对象组成。

## 中文要点

- Dynamic Scheduling 的最小模型有 Schedule 与 Resource 两种对象类型；Schedule 表示有起止时间或预计时长的任务/活动，Resource 表示被安排或分配任务的人员、地点、项目等实体。
- Schedule 至少需要资源外键（String）、开始时间（Timestamp）和结束时间（Timestamp）属性。
- Schedule 类型要链接到每种 Resource 类型；支持多对一和多对多。Workshop 排程组件中的 Resource Link Type 决定采用哪种关系基数。
- 文档以飞机维修为例：维修任务作为 Schedule，Aircraft 作为 Resource；排程 UI 使用这些可查询、可链接的本体对象。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Schedule object | 排程对象 | 表示有时间边界的任务或活动 |
| Resource object | 资源对象 | 表示被安排任务的人、地点、项目或设备 |
| Resource Link Type | 资源链接类型 | 决定 Schedule 与 Resource 的关系基数 |
| many-to-many | 多对多 | 一个任务可关联多个资源、资源可承接多个任务 |

## 疑问与待验证项

- 页面要求资源外键和 Schedule-Resource 链接并存；二者的同步/权威来源关系应结合小组件配置确认。
- 文档未说明排程冲突检测、时间区、重复任务、取消和并发修改规则，不能从最小 schema 推断完整排程引擎能力。
- Schedule 起止与 duration 可并存，数据有效性约束和跨日时区语义需在具体组件中验证。

## 复刻启示

- 画布可以把 Schedule、Resource、时间属性及多基数关系作为真实节点和边展示，并从节点直接进入排程可视化。
- 排程对象的 schema 校验应要求起止时间、资源外键与有效链接；若使用多对多，明确显示基数及参与对象。
- 业务排程的冲突和时区策略属于上层推理规则，不应埋在图形组件内部。