<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/v1/ontology-resources/action-types/get-action-type -->
<!-- 研读状态：已完成 -->

# Get Action Type (v1) • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/v1/ontology-resources/action-types/get-action-type)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/v1/ontology-resources
- 相关性：direct；Ontology API v1 端点参考；保留作兼容性对照，并优先关注 v2
- 官方更新时间：2026-11-12T17:46:46.923Z
- 目录核对时间：2026-11-14T14:55:34Z
- 产品状态：v1 只读 API；OAuth2 第三方应用需 `api:ontologies-read`

## 英文原文短摘录（每个来源不超过 25 词）

> “Gets a specific action type with the given API name.”

## 摘录译文

获取指定 API 名对应的单个动作类型。

## 中文要点

`GET /api/v1/ontologies/{ontologyRid}/actionTypes/{actionTypeApiName}` 通过本体 RID 与动作类型 API 名读取定义。响应包括 API 名、描述、显示名、发布状态、参数、RID 和可选 operations；状态枚举为 `ACTIVE`、`ENDORSED`、`EXPERIMENTAL`、`DEPRECATED`。第三方 OAuth2 调用要求 `api:ontologies-read`。该文档在 v1 示例里返回外层 `data` 对象，客户端应以具体响应 schema 为准。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| `ontologyRid` | 本体 RID | 动作类型所属本体的资源标识 |
| `actionTypeApiName` | 动作类型 API 名 | 单个动作定义的查询键 |
| `status` | 发布状态 | ACTIVE、ENDORSED、EXPERIMENTAL 或 DEPRECATED |
| `parameters` | 参数定义 | 动作执行所需的输入参数结构 |

## 疑问与待验证项

- 页面字段没有完整展开 `Parameter` 和 `LogicRule` 子结构，需对照接口 schema/SDK。
- 文档列出状态枚举但未说明每种状态对运行时调用的权限或限制；不能仅凭状态值推断可执行性。

## 复刻启示

- 动作节点详情展示参数、状态、版本 RID 与操作逻辑引用，状态徽标不能替代实际权限检查。
- 面向 Agent 的只读发现 API 需与动作执行工具分别授权；对 deprecated/experimental 状态给出策略提示。
