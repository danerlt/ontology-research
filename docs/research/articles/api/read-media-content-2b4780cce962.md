<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/media-reference-properties/read-media-content -->
<!-- 研读状态：已完成 -->

# Read Media Content • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/media-reference-properties/read-media-content)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/v2/ontologies-v2-resources
- 相关性：direct；Ontology REST API v2 媒体引用内容读取
- 官方更新时间：2026-11-12T17:46:46.921Z
- 目录核对时间：2026-11-14T14:56:55Z
- 产品状态：Preview；请求必须设置 `preview=true`

## 英文原文短摘录（每个来源不超过 25 词）

> “Supports a single byte range specified by the `Range` header as `bytes=start-end` or `bytes=start-`.”

## 摘录译文

支持通过 `Range` 请求头指定一个字节范围，格式为 `bytes=start-end` 或 `bytes=start-`。

## 中文要点

- 端点：`GET /api/v2/ontologies/{ontology}/objects/{objectType}/{primaryKey}/media/{property}/content`。读取对象 MediaReference 属性所指媒体的内容；OAuth 范围为 `api:ontologies-read`。
- 这是 Preview 接口，需 `preview=true`。可选参数包含 SDK 包 RID/版本、`branch`、实验性 `transactionId` 和 `scenarioRid`。
- 支持单个 Range 区间：可满足时返回 `206 Partial Content` 及 `Content-Range`、`Accept-Ranges` 和区间内容长度；不可满足时返回 `416` 与总长度范围标记、空响应体。
- 不支持或格式错误的 Range 会被忽略，并返回完整内容 `200 OK`。响应 schema 把 body 描述为内容流。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Range header | Range 请求头 | 请求读取部分媒体字节 |
| Partial Content | 部分内容 | 满足单段 Range 时的 HTTP 206 响应 |
| Content-Range | 内容范围 | 描述返回字节区间或总长度 |
| Transaction ID | 交易 ID | 实验性本体交易读取上下文 |

## 疑问与待验证项

- endpoint 为 Preview，后续可能修改或移除；`transactionId` 页面明确标为 experimental，相关工作流未必全部支持。
- 媒体引用基础页限制对象加载支持的引用来源；此端点对各类 MediaReference 是否都可读需根据具体引用确认。
- 认证 scope 与媒体对象授权、响应缓存和跨分支内容一致性需结合其他授权文档验证。

## 复刻启示

- 媒体预览组件可采用 HTTP Range 加载局部内容，按 206/416/200 更新播放器或查看器状态，并保留明确的预览功能标识。
- 连接器服务应遵循单范围边界；遇到多段或非法 Range 时按契约处理，不要自作主张拼接多段媒体响应。
- 预览读取需把对象属性和媒体内容策略绑定，并将 `branch`、scenario/transaction 上下文纳入缓存键和审计信息。
