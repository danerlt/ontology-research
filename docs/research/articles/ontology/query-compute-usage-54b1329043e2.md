<!-- 页面 URL：https://www.palantir.com/docs/zh/foundry/ontologies/query-compute-usage -->
<!-- 研读状态：已完成 -->

# 本体 • Usage • 使用Ontology查询计算使用情况 • Palantir

- 英文来源：[当前英文原文](https://www.palantir.com/docs/foundry/ontologies/query-compute-usage)
- 官方中文来源：[中文原文](https://www.palantir.com/docs/zh/foundry/ontologies/query-compute-usage)
- 页面语言：中文（官方机器翻译，准确性未验证）
- 主题栏目：ontologies
- 相关性：direct；本体管理与治理文档
- 官方更新时间：2026-11-12T17:46:46.935Z
- 目录核对时间：2026-11-14T15:00:11Z
- 产品状态：Ontology 查询计算模型；2026 版自 2026-01-01 生效

<!-- 研读状态：已完成 -->
# 英文原文短摘录（每个来源不超过 25 词）

> “Ontology Query Compute is driven by Ontology use by users and agents.”

## 摘录译文

本体查询计算量由用户和 Agent 对 Ontology 的使用驱动。

## 中文要点

- 2026 年 1 月 1 日起生效的模型把用户和 Agent 的查询与变换纳入 Ontology 查询计算；对象类型代表实体 schema，对象集代表实际对象集合。
- 当前最低开销：基础查询 2，Search Around、聚合和 SQL 各 5，高级查询与派生属性查询各 10，Action 写回 18；首个对象以外，每增加一个 Action 编辑对象再加 1。OSv1 保留 legacy 最低 16。
- 派生属性在查询时根据对象属性或链接计算，可在同一请求中继续过滤、排序或聚合；实时试算和 Agent 链路计算会消耗查询资源。
- 计算通常归到发起查询的已保存资源；API、Object Explorer 等无保存资源请求归到被查询对象类型，多类型查询按类型均分。
- 企业合同用户应先向 Palantir 代表确认费用；最低开销不代表复杂查询的最终用量。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Ontology query compute | 本体查询计算 | 对象集读取、搜索、聚合、推理和写回使用的计算 |
| Search Around | 关联对象搜索 | 基于输入对象属性在另一对象集筛选 |
| Derived Property query | 派生属性查询 | 读取时沿属性或链接计算属性值 |
| Compute-seconds | 计算秒 | 查询类型最低开销的计量单位 |

## 疑问与待验证项

- 最终费用受对象规模、查询复杂度、部署和合同影响；OSv1 的 legacy 数值不可套用于 OSv2。
- 文档未公开所有高级查询拆分、缓存抵扣与 Agent 调用的完整归因公式。

## 复刻启示

- 推理运行时作为独立查询类型计量；记录定义版本、遍历路径、访问对象数量和聚合步骤以解释成本。
- Agent 工具调用绑定用户和项目上下文并设置预算，避免多轮循环放大查询量。