<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/aip-agents-v2-resources/agents/list-sessions-for-agents -->
<!-- 研读状态：已完成 -->

# List Sessions For Chatbot Studio Agents • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/aip-agents-v2-resources/agents/list-sessions-for-agents)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/aip-agents-v2-resources/agents
- 相关性：direct；Agent REST API v2 参考
- 官方更新时间：2026-11-12T17:46:46.917Z
- 目录核对时间：2026-11-14T14:53:27Z
- 产品状态：按页面现行表述整理；若标注 Preview，相关 API 可能变化。

## 英文原文短摘录（每个来源不超过 25 词）

> “Sessions are returned in order of most recently updated first.”

## 摘录译文

会话按最近更新时间从新到旧返回。

## 中文要点

- GET `/api/v2/aipAgents/agents/allSessions` 返回当前调用用户可访问、且由该客户端创建的 Chatbot Studio Agent 会话，不等价于平台内所有用户的全局会话清单。
- 该预览端点要求 `preview=true`；文档列出的第三方 OAuth scope 是 `api:aip-agents-write`，虽端点本身为读取操作，授权要求应严格以文档为准。
- 默认每页最多 100 条，可用 pageSize 与 pageToken 分页；结果按最近更新时间降序。响应数据包括会话 RID、Agent RID/版本和会话元数据。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| session | 会话 | 一次 Agent 对话运行及其消息/状态容器。 |
| client-created session | 客户端创建的会话 | 该端点范围限定为由调用客户端创建的会话。 |
| api:aip-agents-write | Agent 写操作 scope | 该特定预览列表接口文档声明的 OAuth scope。 |

## 疑问与待验证项

- 为什么只读列举端点要求 write scope，本页没有解释；接入前应在目标环境验证实际授权设置。
- 文档表述为 calling user 与 accessible agents 的会话，实际 tenant/project 作用域还需由平台权限验证。

## 复刻启示

- 会话查询必须按项目、用户、Agent 权限过滤，不能将“能访问 Agent”推导为能查看所有会话。
- scope 命名与操作语义不一致时，应使用服务端能力映射和审计记录，避免前端误判为无权限或放宽授权。
