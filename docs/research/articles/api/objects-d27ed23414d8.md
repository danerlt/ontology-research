<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/v1/ontology-resources/objects -->
<!-- 研读状态：已完成 -->

# Ontology Object basics (v1) • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/v1/ontology-resources/objects)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/v1/ontology-resources
- 相关性：direct；Ontology API v1 端点参考；保留作兼容性对照，并优先关注 v2
- 官方更新时间：2026-11-12T17:46:46.923Z
- 目录核对时间：2026-11-14T14:55:46Z
- 产品状态：v1 对象基础概念页入口，包含对象查询过滤说明

## 英文原文短摘录（每个来源不超过 25 词）

> “An Object is a data container for a specific instance of an Object Type.”

## 摘录译文

Object 是某个 Object Type 具体实例的数据容器。

## 中文要点

对象基础页将 Object 定义为 Object Type 的单个实例数据容器。它同时记录 v1 List Objects 可用的属性过滤形式：属性路径支持 `properties.` 和简写 `p.`；运算符包括等值/不等值、数值/时间范围、数组包含与 null 检查。重复等值/contains 条件可匹配任一提供值，而多个范围约束同时生效。该 `/api/v1/.../objects` 路由在导航中是概念基础页，不是单个对象查询端点。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Object | 对象实例 | 对象类型的单个运行时数据记录 |
| `properties.{name}` | 属性路径 | v1 列表查询过滤对象属性的路径形式 |
| `contains` | 包含 | 过滤数组属性是否包含给定值 |
| `isNull` | 空值判断 | 检查某个属性是否为空 |

## 疑问与待验证项

- 过滤 DSL 的类型适用范围不同（如附件不支持 eq/isNull），具体以运算符表为准。
- 概念页没有说明对象 RIDs、主键和对象实例数据的版本一致性。

## 复刻启示

- 查询体验把语义过滤器编译为安全参数，服务端根据字段与对象权限筛除不可见值。
- 多系统图谱把 Object Type schema、对象记录与关系实例分别建模，查询路径根据对象主键和 link API 名解析。
