<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/ontology-objects/search-objects -->
<!-- 研读状态：已完成 -->

# Search Objects (v2, latest) • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/ontology-objects/search-objects)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/ontologies-v2-resources/ontology-objects
- 相关性：direct；Ontology REST API v2 参考
- 官方更新时间：2026-11-12T17:46:46.921Z
- 目录核对时间：2026-11-14T14:54:12Z
- 产品状态：v2 搜索；当前文档列出 `startsWith` 为弃用别名，派生属性加载为实验性、尚未普遍开放

## 英文原文短摘录（每个来源不超过 25 词）

> “Queries can be at most three levels deep.”

## 摘录译文

搜索请求中的查询子句最多嵌套三层。

## 中文要点

- 端点为 `POST /api/v2/ontologies/{ontology}/objects/{objectType}/search`，请求体用组合查询过滤指定类型对象。支持数值/字符串/日期时间比较、空值、数组包含，以及 `not`、`and`、`or` 和字符串词项查询。
- 查询可按字段或相关性排序，可通过 `pageSize`/`pageToken` 和 `select` 控制分页与返回字段；字段投影也有 `selectV2` 标识形式，两者不可同时设置。可配置默认属性加载级别，例如应用数组 reducer、提取 Struct 主值。
- 查询子句最多三层；默认字符串分词由空白或指定标点分割，除显式前缀操作外不匹配部分词。`startsWith` 是已弃用别名，文档推荐 `containsAllTermsInOrderPrefixLastTerm`。
- 请求可设置 `executeInMemoryOnly=true`：如果无法在内存中计算则快速失败，避免悄然启动较重计算；缺省为 false。
- 相关性排序可能昂贵，而且跨页时不保证顺序一致，可能重复或遗漏对象；要求完整结果时应只请求一页。Ontology 派生属性加载默认开启但标记为实验性、未普遍开放，显式 `select` 后该开关不起作用。
- OAuth2 第三方应用需 `api:ontologies-read`。可选 branch 当前属于实验能力，工作流支持有限。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| `SearchObjectsRequestV2` | 搜索对象请求 | 查询过滤、排序、分页和属性投影参数的请求体。 |
| `where` | 过滤条件 | 可组合类型化查询子句的入口。 |
| `executeInMemoryOnly` | 仅内存执行 | 对无法内存执行的查询直接失败，以避免较重计算。 |
| `selectV2` | 属性标识投影 | 新形式的属性标识选择；不能与 `select` 同时使用。 |
| `containsAllTermsInOrderPrefixLastTerm` | 按序词项并前缀匹配末词 | 文档列出的字符串前缀匹配操作。 |

## 疑问与待验证项

- 文档未给出三层嵌套中各逻辑运算符的完整计数定义；实现需按查询树深度静态校验并与接口验证保持一致。
- 相关性分页的不完整性是该排序模式的特殊限制，不应误推成所有字段排序或 `snapshot` 列表 API 的相同保证。
- `select` 与 `selectV2` 的标识差异、默认加载级别及 reducer 能力需与目标 SDK/属性类型版本核对。
- 查询请求体在接口层接受联合结构，但每种运算受属性类型约束；不应将类型校验仅留给运行时数据库。

## 复刻启示

- 画布中的搜索节点应以类型化 AST 表达，静态限制嵌套深度、字段/运算符类型和字符串模式；可将 AST 同时用于实时试算与审计记录。
- “按相关性排序”应标注成本和跨页不完整风险，并限制用于小页预览；需要完整集合时提供稳定字段排序/快照路径。
- 推理或 Agent 生成查询时，把范围、字段、筛选深度和仅内存快速失败开关置于权限与资源预算策略下；返回查询解释和被截断/省略字段说明。
