<!-- 页面 URL：https://www.palantir.com/docs/zh/foundry/ontology-sdk/application-metrics -->
<!-- 研读状态：已完成 -->

# OSDK • 应用指标 • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/developer-console/application-metrics)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/ontology-sdk/application-metrics)
- 页面语言：中文（官方机器翻译，准确性未验证）
- 主题栏目：ontology-sdk
- 相关性：direct；OSDK 应用调用指标的中文路由
- 官方更新时间：2026-11-12T17:46:46.932Z
- 目录核对时间：2026-11-14T15:00:41Z
- 产品状态：Beta；页面提示可能未对所有 enrollment 开放

## 英文原文短摘录（每个来源不超过 25 词）

> “view the 50th, 75th, 95th, and 99th percentiles for latency associated with API calls made by your OSDK.”

## 摘录译文

延迟卡片可查看 OSDK API 调用延迟的第 50、75、95 和 99 百分位数。

## 中文要点

- 中文页面介绍 OSDK 应用的请求量、请求成功率和 API endpoint 延迟图表，数据约延迟 24 小时，历史跨度最多 30 天。
- 不超过 5 天的查询范围使用小时粒度；更长范围使用日粒度。延迟图表提供 p50、p75、p95、p99，可按 endpoint 查看。
- 只有通过受支持 OAuth 流程发出的调用会被计入；在 TypeScript/Python 使用 `UserTokenAuth` 的调用不显示，`PublicClientAuth` 和 `ConfidentialClientAuth` 的调用会进入 Developer Console。
- 这条中文路由属于旧 OSDK 路径，当前英文页位于 Developer Console；中文正文明确提示是 AIP 机器翻译，准确性未验证。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| API latency | API 延迟 | endpoint 调用耗时指标 |
| Percentile | 百分位数 | 延迟分布的分位统计 |
| UserTokenAuth | 用户令牌认证 | 本页指出其调用不被此指标采集 |
| ConfidentialClientAuth | 机密客户端认证 | 指标支持的 OAuth 客户端流程之一 |

## 疑问与待验证项

- 中文原文是机器翻译，具体术语以英文当前版本为准；页面导航与英文 Developer Console 结构可能不同。
- 页面未说明指标的采集采样率、endpoint 命名规范、响应分页或按用户筛选能力。
- Beta 可用范围和数据时延在更新后可能变化，引用时应记录文档版本/核查日期。

## 复刻启示

- 把多语言文档路由与产品能力 ID 分开保存，同一功能的旧路径和迁移后路径可以追踪而不重复造能力。
- 指标页面展示分位数而不只显示平均延迟，并标明数据迟滞与时间桶粒度。
- 让指标采集身份与认证方式可见，避免用户把不采集的调用误认为成功率为零或 API 没被调用。
