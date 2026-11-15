<!-- 页面 URL：https://www.palantir.com/docs/foundry/agents/build-agent-continue -->
<!-- 研读状态：已完成 -->

# Pro-code agents • How-to guides • Build a pro-code agent with Continue • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/agents/build-agent-continue)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：agents
- 相关性：direct；Agent 文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:05:35Z
- 产品状态：当前页面介绍用 Continue 和 Palantir MCP 在编辑器内辅助构建、配置和发布 pro-code Agent。

## 英文原文短摘录（每个来源不超过 25 词）

> “The resources you add also become available as OMCP tools.”

## 摘录译文

添加到 SDK 的资源也会成为 OMCP 工具。

## 中文要点

- 前提是已有基于 Agent 模板创建的仓库，并在编辑器安装 Palantir MCP 与 Continue 扩展。
- Continue 可根据自然语言提示修改 Agent prompt、参数和自定义工具，也能通过 Palantir MCP 管理 Agent 所需的本体资源并发布。
- 当 SDK 不存在时，Continue 会创建 SDK；添加对象/Action 类型后生成新 SDK 版本并安装到仓库。OMCP 工具目录由相同 SDK 资源形成，因此 SDK scope 变更会同步影响 Agent 可用的 OMCP 工具。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Continue | Continue 编辑器扩展 | 通过自然语言提示辅助构建 Agent 的开发工具。 |
| SDK scope | SDK 资源范围 | Agent SDK 中包含的对象类型和 Action 类型集合。 |
| OMCP tool | OMCP 工具 | 从当前 SDK 资源集合提供给 Agent 的本体工具。 |

## 疑问与待验证项

- 自然语言开发工具可能修改仓库或本体 SDK 范围；页面没有详细说明每项变更的自动权限检查与回滚要求。
- 发布操作仍受 Agent 绑定本体、权限范围及分支发布规则约束；开发助手不能代替发布审阅。

## 复刻启示

- 在开发工作台把提示生成的变更作为可审阅 diff 展示，并注明影响的本体资源、SDK 版本及可新增的 OMCP 工具。
- 发布必须经过显式权限校验；工具辅助完成发布后仍保留发布版本、操作者、目标分支和审批记录。
