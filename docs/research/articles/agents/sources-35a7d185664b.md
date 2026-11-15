<!-- 页面 URL：https://www.palantir.com/docs/foundry/agents/sources -->
<!-- 研读状态：已完成 -->

# Pro-code agents • Core concepts • Connect pro-code agents to external systems • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/agents/sources)
- 官方中文来源：尚未确认（配对状态：ambiguous）
- 页面语言：英文
- 主题栏目：agents
- 相关性：direct；Agent 文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:05:32Z
- 产品状态：页面说明外部系统 Source 提供受控网络出口和运行时 secret 注入；CBAC-enabled 环境不支持该功能。

## 英文原文短摘录（每个来源不超过 25 词）

> “A source provides two things to your pro-code agent at runtime:”

## 摘录译文

Source 在运行时为 pro-code Agent 提供两类能力：

## 中文要点

- Source 为 Agent 提供到目标主机的网络出口策略，并把 secret 解析后注入运行中的容器。
- 凭据文件 `/app/var/run/source_credentials.json` 按 source API 名和 secret API 名组织；解析失败时内容可能是 `{}`。
- 凭据文件采用原子替换，代码不要缓存内容；需要当前值时重新读取。该能力不适用于 CBAC-enabled 环境。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| source | 来源连接 | 配置外部主机连通策略和密钥注入的资源。 |
| network egress | 网络出口 | Agent 向获准外部主机发起连接的能力。 |
| secret | 密钥 | 运行时注入的 API key、token 等敏感值。 |

## 疑问与待验证项

- - 页面未说明密钥轮换、过期错误与主机白名单维护方式；需在连接器层提供健康检查和凭据状态。
- - 应在创建/发布前验证运行环境是否支持 Source。

## 复刻启示

- - 来源系统模型应包括 project、协议/主机、网络策略、密钥引用、状态与健康检查时间；secret 不写入普通本体属性和日志。
- - 用独立 secrets backend 提供运行时凭据；失败清楚报错，审计只记凭据引用。
