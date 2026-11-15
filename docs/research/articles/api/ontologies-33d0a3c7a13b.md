<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/v1/ontology-resources/ontologies -->
<!-- 研读状态：已完成 -->

# Ontology basics (v1) • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/v1/ontology-resources/ontologies)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/v1/ontology-resources
- 相关性：direct；Ontology API v1 基础说明，保留兼容性对照并优先关注 v2
- 官方更新时间：2026-11-12T17:46:46.922Z
- 目录核对时间：2026-11-14T14:55:53Z
- 产品状态：基础页；正文与其他 v1 Ontology basics 路由重叠

## 英文原文短摘录（每个来源不超过 25 词）

> “Together, these concepts form a descriptive object graph that links together all the key entities in an organization.”

## 摘录译文

这些概念共同组成描述性对象图，将组织内的关键实体连接起来。

## 中文要点

- Ontology 将现实概念映射为对象类型、属性、链接类型与动作类型，并共同形成组织实体的描述性对象图。
- API 的 Ontology 资源可在 v1 下枚举、读取；新建本体后变化最终一致，API 可能需要几分钟才可见，期间短暂的 `OntologyNotFound` 可能是传播延迟。
- 此 `/api/v1/ontology-resources/ontologies` 概念路径与 `/api/v1/ontology-resources` 等基础入口内容存在重叠，卡片保留 URL 以对齐目录，不能据此推断不同本体模型。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Ontology | 本体 | 组织业务概念的语义结构 |
| descriptive object graph | 描述性对象图 | 实体、属性、链接和动作形成的图 |
| link type | 链接类型 | 不同对象类别之间的语义关系 |
| eventual consistency | 最终一致性 | 新建/更新资源对 API 的传播延迟 |

## 疑问与待验证项

- 延迟只有定性描述，未给出 SLA；生产端应按环境观测并使用有上限的退避重试。
- 此基础说明不描述项目/组织层级和权限；多项目隔离需另查 Ontology permissions。

## 复刻启示

- 本体核心结构作为可编辑属性图保存，类型、链接和动作都是一等资源，画布节点应映射到可持久化定义。
- 发布接口要暴露 schema 版本、索引传播状态和可查询时间，短时不可见应区分于永久未授权/不存在。
- 资源 URL/名称与内部 schema ID 分离，便于 API 版本和多项目迁移。
