<!-- 页面 URL：https://www.palantir.com/docs/zh/foundry/functions/external-sources -->
<!-- 研读状态：已完成 -->

# 函数 • 函数中的外部来源 • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/functions/api-calls)
- 官方中文来源：尚未确认（配对状态：not_applicable）
- 页面语言：中文
- 主题栏目：functions
- 相关性：direct；本体函数文档
- 官方更新时间：2026-11-12T17:46:46.935Z
- 目录核对时间：2026-11-14T14:59:18Z
- 产品状态：官方中文页标注为未经验证的 AIP 机器翻译；英文原文为核对依据。

## 原文短摘录与翻译

> 英文原文：By default, functions are not allowed to call external APIs.

> 中文译文：默认情况下，函数不允许调用外部 API。

## 摘录译文

以上为英文短摘录及中文译文。官方中文页面为 AIP 机器翻译，准确性未经验证。

## 中文要点

- 旧目录路由当前为 404；现行规范页是 Make API calls from functions。函数外呼需先在 Data Connection 配置 source，并开启 exports 与代码仓库资源导入。
- TSv2/Python 推荐用 source alias，使 Marketplace 安装时可以按环境映射到不同 source；TSv1 直接引用导入资源且不支持 source alias。
- 函数应使用 source 提供的预配置 HTTPS client/代理，以便携带证书、凭据和出站策略；Webhook 可成功不代表函数运行时请求一定成功。
- 第三方 client 在 serverless/live preview 环境存在限制，直接请求外部或内部 Foundry URL 也不保证跨环境可用。中文旧路由为 AIP 机器翻译且其同名英文路由失效。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Data Connection source | Data Connection 来源 | 封装外部系统连接参数、网络路径和安全凭据的资源。 |
| Source alias | 来源别名 | TSv2/Python 中可跨环境映射的来源标识。 |
| Egress policy | 出站策略 | 控制函数可访问的外部网络目标的规则。 |

## 疑问与待验证项

- 开启 export、source 导入与出站策略可能由管理员执行；各租户的代理证书和网络可达性必须逐项目验证。
- 外部调用成功但本体写入失败时的补偿、幂等键与审计归属不由 source alias 自动解决。

## 复刻启示

- 将多系统连接器配置为项目级 source，凭据存服务端，函数只引用受控别名并由网关执行网络出站授权。
- 所有外部请求记录 source/version、别名映射、耗时与结果；凭据和请求敏感字段禁止进入日志。
