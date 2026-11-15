<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/ontology-object-sets -->
<!-- 研读状态：已完成 -->

# Ontology Object Set basics • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/ontology-object-sets)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/ontologies-v2-resources/ontology-object-sets
- 相关性：direct；Ontology REST API v2 参考
- 官方更新时间：2026-11-12T17:46:46.922Z
- 目录核对时间：2026-11-14T14:54:03Z
- 产品状态：Ontology REST API v2 中的基础概念页；具体临时集合创建、加载和聚合另有独立端点

## 英文原文短摘录（每个来源不超过 25 词）

> “An object set represents a set of objects in the Ontology.”

## 摘录译文

对象集表示本体中的一组对象。

## 中文要点

- 本页用最小定义说明对象集是 Ontology 对象的集合，可对多个对象执行操作。
- “对象集”与“对象类型”不是同一个概念：类型定义对象的 schema；对象集是面向一组实例进行批量操作的 API 资源/查询结果抽象。
- 参考导航把对象集能力拆成临时对象集创建、单类型加载、多对象类型加载、对象/接口加载和聚合端点。此基础页本身不定义这些端点的请求体、持久化或一致性语义。
- 在画布上，对象集适合表示查询或操作的实例范围，不应画成新的对象类型，也不应把临时集合解释为持久化实体。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| `Object set` | 对象集 | 一组 Ontology 对象，可作为多对象操作的目标。 |
| `Object type` | 对象类型 | 定义一类对象 schema；与具体对象集区分。 |
| `Temporary object set` | 临时对象集 | API 导航列出的集合创建资源；持久化行为需另查对应端点。 |
| `Ontology interface` | 本体接口 | API 导航还提供对象或接口类型的集合加载能力。 |

## 疑问与待验证项

- 基础概念页没有说明对象集 ID 的生命周期、是否可保存、成员快照、上限或重新读取方式；需分别研读创建/加载端点。
- 文档中的“对多个对象操作”不等于所有 Action 都允许批量执行，也不代表批量写入具有原子性。

## 复刻启示

- 设计本体关系图时分层呈现：schema 图展示类型/链接，查询图展示对象集来源与过滤条件，实例图才展示实际对象成员。
- 把对象集描述为可追踪查询表达式（起始类型、筛选、链接遍历和聚合），可在画布中展开节点、检查成员并复用到 Action 或 Agent 工具输入。
- 对任何批量 Action 另设授权范围、影响对象数、预览和提交结果，不能从对象集的定义推导写操作保证。
