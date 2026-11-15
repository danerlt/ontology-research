<!-- 页面 URL：https://www.palantir.com/docs/zh/foundry/time-series/sensor-object-end-to-end-ontology -->
<!-- 研读状态：已完成 -->

# 时间序列 • Sensor object types use case • 使用Ontology Manager创建传感器Object类型 • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/time-series/sensor-object-end-to-end-ontology)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/time-series/sensor-object-end-to-end-ontology)
- 页面语言：中文（官方机器翻译，准确性未验证）
- 主题栏目：time-series
- 相关性：direct；传感器对象、根对象链接和时序能力配置
- 官方更新时间：2026-11-12T17:46:46.929Z
- 目录核对时间：2026-11-14T15:01:29Z
- 产品状态：示例需要 Sensor object type 与 root object type，并在传感器能力中绑定时序同步

## 英文原文短摘录（不超过 25 词）

> “This guidance explains how to use Ontology Manager to create a sensor object type and link it to a root object type.”

## 摘录译文

本指南说明如何使用 Ontology Manager 创建传感器对象类型并将其链接到根对象类型。

## 中文要点

- 示例用 Sensors 数据集创建 Flight Sensor：以 `unique_sensor_flight_id` 作为主键、Title 列作为可读标题，可同步数据源列。
- 在 Sensor 对象类型 Capabilities 中选择现有 Series Id 属性作为时序属性，设为 Quiver 默认项，并绑定 Pipeline Builder 创建的 Sensor Readings 同步。
- 创建 Flight Sensor→Flight 链接：传感器端基数 Many、Flight 端 One；以 `flight_id` 外键映射到根 Flight。
- 启用 sensor object type 能力，选择刚创建的 Flight→Flight Sensor 链接；用 Series Name 属性提供应用显示的时序名称，并配置单位。
- 分类值、内部插值是按用例选择的可选属性；保存后 Sensor 与 Flight 对象可在 Workshop、Quiver 使用。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| sensor object type | 传感器对象类型 | 每个传感器/测点作为可查询本体对象 |
| root object type | 根对象类型 | 传感器所归属的业务实体类型，例如 Flight |
| Series Name | 序列名称 | 在应用中呈现传感器时序数据的名称字段 |
| internal interpolation | 内部插值 | 使应用能够推断相邻数据点之间序列值的能力 |

## 疑问与待验证项

- 文档示例中 Sensor 侧 `flight_id` 与 Flight 主键/外键表述容易混淆，实施时应核对 link type 的准确方向和两端主键。
- 是否需要 Is categorical 与单位依赖时序值类型；单位换算和枚举语义未在本页完整说明。
- 插值只说明可推断相邻点之间的值，不等同于原始采样数据；图表应区分插值结果和源点。

## 复刻启示

- 在本体画布中将 Sensor 作为独立对象类型节点，显式显示它到业务根对象的一对多/多对一关系和数据来源。
- 时序绑定检查器应显示系列 ID 属性、同步资源、展示名称、单位、分类标记和插值策略。
- 传感器对象详情同时提供对象属性、上级业务对象和时间序列视图，便于从模型图追到运行数据。