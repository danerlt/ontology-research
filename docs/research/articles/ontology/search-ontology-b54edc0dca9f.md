<!-- 页面 URL：https://www.palantir.com/docs/foundry/foundryts/search-ontology -->
<!-- 研读状态：已完成 -->

# FoundryTS • API Reference • search.ontology • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/foundryts/search-ontology)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/foundryts/search-ontology)（配对状态：matched）
- 页面语言：英文
- 主题栏目：foundryts
- 相关性：direct；Ontology 查询 SDK 文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:04:56Z
- 产品状态：待核对 Beta、预览、弃用或更名信息

## 英文原文短摘录（每个来源不超过 25 词）

> “Creates an Ontology property reference for search.”

## 摘录译文

创建供搜索使用的 Ontology 属性引用。

## 中文要点

- `foundryts.search.ontology(name, should_normalize=False, force_analyze=False)` 按 Ontology 中的属性名生成 `Property` 引用，可用于 `Search.series()` 的条件表达式；示例对一个时间序列属性与目标值比较后执行搜索。
- `should_normalize` 控制属性名是否规范化，默认 `False`；`force_analyze` 被明确标为 Deprecated。该函数服务于 FoundryTS 的时间序列查询，不是通用 Ontology 对象搜索 API。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Property | 属性引用 | FoundryTS 查询 DSL 中用于比较的本体属性句柄。 |
| Search.series() | 时间序列搜索 | 在时间序列搜索器上执行属性过滤。 |
| force_analyze | 强制分析 | 已弃用的参数，不应在新实现中依赖。 |

## 疑问与待验证项

- 函数接收名称而不是稳定 RID；属性改名或规范化策略变化可能影响运行，需要确认目标 FoundryTS 版本行为。
- 页面对弃用参数未列出替代项；应按 `Search.series()` 文档确认当前搜索分析选项。

## 复刻启示

- 时间序列推理节点应将 Ontology 属性引用和时间序列搜索条件保存为类型化表达式，避免误用通用对象过滤接口。
- 构建工具可检测被弃用的选项，并将名称解析失败、属性重命名及规范化行为纳入上线前校验。
