<!-- 页面 URL：https://www.palantir.com/docs/foundry/palantir-mcp/installation -->
<!-- 研读状态：已完成 -->

# Palantir MCP • Installation • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/palantir-mcp/installation)
- 官方中文来源：目录中未发现对应中文页面
- 页面语言：英文
- 主题栏目：palantir-mcp
- 相关性：direct；Palantir MCP 文档
- 官方更新时间：页面未提供
- 目录核对时间：2026-11-15
- 产品状态：本地 MCP 需要管理员启用并限制用户/用户组；可通过 MCP Hub 获取安装配置。

## 英文原文短摘录（每个来源不超过 25 词）

> “Palantir MCP for local development is disabled by default.”

## 摘录译文

本地开发使用 Palantir MCP 默认处于禁用状态。

## 中文要点

- 管理员需先在 Control Panel 启用本地 Palantir MCP，并可限定允许的用户或群组；用户再按 MCP Hub 指引配置 IDE。
- 在 Foundry 仓库内可使用 Foundry Git token 建立认证上下文；其他环境需显式配置身份凭据。工具执行使用配置 token 的权限。
- 本地 MCP 读取的数据和元数据会传到所连接的外部 Agent/LLM，平台侧治理范围随数据离开平台而改变；模型供应商由 IDE/外部系统决定。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| local development | 本地开发 | 在外部 IDE/电脑连接 Foundry MCP 的方式。 |
| Foundry Git token | Foundry Git 令牌 | 仓库环境中可用于引导 MCP 身份认证的凭据。 |
| external LLM provider | 外部模型提供商 | 由本地 Agent/IDE 选择并处理 MCP 数据的模型服务。 |

## 疑问与待验证项

- 管理员开启 MCP 会允许外部 Agent 以配置用户权限访问数据；数据离开 Foundry 后的保留与训练策略由外部模型服务协议决定。
- 本地令牌存放、轮换、撤销和日志脱敏需结合具体 IDE 的安全配置。

## 复刻启示

- MCP 接入默认关闭；启用前要求管理员设置用户范围、工具类别、令牌策略和可访问项目。
- 为每个 MCP 客户端提示数据流向、外部 LLM 供应商和授权身份；记录工具请求但对凭证和敏感输出脱敏。
