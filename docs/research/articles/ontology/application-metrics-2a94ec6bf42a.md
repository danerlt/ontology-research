<!-- 页面 URL：https://www.palantir.com/docs/foundry/developer-console/application-metrics -->
<!-- 研读状态：已完成 -->

# Developer Console • Core concepts • Application metrics • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/developer-console/application-metrics)
- 官方中文来源：[OSDK 应用指标中文页](https://www.palantir.com/docs/zh/foundry/ontology-sdk/application-metrics)（配对状态：needs_review）
- 页面语言：英文
- 主题栏目：developer-console
- 相关性：direct；OSDK 应用调用观测与延迟指标
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:05:02Z
- 产品状态：Beta；可能未对所有 enrollment 开放，开发期间可变

## 英文原文短摘录（每个来源不超过 25 词）

> “Metrics are currently served with around 24 hours of latency and a historical view up to the last 30 days.”

## 摘录译文

当前指标数据约延迟 24 小时，历史视图最多覆盖最近 30 天。

## 中文要点

- Developer Console 指标页通过图表展示请求数量、请求成功率及调用 API 端点的延迟；指标用于观察 OSDK 应用随时间的运行表现。
- 数据约延迟 24 小时，历史最长 30 天。查看不超过 5 天的时间范围按小时聚合，更长范围按天聚合。
- 延迟卡片可看 p50、p75、p95、p99 分位数，并按具体 endpoint 与分位数查看变化。
- 只有通过文档支持 OAuth 流程发出的调用才会进入此应用指标。`UserTokenAuth` 客户端的调用不计入；`PublicClientAuth`/`ConfidentialClientAuth` 调用会显示。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Application metrics | 应用指标 | OSDK 应用 API 使用量、成功率与延迟图表 |
| Latency percentile | 延迟分位数 | p50/p75/p95/p99 端点延迟统计 |
| Hourly bucket | 小时桶 | 不超过 5 天时间范围的聚合粒度 |
| OAuth flow | OAuth 流程 | 指标采集所依赖的应用认证方式 |

## 疑问与待验证项

- 这是 Beta 且存在 enrollment 门槛；采集口径、页面可用性及指标定义可能变化。
- 24 小时延迟意味着指标不适合作为实时告警源，本文没有说明补采、缺失数据和 percentile 计算样本量。
- 中文配对页位于旧/不同 OSDK 路由，内容本身标注为 AIP 机器翻译且尚未验证；以当前英文页为事实依据。

## 复刻启示

- 集成运维视图应分别展示请求量、错误率、endpoint 延迟分布，并说明采集延迟/保留期和数据聚合粒度。
- 观测采集应从明确的 OAuth 客户端/SDK instrumentation 取得，不能把外部 token 或服务端未经埋点的调用假设为已监控。
- 复刻系统将在线实时告警与延迟汇总报表分开；指标历史窗口、授权身份和过滤维度要可审计。
