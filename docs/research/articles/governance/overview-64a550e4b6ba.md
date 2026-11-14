<!-- 页面 URL：https://www.palantir.com/docs/foundry/object-permissioning/overview -->
<!-- 研读状态：已完成 -->

# Object permissioning • Overview • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/object-permissioning/overview)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/object-permissioning/overview)（配对状态：matched）
- 页面语言：英文
- 主题栏目：object-permissioning
- 相关性：direct；本体对象权限文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T14:53:18Z
- 产品状态：本页未标记 Beta 或弃用状态；核对日期 2026-11-14

## 英文原文短摘录（每个来源不超过 25 词）

> “The Foundry Ontology allows for granular, robust, and flexible security controls for all ontology entities.”

## 摘录译文

Foundry Ontology 为所有本体实体提供细粒度、稳健且灵活的安全控制。

## 中文要点

文档将授权对象分为两个层次：Ontology resource（对象类型、链接类型、动作类型等 schema 资源）以及 Objects and links（带主键和实际属性值的数据）。因此“能查看类型定义”与“能读取某对象实例”是不同授权问题，权限模型需要分别覆盖定义和数据。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Ontology resource | 本体资源 | 定义对象、链接、动作等 schema 的元数据 |
| Object security | 对象安全 | 对具体对象实例及属性值实施访问控制 |
| Project permissions | 项目权限 | 管理本体资源修改和审批的权限体系之一 |
| Mandatory controls | 强制控制 | 由组织、标记等条件限制访问的控制 |

## 疑问与待验证项

- 这篇概览不列出完整权限矩阵；不同授权迁移方式以及强制控制和资源角色的组合需要在后续权限卡片核对。
- 动作读取权限、写入权限和对象字段过滤的精确执行顺序需再查专项文档。

## 复刻启示

- 区分 schema 管理权限与实例数据权限；不因用户可浏览对象类型就推断其可读取该类型的所有对象。
- 查询、对象链接展开、动作读取和动作执行分别做授权检查，并把拒绝决定写入审计日志。
- Agent 的工具清单与应用级 scope 需显式列出资源类型、可读查询和可执行动作；默认拒绝未配置能力。
