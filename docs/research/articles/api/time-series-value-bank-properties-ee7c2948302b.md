<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/time-series-value-bank-properties -->
<!-- 研读状态：已完成 -->

# Time Series Value Bank Property basics • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/time-series-value-bank-properties)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/ontologies-v2-resources/time-series-value-bank-properties
- 相关性：direct；Ontology REST API v2 参考
- 官方更新时间：2026-11-12T17:46:46.921Z
- 目录核对时间：2026-11-14T14:54:35Z
- 产品状态：基础概念页；目标组根路由未能由文档读取端打开，定义依据为官方同组子页

## 英文原文短摘录（每个来源不超过 25 词）

> “A Time Series Value Bank property is a property that contains a series of time based data points.”

摘录来源：[Time Series Value Bank Property basics](https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/time-series-value-bank-properties/time-series-value-bank-property-basics)（可读取的官方同组子页）。

## 摘录译文

Time Series Value Bank 属性是一种包含一系列基于时间的数据点的属性。

## 中文要点

- 可读取的同组官方子页将其定义为包含时间序列数据点的属性。配套 API 提供读取最新值及按范围流式读取整段数据的操作。
- `Get Latest Value` 返回一个时间戳和值；文档列出的值类型包括枚举字符串、双精度数或地理点。`Stream Values` 可读取全部点，并涵盖 geotime series 引用。
- 本体管理实现需要将普通标量属性与时序值引用区分开：画布/schema 显示时序绑定，实例视图负责查询数据点；不应把整个序列误当成对象行内的简单数组字段。
- 组根路由在本次读取中不可访问，本文定义和用途由链接子页及同组读取 API 交叉确认；其他底层存储结构没有在这里推断。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Time Series Value Bank property | 时间序列值库属性 | 指向按时间组织的数据点的本体属性 |
| data point | 数据点 | 含时间与对应值的时序记录 |
| geotime series | 地理时序 | 带地理位置/轨迹语义的时序引用 |
| time range | 时间范围 | 读取流时可提供的绝对或相对范围 |

## 疑问与待验证项

- 可读基础页没有说明 Value Bank 的内部物理模型、保留策略、采样/压缩方式或时区处理，需要以具体 Foundry 能力和部署配置验证。
- 时序属性值类型包含哪些枚举、double、geopoint 以外的情况，当前两个读取 API 的说明不足以完整界定。

## 复刻启示

- schema 中单独记录时序属性绑定和类型，不把数据点冗余写入对象主记录；对时序读取提供最新值与时间窗流接口。
- 在流程图式画布中，将对象类型到时序属性建模为带时间语义的属性端口；提供实时折线/地理轨迹预览，并把时间范围作为试算上下文。
- 派生属性若读取时序值，应明确是“最新点”还是“时间窗聚合”，把时间窗、聚合函数与来源时间戳纳入解释轨迹及版本签名。
