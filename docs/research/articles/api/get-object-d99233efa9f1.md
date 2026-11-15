<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/ontology-objects/get-object -->
<!-- 研读状态：已完成 -->

# Get Object (v2, latest) • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/ontology-objects/get-object)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/v2/ontologies-v2-resources
- 相关性：direct；Ontology REST API v2 参考
- 官方更新时间：2026-11-12T17:46:46.921Z
- 目录核对时间：2026-11-14T14:57:25Z
- 产品状态：常规读取接口；本体定义派生属性尚属实验性，分支/事务也有限制。

## 英文原文短摘录（每个来源不超过 25 词）

> “Gets a specific object with the given primary key.”

## 摘录译文

按给定的主键获取一个指定对象。

## 中文要点

- GET `/api/v2/ontologies/{ontology}/objects/{objectType}/{primaryKey}` 按本体、对象类型和主键读取对象；OAuth 需要 `api:ontologies-read`。
- `select` 可限制返回属性；还可指定情景、排除 `__rid`、从分支/事务读取。分支与事务为实验性工作流。
- `loadOntologyDefinedDerivedProperties` 默认开启，但仅在未显式选择属性时生效；该 OTDP 能力当前为实验性、尚未普遍开放。属性值按类型编码为 JSON。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| primaryKey | 主键 | 定位单个对象的业务键。 |
| select | 属性选择 | 指定响应中包含的对象属性。 |
| OTDP | Ontology 定义派生属性 | 对象读取可选择返回的派生属性能力；页面标为实验性。 |
| scenarioRid | 情景 RID | 指定读取对象的情景上下文。 |

## 疑问与待验证项

- OTDP 表达式、依赖限制、权限传播和错误语义不在 Get Object 页面说明范围内。
- 显式选择属性时 OTDP 开关不生效，调用方应清楚区分投影与默认读取。
- 同一对象在默认分支、实验分支及情景中的合并/优先级需由情景与分支文档补足。

## 复刻启示

- 对象详情 API 保留主键、RID 与 API 名；属性投影允许画布检查器按需加载字段。
- 把 OTDP 作为独立实验能力建模：显示计算来源和依赖，执行时受字段权限约束，并标记当前实现与 Palantir GA 能力的差别。
- 分支、情景、事务参数都要成为读取上下文，不能混入全局缓存。
