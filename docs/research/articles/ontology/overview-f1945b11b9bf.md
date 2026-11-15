<!-- 页面 URL：https://www.palantir.com/docs/zh/foundry/ontology/overview -->
<!-- 研读状态：已完成 -->

# Ontology搭建 • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/ontology/overview)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/ontology/overview)
- 页面语言：中文
- 主题栏目：ontology
- 相关性：direct；本体模型与治理文档
- 官方更新时间：2026-11-12T17:46:46.935Z
- 目录核对时间：2026-11-15
- 产品状态：官方中文页标注为未经验证的 AIP 机器翻译；本卡对照英文原文整理。

## 英文原文短摘录（每个来源不超过 25 词）

> “The Palantir Ontology is an operational layer for the organization.”

## 摘录译文

Palantir Ontology 是组织的运营层。

## 中文要点

- 本体将集成进 Foundry 的数据集、虚拟表和模型映射到现实实体或事件，形成组织的语义表示。
- 对象、属性和链接表达“是什么、彼此如何关联”；动作、函数与动态安全支持“如何计算、如何在约束下改变现实”。
- 映射数据源、定义字段元数据、授权和变更治理共同构成本体基础；动作与函数提供对现有系统的决策执行和业务逻辑。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| semantic elements | 语义元素 | 对象、属性和链接等业务表示。 |
| kinetic elements | 动态元素 | 动作、函数和动态授权等可执行能力。 |
| backing datasource | 支撑数据源 | 本体对象属性所映射的底层数据资产。 |

## 疑问与待验证项

- 此概述没有给出具体数据源同步延迟、事务边界或写回一致性承诺。
- “数字孪生”是组织语义与行动能力的整体表述，不等价于三维仿真或自动推理。

## 复刻启示

- 画布应显式区分语义结构和可执行行为；动作与函数用独立资源类型建模并关联至对象/链接。
- 来源映射、字段描述、安全策略和变更审查是一等配置，不能只实现对象/边 CRUD。
