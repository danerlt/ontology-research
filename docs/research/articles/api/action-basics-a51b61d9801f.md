<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/v1/ontology-resources/actions/action-basics -->
<!-- 研读状态：已完成 -->

# Action basics (v1) • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/v1/ontology-resources/actions/action-basics)
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

本页说明 Action 是 Action Type 的一次应用，可通过 API 对 Ontology 应用变更。它与 Action Type 的分工是定义与执行：前者声明可用操作及逻辑，后者对应一次带本次参数的执行。此为 Ontology API v1 的基础概念页，具体请求与结果结构由 Apply/Validate Action 端点定义。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Action | 动作 | 某个动作类型的一次应用 |
| Action Type | 动作类型 | 由 Ontology Manager 定义的操作模型 |
| Apply Action | 应用动作 | 通过 API 将变更应用到 Ontology 的操作 |

## 疑问与待验证项

- 概念页没有规定动作执行的一致性、事务边界、重试/幂等或并发冲突处理方式。
- 必须结合 Apply Action 与 Validate Action 页面区分请求接受、验证通过和最终数据生效。

## 复刻启示

- 数据模型分开保存动作定义和每次调用实例，运行实例保留发起用户、参数摘要、验证和提交状态。
- Agent 的可调用工具绑定 Action Type，受权限过滤并要求预览参数和执行结果。
