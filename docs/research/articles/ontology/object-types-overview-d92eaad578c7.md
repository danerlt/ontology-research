<!-- 页面 URL：https://www.palantir.com/docs/foundry/object-link-types/object-types-overview -->
<!-- 研读状态：已完成 -->

# Object and link types • Object types • Overview • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/object-link-types/object-types-overview)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/object-link-types/object-types-overview)（配对状态：matched）
- 页面语言：英文
- 主题栏目：object-link-types
- 相关性：direct；本体对象链接类型文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:01:47Z
- 产品状态：本页未标记 Beta 或弃用状态；核对日期 2026-11-14

## 英文原文短摘录（每个来源不超过 25 词）

> “An object type is the schema definition of a real-world entity or event.”

## 摘录译文

对象类型是对现实世界实体或事件的模式定义。

## 中文要点

页面区分三个层次：对象类型定义一类实体/事件的结构，对象是该类型的单个实例，对象集是一组实例。对象类型可连接一个或多个支撑数据源；若对象都由动作创建，也可不配置支撑数据源。类型/对象/对象集与表模式、行、过滤结果相似，但 Ontology 对象仍与组织中的真实数据绑定。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Object type | 对象类型 | 定义实体或事件的 schema、属性和数据关联 |
| Object instance | 对象实例 | 某对象类型下的一个具体实体或事件 |
| Object set | 对象集 | 按条件组织的多个对象实例 |
| Backing datasource | 支撑数据源 | 为对象类型提供实例数据的来源 |
| Primary key | 主键 | 标识一个对象实例的键值 |

## 疑问与待验证项

- 多个支撑数据源如何合并为唯一实例、主键冲突如何处理，需要查看对象类型创建和多数据源配置文档。
- 对象集是查询结果的稳定快照还是动态条件，需要由 Object Set API 和查询文档核实。

## 复刻启示

- 数据库模型分开保存 `ObjectType`、`PropertyDefinition`、`ObjectInstance` 与 `ObjectSet` 查询定义，避免把 schema 和行数据混为一张表。
- 支持对象类型关联多个数据源，也支持由动作创建的新对象；保存主键映射与来源映射。
- 在管理 UI 中并列呈现类型元数据、属性、关系图、依赖、数据样例和用量。
