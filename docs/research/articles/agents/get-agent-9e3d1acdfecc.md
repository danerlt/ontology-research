<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/aip-agents-v2-resources/agents/get-agent -->
<!-- 研读状态：已完成 -->

# Get Chatbot Studio Agent • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/aip-agents-v2-resources/agents/get-agent)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/aip-agents-v2-resources/agents
- 相关性：direct；Agent REST API v2 参考
- 官方更新时间：2026-11-12T17:46:46.917Z
- 目录核对时间：2026-11-14T14:53:27Z
- 产品状态：按页面现行表述整理；若标注 Preview，相关 API 可能变化。

## 英文原文短摘录（每个来源不超过 25 词）

> “If not specified, the latest published version will be returned.”

## 摘录译文

如果没有指定版本，将返回最新发布版本。

## 中文要点

- GET `/api/v2/aipAgents/agents/{agentRid}` 读取 Chatbot Studio Agent；可选 version 参数指定版本，省略时默认读取最新发布版本。
- 端点处于 Preview，需传 `preview=true`；第三方 OAuth 客户端需要 `api:aip-agents-read` 操作 scope。
- 响应含 RID、版本、元数据和可选参数映射；参数描述 Agent 在 Chatbot Studio application state 中配置的变量，可用于提示词定制和行为控制。
- 若没有发布版本且又未指定版本，会返回明确错误；Agent 或指定版本不存在则返回 404。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| metadata | 元数据 | 显示名、描述、建议提示等 Agent 信息。 |
| parameters | 参数映射 | 提示词可用的 Agent 变量及其类型/名称。 |
| latest published version | 最新发布版本 | 未指定版本时的读取默认值。 |

## 疑问与待验证项

- 参数是否允许写入、其访问级别和具体类型需检查完整响应 schema；不能只依赖显示名称。
- “latest”绑定发布时点还是查询时点，本页只说明默认取最新已发布版本。

## 复刻启示

- 运行 Agent 前把选定的发布版本固化进会话记录，保证后续可追溯和复现。
- 把参数 schema 作为 Agent 发布契约的一部分，在调用前进行类型校验，并避免让敏感参数进入普通提示词日志。
