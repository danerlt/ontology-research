<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/ontology-objects/list-objects -->
<!-- 研读状态：已完成 -->

# List Objects (v2, latest) • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/ontology-objects/list-objects)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/ontologies-v2-resources/ontology-objects
- 相关性：direct；Ontology REST API v2 参考
- 官方更新时间：2026-11-12T17:46:46.921Z
- 目录核对时间：2026-11-14T14:54:12Z
- 产品状态：v2 列表 API 默认 `snapshot=false`；`loadOntologyDefinedDerivedProperties` 为实验性、尚未普遍开放

## 英文原文短摘录（每个来源不超过 25 词）

> “This endpoint does not guarantee consistency. Changes to the data could result in missing or repeated objects in the response pages.”

## 摘录译文

该列表端点默认不提供跨页一致性；读取期间的数据变化可能造成遗漏或重复。

## 中文要点

- 端点 `GET /api/v2/ontologies/{ontology}/objects/{objectType}` 返回指定本体和对象类型的分页对象。第一请求省略 `pageToken`，后续请求从响应的 `nextPageToken` 续读；默认 `pageSize` 为 1,000。
- `pageSize` 是期望值而非返回保证：单页可大于或小于请求值，但只要仍有结果，响应至少含一条。空值属性不会出现在返回对象中，调用方需区分“属性缺席”和其他显式值。
- 默认 `snapshot=false`，跨页期间出现新增/修改可能导致重复或遗漏；设置 `snapshot=true` 可按开始翻页前的视图读取，保证无重复/遗漏。OSv1 最多返回 10,000 个对象；OSv2 无此请求数限制。
- `select` 控制返回属性；`orderBy` 可按多个属性和方向排序；`excludeRid` 可在 OSv2 上提升性能。SDK 包/版本和可选 branch 也能作为查询上下文。
- 与单对象端点相似，派生属性加载默认开启但属于实验性、尚未普遍开放，只在没有显式属性选择时应用。OAuth2 第三方应用需 `api:ontologies-read`。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| `pageToken` / `nextPageToken` | 分页令牌 / 下一页令牌 | 通过上一响应继续请求剩余结果。 |
| `snapshot` | 快照一致性 | 固定遍历期间的数据视图；默认关闭。 |
| `select` | 属性选择 | 指定每个对象需要返回的属性。 |
| `totalCount` | 总数 | 响应中的跨页总项目数字段。 |
| `loadOntologyDefinedDerivedProperties` | 加载本体定义派生属性 | 无显式属性选择时加载；文档标为实验性且未普遍开放。 |

## 疑问与待验证项

- 默认弱一致遍历不适合直接用于需要精确全量结果的导出或计数；选择快照也需验证大集合读取成本和保留时长。
- null 属性省略规则会使消费者无法通过返回对象区分“原值为空”和“未请求/未返回”；实现需和对象 schema 配合解释。
- 页面给出的 OSv1/OSv2 数量边界与特定端点有关，仍需对照查询限额、最大 page size 和 API 限制参考。

## 复刻启示

- 对象浏览器要向用户解释分页一致性，并允许明确选择“实时最新”或“固定快照”；导出场景默认采用固定快照。
- 在画布/检查器中将缺失属性显示为“未返回/空值待判定”，不要把缺键自动归一为业务 null；用 schema 的可空性和选择字段作解释。
- 大集合浏览支持属性投影、排序、限量与进度/续页，并显示数据源限制；操作预览必须以实际估算/计数结果校准影响范围。
