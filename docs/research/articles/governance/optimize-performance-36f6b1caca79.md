<!-- 页面 URL：https://www.palantir.com/docs/foundry/functions/optimize-performance -->
<!-- 研读状态：已完成 -->

# Functions • Function consumption • Optimize performance • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/functions/optimize-performance)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/functions/optimize-performance)（配对状态：matched）
- 页面语言：英文
- 主题栏目：functions
- 相关性：direct；本体函数文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:02:39Z
- 产品状态：页面当前未标注特定 Beta/预览/弃用状态；关联功能状态按引用子页复核。

## 英文原文短摘录（每个来源不超过 25 词）

> “Asynchronous operations can speed up function execution, but they may not reduce resource usage.”

## 摘录译文

异步操作可以加快函数执行，但未必会降低资源消耗。

## 中文要点

- 函数资源成本包含固定执行开销、实际 vCPU 计算时间及外部平台调用等部分；当前页面说明每次执行另有固定 4 compute-seconds 开销。
- 对象集通常优于对象数组或单对象输入：对象集延迟加载，count/sum 等可由 Ontology 后端直接聚合，避免把大量实例载入函数内存。
- 大量链接遍历要避免循环内逐对象读取导致 N+1 往返；优先批量 Search Around/Objects API。Promise.all 并行可降低墙钟时间，但相同数量的请求仍会产生相同资源调用成本。
- 性能页也覆盖函数支持的 Workshop 派生列：对输入字段做投影、限制内存对象量、使用对象集聚合，并在需要时并发计算结果。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| compute-seconds | 计算秒 | 平台用于度量函数计算资源的单位。 |
| ObjectSet | 对象集 | 由本体后端查询/聚合的惰性对象集合。 |
| N+1 query pattern | N+1 查询模式 | 在遍历对象时对每个对象重复请求关联数据。 |
| wall-clock time | 墙钟时间 | 用户实际等待的总时长。 |

## 疑问与待验证项

- 页面所列固定开销和计量规则可能随平台计划调整；复刻成本模型应以配置与实测为准，不能固化为产品常量。
- 并行度也受服务限流、函数超时和内存限制约束，不能仅靠 Promise.all 无限扩张。

## 复刻启示

- 本体推理/派生属性引擎优先将过滤、链接遍历、聚合下推到查询层；预览展示计划节点、数据规模、请求次数和耗时。
- 对运行成本分别记录计算、数据读取与模型/外部 API 调用，避免只展示总耗时而找不到瓶颈。
