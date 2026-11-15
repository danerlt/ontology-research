<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/ontologies -->
<!-- 研读状态：已完成 -->

# Ontology basics (v2, latest) • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/ontologies)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/v2/ontologies-v2-resources
- 相关性：direct；Ontology REST API v2 本体基础概念页，存在同文的根路径版本
- 官方更新时间：2026-11-12T17:46:46.921Z
- 目录核对时间：2026-11-14T14:57:04Z
- 产品状态：概念页未标注 Preview；具体端点状态以各端点页为准

## 英文原文短摘录（每个来源不超过 25 词）

> “Together, these concepts form a descriptive object graph that links together all the key entities in an organization.”

## 摘录译文

这些概念共同组成描述性对象图，把组织中的关键实体连接起来。

## 中文要点

- 页面将本体描述为现实概念的分类；对象类型、属性、链接类型和动作类型共同构成组织关键实体的对象图。
- 该路径与 API v2 资源根路径的 Ontology basics 页面重复表达同一基础定义；这是另一条 canonical 路由卡，保留链接以便目录逐项核对，不将重复内容计作额外产品能力。
- 页面同时提醒本体变更最终一致：新建本体后 API 可能有几分钟返回 `OntologyNotFound`。具体查询和编辑能力仍由对象/链接/动作等独立端点定义。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Descriptive object graph | 描述性对象图 | 语义对象及其关系组成的图 |
| Real-world concepts | 现实世界概念 | 业务数据所代表的实体/概念 |
| Ontology API | 本体 API | 访问本体 schema 和对象数据的接口集合 |
| Eventual consistency | 最终一致性 | 新变更传播至读取 API 有延迟 |

## 疑问与待验证项

- 本页没有定义对象图模式的持久化实现、关系基数或多项目隔离方式；不能把概念图直接当作内部存储结构。
- 最终一致延迟无上限承诺；重试需有界并区分暂时传播失败与真实无权限/不存在。
- 路径 `.../ontologies` 与 `.../ontologies-v2-resources` 的内容重复；目录维护应以后续官方 canonical 路由调整为准。

## 复刻启示

- 用明确 schema 表示对象类型、属性、链接类型和动作类型，再由它们构建可浏览的图；画布边应保留关系语义、方向和端点类型。
- 项目/系统边界需由复刻系统自己的授权模型定义；为每个项目保留多个本体和来源系统，图谱查询必须带项目上下文。
- 新建或更新后显示传播中状态，允许受控重试，并在发布审计中区分“定义提交”和“读取端可见”。
