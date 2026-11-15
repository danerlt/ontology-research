<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/v1/ontology-resources/actions -->
<!-- 研读状态：已完成 -->

# Action basics (v1) • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/v1/ontology-resources/actions)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/v1/ontology-resources
- 相关性：direct；Ontology API v1 端点参考；保留作兼容性对照，并优先关注 v2
- 官方更新时间：2026-11-12T17:46:46.923Z
- 目录核对时间：2026-11-14T14:55:34Z
- 产品状态：v1 Action 基础概念页，无 Preview 标记

## 英文原文短摘录（每个来源不超过 25 词）

> “An Action represents one application of an action type.”

## 摘录译文

一个 Action 表示对某个 Action Type 的一次应用。

## 中文要点

API v1 的 Action 概念是某 Action Type 的一次具体应用；使用 Action API 可以向 Ontology 写入变更。此页面与 v1 Action basics 子页为同类入口，提供概念定义，不规定动作参数校验和副作用回调细节。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Action | 动作 | 动作类型的一次应用 |
| Action Type | 动作类型 | 操作的声明与逻辑定义 |
| Ontology write | 本体写入 | Action API 可触发的变更应用行为 |

## 疑问与待验证项

- 本页未给出具体端点和执行响应结构；必须通过 Apply Action 与 Validate Action 确认运行契约。
- 页面入口重复不能视为重复 Action Type 定义，应与其 canonical 基础页关联。

## 复刻启示

- 保存动作模型和执行历史的独立资源，并用动作类型 RID/API 名连接，便于版本治理与审计回溯。
- 对智能体的写入工具采用显式授权、参数校验、操作预览和执行审计闭环。
