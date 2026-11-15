<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/aip-agents-v2-resources/agent-versions/list-agent-versions -->
<!-- 研读状态：已完成 -->

# List Chatbot Studio Agent Versions • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/aip-agents-v2-resources/agent-versions/list-agent-versions)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/aip-agents-v2-resources/agent-versions
- 相关性：direct；Agent REST API v2 参考
- 官方更新时间：2026-11-12T17:46:46.917Z
- 目录核对时间：2026-11-14T14:53:22Z
- 产品状态：按页面现行表述整理；若标注 Preview，相关 API 可能变化。

## 英文原文短摘录（每个来源不超过 25 词）

> “Versions are returned in descending order, by most recent versions first.”

## 摘录译文

版本按降序返回，最新版本排在最前面。

## 中文要点

- GET `/api/v2/aipAgents/agents/{agentRid}/agentVersions` 列出某个 Agent 的版本，并按最新优先的降序排列。
- 端点处于 Preview，需带 `preview=true`；第三方 OAuth 客户端需要 `api:aip-agents-read` 操作 scope。
- 响应使用 `data` 数组与可选 `nextPageToken`；下一页请求应原样传回上页 token，首请求不带 token。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| pageSize | 页大小 | 控制一次请求的结果数量。 |
| pageToken | 分页令牌 | 用上一页的 nextPageToken 请求后续页。 |
| nextPageToken | 下一页令牌 | 无更多结果时为空或不存在。 |

## 疑问与待验证项

- 页面没有给出 pageSize 最大值，客户端需遵从 API 错误提示或平台通用限制。
- “最新”按发布时间还是版本创建时间排序，本页只说明降序和最近版本优先。

## 复刻启示

- 版本列表 API 应实现游标分页并保留稳定排序，避免依赖某一页返回的固定数量。
- 界面可将最新已发布版本置顶，但必须标记其状态和来源，避免将草稿误当作可运行发布版。
