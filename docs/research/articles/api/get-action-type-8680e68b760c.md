<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/action-types/get-action-type -->
<!-- 研读状态：已完成 -->

# Get Action Type (v2, latest) • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/action-types/get-action-type)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/ontologies-v2-resources/action-types
- 相关性：direct；本体动作文档
- 官方更新时间：2026-11-12T17:46:46.921Z
- 目录核对时间：2026-11-14T14:53:29Z
- 产品状态：按页面现行表述整理；涉及分支/事务的能力以 Preview 或实验性限制为准。

## 英文原文短摘录（每个来源不超过 25 词）

> “Optional description intended for tool use contexts, such as AI agents.”

## 摘录译文

可选的描述，供 AI Agent 等工具调用场景使用。

## 中文要点

- GET `/api/v2/ontologies/{ontology}/actionTypes/{actionType}` 按 Action Type API 名称读取定义；Ontology 可用 API 名称或 RID 指定。
- 响应包含 apiName、描述、显示名、发布状态（ACTIVE/ENDORSED/EXPERIMENTAL/DEPRECATED）、参数、RID、逻辑规则、返回类型，以及面向工具/Agent 的 toolDescription。
- 可选传入 SDK 包和版本；branch 可读取指定分支定义，但分支仍属实验能力且并非所有工作流都支持。第三方 OAuth 读取需要 `api:ontologies-read`。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| apiName | API 名称 | 用于端点路径中稳定引用 Action Type。 |
| toolDescription | 工具描述 | 面向 AI Agent 等工具调用方的动作语义说明。 |
| release status | 发布状态 | Active、Endorsed、Experimental 或 Deprecated。 |

## 疑问与待验证项

- 该 schema 中的 operations 与 toolDescription 如何精确被 Agent Builder/SDK消费，需对照 Agent 工具配置文档。
- 分支查询目前不能假设所有 Ontology 工作流都完整支持。

## 复刻启示

- Action Type 元数据模型应包含独立的工具描述和生命周期状态，Agent 工具目录只暴露获授权且可执行的动作。
- 详情页需要同时展示人类显示名、API 名称、RID、参数、逻辑和状态，不能只显示标签。
