<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/v1/ontology-resources/ontologies/ontology-basics -->
<!-- 研读状态：已完成 -->

# Ontology basics (v1) • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/v1/ontology-resources/ontologies/ontology-basics)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/v1/ontology-resources
- 相关性：direct；Ontology API v1 端点参考；保留作兼容性对照，并优先关注 v2
- 官方更新时间：2026-11-12T17:46:46.922Z
- 目录核对时间：2026-11-14T14:55:54Z
- 产品状态：基础概念页（v1/v2 均未标注 Preview）

## 英文原文短摘录（每个来源不超过 25 词）

> “Ontologies are categorizations of data into real-world concepts.”

## 摘录译文

本体是对现实世界概念进行组织分类的数据结构。

## 中文要点

- 页面把 Foundry Ontology 描述为将现实概念映射为对象类型、属性、链接类型和动作类型；这些元素共同组成连接组织关键实体的描述性对象图。
- API 参考明确提示本体变更采用最终一致性：新建本体后，API 可能在几分钟内仍返回 `OntologyNotFound`。
- v1 与 v2 的基础概念说明相同；本页只解释概念与读取延迟，不定义推理规则、版本冲突或发布流程。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Ontology | 本体 | 用业务概念及关系组织数据的语义模型 |
| Object type | 对象类型 | 描述一类现实实体 |
| Link type | 链接类型 | 表达对象类型之间的关系 |
| Eventual consistency | 最终一致性 | 变更传播至 API 存在短暂延迟 |

## 疑问与待验证项

- “几分钟”不是严格 SLA，客户端应如何区分暂时传播延迟与本体 RID/API 名配置错误？
- 基础页没有展开“描述性对象图”是否包含派生属性、规则引擎或运行时推理；需分别阅读专门功能文档。

## 复刻启示

- 本体浏览器的新建/导入完成后应设计可重试的状态，而不是把短暂 `OntologyNotFound` 直接标记为失败。
- 领域图的节点、边和动作应是有类型的元模型资源；需要把读模型的对象图与推理/派生定义独立研究、独立建模。
