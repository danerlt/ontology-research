<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/ontology-value-types -->
<!-- 研读状态：已完成 -->

# Ontology Value Type basics • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/ontology-value-types)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/ontologies-v2-resources/ontology-value-types
- 相关性：direct；Ontology REST API v2 参考
- 官方更新时间：2026-11-12T17:46:46.922Z
- 目录核对时间：2026-11-14T14:54:19Z
- 产品状态：v2 值类型基础页兼容路由，canonical 页面未标 Preview

## 英文原文短摘录（每个来源不超过 25 词）

> “Value types are custom types that add semantic meaning and constraints to Foundry data.”

## 摘录译文

值类型是为 Foundry 数据增加语义含义和约束的自定义类型。

## 中文要点

此别名 URL 是 v2 值类型基础页入口。值类型为基础字段类型提供领域语义、元数据和可复用校验约束；其定义和使用受 Space 范围限制。权限和版本功能用于控制使用者和兼容性更新。页面 canonical 到 `/api/v2/ontologies-v2-resources/ontology-value-types/ontology-value-type-basics`，本卡保留目录源 URL。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Value Type | 值类型 | 在字段类型上附加语义和约束的自定义类型 |
| Constraint | 约束 | 在数据 pipeline 和本体中执行的校验规则 |
| Space | 空间 | 值类型的归属/使用范围 |
| Canonical URL | 规范地址 | 对应官方主要路由，供页面去重和版本识别 |

## 疑问与待验证项

- 本页只给概念定义；具体约束结构、版本策略和权限配置需要查对应使用文档。
- URL 是规范路由别名，不对应另一套 API 版本或独立作用域。

## 复刻启示

- 画布属性检查器显示语义类型与约束，并可点击进入值类型版本和权限信息。
- 项目间复用值类型应显式授权或复制审批；推理结果要通过属性定义关联的校验规则。
