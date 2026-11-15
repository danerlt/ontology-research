<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/ontology-objects -->
<!-- 研读状态：已完成 -->

# Ontology Object basics (v2, latest) • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/ontology-objects)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/v2/ontologies-v2-resources
- 相关性：direct；Ontology REST API v2 参考
- 官方更新时间：2026-11-12T17:46:46.921Z
- 目录核对时间：2026-11-14T14:57:24Z
- 产品状态：v2 Object 基础页入口，未标 Preview

## 英文原文短摘录（每个来源不超过 25 词）

> “An Object is a data container for a specific instance of an Object Type.”

## 摘录译文

Object 是某个 Object Type 具体实例的数据容器。

## 中文要点

v2 `/ontology-objects` 导航入口在目录中对应 Object 基础页。Object 是 Object Type 的单个实例及其数据容器；其 schema 在 Object Type 资源定义，对象集合则是多个实例的另一种查询资源。该页面没有重复 v1 概念页的过滤 DSL 说明。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Object | 对象实例 | 具体运行时实体及属性数据 |
| Object Type | 对象类型 | 定义对象结构的本体 schema |
| Object Set | 对象集合 | 多个 Object 的查询集合 |
| Canonical URL | 规范地址 | `/ontology-object-basics` 子页 |

## 疑问与待验证项

- 导航入口 canonical 到基础页；实际对象读取 API 需使用 Get/List/Search Object 操作。
- 页面不说明 v2 的字段筛选、分页或对象权限细节。

## 复刻启示

- 让画布从 schema 节点进入对象样例浏览，但明确切换视图并携带项目/本体/类型作用域。
- 实例关系图应来自运行时链接数据，结构图使用对象类型和 Link Type 定义，两者能相互跳转但语义不同。
