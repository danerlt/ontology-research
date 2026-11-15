<!-- 页面 URL：https://www.palantir.com/docs/foundry/functions/api-object-sets -->
<!-- 研读状态：已完成 -->

# Functions • Functions on objects • Object sets (TSv1) • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/functions/api-object-sets)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/functions/api-object-sets)（配对状态：matched）
- 页面语言：英文
- 主题栏目：functions
- 相关性：direct；本体函数文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:03:14Z
- 产品状态：本页覆盖 TypeScript v1（TSv1）；TSv2 与 Python 改用 Ontology SDK，文档提供迁移对应表。

## 英文原文短摘录（每个来源不超过 25 词）

> “An object set represents an unordered collection of objects of a single type.”

## 摘录译文

对象集合表示单一对象类型的无序对象集。

## 中文要点

- TSv1 的 ObjectSet 是惰性集合：可筛选、按本体 Link Type 做 Search Around、排序、分桶聚合或最后才加载具体对象；作为函数输入时不会像数组一样预先把全部实例放进执行内存。
- 过滤、排序与聚合仅对启用 `Searchable` 渲染提示的属性可用；同类型对象集可做 union/intersect/subtract。TSv2 仍提供同名集合操作，但查询 API 转到 OSDK。
- `.all()`/`.allAsync()` 会完整加载对象，TSv1 上限 100,000 条，超过 10,000 条也可能超时；若只需汇总应使用后端聚合，若只需局部展示可用有序 `.take(n)`，但它会静默截断且不是分页。完整遍历采用 OSS 快照分页，流式源不保证快照一致，超长查询还会遇到快照到期或 `PagingInconsistencyDetected`。
- 内存加载最多允许三次 Search Around；单次 Search Around 的目标集合限制为 OSv2 1,000 万、OSv1 100,000 个实例。需稳定分批时按唯一、非空且支持范围过滤的键递增遍历。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Search Around | 周边搜索/链接遍历 | 沿已定义 Link Type 从当前集合查询关联对象集合。 |
| lazy object set | 惰性对象集合 | 集合运算可以先组合查询，按需再加载实例。 |
| Searchable | 可搜索 | 允许 TSv1 在该属性上进行筛选、排序和聚合的索引提示。 |
| take(n) | 取前 n 项 | 有序集合中返回至多 n 个对象；不足以覆盖全量数据。 |

## 疑问与待验证项

- 文档强调对象集合通常比数组更适合作为函数参数，但执行上限仍依赖存储版本、运行时预算及查询链；不能只按对象总数评估成本。
- `take(n)` 的静默截断对要求完整性特别危险；API/UI 应明确显示“部分结果”状态。

## 复刻启示

- 推理画布应把筛选、链接遍历和集合运算保留为惰性查询 AST，只有显示实例明细时才加载对象；计算聚合则尽量下推到后端。
- 执行计划应显示跳数、目标对象规模、存储版本与是否完整遍历；大结果启用唯一键游标分批，禁止把带 `take` 的预览误当成完整推理证据。
