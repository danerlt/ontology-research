<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/ontology-objects/ontology-object-basics -->
<!-- 研读状态：已完成 -->

# Ontology Object basics (v2, latest) • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/ontology-objects/ontology-object-basics)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/ontologies-v2-resources/ontology-objects
- 相关性：direct；Ontology REST API v2 参考
- 官方更新时间：2026-11-12T17:46:46.921Z
- 目录核对时间：2026-11-14T14:54:12Z
- 产品状态：v2 对象概念页兼容入口，未标 Preview

## 英文原文短摘录（每个来源不超过 25 词）

> “An Object is a data container for a specific instance of an Object Type.”

## 摘录译文

Object 是某个 Object Type 具体实例的数据容器。

## 中文要点

该兼容 URL 指向 Ontology API v2 Object 基础页，核心定义是 Object 表示某个 Object Type 的具体实例并容纳其数据。它关注运行时对象资源，不等同于 Object Type schema，也不等同于多个对象组成的 Object Set。此页与 v1 基础定义相同，但 v1 另含属性过滤说明；不要把旧页的细节当作该 v2 基础页的完整规范。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Object | 对象实例 | 一个特定对象类型的运行时实例 |
| Object Type | 对象类型 | 定义对象实例结构的 schema |
| Object Set | 对象集合 | 多个对象实例的集合资源 |
| API v2 | API v2 | 此页面兼容入口对应的新版 API |

## 疑问与待验证项

- v2 基础页没有列出属性过滤规则；需以 v2 List/Search Objects 端点而非 v1 概念页为准。
- 概念文本相同不能证明 v1/v2 对象读取响应或一致性相同。

## 复刻启示

- 数据模型隔离对象实例资源和类型 schema，给画布两种不同的视图模式及节点语义。
- 后端 API 适配器依据明确版本实现读取、分页和字段权限，不复用 v1 参数规则作为默认值。
