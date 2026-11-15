<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/v2/aip-agents-v2-resources/agent-versions/get-agent-version -->
<!-- 研读状态：已完成 -->

# Get Chatbot Studio Agent Version • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/v2/aip-agents-v2-resources/agent-versions/get-agent-version)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/v2/aip-agents-v2-resources
- 相关性：direct；Agent REST API v2 参考
- 官方更新时间：2026-11-12T17:46:46.917Z
- 目录核对时间：2026-11-14T14:56:05Z
- 产品状态：预览（Preview；请求需显式启用 `preview=true`）

## 英文原文短摘录（每个来源不超过 25 词）

> “The semantic version of the Chatbot Studio Agent, formatted as “majorVersion.minorVersion”.”

## 摘录译文

Chatbot Studio Agent 的语义化版本，格式为“主版本.次版本”。

## 中文要点

- 端点按 Agent RID 和版本字符串读取某个版本详情；版本号仅规定主版本与次版本，例如 `1.0`。
- 返回版本字符串和拆分后的 major/minor 结构；接口为 Preview，需 `preview=true` 与 `api:aip-agents-read`。
- 不指定版本读取最新已发布 Agent 时，如没有已发布版本会返回错误；无效版本号会返回 InvalidAgentVersion。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Agent RID | Agent 资源标识符 | 定位 Chatbot Studio Agent |
| Version string | 版本字符串 | major.minor 格式 |
| Latest published version | 最新已发布版本 | 默认读取的已发布版本 |

## 疑问与待验证项

- 仅有 major/minor 两段，补丁版本、构建号和预发布标签是否支持，格式定义不支持或至少未说明。
- 文档示例的 `string` 为 `1.0`，拆分字段示例却是 major=1、minor=2，示例数据不一致，需以实际响应核验。
- 端点的返回结构只有版本信息，实际 Agent 配置仍需通过 Get Agent 获取。

## 复刻启示

- 发布时保存不可变版本快照，执行/会话明确记录使用的 agentVersion，保证排错和回放可追溯。
- 部署界面校验版本格式，并把“没有已发布版本”和“版本不存在”作为不同错误状态呈现。
