<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/v1/ontology-resources/objects/aggregate-objects -->
<!-- 研读状态：已完成 -->

# Aggregate Objects (v1) • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/v1/ontology-resources/objects/aggregate-objects)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/v1/ontology-resources
- 相关性：direct；Ontology API v1 聚合端点，保留兼容性对照并优先关注 v2
- 官方更新时间：2026-11-12T17:46:46.923Z
- 目录核对时间：2026-11-14T14:55:46Z
- 产品状态：页面未标注 Preview；使用 v1 Ontology RID 路径

## 英文原文短摘录（每个来源不超过 25 词）

> “Perform functions on object fields in the specified ontology and object type.”

## 摘录译文

对指定本体和对象类型中的对象字段执行聚合函数。

## 中文要点

- `POST /api/v1/ontologies/{ontologyRid}/objects/{objectType}/aggregate` 按本体和对象类型执行对象字段聚合；请求可携带 `aggregation`、对象过滤 `query` 和 `groupBy`。
- 可返回 min/max/sum/avg/count/approximateDistinct 等指标，并将结果按 exact、range 等类型分组；响应包括每组的 `metrics` 与 `group`，可能包含 `nextPageToken` 和 `excludedItems`。
- 这是统计结果 API，不返回可直接编辑的对象实例。OAuth2 第三方调用需要 `api:ontologies-read`。
- API v1 以 ontology RID 标识资源；v2 形式采用 `{ontology}` 并允许 API 名或 RID，适配层应保留该版本区别。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| aggregate objects | 聚合对象 | 对对象子集做计算和分组 |
| aggregation | 聚合指标 | 要计算的统计函数及目标字段 |
| groupBy | 分组条件 | 将结果按属性值/区间汇总 |
| ontologyRid | 本体 RID | v1 路径参数 |

## 疑问与待验证项

- 页面 schema 将若干请求字段标为 optional，没有说明不传任何字段时是否默认计数或报错。
- 分组结果跨页是否一致、分组顺序如何稳定，需查通用分页说明与运行接口。
- 近似计数精度与资源消耗没有在 endpoint 总览页约定。

## 复刻启示

- 定义 typed aggregation AST，编译前根据属性类型检查聚合支持、过滤条件和分组边界。
- 派生值面板复用统计表达式，但结果需要注明查询过滤、权限裁剪、近似性质和被排除组数。
- 通过 API 版本适配器统一 v1 RID 与 v2 API 名，避免前端画布依赖 REST 路由细节。
