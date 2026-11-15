<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/v1/ontology-resources/objects/ontology-object-basics -->
<!-- 研读状态：已完成 -->

# Ontology Object basics (v1) • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/v1/ontology-resources/objects/ontology-object-basics)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/v1/ontology-resources
- 相关性：direct；Ontology API v1 端点参考；保留作兼容性对照，并优先关注 v2
- 官方更新时间：2026-11-12T17:46:46.923Z
- 目录核对时间：2026-11-14T14:55:53Z
- 产品状态：v1 对象基础页，无 Preview 标记

## 英文原文短摘录（每个来源不超过 25 词）

> “An Object is a data container for a specific instance of an Object Type.”

## 摘录译文

Object 是某个 Object Type 具体实例的数据容器。

## 中文要点

Ontology API v1 对象基础页区分了对象类型与对象实例：对象是某个类型下单一实体的数据容器。此页还给出对象列表的过滤 DSL，使用属性路径和比较运算符，并解释多个条件对同属性的组合方式。它不是用于定义类型 schema 的页面，过滤说明也针对 v1 List Objects 查询。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Object | 对象实例 | 特定 Object Type 的单个数据容器 |
| `eq` / `neq` | 等于 / 不等于 | 精确值比较运算符 |
| Range filters | 范围过滤 | `lt/lte/gt/gte` 数值或时间比较 |
| `isNull` | 空值检查 | 根据属性空值状态过滤对象 |

## 疑问与待验证项

- 该 v1 基础页未描述本体对象的字段权限、对象安全策略或读取一致性。
- 过滤条件的 URL 编码、空字符串与 null 的区别需要参照查询 API 实测。

## 复刻启示

- 图编辑器区分 schema 图和对象关系图，只有第二种视图显示对象实例作为节点。
- 查询画布把过滤条件保留为结构化 AST，再编译为参数，而非拼接不安全的原始 URL 字符串。
