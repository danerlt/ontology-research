<!-- 页面 URL：https://www.palantir.com/docs/zh/foundry/time-series/time-series-properties-use-case-ontology -->
<!-- 研读状态：已完成 -->

# 时间序列 • Time series property use case • 使用 Ontology Manager 为 Object 添加时间序列属性 • Palantir

- 英文来源：[现行英文原文](https://www.palantir.com/docs/foundry/time-series/time-series-properties-use-case-ontology)
- 官方中文来源：[官方中文页（AIP 机器翻译）](https://www.palantir.com/docs/zh/foundry/time-series/time-series-properties-use-case-ontology)
- 页面语言：中文（官方机器翻译，准确性未验证）
- 主题栏目：time-series
- 相关性：direct；在普通本体对象类型上挂接时序序列
- 官方更新时间：2026-11-12T17:46:46.929Z
- 目录核对时间：2026-11-14T15:01:30Z
- 产品状态：可为对象类型配置多个 Time series property；文档假设每个对象都有对应序列集

## 英文原文短摘录（不超过 25 词）

> “You can add as many time series properties to the object type as necessary”

## 摘录译文

可以按需为对象类型添加任意数量的时间序列属性。

## 中文要点

- 本指南把 Pipeline Builder 创建的时间序列同步与 Ontology Manager 中的对象类型能力连接起来。
- 在对象类型的 Capabilities 页签添加 Time series property：选择已有属性作为序列属性，可设为默认序列属性，再选择对应的 time series sync。
- 示例为 Carrier、Route、Airport 对象类型挂接 Daily Count、平均到达延误和平均离开延误三条序列；Route、Airport 需分别重复配置。
- 默认时序属性可自动出现在 Quiver；之后可在 Workshop 和 Quiver 中以业务对象为入口查看其时序数据。
- 文档明确假设每个对象始终关联一个 time series set，并建议先判断应使用普通 time series object type 还是 sensor object type。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Time series property | 时间序列属性 | 在本体对象类型能力中配置的时序数据入口 |
| time series sync | 时间序列同步 | 将流水线时序输出接入平台时序后端的资源 |
| default time series property | 默认时间序列属性 | 自动显示到 Quiver 的首选序列 |
| time series set | 时间序列集 | 与业务对象关联的时序序列集合 |

## 疑问与待验证项

- 文档对“每个对象都有时序集”的假设是否适用于可选/缺失序列的数据源，需结合空序列行为确认。
- 普通时序属性与 Sensor object type 的选型标准链接到另一指南；高基数、多测点对象应按关联模型判断。
- 数据授权、时序窗口、插值、存储策略不在此页展开，不能只凭添加属性就推断其安全与查询语义。

## 复刻启示

- 对象 schema 可声明一个或多个时序资源绑定；绑定关系同时记录对应属性、同步资源、默认展示项和来源系统。
- 画布应将业务对象与时序数据源用专用边连接，并在检查器呈现序列 ID、默认项和同步状态。
- 时序能力应与普通链接属性区分，支持在对象详情直接进入时间范围/聚合分析界面。