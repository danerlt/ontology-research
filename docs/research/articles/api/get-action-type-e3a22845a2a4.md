<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/action-types/get-action-type -->
<!-- 研读状态：已完成 -->

# Get Action Type (v2, latest) • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/action-types/get-action-type)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/v2/ontologies-v2-resources
- 相关性：direct；本体动作文档
- 官方更新时间：2026-11-12T17:46:46.921Z
- 目录核对时间：2026-11-14T14:56:13Z
- 产品状态：常规 v2 读取接口；可选 branch 参数属于实验性功能。

## 英文原文短摘录（每个来源不超过 25 词）

> “Gets a specific action type with the given API name.”

## 摘录译文

按给定的 API 名称获取一个指定的 Action Type。

## 中文要点

- GET `/api/v2/ontologies/{ontology}/actionTypes/{actionType}` 按 Ontology 与 Action Type API 名读取定义；OAuth 应用需要 `api:ontologies-read`。
- 返回 `ActionTypeV2`：包含 API 名、描述、显示名、发布状态、参数、RID、LogicRule 操作、返回类型；可选 `toolDescription` 专供工具/AI Agent 场景。
- 可选生成 SDK 包/版本参数；可选 branch 用于读取分支定义，但文档将分支功能标为实验性且工作流可能不完整。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| ActionTypeV2 | Action Type v2 结构 | 单个动作类型的 API 响应模型。 |
| toolDescription | 工具说明 | 面向工具使用上下文（例如 AI Agent）的可选说明。 |
| status | 发布状态 | ACTIVE、ENDORSED、EXPERIMENTAL 或 DEPRECATED。 |
| LogicRule | 逻辑规则 | Action Type 响应中的操作逻辑列表。 |

## 疑问与待验证项

- API 字段定义了 Agent 工具说明，但 Agent 何时读取它、与用户说明如何合并，需结合 Agent 文档验证。
- 实验性 branch 的读取权限、分支不存在时错误形态及定义缓存行为，本页未展开。

## 复刻启示

- 详情检查器应展示 `toolDescription`、参数 schema、操作规则、返回类型和发布状态，供 Agent 注册与人工审查共用。
- 读模型应同时支持 API 名定位和 RID 稳定引用；分支读取要明确标示实验状态并隔离缓存键。
