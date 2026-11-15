<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/v2/aip-agents-v2-resources/agents/list-sessions-for-agents -->
<!-- 研读状态：已完成 -->

# List Sessions For Chatbot Studio Agents • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/v2/aip-agents-v2-resources/agents/list-sessions-for-agents)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/v2/aip-agents-v2-resources
- 相关性：direct；Agent REST API v2 参考
- 官方更新时间：2026-11-12T17:46:46.917Z
- 目录核对时间：2026-11-14T14:56:08Z
- 产品状态：预览（Preview；请求需显式启用 `preview=true`）

## 英文原文短摘录（每个来源不超过 25 词）

> “List all conversation sessions between the calling user and all accessible Agents that were created by this client.”

## 摘录译文

列出当前用户与其可访问 Agent 之间、由此客户端创建的所有会话。

## 中文要点

- 会话列表限于调用用户可访问的 Agent，且只包含由当前 client 创建的会话；按最近更新时间倒序。
- pageSize 默认 100，最大 100；使用 pageToken 继续读取。返回的会话元数据含标题、消息数、创建/更新/预计过期时间，并关联 Agent RID 与版本。
- 该端点为 Preview，且需要 `api:aip-agents-write` scope。虽然是 GET 列表，仍需写权限级 scope；无权时返回 403。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Session | 会话 | 用户与 Agent 的一段对话 |
| Client-scoped | 客户端范围 | 仅列由当前 client 创建的会话 |
| Estimated expiry | 预计过期时间 | 会话预期失效时间 |
| AIP Agents write scope | Agent 写入权限范围 | 此列表接口要求的 OAuth scope |

## 疑问与待验证项

- 客户端身份如何与会话创建时的身份绑定，涉及多用户共享 client 的安全边界，需要查认证文档。
- 过期时间是硬删除、逻辑失效还是可续期，页面没有说明。

## 复刻启示

- 会话存储至少绑定 tenant/project、agentRid、agentVersion、userId、clientId 与有效期，查询时执行这些范围限制。
- 不要把会话标题或计数当作完整对话内容；对话读取、保留期限和删除机制须单独授权与实现。
