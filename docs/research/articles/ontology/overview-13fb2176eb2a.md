<!-- 页面 URL：https://www.palantir.com/docs/foundry/ontology/overview -->
<!-- 研读状态：已完成 -->

# Overview • Ontology • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/ontology/overview)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/ontology/overview)（配对状态：matched）
- 页面语言：英文
- 主题栏目：ontology
- 相关性：direct；本体模型与治理文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T14:53:09Z
- 产品状态：本页未标记 Beta 或弃用状态；核对日期 2026-11-14

## 英文原文短摘录（每个来源不超过 25 词）

> “The Palantir Ontology is an operational layer for the organization.”

## 摘录译文

Palantir Ontology 是组织的运营层。

## 中文要点

Ontology 把平台中的数据资产连接到组织里的真实对象与事件。它包含描述组织语义的对象、属性、链接，也包含推动业务变化的动作、函数和动态安全规则。它不是单纯的数据目录：页面强调这些模型要服务于操作工作流，并被面向用户的应用共同使用。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Ontology | 本体 | 连接底层数据与组织中的真实概念、业务操作 |
| Object type | 对象类型 | 对一类实体或事件定义结构 |
| Link type | 链接类型 | 描述本体对象之间的关系 |
| Action type | 动作类型 | 定义用户可执行的一组数据变更 |
| Kinetic elements | 运营要素 | 文档对动作和函数等可驱动变化能力的概括 |

## 疑问与待验证项

- 本页把动作、函数和动态安全列为运营要素；它们在对象类型、授权、版本治理中的边界需要结合各专题文档确认。
- 文档将 Ontology 形容为数字孪生，但没有在此页规定关系图、对象存储和底层数据的具体实现。

## 复刻启示

- 将定义层与实例数据层分开：类型、属性、链接、接口和动作属于可治理资源；对象实例由数据源映射或动作创建。
- 将动作和函数视为模型的运营能力，而不是普通对象字段；面向应用公开统一读写接口。
- 产品界面要帮助用户从业务对象导航到关系、动作、依赖与用量，并能被应用和 Agent 复用。
