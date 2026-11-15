<!-- 页面 URL：https://www.palantir.com/docs/foundry/palantir-mcp/tool-search -->
<!-- 研读状态：已完成 -->

# Palantir MCP • Tool search • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/palantir-mcp/tool-search)
- 官方中文来源：目录中未发现对应中文页面
- 页面语言：英文
- 主题栏目：palantir-mcp
- 相关性：direct；Palantir MCP 文档
- 官方更新时间：页面未提供
- 目录核对时间：2026-11-15
- 产品状态：Tool search 于 2026 年 6 月发布；官方说明旨在减少 Agent 上下文中的工具定义 token。

## 英文原文短摘录（每个来源不超过 25 词）

> “When tool search is enabled, Palantir MCP starts up exposing only one tool — `search_tools` — instead of the full tool catalog.”

## 摘录译文

启用工具搜索后，Palantir MCP 启动时只暴露 `search_tools`，而不是整个工具目录。

## 中文要点

- `search_tools` 根据任务描述在工具名、类别和整理关键词中本地排序，激活最相关工具并返回说明；搜索不额外调用模型或网络。
- 已激活工具在当前会话保留；重新连接后只剩搜索入口。工具搜索依赖客户端刷新 MCP 工具列表的 `tools/list_changed` 通知。
- 未动态刷新工具列表的客户端无法看到新激活工具；Palantir 文档以 Continue 为例说明它不使用此能力。若关闭工具搜索，则启动时加载所有授权工具。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| tool search | 工具搜索 | 按任务动态发现并激活工具的方式。 |
| tools/list_changed | 工具列表变更通知 | MCP Server 通知客户端刷新可调用工具列表的事件。 |
| context tokens | 上下文 token | 模型输入窗口中工具定义和对话占用的 token。 |

## 疑问与待验证项

- getting started 页面与发布公告对默认启用描述存在版本差异，配置时应以当前安装包和 Control Panel 指引为准。
- 工具搜索仅减少初始上下文，不扩大原本被禁用或仅本地可用的工具权限。

## 复刻启示

- 构建 MCP 网关时可先暴露低成本的能力检索工具，再按请求授权的工具子集动态提供 schema。
- 工具发现必须保留原有权限范围和环境约束，并测试客户端能收到动态工具列表刷新通知。
