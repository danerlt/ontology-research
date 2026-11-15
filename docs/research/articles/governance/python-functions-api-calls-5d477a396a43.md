<!-- 页面 URL：https://www.palantir.com/docs/zh/foundry/functions/python-functions-api-calls -->
<!-- 研读状态：已完成 -->

# 函数 • Python functions • 从Python函数进行API调用 • Palantir

- 英文来源：[现行英文原文](https://www.palantir.com/docs/foundry/functions/api-calls)
- 官方中文来源：[官方中文页（AIP 机器翻译，准确性未独立验证）](https://www.palantir.com/docs/zh/foundry/functions/python-functions-api-calls)
- 页面语言：中文（官方 AIP 机器翻译，需与英文原文交叉核对）
- 主题栏目：functions
- 相关性：direct；本体函数文档
- 官方更新时间：2026-11-12T17:46:46.935Z
- 目录核对时间：2026-11-14T14:59:32Z
- 产品状态：该中文旧路由已迁移到通用 Functions API calls 页面；TSv1、TSv2 和 Python 可调用外部来源，但必须经 Data Connection 配置、导入并声明依赖。

## 原文短摘录与翻译

> “By default, functions are not allowed to call external APIs.”

## 摘录译文

默认情况下，函数不允许调用外部 API。

## 中文要点

- 先在 Data Connection 配置 source、exports 和代码仓库导入权限，再将 source 导入函数仓库，并在函数定义声明使用该 source。
- TSv2/Python 推荐使用可按环境映射的 source alias；TSv1 使用生成的 source symbol，不支持同一别名机制。
- 应优先使用 source 提供的预配置 HTTP 客户端，以继承证书、代理和出口配置；函数运行环境与 webhook 不完全相同。
- OAuth outbound application 可在 Python/TSv2 中传递调用用户 token；部署模式不能刷新 token，Workshop 直接调用也不能触发交互授权。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| source alias | 来源别名 | 可移植且可在 Marketplace 安装环境重新映射的外部来源标识 |
| Data Connection | 数据连接 | 配置 Foundry 到外部系统的凭据、出口与 source 的能力 |
| pre-configured client | 预配置客户端 | 已附带 source 证书和代理配置的 HTTP 客户端 |
| outbound application | 出站应用 | 为外部 API 调用配置 OAuth 身份的应用 |

## 疑问与待验证项

- 机器翻译页面路由聚焦 Python，但现行英文页覆盖三个函数语言；不同版本的 source alias 与 OAuth 能力不能混为一谈。
- 直接访问内网 URL 或使用任意第三方 HTTP client 并不保证在所有 serverless、Live Preview、deployed 环境工作。
- OAuth token 过期、source 证书链不完整和跨环境 alias 未映射都可能导致运行时失败；实际支持矩阵需对目标环境验证。

## 复刻启示

- 把外部连接器作为项目资源单独授权，secret 只保存在连接配置中；函数依赖明确声明，部署时将别名映射到目标系统。
- 运行面板记录调用的连接器、操作、响应状态和耗时，不记录原始 secret 或完整敏感响应。
- Agent 的外部工具调用沿用同一 source policy：默认关闭、按项目授权、限制出口域名，并将 OAuth 用户委托与服务身份区分。
