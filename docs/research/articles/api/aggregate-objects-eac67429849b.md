<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/ontology-resources/objects/aggregate-objects -->
<!-- 研读状态：已完成 -->

# Aggregate Objects (v1) • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/ontology-resources/objects/aggregate-objects)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/ontology-resources/objects
- 相关性：direct；Ontology API v1 端点参考，保留兼容性对照并优先关注 v2
- 官方更新时间：2026-11-12T17:46:46.922Z
- 目录核对时间：2026-11-14T14:54:58Z
- 产品状态：页面未标注 Preview；分支与版本能力按部署核验

## 英文原文短摘录（每个来源不超过 25 词）

> “Perform functions on object fields in the specified ontology and object type.”

## 摘录译文

对指定本体和对象类型中的对象字段执行函数计算。

## 中文要点

- `POST /api/v1/ontologies/{ontologyRid}/objects/{objectType}/aggregate` 对一个对象类型执行聚合，可提交 `aggregation`、过滤用 `query` 和分组条件 `groupBy`。
- 请求可以同时定义多个聚合和分组，结果 `data` 为每组的指标与分组键；响应还可含 `nextPageToken` 和 `excludedItems`。OAuth2 第三方客户端需要 `api:ontologies-read`。
- 页面示例包括 min/avg 与日期范围、城市精确值的组合。统计契约细节（类型支持、null 和区间边界）见同组 Aggregate Objects Details 页面。
- 本接口返回统计结果而不是完整对象列表，适合分析或对象集摘要；不要把聚合结果当成可直接编辑的对象实例。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| aggregate objects | 聚合对象 | 对筛选对象集做统计和分组 |
| ontologyRid | 本体 RID | API v1 的本体资源标识 |
| aggregation | 聚合项 | 指标类型、属性字段和结果名称 |
| groupBy | 分组条件 | 按属性精确值或区间组织结果 |

## 疑问与待验证项

- 请求字段在 API schema 中为 optional；页面未明确空请求的默认行为，客户端应在校验层要求至少一个有效计算。
- `nextPageToken` 适用于何种聚合结果分页以及分页期间结果一致性未在该接口摘录中说明。
- 用户所需的精确近似度和数值溢出/精度行为，应按属性类型及后端实现验证。

## 复刻启示

- 将 aggregation/query/groupBy 定义为有类型的 AST，服务端根据对象类型 schema 校验字段引用、操作符和输出名称。
- 结果保持 `{group, metrics}` 结构，可供画布中的派生聚合节点直接连接；同时记录查询版本、筛选、时间边界和权限裁剪。
- v1 接口用 ontology RID，较新 v2 接口改用 API 名或 RID；SDK/API 适配层应隔离资源标识差异。
