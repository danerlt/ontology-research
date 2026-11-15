<!-- 页面 URL：https://www.palantir.com/docs/foundry/ontologies/oss-limitations -->
<!-- 研读状态：已完成 -->

# Ontologies • Usage • Object Set Service limitations • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/ontologies/oss-limitations)
- 官方中文来源：尚未发现直接对应页面（配对状态：missing）
- 页面语言：英文
- 主题栏目：ontologies
- 相关性：direct；对象集查询、链接遍历、聚合与分页限制
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:01:47Z
- 产品状态：OSv1 planned deprecation 区块给出的 2026-06-30 日期已过，须向当前环境核验实际状态

## 英文原文短摘录（不超过 25 词）

> “Do not interpret a short page as the end of the result set.”

## 摘录译文

不要把较短的一页误认为结果集已经结束。

## 中文要点

- Object Set Service（OSS）会按查询复杂度自动分层执行：简单请求下推到存储索引，中等规模在内存处理，超过容量后转为 Spark 分布式计算；复杂查询的不同阶段可使用不同策略。
- OSv2 Search Around 通常对不超过 100,000 个对象使用内存处理，超过阈值可转到 Spark；单次 Search Around 返回叶对象集上限为 1,000 万，整个查询从各数据源加载的对象总量上限为 3,000 万。
- 若内部读取超过 25 个 Object Storage v2 分页，OSS 可回退到 Spark；Functions on Objects 一次加载超过 10,000 个对象时，复杂逻辑可能超时。
- 因内存限制，分页响应可能小于请求 page size；只要返回 page token 未空，就必须继续读，不能以短页作为结束条件。
- Search Around 使用关系连接查找目标对象；建议先过滤、分页处理大集合，并在昂贵链接查询前评估集合规模。页面的 OSv1 计划弃用日期现已过去，不能直接假设旧对象当前仍可访问或已下线。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Object Set Service (OSS) | 对象集服务 | 负责执行本体对象集查询和检索 |
| Search Around | 关系遍历搜索 | 根据对象类型间链接查找关联对象 |
| leaf object set | 叶对象集 | Search Around 从单个数据源实际加载的目标结果 |
| page token | 分页令牌 | 即使当前页不足 page size，仍用于继续读取 |

## 疑问与待验证项

- 文档中的阈值标注为默认值，可能随环境和资源调整；不要把它们当成所有 enrollment 的强制服务契约。
- OSv1 planned deprecation 写明“2026-06-30 后不可用”，该时间已过去，需查当前迁移文档和运行环境实际响应状态。
- OSS 对更复杂的多阶段查询如何计算各级阈值，文中只给出总体策略与少数限制。

## 复刻启示

- 对象集查询引擎需要执行计划策略：索引下推、小集合内存处理、大集合分布式执行，并暴露策略与成本。
- Search Around 在运行前报告估算规模和叶/总对象上限；建议先过滤，避免无提示的超大关系遍历。
- 分页客户端必须以 token 为空作为终止条件，并允许因服务端内存压力返回短页。