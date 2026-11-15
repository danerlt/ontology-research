<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/time-series-properties/stream-points -->
<!-- 研读状态：已完成 -->

# Stream Points • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/time-series-properties/stream-points)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/v2/ontologies-v2-resources
- 相关性：direct；Ontology REST API v2 时间序列数据点流式读取
- 官方更新时间：2026-11-12T17:46:46.921Z
- 目录核对时间：2026-11-14T14:57:57Z
- 产品状态：本页未标注 Preview

## 英文原文短摘录（每个来源不超过 25 词）

> “ARROW is more efficient than JSON at streaming a large sized response.”

## 摘录译文

流式传输大型响应时，ARROW 比 JSON 更高效。

## 中文要点

- 端点：`POST /api/v2/ontologies/{ontology}/objects/{objectType}/{primaryKey}/timeseries/{property}/streamPoints`；第三方 OAuth 读取范围为 `api:ontologies-read`。
- 可选 `format` 为 `JSON` 或 `ARROW`，默认 JSON；页面建议大响应使用 ARROW。成功响应 schema 写为 `body: string`，实际二进制流解码应依 SDK/协议确认。
- 请求体 `range` 可选，支持绝对或相对时间范围；`aggregate` 也可选，但本页摘要未展开其字段结构。路径中的对象、主键和属性 API 名确定查询目标。
- 页面未列出 `branch` 参数；不要把其他序列端点的分支行为套用到这里。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Stream Points | 流式读取数据点 | 返回时间序列属性中的多个点 |
| Absolute range | 绝对时间范围 | 由明确时间戳界定的查询窗口 |
| Relative range | 相对时间范围 | 相对于当前时间表达的窗口 |
| ARROW | Arrow 格式 | 大型序列响应的二进制列式格式 |

## 疑问与待验证项

- `aggregate` 可选结构及聚合类型、分组与输出粒度需查看完整请求 schema；不要从首末点端点推断。
- JSON/ARROW 对应的 Content-Type、流边界和客户端反序列化 API 未在摘录中完整说明。
- 未提供范围上限、输出大小限制和空窗口响应约定。

## 复刻启示

- 时间序列面板提供时间窗和聚合选项；大数据量优先用列式格式或分页流，不把整个历史序列放进对象详情 JSON。
- 结果需携带时间范围、聚合参数和属性 API 名作为可复核上下文，绘图标注查询窗口和采样数据来源。
- 若做派生属性推理，区分静态链接遍历与按窗口聚合的时序计算，并在解释轨迹中注明所用时间范围。
