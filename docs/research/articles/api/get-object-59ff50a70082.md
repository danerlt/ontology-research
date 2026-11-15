<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/ontology-objects/get-object -->
<!-- 研读状态：已完成 -->

# Get Object (v2, latest) • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/ontology-objects/get-object)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/ontologies-v2-resources/ontology-objects
- 相关性：direct；Ontology REST API v2 参考
- 官方更新时间：2026-11-12T17:46:46.921Z
- 目录核对时间：2026-11-14T14:54:12Z
- 产品状态：v2 `GET` 单对象；Ontology 定义派生属性读取为实验性且未普遍开放，分支/事务读取也有实验标记

## 英文原文短摘录（每个来源不超过 25 词）

> “Gets a specific object with the given primary key.”

## 摘录译文

该端点按 Ontology、对象类型和主键读取一个对象，并支持选择响应属性。

## 中文要点

- 端点为 `GET /api/v2/ontologies/{ontology}/objects/{objectType}/{primaryKey}`；`ontology` 接受 API 名称或 RID，另外两个路径参数分别使用对象类型 API 名和对象主键。
- `select` 可限制返回属性；默认返回全部属性。`excludeRid=true` 在 Object Storage v2 对象上可能提升读取性能。响应是 API 属性名到 JSON 值的映射，不同 Ontology 类型采用不同编码，例如 Date 为 ISO 日期字符串，Decimal/Long 为字符串，Geo 类型为 GeoJSON，受保护属性有专用包装。
- 可请求 `loadOntologyDefinedDerivedProperties`，默认值为 true，但只在没有显式属性选择时生效；指定属性后该标志不影响返回值。该功能被标为实验性、尚未普遍开放。
- 可传 `branch` 或 `transactionId` 指定读取上下文，文档分别标记为实验功能且并非所有工作流受支持；`scenarioRid` 用于从本体场景读取。
- OAuth2 第三方应用需请求 `api:ontologies-read` 操作范围。使用 RID、对象类型 API 名和主键时应由元数据接口/本体管理器取得，避免依赖展示标签。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| `primaryKey` | 主键 | 对象类型定义的业务键，用于读取特定实例。 |
| `select` | 属性选择 | 控制响应包含哪些属性；缺省为全部属性。 |
| `loadOntologyDefinedDerivedProperties` | 加载本体定义派生属性 | 请求派生属性；当前标为实验性，且显式 `select` 时该选项无效。 |
| `scenarioRid` | 场景 RID | 指定从隔离的 Ontology Scenario 读取对象。 |
| `api:ontologies-read` | 本体读取范围 | 第三方 OAuth2 应用调用此端点所需的操作范围。 |

## 疑问与待验证项

- 文档没有定义派生属性计算超时、缓存、跨链接授权和具体错误格式；需结合派生属性、权限及错误参考页面核实。
- `select` 与派生属性加载开关之间存在条件关系；客户端不能把请求成功等同于所选字段都已经按预期计算。
- Branch/transaction 的兼容范围有限，生产调用需核验目标工作流是否支持，且不可据单对象 GET 推断所有端点都接受这些上下文参数。

## 复刻启示

- 单对象检查器提供属性投影与类型感知 JSON 展开；保留 API 名、展示名、原始值和类型编码，特别标记敏感/受保护属性。
- 用户确认的派生属性路线应把实验能力与稳定能力区分：显示可用性状态、Beta/实验标签、计算输入、结果和失败原因；发布前限制范围并进行权限校验。
- 本体编辑分支/场景的读取应携带明确上下文 ID，响应与缓存键也纳入项目、本体、分支/场景和事务版本，防止把草稿值展示为正式环境结果。
