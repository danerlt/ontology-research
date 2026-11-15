<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources -->
<!-- 研读状态：已完成 -->

# Ontology basics (v2, latest) • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/v2/ontologies-v2-resources
- 相关性：direct；Ontology REST API v2 的本体概念页
- 官方更新时间：2026-11-12T17:46:46.922Z
- 目录核对时间：2026-11-14T14:56:08Z
- 产品状态：概念页未标注 Preview；具体端点状态以各端点页面为准

## 英文原文短摘录（每个来源不超过 25 词）

> “Ontologies are categorizations of data into real-world concepts. Those concepts are represented by object types, properties, link types, and action types.”

## 摘录译文

本体是将数据归类为现实世界概念的方式。这些概念由对象类型、属性、链接类型和动作类型表示。

## 中文要点

- 本体不是单纯的表结构目录：文档把它定义为现实概念的分类，并把对象类型、属性、链接类型、动作类型组合成描述组织关键实体的对象图。
- 该页面将 API v2 的 Ontology 资源作为一组可调用接口组织；同一文档导航还按对象类型、对象、链接对象、动作、查询类型、附件属性等资源分组。分组中的每个操作有独立契约，不能从目录标题推定全部行为。
- 本体变更通过 API 最终一致地传播；新建本体后，接口可能在几分钟内仍返回 `OntologyNotFound`。这要求调用方处理传播延迟，而不是把短暂不可见误判为永久创建失败。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Ontology | 本体 | 将业务数据组织为现实概念及关系的语义层 |
| Object type | 对象类型 | 描述一类业务实体的类型定义 |
| Link type | 链接类型 | 描述不同对象类型之间关系的 schema |
| Action type | 动作类型 | 定义对本体对象执行业务变更的操作 |
| Eventual consistency | 最终一致性 | 写入后读取可见性存在传播延迟 |

## 疑问与待验证项

- 本页没有给出多项目、多本体之间的隔离模型，也没有说明不同源系统对同一业务实体的身份合并规则；这些需要由具体部署和治理规则确定。
- 最终一致的延迟上界没有承诺。客户端只能据错误语义做有限退避和重试，不能声称几分钟后必然可见。
- “对象图”是概念表述；对象边的基数、删除策略、事务边界和权限传播需要逐项参考对象、链接与动作端点。

## 复刻启示

- 多项目系统可将项目/空间作为隔离与授权边界，在边界下容纳多个本体；每个本体有独立修订版本、类型 schema 和对象图。该结构是复刻设计建议，并非本页公开的 Palantir 内部租户实现。
- 流程图画布应呈现对象类型、属性、链接类型和动作节点；把 schema 边与运行时对象边区分，并能从节点跳转到其 API/权限/数据来源。
- 发布状态应分开记录“定义已提交”和“读取端已观察到”；新建或更新后允许传播中状态，并对暂时 `OntologyNotFound` 做有上限的重试。
