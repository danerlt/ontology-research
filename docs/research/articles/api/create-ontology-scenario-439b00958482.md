<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/ontology-scenarios/create-ontology-scenario -->
<!-- 研读状态：已完成 -->

# Create Ontology Scenario • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/ontology-scenarios/create-ontology-scenario)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/v2/ontologies-v2-resources
- 相关性：direct；Ontology REST API v2 参考
- 官方更新时间：2026-11-12T17:46:46.922Z
- 目录核对时间：2026-11-14T14:57:30Z
- 产品状态：预览（Preview；请求需显式启用 `preview=true`）

## 英文原文短摘录（每个来源不超过 25 词）

> “Creates an ontology scenario.”

## 摘录译文

创建一个本体情景。

## 中文要点

- `POST /api/v2/ontologies/{ontology}/scenarios/create` 创建情景；请求体可带 `base`，官方示例以 branch 作为初始化基线，并返回唯一 `scenarioRid`。
- 可设置 `expireAfter`；默认在创建后 31 天过期，指定时间不得晚于创建后 31 天，过期情景会自动清理。
- 该创建端点处于 Preview，需显式 `preview=true`；第三方 OAuth 应用需要 `api:ontologies-read` 与 `api:ontologies-write`。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Base | 基线 | 初始化情景时采用的源 |
| Scenario RID | 情景 RID | 后续情景读写操作的唯一标识 |
| Expire after | 过期时间 | 自动清理的情景生命周期边界 |

## 疑问与待验证项

- `base` union 支持哪些类型及其含义，API 示例仅展示 branch 形式，需查请求 schema 或用户指南。
- 自动清理是否有回收站或恢复能力未说明；本地实现应规定删除前导出/保留策略。

## 复刻启示

- 创建情景后保存其 base、创建者、创建时间和过期时间，供评审对照。
- 若要支持长期本体版本评审，不应照搬最长 31 天的临时 Scenario 生命周期；情景试算与长期 schema 分支应分别设计。
