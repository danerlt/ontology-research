<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/ontology-resources/actions -->
<!-- 研读状态：已完成 -->

# Action basics (v1) • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/ontology-resources/actions)
- 官方中文来源：尚未确认（配对状态：needs_review）
- 页面语言：英文
- 主题栏目：api/ontology-resources/actions
- 相关性：direct；Ontology API v1 端点参考；保留作兼容性对照，并优先关注 v2
- 官方更新时间：2026-11-12T17:46:46.923Z
- 目录核对时间：2026-11-14T14:54:55Z
- 产品状态：v1 Action 基础页兼容路由，canonical 页面无 Preview 标记

## 英文原文短摘录（每个来源不超过 25 词）

> “An Action represents one application of an action type.”

## 摘录译文

一个 Action 表示对某个 Action Type 的一次应用。

## 中文要点

该 v1 API 兼容入口映射到 Action 基础概念：Action 表示 Action Type 的一次应用，API 可用它向 Ontology 应用变更。动作定义与具体执行需分开处理；调用参数、验证和最终写入状态由各操作端点补足。目录 canonical 路由为 `/api/v1/ontology-resources/actions/action-basics`。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Action Type | 动作类型 | 可复用的动作定义 |
| Action | 动作 | 对动作类型的一次具体应用 |
| Canonical URL | 规范地址 | 目录登记的主要 v1 基础页面 |

## 疑问与待验证项

- 兼容路径与显式 v1 路径不能据路径名称推断不同的动作语义；需根据 canonical 元数据去重。
- 此基础条目未定义事务、幂等和审计字段。

## 复刻启示

- 将 Action Type 当作画布上的操作定义节点，将执行记录作为运行时审计数据，不混入本体 schema 节点。
- 面向 Agent 展示动作工具时附带权限、输入 schema、验证状态与执行后对象差异。
