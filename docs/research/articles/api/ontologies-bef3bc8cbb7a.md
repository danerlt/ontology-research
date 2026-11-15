<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/ontologies -->
<!-- 研读状态：已完成 -->

# Ontology basics (v2, latest) • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/ontologies)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/ontologies-v2-resources/ontologies
- 相关性：direct；本体管理与治理文档
- 官方更新时间：2026-11-12T17:46:46.921Z
- 目录核对时间：2026-11-14T14:53:57Z
- 产品状态：本卡对应 Ontology REST API v2；API 文档另列 v3 Beta 导航。Ontology 元数据变更对 API 最终一致，可能延迟数分钟可见

## 英文原文短摘录（每个来源不超过 25 词）

> “Ontologies are categorizations of data into real-world concepts.”

## 摘录译文

Ontology 将数据归类为现实世界概念。

## 中文要点

- 本页给出 Ontology 在 REST API 参考中的领域定义：现实概念由对象类型、属性、链接类型和操作类型表示，这些元素合成描述组织关键实体的对象图。
- 这是概念页而非完整 schema 端点说明；实际读取 Ontology 元数据需继续使用列表/获取 Ontology、对象类型、链接类型和 Action Type 等 API。
- Ontology 元数据变更采用最终一致语义。新建 Ontology 后，API 可能在几分钟内仍返回 `OntologyNotFound`，这是可见性延迟而非必然代表写入失败。
- 页面路由属于 Ontology REST API v2；API 参考导航另列 v3 Beta。本卡不把 v3 预览语义并入 v2 契约。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| `Ontology` | 本体 | 组织现实世界概念及其对象、属性、关系和操作定义的模型。 |
| `Object type` | 对象类型 | 本体中某类现实实体的类型定义。 |
| `Link type` | 链接类型 | 对象类型之间的关系定义。 |
| `Action type` | 操作类型 | 可对本体对象执行的业务操作定义。 |
| `Eventually consistent` | 最终一致 | 元数据变更经过传播后才保证 API 可见。 |

## 疑问与待验证项

- 该页没有说明最终一致延迟的上界或读取重试建议；客户端需区分创建请求成功与查询端可见。
- “本体对象图”是领域模型表达，并不说明 API 查询必须采用图数据库或图查询语言。
- 不同 API 版本的可用字段、Beta 标记和语义应以各自版本文档为准。

## 复刻启示

- 把对象类型、属性、链接和操作作为本体画布的一级节点/边，并保持与 API schema 的 API 名称、类型和版本关联。
- 多项目/多系统设计中，应将项目归属和外部来源映射作为本体的治理元数据；图形关系不能仅是手工绘制的装饰。
- 新建/发布本体后提供“处理中/已可查询”状态或有退避的重试提示，防止最终一致造成误判、重复创建或用户困惑。
