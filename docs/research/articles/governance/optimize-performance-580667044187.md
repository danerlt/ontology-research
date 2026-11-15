<!-- 页面 URL：https://www.palantir.com/docs/zh/foundry/functions/optimize-performance -->
<!-- 研读状态：已完成 -->

# 函数 • Performance and limits • 优化性能 • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/functions/optimize-performance)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/functions/optimize-performance)
- 页面语言：中文（官方 AIP 机器翻译，需与英文原文交叉核对）
- 主题栏目：functions
- 相关性：direct；本体函数文档
- 官方更新时间：2026-11-12T17:46:46.935Z
- 目录核对时间：2026-11-14T14:59:26Z
- 产品状态：文档以函数性能页、瀑布图和 Ontology 查询成本为中心；页面列出的固定执行开销和资源计量属于可能变化的服务参数。

## 英文原文短摘录（每个来源不超过 25 词）

> “This page describes best practices for optimizing function performance and resource usage.”

## 摘录译文

本页介绍优化函数性能和资源使用的最佳实践。

## 中文要点

- 性能面板用时间瀑布图区分函数 CPU 执行、从参数加载对象和沿链接加载对象等阶段，可据此定位瓶颈。
- 输入类型影响加载成本：对象集适合延迟读取和聚合，对象数组适用于内存遍历，单对象参数应限于确需逐对象处理的场景。
- 并行 `Promise.all` 可减少串行等待时间，但不减少调用次数或计量成本；批量操作才可能同时改善耗时与成本。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Object set | 对象集 | 可查询、聚合的惰性对象集合 |
| waterfall graph | 瀑布图 | 按时间展示函数与本体服务操作耗时的诊断图 |
| compute-seconds | 计算秒 | 函数平台使用的资源计量单位 |

## 疑问与待验证项

- 页面示例列出每次执行 4 计算秒固定开销；该数字是当前文档快照，复刻系统不能写死为稳定商业规则。
- 文档建议某些聚合/链接遍历改用 Objects API，但不同语言、查询形态和数据量下的切换阈值需实测。
- 并行请求可能加大瞬时并发和后端压力；批量接口的最大规模和超时策略需单独定义。

## 复刻启示

- 画布和函数详情应展示可解释的查询计划：对象集加载、链接遍历、聚合、函数 CPU 与外部模型调用阶段耗时。
- 推理引擎优先在数据层做对象集过滤/聚合，避免将大批对象预加载到 Python 进程后循环计算；显式限制遍历深度和结果规模。
- 性能面板同时给出端到端耗时、后端调用数、扫描/返回对象数和成本估算，区分并行降延迟与批处理降成本。
