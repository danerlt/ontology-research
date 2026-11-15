<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/v1/ontology-resources/action-types/action-type-basics -->
<!-- 研读状态：已完成 -->

# Action Type basics (v1) • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/v1/ontology-resources/action-types/action-type-basics)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/v1/ontology-resources
- 相关性：direct；Ontology API v1 端点参考；保留作兼容性对照，并优先关注 v2
- 官方更新时间：2026-11-12T17:46:46.923Z
- 目录核对时间：2026-11-14T14:55:29Z
- 产品状态：v1 Action Type 概念页，无 Preview 标记

## 英文原文短摘录（每个来源不超过 25 词）

> “An action type represents a set of changes and logic that can be applied in the Ontology.”

## 摘录译文

Action Type 表示一组可应用于本体的变更与逻辑。

## 中文要点

Action Type 是一种由 Ontology Manager 创建的操作定义，声明在本体上可执行的一组变更及逻辑。配套接口会将其呈现为参数 schema、状态和可执行操作。它是本体写入工具的治理边界，区别于直接修改数据库记录，也区别于某次 Action 执行实例。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Action Type | 动作类型 | 由 Ontology Manager 管理的变更/逻辑定义 |
| Parameter | 参数 | 执行动作时提供的输入值 |
| Action | 动作 | 某动作类型的一次应用 |

## 疑问与待验证项

- 基础页未说明类型创建、参数校验、提交条件、对象权限和分支发布规则，需联合用户文档及 API 端点研读。
- API 参考不能证明某个动作对当前用户或 Agent 可见/可执行，权限需独立判断。

## 复刻启示

- 画布将 Action Type 作为操作节点，以参数/目标对象边表示其输入与影响；将状态和治理信息放在节点检查器。
- Agent 工具目录以 Action Type 暴露受权限约束的操作，调用前先做本地参数 schema 校验和预检查。
