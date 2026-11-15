<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/ontology-value-types -->
<!-- 研读状态：已完成 -->

# Ontology Value Type basics • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/ontology-value-types)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/v2/ontologies-v2-resources
- 相关性：direct；Ontology REST API v2 参考
- 官方更新时间：2026-11-12T17:46:46.922Z
- 目录核对时间：2026-11-14T14:57:37Z
- 产品状态：v2 值类型基础页兼容路由，canonical 页面未标 Preview

## 英文原文短摘录（每个来源不超过 25 词）

> “Value types are custom types that add semantic meaning and constraints to Foundry data.”

## 摘录译文

值类型是为 Foundry 数据增加语义含义和约束的自定义类型。

## 中文要点

本路由映射到 Ontology API v2 的值类型基础页。值类型在基础字段类型上增加领域语义、元数据和约束，以复用数据校验；它属于定义它的 Space，只能在该 Space 使用，不能用于 Default ontology。约束可在 Builder pipeline 与 Ontology 中执行；权限与版本机制用于管理复用范围及兼容性修改。canonical 地址为 `/api/v2/ontologies-v2-resources/ontology-value-types/ontology-value-type-basics`。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Value Type | 值类型 | 带领域语义、元数据和校验约束的自定义类型 |
| Base Type | 基础类型 | 值类型所包装的底层字段类型 |
| Space | 空间 | 值类型的定义和使用边界 |
| Version | 版本 | 管理类型修改的兼容性 |

## 疑问与待验证项

- 基础页没有展开约束语言、权限配置和版本迁移操作，需继续研读关联的管理文档。
- 页面路由为兼容入口，不能从该 URL 推断出不同的跨 Space 语义。

## 复刻启示

- 在画布中把值类型呈现为属性上的类型引用/徽标，而非实体节点；检查器展示底层类型、约束、版本及所属 Space。
- 多项目共享语义类型需设置显式作用域及授权；派生属性试算要执行值类型约束并显示失败原因。
