<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/media-reference-properties/read-media-content -->
<!-- 研读状态：已完成 -->

# Read Media Content • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/media-reference-properties/read-media-content)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/ontologies-v2-resources/media-reference-properties
- 相关性：direct；Ontology REST API v2 参考
- 官方更新时间：2026-11-12T17:46:46.921Z
- 目录核对时间：2026-11-14T14:53:49Z
- 产品状态：按当前 API 参考整理；列表一致性、分支和部分媒体能力有明确限制。

## 英文原文短摘录（每个来源不超过 25 词）

> “Supports a single byte range specified by the `Range` header as `bytes=start-end` or `bytes=start-`.”

## 摘录译文

支持通过 `Range` 请求头指定一个字节区间。

## 中文要点

- GET `/api/v2/ontologies/{ontology}/objects/{objectType}/{primaryKey}/media/{property}/content` 读取对象媒体引用内容；端点处于 Preview，需显式传 `preview=true`。
- 支持一个 HTTP byte range：有效范围返回 206 和 Content-Range；无效范围返回 416；格式错误或不支持的范围会被忽略并返回完整内容 200。
- 可在 branch 或 scenario 上读取，transactionId 支持仍属实验；OAuth scope 为 `api:ontologies-read`。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Range header | 范围请求头 | 按字节区间请求部分媒体内容。 |
| 206 Partial Content | 部分内容响应 | 成功读取有效字节范围时的状态码。 |
| 416 Range Not Satisfiable | 范围不可满足 | 请求字节范围超过媒体内容边界时的状态码。 |

## 疑问与待验证项

- 接口处于 Preview；调用方需处理无效 Range 与完整内容返回间的状态差异。
- scenario/branch 指定后媒体内容是否与本体属性快照完全一致，要结合平台行为验证。

## 复刻启示

- 媒体预览组件使用 Range 做渐进加载，同时确保错误范围不会意外触发重复下载整份大文件。
- 把 Preview 与 scenario 上下文写入请求日志/调试信息，并受媒体对象权限约束。
