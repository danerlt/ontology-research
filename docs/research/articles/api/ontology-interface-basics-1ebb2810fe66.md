<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/ontology-interfaces/ontology-interface-basics -->
<!-- 研读状态：已完成 -->

# Ontology Interface basics • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/ontology-interfaces/ontology-interface-basics)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/ontologies-v2-resources/ontology-interfaces
- 相关性：direct；Ontology REST API v2 参考
- 官方更新时间：2026-11-12T17:46:46.921Z
- 目录核对时间：2026-11-14T14:54:03Z
- 产品状态：规范路由的兼容入口；接口类型相关 REST API 当前处于 Preview

## 英文原文短摘录（每个来源不超过 25 词）

> “An Interface describes the contract that a set of Object Types will implement.”

## 摘录译文

接口（Interface）描述一组对象类型将要实现的契约。

## 中文要点

本页用一句话界定接口类型：它表达对象类型需要共同遵守的契约。结合同组读取 API，接口可承载共享属性与链接，可由多个对象类型实现，也可扩展其他接口。接口适合表达跨对象类型的稳定语义，例如统一不同来源系统的人员对象。此 URL 的 canonical 页面位于 `/api/v2/.../ontology-interface-basics`；本卡保留目录中的原始路由，页面内容与 v2 canonical 页面相同。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Interface | 接口类型 | 对象类型共同实现的语义契约 |
| Object Type | 对象类型 | 具体实体的结构类型，可实现接口 |
| Contract | 契约 | 对象类型承诺提供的共同语义 |

## 疑问与待验证项

- 本页未说明接口创建、兼容性校验、属性冲突和生命周期管理规则；需要以 Ontology Manager 实际编辑能力验证。
- 接口相关 API 为 Preview，需确认租户开放状态及后续稳定性。

## 复刻启示

- 画布分别展示接口扩展边和对象类型实现边；接口节点的检查器展示声明属性、继承属性、链接与实现者。
- 跨项目或多系统映射可以复用统一契约，但发布前的实现一致性校验属于本地要明确实现的治理规则。
