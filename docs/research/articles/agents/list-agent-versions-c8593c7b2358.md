<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/v2/aip-agents-v2-resources/agent-versions/list-agent-versions -->
<!-- 研读状态：已完成 -->

# List Chatbot Studio Agent Versions • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/v2/aip-agents-v2-resources/agent-versions/list-agent-versions)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/v2/aip-agents-v2-resources
- 相关性：direct；Agent REST API v2 参考
- 官方更新时间：2026-11-12T17:46:46.917Z
- 目录核对时间：2026-11-14T14:56:05Z
- 产品状态：预览（Preview；请求需显式启用 `preview=true`）

## 英文原文短摘录（每个来源不超过 25 词）

> “Versions are returned in descending order, by most recent versions first.”

## 摘录译文

版本按最近发布优先，以降序返回。

## 中文要点

- 端点分页列出指定 Agent 的全部版本，按最近版本优先排列。
- 可使用 pageSize/pageToken 续页，响应返回 AgentVersion 列表与 nextPageToken；Agent RID 不存在时返回 AgentNotFound。
- 接口为 Preview，需 `preview=true` 与 `api:aip-agents-read`；文档未给出 pageSize 上限。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Descending order | 降序 | 较新 Agent 版本排在前面 |
| Page token | 分页令牌 | 从上一页继续读取版本列表 |
| AgentVersion | Agent 版本资源 | 包含版本号与版本语义结构 |

## 疑问与待验证项

- 同一发布时间内的排序是否稳定，页面未说明；客户端应使用版本号作为二级排序。
- 版本发布状态以列表项是否出现表达，是否还包含已撤回版本需要核对返回 schema。

## 复刻启示

- 版本选择器按 API 顺序呈现并保留分页，运行记录固定引用选定版本。
- 对 Agent 管理面板，需分别显示草稿、已发布和历史版本；列表端点当前只描述版本枚举，不足以推导所有状态。
