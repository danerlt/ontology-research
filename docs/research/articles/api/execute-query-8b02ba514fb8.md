<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/queries/execute-query -->
<!-- 研读状态：已完成 -->

# Execute Query (v2, latest) • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/queries/execute-query)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/v2/ontologies-v2-resources
- 相关性：direct；Ontology REST API v2 参考
- 官方更新时间：2026-11-12T17:46:46.922Z
- 目录核对时间：2026-11-14T14:57:48Z
- 产品状态：常规 v2 查询执行接口；branch 与 transactionId 属于实验性功能。

## 英文原文短摘录（每个来源不超过 25 词）

> “Executes a Query using the given parameters.”

## 摘录译文

使用给定参数执行一个 Query。

## 中文要点

- POST `/api/v2/ontologies/{ontology}/queries/{queryApiName}/execute` 执行 Query，OAuth 需要 `api:ontologies-read`；可选参数可以省略。
- 默认使用最近发布的版本，且该版本可能是预发布版；`version` 接受语义版本范围。指定 branch 后不带 version 会执行该分支最新版本（包括预发布版）。
- 请求参数为 ParameterId 到 DataValue 的映射；响应 `value` 可包含嵌套数组、对象引用、对象集等多种数据。情景可用于执行上下文，branch 和 transactionId 有实验性限制。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| queryApiName | 查询 API 名称 | 标识要执行的 Query。 |
| semantic version range | 语义版本范围 | 选择满足范围的查询版本。 |
| pre-release version | 预发布版本 | 默认最新发布版本可能包含的版本类型。 |
| scenarioRid | 情景 RID | 指定查询运行的本体情景。 |

## 疑问与待验证项

- 默认使用的 latest 可能是预发布版本；生产调用方是否要 pin 版本需结合自己的发布流程决定。
- 查询运行的超时、取消、幂等和缓存策略不在本页描述。

## 复刻启示

- 执行记录固定保存 Query RID/API 名、语义版本、参数摘要、项目/本体、分支或情景及输出类型。
- 试算与正式调用区分预发布版本；Agent 只能看到已授权且符合发布策略的 Query。
