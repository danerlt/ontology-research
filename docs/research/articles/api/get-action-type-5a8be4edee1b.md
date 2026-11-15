<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/ontology-resources/action-types/get-action-type -->
<!-- 研读状态：已完成 -->

# Get Action Type (v1) • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/ontology-resources/action-types/get-action-type)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/ontology-resources/action-types
- 相关性：direct；Ontology API v1 端点参考；保留作兼容性对照，并优先关注 v2
- 官方更新时间：2026-11-12T17:46:46.923Z
- 目录核对时间：2026-11-14T14:54:55Z
- 产品状态：v1 Get Action Type 兼容路由，OAuth2 读取范围为 `api:ontologies-read`

## 英文原文短摘录（每个来源不超过 25 词）

> “Gets a specific action type with the given API name.”

## 摘录译文

获取指定 API 名对应的单个动作类型。

## 中文要点

该 v1 兼容路由读取指定动作定义：以本体 RID 和 Action Type API 名定位，返回 API 名、描述/显示名、状态、参数、RID 和 operations。状态值包括 ACTIVE、ENDORSED、EXPERIMENTAL、DEPRECATED；OAuth2 第三方应用需要 `api:ontologies-read`。目录 canonical URL 为 `/api/v1/ontology-resources/action-types/get-action-type`。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Get Action Type | 获取动作类型 | 读取单个动作定义的 API |
| `actionTypeApiName` | 动作类型 API 名 | 查询目标的稳定 API 标识 |
| `status` | 发布状态 | API 返回的动作类型发布状态枚举 |
| `api:ontologies-read` | 本体读取范围 | 第三方 OAuth2 operation scope |

## 疑问与待验证项

- 兼容路径不代表另一套 v1 行为；字段解释应以规范响应 schema 为准。
- 状态与实际运行授权的关系未在此页定义，调用前必须执行权限检查。

## 复刻启示

- 对动作类型详情建立可观察的状态、参数和操作逻辑视图，并把执行权限校验留给服务端策略。
- 用 canonical 路由索引 API 文档，同时原样保留采集 URL 供目录审计和覆盖检查。
