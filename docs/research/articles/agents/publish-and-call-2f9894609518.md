<!-- 页面 URL：https://www.palantir.com/docs/foundry/agents/publish-and-call -->
<!-- 研读状态：已完成 -->

# Pro-code agents • Core concepts • Publish and call a pro-code agent • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/agents/publish-and-call)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：agents
- 相关性：direct；Agent 文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:05:32Z
- 产品状态：发布时必须选择 Ontology binding；Agent 作为异步 function 暴露，推荐从 Automate 触发。

## 英文原文短摘录（每个来源不超过 25 词）

> “Every pro-code agent is published with an Ontology binding and an agent API name.”

## 摘录译文

每个 pro-code Agent 发布时都带有本体绑定和 Agent API 名称。

## 中文要点

- 发布把 Agent API name 与指定本体绑定，并将 Agent 注册成 function；可从 Workshop、OSDK 和 Ontology action/function effect 调用。
- Agent function 异步运行，不受同步 function 五分钟限制，但返回 Void；不支持 streaming 或批量调用。
- Agent 应把 transcript/结果写回本体对象；调用参数传对象主键，再由 Agent 内部重新读取。
- Automate 触发时执行主体可能是触发用户或 Automation 的 service user。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Ontology binding | 本体绑定 | 决定 Agent 通过范围权限可访问的本体。 |
| agent API name | Agent API 名称 | 调用 Agent function 时使用的稳定标识。 |
| function effect | 函数效果 | 在 Automate/应用中触发异步函数的动作配置。 |

## 疑问与待验证项

- - Void 返回要求提供运行状态、结果对象、失败原因和执行 ID，便于调用方确认结果。
- - 用户与 service user 两类执行身份具有不同审计含义，应记录触发来源和实际身份。

## 复刻启示

- - 建立发布版本、绑定本体、API 名称、参数 schema、异步运行和结果对象的引用。
- - 使用后台任务队列，提供运行记录、幂等键、重试策略；结果写回前再次校验对象权限。
