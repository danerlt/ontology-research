<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/v2/aip-agents-v2-resources/agents/get-agent -->
<!-- 研读状态：已完成 -->

# Get Chatbot Studio Agent • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/v2/aip-agents-v2-resources/agents/get-agent)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/v2/aip-agents-v2-resources
- 相关性：direct；Agent REST API v2 参考
- 官方更新时间：2026-11-12T17:46:46.917Z
- 目录核对时间：2026-11-14T14:56:07Z
- 产品状态：预览（Preview；请求需显式启用 `preview=true`）

## 英文原文短摘录（每个来源不超过 25 词）

> “If not specified, the latest published version will be returned.”

## 摘录译文

如果未指定版本，则返回最新已发布版本。

## 中文要点

- Get Agent 以 Agent RID 读取定义；可选 `version` 固定版本，省略时返回最新已发布版本。
- 响应包含 Agent RID、实例版本、metadata 与参数 schema；参数用于向提示传入自定义值以控制 Agent 行为。
- 端点为 Preview，需要 `preview=true` 与 `api:aip-agents-read`；如果没有发布版本且未指定版本会失败。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Metadata | 元数据 | 展示名称、描述、建议提示语等 |
| Parameter | 参数 | Agent 可在请求提示中读取的变量定义 |
| Published version | 已发布版本 | 省略 version 时的默认读取目标 |
| READ_ONLY | 只读访问 | 示例中的参数访问模式 |

## 疑问与待验证项

- 参数的访问控制枚举和运行时注入接口应与 Execute/Session 文档联合确认。
- 响应未展示完整对话/工具配置，不能只靠此读端点复现整个 Agent。

## 复刻启示

- Agent 运行配置固定到已发布版本；参数以声明式 schema 管理，应用调用时校验取值并限制敏感写入。
- 版本和参数变更应进入审计与分支评审；不要直接把未发布编辑态暴露给生产调用者。
