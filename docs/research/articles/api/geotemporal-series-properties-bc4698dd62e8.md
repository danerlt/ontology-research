<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/geotemporal-series-properties -->
<!-- 研读状态：已完成 -->

# Geotemporal Series Property basics • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/geotemporal-series-properties)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/ontologies-v2-resources/geotemporal-series-properties
- 相关性：direct；Ontology REST API v2 参考
- 官方更新时间：2026-11-12T17:46:46.921Z
- 目录核对时间：2026-11-14T14:53:42Z
- 产品状态：目录页按版本化 API 规范页核对；涉及 Preview 的端点可能变化。

## 英文原文短摘录（每个来源不超过 25 词）

> “A Geotemporal Series property is a property that contains a series of time-based geographic positions.”

## 摘录译文

Geotemporal Series 属性保存一系列带时间的地理位置。

## 中文要点

- 该目录路由重定向到 `/geotemporal-series-properties/geotemporal-series-property-basics` 版本化规范页。
- 规范页只定义了时空序列属性的核心含义；读取时间范围内记录需用 Load Geotemporal Series Entries。
- 目录别名与基础页内容相同，作为 catalog URL 覆盖项保留。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Geotemporal Series | 时空序列 | 按时间索引的地理位置记录。 |
| position | 位置 | 序列中的地理坐标。 |

## 疑问与待验证项

- 概念页未指定坐标参考系、采样频率或存储保留策略。

## 复刻启示

- 时空序列应作为属性的专门类型建模，画布与实例查看器展示位置和时间维度。
- 避免把海量时序点全部作为单一对象普通字段加载。
