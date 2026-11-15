<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/time-series-properties -->
<!-- 研读状态：已完成 -->

# Time Series Property basics • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/time-series-properties)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/ontologies-v2-resources/time-series-properties
- 相关性：direct；Ontology REST API v2 参考
- 官方更新时间：2026-11-12T17:46:46.921Z
- 目录核对时间：2026-11-14T14:54:34Z
- 产品状态：API v2 时间序列属性目录入口；当前文档读取工具未能单独读取此路由正文

## 英文原文短摘录（每个来源不超过 25 词）

> “Time Series Property basics”

## 摘录译文

“时间序列属性基础”。该分类入口没有独立正文可核对；同主题基础页定义了其数据点序列语义。

## 中文要点

- 当前可访问的此路由只确认 API v2 时间序列属性章节入口；浏览器读取没有返回正文，搜索索引也未找到该 URL 的独立内容。
- 同主题子页面 [Time Series Property basics](https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/time-series-properties/time-series-property-basics) 将其定义为包含一系列时间数据点的属性。API 章节提供按对象主键获取首点、末点和流式读取点的端点。
- 本卡只记录入口与可确认的章节结构，不把同主题子页面内容冒充成当前入口的正文。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| `Time Series Property` | 时间序列属性 | 章节中以对象属性形式关联的时间数据点序列。 |
| `Get First Point` | 获取首个数据点 | 读取时间序列属性首点的 API 操作。 |
| `Get Last Point` | 获取末个数据点 | 读取时间序列属性末点的 API 操作。 |
| `Stream Points` | 流式读取数据点 | 按查询范围读取时间序列点的 API 操作。 |

## 疑问与待验证项

- 当前入口路由无法单独读取正文；后续如能访问其页面，应复核是否存在与子页不同的章节级说明。
- 时间序列属性的数据源绑定、系列 ID、单位/插值配置与安全标记不在本入口页中；需参考时间序列设置和权限指南。

## 复刻启示

- Ontology 画布应把时间序列属性作为属性类型的一种特殊能力节点，并关联其对象、数据系列与读写/时间窗操作。
- 将时间序列点读取与普通对象字段读取分为不同访问接口；表达式画布如支持时间序列计算，应以有类型的时间范围、聚合和输出节点表示。
