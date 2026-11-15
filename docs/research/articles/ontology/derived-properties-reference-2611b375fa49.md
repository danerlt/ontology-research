<!-- 页面 URL：https://www.palantir.com/docs/foundry/ontology/derived-properties-reference -->
<!-- 研读状态：已完成 -->

# Derived properties reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/ontology/derived-properties-reference)
- 官方中文来源：未确认对应页
- 页面语言：英文
- 主题栏目：ontology
- 相关性：direct；本体模型与治理文档
- 官方更新时间：页面未提供
- 目录核对时间：2026-11-15
- 产品状态：参考页；包含各种聚合/表达式的类型与性能约束。

## 英文原文短摘录（每个来源不超过 25 词）

> “An aggregation combines values from many linked objects into one value.”

## 摘录译文

聚合会把多个关联对象的值合成为一个值。

## 中文要点

- 多对象链接路径必须聚合后才能得到标量；若任一段可能抵达多个对象，或路径包含多对多链接，就不能直接选取单值。
- 文档列出的操作包括 Count、Average、Sum、Minimum、Maximum、近似/精确基数，以及收集列表/集合；操作对输入类型有约束，向量既不能被选择，也不能参与聚合。
- 查询时计算的派生值不建立索引。过滤关联对象后再聚合通常能减少工作量；近似基数通常比精确基数更省，收集结果的显示上限不会限制底层筛选所检查的全部值。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| aggregation | 聚合 | 将多对象的属性值缩并为结果。 |
| cardinality | 基数 | 不同值的数量；可近似或精确计算。 |
| fan-out | 扇出 | 沿链接展开后中间对象数量的增长。 |

## 疑问与待验证项

- 页面提供相对成本和建议，但具体查询的延迟门槛与回退行为由单独的查询限制文档定义。
- 收集数组的展示截断与筛选范围不同，界面应明确标示截断，避免用户误读。

## 复刻启示

- 推理编辑器按链接基数推导操作类型；多对象路径强制添加聚合器，不允许把隐式 first() 当作确定结果。
- 将过滤、排序、聚合和返回限制分开展示；监控候选数量、跳数、输出大小和耗时，提供预览上限。
