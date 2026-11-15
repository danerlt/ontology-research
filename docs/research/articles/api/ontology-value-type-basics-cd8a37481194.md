<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/ontology-value-types/ontology-value-type-basics -->
<!-- 研读状态：已完成 -->

# Ontology Value Type basics • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/ontology-value-types/ontology-value-type-basics)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/v2/ontologies-v2-resources
- 相关性：direct；Ontology REST API v2 参考
- 官方更新时间：2026-11-12T17:46:46.922Z
- 目录核对时间：2026-11-14T14:57:39Z
- 产品状态：v2 基础概念页；本页未标 Preview

## 英文原文短摘录（每个来源不超过 25 词）

> “Value types are custom types that add semantic meaning and constraints to Foundry data.”

## 摘录译文

值类型是为 Foundry 数据增加语义含义和约束的自定义类型。

## 中文要点

本页是 Ontology API v2 的值类型概念页。关联用户文档进一步说明：值类型是基础字段类型之上的语义包装层，可带元数据与约束，增强类型安全并复用领域校验。它属于某个 Space，只能在定义它的 Space 内使用，不能用于 Default ontology；约束可在 Builder pipeline 与 Ontology 中执行。值类型支持权限和版本，以便控制复用范围并处理破坏性/非破坏性修改。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Value Type | 值类型 | 在字段类型上增加领域语义、元数据和约束的自定义类型 |
| Field Type / Base Type | 字段类型 / 基础类型 | 值类型底层包装的原始类型 |
| Space | 空间 | 值类型定义与使用范围；不能跨 Space 使用 |
| Constraint | 约束 | 可复用的数据校验条件，可在数据流与 Ontology 中执行 |

## 疑问与待验证项

- API 基础页自身只定义概念；约束表达式、权限设置和版本迁移细节需要查关联用户文档与 Get/List API。
- “跨平台复用”不能解释为跨 Space 可用；用户文档明确规定值类型只能在定义它的 Space 中使用。

## 复刻启示

- 画布将值类型呈现在属性类型徽标或检查器中，而非实体节点；详情要显示底层类型、约束、版本、权限与 Space 归属。
- 多项目环境若要共享语义类型，应有明确的项目/Space 作用域和复用授权；本地跨项目复制策略需标记为自有设计。
- 派生属性试算执行时应校验输入/输出的值类型约束，并将失败项作为可解释的验证结果展示。
