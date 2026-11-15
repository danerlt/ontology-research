<!-- 页面 URL：https://www.palantir.com/docs/zh/foundry/functions/marketplace-functions -->
<!-- 研读状态：已完成 -->

# 函数 • 将函数添加到 Marketplace 产品 • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/functions/marketplace-functions)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/functions/marketplace-functions)
- 页面语言：中文
- 主题栏目：functions
- 相关性：direct；本体函数文档
- 官方更新时间：2026-11-12T17:46:46.935Z
- 目录核对时间：2026-11-14T14:59:26Z
- 产品状态：官方中文页标注为未经验证的 AIP 机器翻译；英文原文为核对依据。

## 英文原文短摘录（每个来源不超过 25 词）

> “You can use Foundry DevOps to include your functions in Marketplace products for other users to install and reuse.”

## 摘录译文

你可以通过 Foundry DevOps 将函数纳入 Marketplace 产品，供其他用户安装和复用。

## 中文要点

- 打包时选具体函数版本；model function 产品会带模型版本和 live deployment 依赖，安装目标环境部署需运行。
- 代码仓库会作为依赖输出，但普通安装产品通常不必带源代码；修改安装后的函数，应在原产品发布新版本并升级安装。
- 若函数要在运行时调用 Action 或使用长时令牌，目标项目必须被管理员加入 Extended function execution allowlist。
- 安装有默认去重与 Beta stable 两种版本/API 名解析模式；不可变函数版本及 Ontology 内 API 名唯一性影响冲突处理。中文页机器翻译准确性未验证。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Marketplace product | Marketplace 产品 | 可以安装、升级和复用的一组函数及其依赖。 |
| Extended execution allowlist | 扩展执行允许列表 | 管理员为函数扩展执行权限设置的目标项目白名单。 |
| Stable mode | 稳定模式 | 保留打包版本/API 名的 Beta Marketplace 安装方式。 |

## 疑问与待验证项

- 目标环境模型部署启动失败、外部凭据映射和 API 名冲突的回滚/清理机制需结合具体 Marketplace 类型核实。
- Beta stable mode 可用性和行为可能变化；页面建议上线前重新核对租户状态。

## 复刻启示

- 分发包包含版本锁定的函数、模型、部署模式、资源配置和权限依赖，安装前进行依赖闭包验证。
- 允许高权限函数跨环境安装时做管理员审批、目标项目白名单和安装调用审计。
