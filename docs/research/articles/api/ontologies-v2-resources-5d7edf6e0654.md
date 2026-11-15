<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/ontologies-v2-resources -->
<!-- 研读状态：已完成 -->

# Ontology basics (v2, latest) • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/ontologies-v2-resources)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/ontologies-v2-resources
- 相关性：direct；Ontology REST API v2 参考
- 官方更新时间：2026-11-12T17:46:46.921Z
- 目录核对时间：2026-11-14T14:53:27Z
- 产品状态：按页面现行表述整理；涉及分支/事务的能力以 Preview 或实验性限制为准。

## 英文原文短摘录（每个来源不超过 25 词）

> “Ontologies are categorizations of data into real-world concepts.”

## 摘录译文

Ontology 是把数据归类到现实世界概念中的语义结构。

## 中文要点

- 本体由对象类型、属性、链接类型和动作类型表达业务概念，并形成连接组织关键实体的描述性对象图。
- 这是 v2 API 参考中的概念定义，不等于具体的 Ontology Manager 编辑流程或数据库 schema。
- 新建 Ontology 后 API 查询可能有数分钟的最终一致性延迟，在此期间暂时返回 OntologyNotFound。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| object type | 对象类型 | 现实概念的类型定义。 |
| link type | 链接类型 | 对象类型之间的关系定义。 |
| eventual consistency | 最终一致性 | 变更传播至 API 可见状态存在短暂延迟。 |

## 疑问与待验证项

- API 可见性延迟随资源或环境而异，页面未给出上界。
- API 层对象图与本地 UI 中的画布布局是不同概念；文档没有规定自动布局。

## 复刻启示

- 画布核心实体应覆盖对象类型、属性、链接类型、动作类型，边应表达明确的语义引用。
- 新建或发布后要显示同步状态并对暂时查不到的资源做重试/提示，不能把最终一致延迟判成数据丢失。
