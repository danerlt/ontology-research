<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/ontology-interfaces/ontology-interface-basics -->
<!-- 研读状态：已完成 -->

# Ontology Interface basics • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/ontology-interfaces/ontology-interface-basics)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/v2/ontologies-v2-resources
- 相关性：direct；Ontology REST API v2 参考
- 官方更新时间：2026-11-12T17:46:46.921Z
- 目录核对时间：2026-11-14T14:57:16Z
- 产品状态：接口类型相关 REST API 当前处于 Preview；本页为概念说明

## 英文原文短摘录（每个来源不超过 25 词）

> “An Interface describes the contract that a set of Object Types will implement.”

## 摘录译文

接口（Interface）描述一组对象类型将要实现的契约。

## 中文要点

本页用一句话界定接口类型：它表达对象类型需要共同遵守的契约。结合同组读取 API，接口可承载共享属性与链接，并可由一个或多个对象类型实现；接口还可以扩展其他接口。接口适合表达跨对象类型的稳定语义，例如把不同系统里的员工、承包商统一归入“可联系人员”契约。注意，这张基础页本身只给出契约定义，属性、继承和实现者字段来自配套读取 API。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Interface | 接口类型 | 对象类型共同实现的语义契约；可扩展其他接口 |
| Object Type | 对象类型 | 具体实体的结构类型，可实现接口 |
| Contract | 契约 | 对象类型承诺提供的共同属性/链接语义 |

## 疑问与待验证项

- 本页没有说明如何创建、编辑、验证接口，也没有给出属性类型兼容、冲突消解或实现约束规则；需结合 Ontology Manager 页面与实际 API 行为核实。
- 当前接口类型 API 页面均标注 Preview；不能据此假定所有租户已开放或行为稳定。

## 复刻启示

- 画布要把“接口继承”与“对象类型实现接口”分别建模成有方向的语义边，并可从接口节点展开继承属性、链接和实现对象；不能把契约边画成对象实例关系。
- 多项目模型可以在项目内定义共享契约，再让多个系统映射到各自对象类型；发布校验应检查实现者是否满足必需属性与链接，具体规则需在本地明确并标成自有实现。
