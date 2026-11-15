<!-- 页面 URL：https://www.palantir.com/docs/foundry/ontologies/compute-usage -->
<!-- 研读状态：已完成 -->

# Ontologies • Usage • Ontology indexing compute • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/ontologies/compute-usage)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/ontologies/compute-usage)（配对状态：matched）
- 页面语言：英文
- 主题栏目：ontologies
- 相关性：direct；本体索引作业的计算成本来源与优化
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:01:44Z
- 产品状态：使用与成本说明；非 API Preview 页

## 英文原文短摘录（每个来源不超过 25 词）

> “Ontology indexing jobs are Spark jobs and so are classified as parallelized batch compute.”

## 摘录译文

Ontology 索引作业是 Spark 作业，因此归类为并行批处理计算。

## 中文要点

- Ontology 索引用 Spark 读取数据集并转换为本体后端的可搜索、可编辑对象。计算消耗由 driver/executor 资源配置和作业墙钟时间共同决定；Builds 应用中可观察索引任务，任务归属到被索引的对象。
- 主要成本驱动因素是对象记录数、每个对象的属性数量、各属性大小和上游数据集刷新频率。Ontology 导出作业把 Ontology 直接编辑写回数据集，通常小于完整索引作业。
- 优化可减少索引输入记录、属性数量及属性体量；配置 changelog 索引策略可与现有对象比较、只处理变化对象，显著降低计算，但要求正确的更新策略和额外配置。
- 文档示例按资源 vCPU/内存与运行时计算 driver/executor compute-seconds；示例 driver 10 秒、两个 executor 合计 20 秒，总计 30 compute-seconds。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Ontology indexing | 本体索引 | 将数据集转换并写入本体对象索引 |
| Changelog indexing | 变更日志索引 | 利用已有对象只处理数据变更的策略 |
| Driver / executor | 驱动程序 / 执行器 | 并行 Spark 索引任务中的计算资源角色 |
| Compute-seconds | 计算秒 | 根据资源规格与运行时间计量的成本 |

## 疑问与待验证项

- 该页讲索引作业而非查询计算；对象读取、派生属性、Aggregation 与 Action 的费用在另一篇 Query Compute 文档中解释。
- changelog 策略收益依赖上游数据如何表达新增、更新和删除，不能在变更日志配置不完整时盲目启用。
- 指标计量系数和平台定价会随产品/合同变动；示例用于说明算法，不可直接当报价。

## 复刻启示

- 多项目/多系统导入时分别记录源数据刷新频率、增量游标和被修改对象数，估算索引成本并提供批次级审计。
- 后端可优先使用增量 upsert/changelog 计算对象变更，避免无变化全量重建；同时保留删除墓碑和回填能力。
- 管理台展示索引作业归属对象、资源、运行时间与输入数据量；查询运行开销需另设账本，避免将索引与查询成本混算。
