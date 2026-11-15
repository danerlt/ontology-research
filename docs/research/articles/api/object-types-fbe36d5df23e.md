<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/ontology-resources/object-types -->
<!-- 研读状态：已完成 -->

# Object Type basics (v1) • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/ontology-resources/object-types)
- 官方中文来源：尚未确认（配对状态：needs_review）
- 页面语言：英文
- 主题栏目：api/ontology-resources/object-types
- 相关性：direct；Ontology API v1 端点参考；保留作兼容性对照，并优先关注 v2
- 官方更新时间：2026-11-12T17:46:46.922Z
- 目录核对时间：2026-11-14T14:55:06Z
- 产品状态：v1 规范路由的兼容入口，canonical 到对象类型基础页

## 英文原文短摘录（每个来源不超过 25 词）

> “This represents an object type within a Foundry Ontology.”

## 摘录译文

表示 Foundry 本体中的一种对象类型。

## 中文要点

该 `/api/ontology-resources/object-types` 兼容入口指向 v1 的 Object Type 基础页。对象类型是实体/事件的 schema；对象是一个实例，对象集合是实例群组。关联说明指出本体把这些结构映射到实际数据，亦可由 Action 创建对象。canonical 路由为 `/api/v1/ontology-resources/object-types/object-type-basics`。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Object Type | 对象类型 | 本体中实体/事件的 schema 定义 |
| Object Instance | 对象实例 | 某一条实体/事件数据 |
| Canonical URL | 规范地址 | 元数据记录的 v1 基础页路由 |

## 疑问与待验证项

- 本页未具体说明 v1 对象类型 API 的字段模型和兼容限制，应以相应操作端点为准。
- 兼容路由的路径不能替代 canonical 元数据作为版本判定依据。

## 复刻启示

- 收录官方 API 时记录请求 URL、canonical URL 和版本，页面别名不重复生成不同的 schema 实体。
- 本体图将类型 schema 与对象记录分层，映射到多来源系统的实体通过同一业务键/链接治理。
