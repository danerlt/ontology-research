<!-- 页面 URL：https://www.palantir.com/docs/foundry/functions/functions-settings -->
<!-- 研读状态：已完成 -->

# Functions • 函数设置 • Functions settings • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/functions/functions-settings)
- 官方中文来源：尚未确认（配对状态：ambiguous）
- 页面语言：英文
- 主题栏目：functions
- 相关性：direct；本体函数文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:02:50Z
- 产品状态：管理员可按 Space 级别配置扩展执行能力，并分别对白名单仓库、函数和 Marketplace 项目授权。

## 英文原文短摘录（每个来源不超过 25 词）

> “allows administrators to manage a collection of settings that govern how functions behave within a specific space.”

## 摘录译文

允许管理员管理控制某个 Space 中函数行为的一组设置。

## 中文要点

- 设置入口位于 Control Panel 的 Space 级 Functions settings。
- Extended function execution 可允许函数调用 Actions，并获取有效期最长 4 小时的扩展 TTL 认证令牌，属于高权限能力。
- 三类 allowlist 分别约束谁能发布扩展函数的仓库、谁能执行扩展能力的函数，以及 Marketplace 可安装扩展函数的项目。
- 仓库白名单决定发布权限，函数白名单在每次执行时检查；从白名单仓库发布的新函数会自动进入函数白名单。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Extended function execution | 扩展函数执行 | 允许函数调用动作或获取长有效期认证令牌的能力 |
| Repository allowlist | 仓库白名单 | 控制哪些仓库可以发布扩展函数 |
| Execution allowlist | 执行白名单 | 运行时控制哪些函数可启用扩展能力 |

## 疑问与待验证项

- 令牌最长 TTL 和 Action 调用权限会扩大执行身份影响范围，租户是否开放及具体 allowlist 应在 Control Panel 复核。
- 仓库白名单会自动把新函数传播到函数 allowlist，发布流程需要监控意外扩权。

## 复刻启示

- 将可调用 Action、长效凭据、发布源仓库和目标 Marketplace 项目拆为独立权限能力，默认关闭并按名单启用。
- 扩展授权同时在发布、执行、安装三个阶段校验，审计记录配置来源与变更人。
