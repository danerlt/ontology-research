<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/ontology-resources/objects -->
<!-- 研读状态：已完成 -->

# Ontology Object basics (v1) • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/ontology-resources/objects)
- 官方中文来源：尚未确认（配对状态：ambiguous）
- 页面语言：英文
- 主题栏目：api/ontology-resources/objects
- 相关性：direct；Ontology API v1 端点参考；保留作兼容性对照，并优先关注 v2
- 官方更新时间：2026-11-12T17:46:46.923Z
- 目录核对时间：2026-11-14T14:55:09Z
- 产品状态：v1 对象概念页兼容入口，包含 v1 对象列表的属性过滤说明

## 英文原文短摘录（每个来源不超过 25 词）

> “An Object is a data container for a specific instance of an Object Type.”

## 摘录译文

Object 是某个 Object Type 具体实例的数据容器。

## 中文要点

该 v1 路由映射到 Ontology Object 基础页：Object 是某 Object Type 单个实例的数据容器。页面还解释 List Objects 过滤语法：用 `properties.{propertyApiName}.{operator}={value}` 或简写 `p.`，支持相等/不等、范围、数组 contains 和 isNull 等操作；同一属性上的多个 contains/eq 值可按任一值匹配，范围条件需同时满足。此概念页与 Object Type schema 节点不同，描述运行时记录。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Object | 对象实例 | 一个 Object Type 下的具体数据记录 |
| Filter operator | 过滤运算符 | `eq`、`neq`、范围、`contains`、`isNull` 等 |
| `properties.` / `p.` | 属性过滤前缀 | v1 查询参数中指向对象属性的路径 |

## 疑问与待验证项

- 页面没有给出完整的 URL 编码规则和各数据类型的边界行为；复杂值需参考筛选文档及目标 API。
- 对同一属性重复条件的 AND/OR 规则仅对部分运算符作了说明，不可将此推断为所有过滤器都采用相同逻辑。

## 复刻启示

- 架构分层保存类型定义与运行对象；对象画布边表示对象实例之间的关系，建模画布边则表示类型间的潜在关系。
- 运行时对象查询要实现类型化过滤 DSL、参数编码与权限过滤；展示层说明组合条件语义，避免用户误读结果。
