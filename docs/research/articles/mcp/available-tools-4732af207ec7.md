<!-- 页面 URL：https://www.palantir.com/docs/foundry/palantir-mcp/available-tools -->
<!-- 研读状态：已完成 -->

# Palantir MCP • Available tools • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/palantir-mcp/available-tools)
- 官方中文来源：目录中未发现对应中文页面
- 页面语言：英文
- 主题栏目：palantir-mcp
- 相关性：direct；Palantir MCP 文档
- 官方更新时间：页面未提供
- 目录核对时间：2026-11-15
- 产品状态：工具参考；逐项标注本地开发与 Foundry Code Workspace 的可用范围。

## 英文原文短摘录（每个来源不超过 25 词）

> “Tool search preserves environment and configuration restrictions; it does not make local-only tools available in Code Workspaces.”

## 摘录译文

工具搜索会保留环境和配置限制，不会让仅本地可用的工具在 Code Workspace 中变得可用。

## 中文要点

- Palantir MCP 工具按 Compass/项目、数据集、媒体、健康检查、数据血缘、本体、分支、Developer Console、计算模块、数据连接和文档搜索等域分组。
- 同一个工具在本地与托管 Code Workspace 的可用性可能不同；“System prompt”表示注入上下文，并不代表工具本身可调用。
- 本体类别中包含搜索、查看、创建/更新/删除对象类型、链接类型和动作类型；分支类别包括创建/查看/关闭分支与 proposal。工具表会标记 repository/workspace 限制。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| tool catalog | 工具目录 | 按 Foundry 资源领域和运行环境列出的工具清单。 |
| Code Workspace | 代码工作区 | Foundry 托管的代码与 Agent 运行环境。 |
| system-prompt context | 系统提示上下文 | 自动注入说明文本，不等于一个可调用工具。 |

## 疑问与待验证项

- 工具清单和环境支持会演进；卡片快照需随着官方版本更新，而实现不应把工具名称硬编码成永远不变。
- 删除/修改工具的后果各异；仅有“工具在目录中”不代表用户具有对应资源权限。

## 复刻启示

- 工具注册包含描述、输入 schema、环境/仓库兼容性、资源权限和副作用类别；UI 根据当前 runtime 只显示可用项。
- Agent 工具发现仍需逐次在服务端校验租户、项目、对象授权和工具操作约束。
