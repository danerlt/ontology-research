<!-- 页面 URL：https://www.palantir.com/docs/foundry/functions/functions-deployed -->
<!-- 研读状态：已完成 -->

# Functions • 部署函数 • Deploy functions • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/functions/functions-deployed)
- 官方中文来源：尚未确认（配对状态：ambiguous）
- 页面语言：英文
- 主题栏目：functions
- 相关性：direct；本体函数文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:02:45Z
- 产品状态：多数场景推荐无服务器；长期部署适用于第三方客户端/GPU/长缓存等特定需求。

## 英文原文短摘录（每个来源不超过 25 词）

> “We generally recommend serverless functions for most use cases.”

## 摘录译文

大多数使用场景通常推荐无服务器函数。

## 中文要点

- 部署教程针对已发布的 Python 或 TypeScript v2 函数；若 enrollment 启用 serverless，新建仓库默认使用无服务器。
- 无服务器按需执行，闲置不持续计费，维护更少且可按请求运行多个函数版本；部署函数运行长生命周期容器，单仓库函数共享部署并按流量扩缩。
- 部署模式可用长生命周期缓存、第三方 API 客户端、GPU 和更完整服务发现；无服务器可使用平台提供 Source client，但不支持第三方 clients。
- 部署模式在运行期间持续产生计算费用，版本一次只运行一个；环境会自动重启，因此本地缓存逻辑须容忍重启。Marketplace 可复制函数执行模式与部署配置。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Serverless execution | 无服务器执行 | 按需分配运行资源的函数模式 |
| Deployed execution | 部署式执行 | 部署为长期运行容器环境的函数模式 |
| Source client | 数据源客户端 | 平台提供、用于受控访问外部 Source 的客户端 |

## 疑问与待验证项

- 具体 enrollment 是否启用 serverless 由管理员控制；运行模式应在目标租户验证而非默认假定。
- GPU、第三方客户端和完整服务发现需要部署运行，但持续资源费用与单版本运行是对应代价。

## 复刻启示

- 函数执行模式按负载和依赖选择：默认按需运行，只有需要 GPU/第三方客户端/本地缓存时才配置长期部署。
- 部署策略记录成本模型、实例扩缩、版本发布和重启边界，并对 Marketplace 安装做配置一致性检查。
