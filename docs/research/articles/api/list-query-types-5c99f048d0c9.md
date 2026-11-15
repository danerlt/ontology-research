<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/query-types/list-query-types -->
<!-- 研读状态：已完成 -->

# List Query Types (v2, latest) • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/query-types/list-query-types)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/ontologies-v2-resources/query-types
- 相关性：direct；Ontology REST API v2 参考
- 官方更新时间：2026-11-12T17:46:46.922Z
- 目录核对时间：2026-11-14T14:54:28Z
- 产品状态：页面未标注 Beta/Preview；查询分支为实验特性，需核对具体部署版本

## 英文原文短摘录（每个来源不超过 25 词）

> “Each query type is returned at its latest version.”

## 摘录译文

每个 Query Type 都以其最新版本返回。

## 中文要点

- `GET /api/v2/ontologies/{ontology}/queryTypes` 按本体列出 Query Type 元数据；返回的数据项包含 API 名、显示名、描述、参数、输出类型、RID 与版本等信息。
- 默认页大小为 100，响应通过 `nextPageToken` / `pageToken` 延续分页。文档保证还有结果时页面至少返回一项，但允许实际页小于请求的 `pageSize`，客户端应以令牌是否存在判断是否续页。
- “最新版本”按最近发布版本解释，可能包含预发布版本；若应用要求稳定版本，不能把列表返回值直接当作生产锁定版本。
- 可选 `branch` 指定读取分支，但文档说明分支仍属实验特性，且并非所有工作流都支持；OAuth2 第三方应用需要 `api:ontologies-read`。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Query Type | 查询类型 | 在本体中运行的一段已发布查询逻辑及其输入/输出契约 |
| latest version | 最新版本 | 最近发布版本，可能是预发布版本 |
| page token | 分页令牌 | 通过 `nextPageToken` 获取下一页 |
| branch | 分支 | 查询元数据的可选版本上下文，当前属于实验能力 |

## 疑问与待验证项

- 列表接口返回最新版本可能是 prerelease；页面未给出“仅稳定版本”过滤参数，需通过具体版本查询或发布策略完成稳定性控制。
- 页面没有说明分页期间新增/更新 Query Type 时是否采用一致快照；不要假定多页结果对应同一时刻。
- 页面未明确分支值如何授权、何时会回落到默认分支；部署环境中需验证。

## 复刻启示

- Query Type 应与函数注册表/查询定义关联，并对外暴露参数 schema、输出 schema、RID、语义版本和发布状态；列表接口需要游标分页。
- UI 可同时展示“最新发布版”和“稳定版”，将 prerelease 显式标识，避免 Agent 自动选版导致行为漂移。
- 本体画布可以把 Query Type 作为可执行逻辑节点，边连接输入对象/属性与输出对象集；分支上下文应贯穿画布预览、API 与审计日志。
