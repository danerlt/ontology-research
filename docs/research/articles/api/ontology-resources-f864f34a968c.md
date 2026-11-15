<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/v1/ontology-resources -->
<!-- 研读状态：已完成 -->

# Ontology basics (v1) • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/v1/ontology-resources)
- 官方中文来源：尚未确认（配对状态：needs_review）
- 页面语言：英文
- 主题栏目：api/v1/ontology-resources
- 相关性：direct；Ontology API v1 基础页，保留兼容性对照并优先关注 v2
- 官方更新时间：2026-11-12T17:46:46.923Z
- 目录核对时间：2026-11-14T14:55:28Z
- 产品状态：概念页；未发现可确认的 Preview 标记

## 英文原文短摘录（每个来源不超过 25 词）

> “Ontologies are categorizations of data into real-world concepts.”

## 摘录译文

本体是对数据进行分类、以表达现实世界概念的方式。

## 中文要点

- 本体通过对象类型、属性、链接类型和动作类型表示现实概念，合成连接组织关键实体的描述性对象图。
- 本体变更对 API 是最终一致的；新建后可能需要几分钟才能反映，短时 `OntologyNotFound` 不一定表示创建失败。
- 该 `/api/v1/ontology-resources` 路径与 `/api/ontology-resources` 重复呈现同一 v1 基础说明；卡片保留不同官方目录 URL，但内容按一个概念理解。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Ontology | 本体 | 现实概念的语义数据分类 |
| object type | 对象类型 | 实体类别与属性定义 |
| link type | 链接类型 | 对象类别之间的关系定义 |
| Action Type | 动作类型 | 操作本体对象的业务行为定义 |
| eventual consistency | 最终一致性 | 本体变更对 API 的短暂传播延迟 |

## 疑问与待验证项

- “几分钟”不是 SLA；应验证具体部署的传播延迟并设计可观测的有限重试。
- 概念页没有描述 Ontology 与 Project/Space/组织的授权层级，需结合权限文档。

## 复刻启示

- 本体管理界面应以类型、属性、关系、动作组成可探索的真实语义图，并支持将这些节点关联到各项目/系统。
- 建模变更需要经过发布/传播状态机；读 API 返回暂态未找到时展示原因并提供有上限的重试。
- REST 版本路由与统一领域对象解耦，记录 schema 版本和运行时可见状态。
