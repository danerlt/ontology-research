<!-- 页面 URL：https://www.palantir.com/docs/zh/foundry/foundryts/search-ontology -->
<!-- 研读状态：已完成 -->

# FoundryTS • API Reference • foundryts.search.ontology • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/foundryts/search-ontology)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/foundryts/search-ontology)
- 页面语言：中文
- 主题栏目：foundryts
- 相关性：direct；Ontology 查询 SDK 文档
- 官方更新时间：2026-11-12T17:46:46.932Z
- 目录核对时间：2026-11-14T14:58:42Z
- 产品状态：待核对 Beta、预览、弃用或更名信息

## 英文原文短摘录（每个来源不超过 25 词）

> “Creates an Ontology property reference for search.”

## 摘录译文

为搜索创建 Ontology 属性引用。

## 中文要点

- 中文页将 `foundryts.search.ontology()` 定义为按名称创建属性引用，并将其传给 `Search.series()` 与值比较，从而筛选符合条件的时间序列数据。
- `should_normalize` 默认关闭；`force_analyze` 明确标记为已弃用。此接口只负责 FoundryTS 时间序列搜索 DSL 的属性句柄，不是对 Ontology 全部对象进行自由文本检索。
- 页面提示中文译文由 AIP 自动生成且准确性未验证；关键行为已与英文 API 参考逐项对照。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| 属性引用 | Property reference | 供查询 DSL 使用的本体属性标识对象。 |
| 时间序列搜索 | `Search.series()` | 在 FoundryTS 中按属性和值查询时间序列。 |
| 属性名规范化 | `should_normalize` | 控制构造属性引用时是否规范化名称。 |

## 疑问与待验证项

- 中文文档未说明弃用 `force_analyze` 的替代方式，需查看当前 FoundryTS 搜索页。
- 属性按名称解析的重命名影响需通过实际 SDK 版本验证，文档没有提供稳定 ID 方案。

## 复刻启示

- 在推理画布中把时间序列属性引用显式呈现为可检查节点，并记录解析名称、规范化设置与目标时间序列搜索。
- 对属性更名或删除做依赖检查；时间序列过滤结果不能与对象集合筛选混为一类，以免解释错误数据路径。
