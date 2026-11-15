<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/ontology-interfaces -->
<!-- 研读状态：已完成 -->

# Ontology Interface basics • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/ontology-interfaces)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/v2/ontologies-v2-resources
- 相关性：direct；Ontology REST API v2 参考
- 官方更新时间：2026-11-12T17:46:46.921Z
- 目录核对时间：2026-11-14T14:57:13Z
- 产品状态：此导航路由 canonical 到接口基础页；接口类型读取 API 当前处于 Preview

## 英文原文短摘录（每个来源不超过 25 词）

> “An Interface describes the contract that a set of Object Types will implement.”

## 摘录译文

接口描述一组对象类型将要实现的契约。

## 中文要点

目录把 `/ontology-interfaces` 路由指向 Ontology Interface 基础页，其 canonical 页面补充 `/ontology-interface-basics` 路径。本页核心定义是：接口描述一组对象类型实现的共同契约。配套接口 API 提供列出/获取接口定义的入口；列表页可分页，获取页返回属性、继承关系、实现者和链接等信息。该组 API 当前标注 Preview。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Ontology Interface | 本体接口 | 一组对象类型共享的契约 |
| Interface Type | 接口类型 | 可被扩展、实现并通过 API 查询的接口定义 |
| Implement | 实现 | 对象类型满足并采用接口契约 |

## 疑问与待验证项

- 导航路由没有独立的第二套概念内容；与 canonical 基础页内容重复，保留该卡用于目录精确覆盖。
- 基础概念页未陈述创建/变更/验证流程；单靠只读 API 无法推断管理器的编辑和发布机制。

## 复刻启示

- 将接口概念引入多项目画布时，要显示跨对象类型契约结构，同时保持项目边界：契约的复用范围要由本地授权模型控制。
- 为 Agent 工具目录暴露接口读取能力时，采用稳定的 API 名和 RID，并在 API 适配层处理 Preview 能力标记；不要把 Preview 当成稳定生产依赖。
