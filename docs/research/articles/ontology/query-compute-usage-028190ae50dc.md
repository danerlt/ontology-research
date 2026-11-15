<!-- 页面 URL：https://www.palantir.com/docs/foundry/ontologies/query-compute-usage -->
<!-- 研读状态：已完成 -->

# Ontologies • Usage • Ontology query compute • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/ontologies/query-compute-usage)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/ontologies/query-compute-usage)（目录配对状态：matched）
- 页面语言：英文
- 主题栏目：ontologies
- 相关性：direct；本体对象集、Agent 查询和按资源计算归因
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:01:44Z
- 产品状态：现行查询计算模型自 2026-01-01 生效；页面同时保留旧模型

## 英文原文短摘录（不超过 25 词）

> “Ontology Query Compute is driven by Ontology use by users and agents.”

## 摘录译文

本体查询计算量由用户和 Agent 对本体的使用驱动。

## 中文要点

- 页面按 Ontology query 的计算秒数记录用量；计算一般归因到发起查询的资源。没有可归因资源时按被查对象类型分摊；多对象同请求时均分。
- 2026-01-01 起的新模型将用户交互、Agent 转换和查询类型作为主要因素；查询复杂度和对象集规模可使实际消耗高于最低开销。
- 文档列出的各类单次最低 compute-seconds：Base 2、Search Around 5、Aggregation 5、Ontology SQL 5、Advanced 10、Derived Property 10、Action 18。
- Action 写回超过一个对象时，除基础 18 外，每多编辑一个对象增加 1 compute-second；OSv1 查询仍保留 legacy 16 compute-second 最低开销。
- Workshop、AIP Logic、OSDK 等调用通常归因到相应应用资源；Object Explorer 和直接对象 API 通常归到被查询对象类型。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| compute-seconds | 计算秒数 | 查询或写回工作量的计量单位 |
| Search Around query | 关系遍历查询 | 沿链接到另一对象集进行过滤 |
| Derived Property query | 派生属性查询 | 查询时从属性或链接对象计算值 |
| compute attribution | 计算归因 | 将消耗记入应用资源或对象类型 |

## 疑问与待验证项

- 文档说明企业合同需联系 Palantir 代表进行计算用量核算；列出的最低值不能直接视为完整账单价格。
- 同一查询可按请求复杂度和对象集规模增加消耗；页面未给出所有执行计划到实际计量的换算公式。
- 现行 2026 表与旧模型并列，使用者需按对象存储后端和生效日期选用，不能把 legacy 表作为当前默认。

## 复刻启示

- 查询与派生属性试算应记录调用主体、Agent、项目、请求类型、对象规模和资源来源，生成可追溯的成本归因。
- 提供估算/实际用量两个指标，并把最低固定开销、对象规模增量和运行时计算分开显示。
- Agent 的查询和变换应进入成本与审计轨迹，避免把 Agent 工作量隐藏在普通 UI 请求里。