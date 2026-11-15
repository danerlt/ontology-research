<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/ontology-object-sets/load-object-set -->
<!-- 研读状态：已完成 -->

# Load Object Set • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/ontology-object-sets/load-object-set)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/ontologies-v2-resources/ontology-object-sets
- 相关性：direct；Ontology REST API v2 参考
- 官方更新时间：2026-11-12T17:46:46.922Z
- 目录核对时间：2026-11-14T14:54:05Z
- 产品状态：常规 v2 读取接口；OTDP 加载与属性证券信息仍为实验性能力，分支/事务流程存在实验性限制。

## 英文原文短摘录（每个来源不超过 25 词）

> “Load the ontology objects present in the `ObjectSet` from the provided object set definition.”

## 摘录译文

从给定对象集合定义中加载其中的 Ontology 对象。

## 中文要点

- POST `/api/v2/ontologies/{ontology}/objectSets/loadObjects` 将集合定义求值并返回当前页对象；请求支持字段选择、排序、属性 load level、页令牌、快照和可选计算用量。
- `pageSize` 只是最大值，若有 `nextPageToken` 就必须继续读取。默认 `snapshot=false` 会读取最新状态，分页期间可能重复或遗漏；开启快照可固定一致视图。按相关性排序的多页结果也不保证跨页稳定，需完整性时用单页或稳定字段排序。
- OSv1 对象加载上限为 10,000 条，OSv2 无此端点级上限；null 值不会返回，vector 属性需显式选取。`loadOntologyDefinedDerivedProperties` 默认开启但只在未显式选择属性时生效，目前尚未普遍开放；`loadPropertySecurities` 也属实验性。
- 读取完整对象会占用内存；`executeInMemoryOnly` 可要求无法以内存计算时失败。computeUsage 只对 OSDK 应用开放且可能拖慢查询。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| select / selectV2 | 属性选择 | 两种字段标识方案只能选其一。 |
| defaultLoadLevel | 默认加载层级 | 控制数组 reducer 与结构体主字段是否应用。 |
| snapshot | 快照一致性 | 在分页读取时固定开始前的数据视图。 |
| loadPropertySecurities | 加载属性安全级别 | 实验能力，响应按索引描述每个安全属性值的权限信息。 |

## 疑问与待验证项

- 对相关性排序的分页不能保证不重复或不遗漏，因此该排序不适合要求完整性的遍历。
- OTDP 与属性安全信息加载仍有实验限制；复刻 API 不应把它们宣传成已普遍可用的稳定契约。

## 复刻启示

- 对象检查器需采用令牌驱动分页，并可选一致快照；将选择字段、结构体/数组装载规则和派生属性开关纳入查询计划。
- 大集合默认只做服务端筛选或聚合；完整加载需给出规模与内存保护，权限敏感属性逐字段返回可解释授权标记。
