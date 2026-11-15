<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/ontology-value-types/ontology-value-type-basics -->
<!-- 研读状态：已完成 -->

# Ontology Value Type basics • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/ontology-value-types/ontology-value-type-basics)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/ontologies-v2-resources/ontology-value-types
- 相关性：direct；Ontology REST API v2 参考
- 官方更新时间：2026-11-12T17:46:46.922Z
- 目录核对时间：2026-11-14T14:54:25Z
- 产品状态：v2 值类型基础页兼容路由，canonical 页面未标 Preview

## 英文原文短摘录（每个来源不超过 25 词）

> “Value types are custom types that add semantic meaning and constraints to Foundry data.”

## 摘录译文

值类型是为 Foundry 数据增加语义含义和约束的自定义类型。

## 中文要点

此兼容路由指向 Ontology API v2 值类型基础页。值类型在基础字段类型上附加领域语义、元数据和校验规则，可被多个对象类型与数据 pipeline 复用；它归属于定义所在的 Space，不能跨 Space 或用于 Default ontology。其权限和版本控制用于管理适用范围及变更。目录中的 canonical 路径为 `/api/v2/ontologies-v2-resources/ontology-value-types/ontology-value-type-basics`。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Value Type | 值类型 | 带领域语义及校验约束的可复用类型 |
| Constraint | 约束 | 值类型持有并在数据处理中执行的校验规则 |
| Space | 空间 | 值类型的定义与使用边界 |
| Version | 版本 | 管理值类型修改兼容性 |

## 疑问与待验证项

- 基础 API 页没有展开值类型的创建/更新字段、约束语言与迁移方案；具体行为需从对应管理文档确认。
- 兼容入口与 canonical 页语义一致，URL 路径不意味着另一种值类型作用域。

## 复刻启示

- 在图形编辑器中将值类型显示为属性的语义类型引用，分开展示它与对象类型/链接类型这些本体结构节点。
- 版本、权限与 Space 归属应参与草稿评审及推理试算；跨项目共享用显式复制或授权机制实现。
