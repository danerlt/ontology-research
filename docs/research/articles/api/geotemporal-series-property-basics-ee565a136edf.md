<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/geotemporal-series-properties/geotemporal-series-property-basics -->
<!-- 研读状态：已完成 -->

# Geotemporal Series Property basics • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/geotemporal-series-properties/geotemporal-series-property-basics)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/v2/ontologies-v2-resources
- 相关性：direct；本体时空序列属性概念定义
- 官方更新时间：2026-11-12T17:46:46.921Z
- 目录核对时间：2026-11-14T14:56:50Z
- 产品状态：基础概念页未标注 Preview

## 英文原文短摘录（每个来源不超过 25 词）

> “A Geotemporal Series property is a property that contains a series of time-based geographic positions.”

## 摘录译文

时空序列属性是一种包含按时间排列的地理位置序列的属性。

## 中文要点

- 该属性保存对象关联的一串时态地理位置，而不是单一坐标或对象到对象的链接。
- 官方加载接口说明每个条目都按 `OntologyObjectV2` 类似结构返回属性映射；`time` 与 `position` 始终包含，其他如 `speed`、`heading` 可按请求选择，并取决于底层集成是否提供。
- 概念页未规定坐标系、采样间隔、排序、压缩、轨迹精度或冷/热存储策略；这些属于连接器和专用 API 的约束。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Geotemporal Series property | 时空序列属性 | 保存时间化地理位置观测的对象属性 |
| Geographic position | 地理位置 | 轨迹点的空间位置 |
| Time-based series | 时间序列 | 按时间索引的多个观测值 |
| Geotemporal entry | 时空条目 | 时间、位置以及可用的附加属性 |

## 疑问与待验证项

- 位置值采用何种坐标参考系统、单位和精度，本页未说明；不能把示例经纬度推广到任意集成。
- 当某项附加元数据在一部分条目中缺失时，响应如何表达未说明；文档提示底层集成不提供的字段会被省略。
- 本概念页没有给出 API 生命周期或 Preview 状态，读取行为应以加载端点卡为准。

## 复刻启示

- 类型系统为时空序列提供独立数据类型，并将时间戳、坐标与动态属性作为一条观测，而不是将其压平为字符串或普通关系。
- 画布节点可显示“时空序列属性”图标，检查器提供地图、时间范围和附加字段选择；数据缺失与“属性无值”应区分。
- 对空间坐标系统、采样密度及轨迹保留等策略应由集成配置定义并可见，避免用 schema 概念页无法支持的默认假设。
