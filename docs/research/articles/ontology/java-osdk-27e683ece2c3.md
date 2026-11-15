<!-- 页面 URL：https://www.palantir.com/docs/zh/foundry/ontology-sdk/java-osdk -->
<!-- 研读状态：已完成 -->

# OSDK • Java Ontology SDK (OSDK) • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/ontology-sdk/java-osdk)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/ontology-sdk/java-osdk)
- 页面语言：中文
- 主题栏目：ontology-sdk
- 相关性：direct；Ontology SDK 文档
- 官方更新时间：2026-11-12T17:46:46.932Z
- 目录核对时间：2026-11-14T15:00:52Z
- 产品状态：此机器翻译参考页未将 Java OSDK 整体标为 Beta；读取限制与属性投影能力以英文页为准

## 英文原文短摘录（每个来源不超过 25 词）

> “based on an example Restaurant object and its associated Actions and Queries.”

## 摘录译文

基于示例 Restaurant 对象及其相关 Actions 和 Queries。

## 中文要点

- 中文页面覆盖 `Restaurant` 对象的单个读取、流式读取、排序过滤、分页与聚合，也展示由本体生成的 Action 调用与响应。
- 一次读取使用主键访问对象；对象集合可用类型安全的过滤器与排序器构造查询，再以流或分页形式取数。过滤操作依赖属性类型，字符串搜索操作、数值/日期比较及空值筛选各有适用范围。
- 聚合支持计数、数值统计、近似去重和分组，响应包含分组键、指标和 `excludedItems`。动作响应既含 validation，也含编辑计数和编辑明细，适合将输入校验与变更预览分开展示。
- 本页描述的底层 Object Storage v1（Phonograph）存在 10,000 条读取限制；示例中某些代码片段把 `Restaurant` 与其他类型名混用，属于示例质量问题，不应视为合法类型转换。
- 页面顶部声明译文由 AIP 从英文文本机器翻译，准确性尚未验证。此卡片引用中文短句只用于定位页面，不把机器译文当作独立的权威技术证据。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| `Ontology SDK` | 本体 SDK | 根据某个 Ontology 生成的类型化客户端。 |
| `ObjectSet` | 对象集 | 支持过滤、排序、聚合等操作的对象查询集合。 |
| `Action` | 操作 | 对本体对象执行创建、修改或删除的预定义操作。 |
| `ObjectsExceededLimit` | 对象数超限错误 | 本页所述 v1 存储读取超过 10,000 条时可能出现的错误。 |

## 疑问与待验证项

- 页面自述译文未经验证；枚举方法名、分页参数、限制和响应形状应回到英文文档或版本化 API 参考核实。
- 本页示例偶有类型名不一致（如使用 `Aircraft` 变量/筛选器而上下文为餐馆），需防止机器翻译或文档编辑错误混入实现规格。
- 同一页并列 v1/v2 底层对象存储说明，但没有据此推断所有查询、聚合和数据源均具有相同限制。

## 复刻启示

- 中文文档视图应保留机器翻译提示、原文链接和版本标记；翻译文本适合快速浏览，不应覆盖可追溯的英文契约。
- 对象类型、属性类型、可用过滤操作和 Action 参数应来自 schema，并由代码生成与 UI 检查器共享，避免手写示例造成名称漂移。
- 画布或查询预览的聚合节点应呈现 `excludedItems`、分组键及指标，便于发现因无效值或类型转换导致的数据丢失。
