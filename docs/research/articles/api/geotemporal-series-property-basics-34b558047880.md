<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/geotemporal-series-properties/geotemporal-series-property-basics -->
<!-- 研读状态：已完成 -->

# Geotemporal Series Property basics • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/geotemporal-series-properties/geotemporal-series-property-basics)
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

- 该属性提供对象的时间索引地理位置序列，可用于车辆/飞机等对象的位置历史。
- 概念页不定义读取性能或数据保留；对应数据需通过时空序列专用接口分时间范围分页加载。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| time-based geographic position | 带时间的地理位置 | 每个序列条目的核心时间/空间数据。 |
| series property | 序列属性 | 在对象上引用时空点集合的属性。 |

## 疑问与待验证项

- 基础页未限定点数、时间分辨率和坐标系。
- 页面未说明轨迹数据与对象当前位置字段是否存在一致性规则。

## 复刻启示

- 图谱实例视图提供轨迹时间轴/地图联动，但按时间窗和页大小懒加载点数据。
- 区分对象当前状态属性与历史 geotemporal series，避免将两者混作一条边。
