<!-- 页面 URL：https://www.palantir.com/docs/foundry/functions/instrumentation-telemetry -->
<!-- 研读状态：已完成 -->

# Functions • Function management • Instrumentation and telemetry • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/functions/instrumentation-telemetry)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：functions
- 相关性：direct；本体函数文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:02:33Z
- 产品状态：未见本页另标 Beta、预览或弃用状态。

## 英文原文短摘录（每个来源不超过 25 词）

> A single span over the total execution duration of the function, along with a single request log, is automatically created for all function types.

## 摘录译文

所有函数类型都会自动生成一个覆盖整个函数执行时长的 span，以及一条请求日志。

## 中文要点

- 页面将函数可观测数据分为日志、span 与指标；TSv1 支持日志及产品定义的 span/指标，TSv2 与 Python 可发出自定义 span，但指标仍以产品定义项为主。
- TSv2 和 Python 会自动为出站网络请求埋点，也可在代码中创建自定义 span；第三方日志/追踪库需接入 Foundry 配置的全局 provider。
- 日志可回溯查询。建议使用恰当级别并附带对象标识、计数与操作上下文，同时避免记录凭证或敏感响应正文。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Telemetry | 遥测 | 用于生产监控与排错的运行数据。 |
| Span | 追踪片段 | 记录一次函数或内部操作的耗时区间。 |
| Global provider | 全局 provider | 平台配置的日志或追踪入口，第三方库须将数据输出到此入口。 |

## 疑问与待验证项

- 自动请求日志与自定义日志的保留期限、脱敏和查询权限如何配置？
- 当前版本的各类函数指标清单及自定义指标限制需结合 Observability 页面和租户实测确认。

## 复刻启示

- 为函数运行记录定义结构化日志、请求级 trace/span 和计时指标；给每次运行生成 trace_id，并关联项目、对象类型、动作、版本和结果。
- 提供隐私字段屏蔽及查询权限；页面区分平台自动采集能力与用户自定义埋点能力。
