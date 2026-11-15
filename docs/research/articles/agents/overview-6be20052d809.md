<!-- 页面 URL：https://www.palantir.com/docs/foundry/agents/overview -->
<!-- 研读状态：已完成 -->

# Pro-code agents • Overview • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/agents/overview)
- 官方中文来源：目录中未发现对应中文页面
- 页面语言：英文
- 主题栏目：agents
- 相关性：direct；Agent 文档
- 官方更新时间：页面未提供
- 目录核对时间：2026-11-15
- 产品状态：Pro-code Agent 与 Agent Builder 并行；支持的 SDK/服务范围需按部署版本核对。

## 英文原文短摘录（每个来源不超过 25 词）

> “A pro-code agent is custom logic written in a Foundry code repository and published as a Foundry function.”

## 摘录译文

Pro-code Agent 是写在 Foundry 代码仓库中并以 Foundry 函数发布的自定义逻辑。

## 中文要点

- Pro-code Agent 使用第三方 Agent SDK 在代码仓库中构建，可对话推理并调用读取/写入工具；文档列出的 SDK 包括 Claude Agent SDK、OpenAI Agents SDK 和 Google ADK。
- 模板包含绑定本体的 OSDK 客户端、Ontology MCP 与 Palantir MCP 配置，以及定义 prompt、工具和响应流处理的 Agent 逻辑。
- 发布后 Agent 作为异步函数注册，绑定本体和 API 名称，可由 Workshop、OSDK、Ontology Actions 调用；推荐由 Automate 触发。Global Branching 支持 Agent 与本体/应用并行开发。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| pro-code agent | 代码型 Agent | 在代码仓库中编写并作为函数发布的 Agent。 |
| scoped permissions | 限定范围权限 | Agent 工具按调用身份获得受限权限上下文。 |
| ontology binding | 本体绑定 | 将发布的 Agent 函数关联到具体本体。 |

## 疑问与待验证项

- 文档所说的自动 scoped permissions 与具体 OAuth/运行时策略依赖平台环境；不能误认为 Agent 可绕过对象和动作权限。
- Global Branching 对不同工具的分支上下文并不完全一致，尤其 Palantir MCP 不支持全局分支，需以专项限制为准。

## 复刻启示

- 为自建 Agent 定义本体上下文、可用工具清单和权限主体；运行时按每次用户请求施加授权，Agent API 自身不应拥有无限制服务账号。
- 代码型 Agent 发布为可版本化资源并保留异步任务、函数调用、工具结果及执行状态，支持应用集成和审计。
