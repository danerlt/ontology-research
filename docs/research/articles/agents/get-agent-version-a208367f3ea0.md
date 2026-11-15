<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/aip-agents-v2-resources/agent-versions/get-agent-version -->
<!-- 研读状态：已完成 -->

# Get Chatbot Studio Agent Version • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/aip-agents-v2-resources/agent-versions/get-agent-version)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/aip-agents-v2-resources/agent-versions
- 相关性：direct；Agent REST API v2 参考
- 官方更新时间：2026-11-12T17:46:46.917Z
- 目录核对时间：2026-11-14T14:53:22Z
- 产品状态：按页面现行表述整理；若标注 Preview，相关 API 可能变化。

## 英文原文短摘录（每个来源不超过 25 词）

> “Get version details for a Chatbot Studio Agent.”

## 摘录译文

获取 Chatbot Studio Agent 的版本详情。

## 中文要点

- GET `/api/v2/aipAgents/agents/{agentRid}/agentVersions/{agentVersionString}` 按 Agent RID 与 major.minor 语义版本读取版本详情。
- 端点处于 Preview；请求需显式传 `preview=true`。OAuth 第三方客户端需 `api:aip-agents-read` 操作 scope。
- 响应包含版本字符串和 major/minor 结构；无效版本格式会返回参数错误，版本或 Agent 不存在会返回 404，无已发布版本时读取最新版本也会失败。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| agentRid | Agent 资源标识 | 标识在 Chatbot Studio 创建的 Agent。 |
| agentVersionString | Agent 版本字符串 | major.minor 格式的语义版本。 |
| preview=true | 预览开关 | 启用尚处预览阶段的 API 功能。 |

## 疑问与待验证项

- 本接口返回的 `version` 对象字段较少，不能据此假设它包含 Agent 配置完整快照。
- Preview 端点可能变化或移除；集成层应进行版本隔离并有稳定能力检查。

## 复刻启示

- 读取已发布 Agent 时要求调用者同时指定 Agent 与版本，必要时在请求校验中处理“无发布版本”错误。
- 把 preview API 封装在适配器后面，并把 API scope 映射到本系统的只读 Agent 版本权限。
