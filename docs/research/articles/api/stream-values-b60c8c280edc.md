<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/time-series-value-bank-properties/stream-values -->
<!-- 研读状态：已完成 -->

# Stream Values • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/time-series-value-bank-properties/stream-values)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/v2/ontologies-v2-resources
- 相关性：direct；Ontology REST API v2 Value Bank 时间序列流接口
- 官方更新时间：2026-11-12T17:46:46.921Z
- 目录核对时间：2026-11-14T14:58:00Z
- 产品状态：本页未标注 Preview

## 英文原文短摘录（每个来源不超过 25 词）

> “Stream all of the points of a time series property (this includes geotime series references).”

## 摘录译文

流式读取时间序列属性的全部数据点，其中也包括时空序列引用。

## 中文要点

- 端点：`POST /api/v2/ontologies/{ontology}/objects/{objectType}/{primaryKey}/timeseries/{property}/streamValues`。它面向时间序列支持的属性，也包括 geotime series 引用；OAuth 读取范围为 `api:ontologies-read`。
- 可选 `branch` 指定读取分支，省略时使用默认分支；还可附带生成 SDK 包 RID 与版本。
- 请求体中的 `range` 可选，支持绝对或相对范围；成功响应是 schema 标为 `body: string` 的流式结果。页面没有列出格式参数，因此不能假设与 Stream Points 的 JSON/ARROW 选择一致。
- 该 API 按对象、属性和可选范围读取多点值；与 Get Latest Value 只读取一个最新条目的使用目的不同。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Stream Values | 流式读取值 | 按属性读取完整时间序列点 |
| Geotime series reference | 时空序列引用 | 也包含在该读取端点支持范围中 |
| Range | 时间范围 | 请求体中的绝对/相对查询窗口 |
| Branch | 分支 | 指定本体读取上下文，默认分支可省略 |

## 疑问与待验证项

- body 的实际流协议、JSON/二进制编码、断开续读与背压机制未在本页解释。
- 请求体 schema 未在摘要展开范围联合各类型的字段；具体时间窗口单位需看完整定义。
- 与 `streamPoints` 的能力重叠点及两种端点对 value-bank/geotime 的边界，应按真实 schema 和 SDK 复核。

## 复刻启示

- 提供单点、首末点与全量流式读取等不同操作层级，让调用方按需请求而非每次扫描整段序列。
- 明确在本地 API 中规定时间窗、格式、分页/流控制和查询成本上限；不要从 Palantir 页面未说明的细节推断协议。
- Agent 只有在工具契约显式规定可取历史窗口和记录规模时才应使用完整流读取，避免无界读取扩大成本与敏感数据暴露。
