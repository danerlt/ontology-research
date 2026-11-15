<!-- 页面 URL：https://www.palantir.com/docs/zh/foundry/object-link-types/object-types-overview -->
<!-- 研读状态：已完成 -->

# 对象链接类型 • Object types • 概览 • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/object-link-types/object-types-overview)
- 官方中文来源：[https://www.palantir.com/docs/zh/foundry/object-link-types/object-types-overview](https://www.palantir.com/docs/zh/foundry/object-link-types/object-types-overview)
- 页面语言：中文
- 主题栏目：object-link-types
- 相关性：direct；本体对象链接类型文档
- 官方更新时间：2026-11-12T17:46:46.935Z
- 目录核对时间：2026-11-15
- 产品状态：官方中文页提示其为未经验证的 AIP 机器翻译；已对照英文原文。

## 英文原文短摘录（每个来源不超过 25 词）

> “An object type is the schema definition of a real-world entity or event.”

## 摘录译文

对象类型是对现实世界实体或事件的模式定义。

## 中文要点

- 对象类型定义实体/事件的结构，对象是类型的单个实例，对象集是满足条件的多实例集合。
- 对象类型与数据集 schema 类似，对象与数据行类似；本体概念映射实际数据后才能为用户应用提供具体对象。
- 对象可由支撑数据源索引产生；也可通过动作创建，因此不要求每种对象都必须绑定外部数据源。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| object instance | 对象实例 | 某一对象类型下代表具体实体/事件的单条对象。 |
| object set | 对象集 | 按筛选条件组织的一组对象。 |
| backing datasource | 支撑数据源 | 为对象属性值提供来源的连接数据。 |

## 疑问与待验证项

- 中文翻译中的“对象组”在该处实际指 object set，应与对象类型分组（type group）区分。
- 对象类型与对象集数量可能相差多个数量级；两类信息需要独立呈现。

## 复刻启示

- 画布节点以对象类型 schema 为主；通过实例关系模式或选中节点后的预览抽屉查看对象样例。
- 在类型检查器显示唯一键、来源系统、字段映射和数据更新时间，并允许无来源数据的 Action-created 类型。
