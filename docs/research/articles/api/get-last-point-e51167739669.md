<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/time-series-properties/get-last-point -->
<!-- 研读状态：已完成 -->

# Get Last Point • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/time-series-properties/get-last-point)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/v2/ontologies-v2-resources
- 相关性：direct；Ontology REST API v2 时间序列末点查询
- 官方更新时间：2026-11-12T17:46:46.921Z
- 目录核对时间：2026-11-14T14:57:57Z
- 产品状态：本页未标注 Preview

## 英文原文短摘录（每个来源不超过 25 词）

> “Get the last point of a time series property.”

## 摘录译文

获取时间序列属性的最后一个数据点。

## 中文要点

- 端点：`GET /api/v2/ontologies/{ontology}/objects/{objectType}/{primaryKey}/timeseries/{property}/lastPoint`。定位参数与首点端点相同，读取时间序列尾部的单个点。
- OAuth 读取范围为 `api:ontologies-read`；可选 `sdkPackageRid` 与 `sdkVersion`。
- 响应 `TimeSeriesPoint` 由 ISO 8601 `time` 和 `value` 组成；值定义为 enum 字符串或 double 数字。
- 页面未提供 `branch` 查询参数，也没有保证末点的实时新鲜度、空序列错误语义或与其他读接口的快照一致性。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Last point | 末点 | 时间序列当前可读数据中的最后一点 |
| TimeSeriesPoint | 时间序列数据点 | 含时间戳和值的对象 |
| ISO 8601 timestamp | ISO 8601 时间戳 | 表示采样时间 |
| Value | 值 | enum 字符串或 double 数值 |

## 疑问与待验证项

- 末点按事件时间、采集时间还是数据源定义的排序键确定，需要通过集成文档确认。
- 页面没有说明空序列、权限不足和链接缺失的错误响应。
- `branch` 不在本页列出的参数中；不能假设它读取草稿分支，需实测或向 API schema 复核。

## 复刻启示

- 将“最新本体对象值”与“时序最后观测”标成不同信息来源，展示 `time` 让操作者判断陈旧程度。
- 末点查询的用途是轻量取样；长时间范围分析应使用流式读取或聚合 API，避免逐对象查询产生高请求量。
- 对画布推理中的时序派生值，将采样时间和所用数据源纳入解释路径，不能只显示一个数值。
