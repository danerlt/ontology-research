<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/geotemporal-series-properties -->
<!-- 研读状态：已完成 -->

# Geotemporal Series Property basics • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/geotemporal-series-properties)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/v2/ontologies-v2-resources
- 相关性：direct；Ontology REST API v2 时空序列属性分组入口
- 官方更新时间：2026-11-12T17:46:46.921Z
- 目录核对时间：2026-11-14T14:56:47Z
- 产品状态：分组入口未标注 Preview；加载端点为 Preview

## 英文原文短摘录（每个来源不超过 25 词）

> “Geotemporal Series Properties”

## 摘录译文

时空序列属性。

## 中文要点

- 该 URL 是 Geotemporal Series 属性的 API 分组入口，分组路由未能独立读取正文。官方 v2 导航包含“Geotemporal Series Property basics”和“Load Geotemporal Series Entries”两页。
- 基础页将其定义为随时间记录地理位置的一组观测；加载端点按指定时间范围返回对象的序列条目，并在条目中包含时间、位置及可选属性。
- 与普通链接不同，时空序列表示对象随时间变化的位置/观测；不能把每个采样点误建成静态业务对象链接。具体加载接口目前为 Preview，且仅有冷存储的集成不受支持。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Geotemporal series | 时空序列 | 按时间索引的地理位置观测集合 |
| Position | 位置 | 每个序列观测中的地理坐标 |
| Load entries | 加载条目 | 按对象属性和时间范围读取采样记录 |
| Preview | 预览功能 | 对应加载端点可能变更或移除 |

## 疑问与待验证项

- 分组入口信息依据官方[v2 Ontology API 导航](https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources)；基础定义和端点行为以[属性基础页](https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/geotemporal-series-properties/geotemporal-series-property-basics)及加载页为准。
- 采样频率、轨迹保留、空间坐标系和数据排序保证需要结合具体集成验证。
- Preview 加载能力不支持仅冷存储集成；实时/历史组合如何分页与排序，仍需通过具体连接验证。

## 复刻启示

- 画布将时空序列作为对象上的时态属性/时间流入口，提供时间轴与地图联合视图；把历史采样点显示成动态轨迹，避免它和类型图静态链接混淆。
- 查询 API 应显式要求半开区间时间窗、可选列与分页令牌，并清楚提示预览状态或底层存储不兼容。
- 时空计算属于带时间/位置过滤的专用数据查询；不应假称普通一至三跳本体链接遍历已经完成轨迹推理。
