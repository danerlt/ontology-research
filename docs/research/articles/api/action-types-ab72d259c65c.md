<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/v1/ontology-resources/action-types -->
<!-- 研读状态：已完成 -->

# Action Type basics (v1) • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/v1/ontology-resources/action-types)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/v1/ontology-resources
- 相关性：direct；Ontology API v1 端点参考；保留作兼容性对照，并优先关注 v2
- 官方更新时间：2026-11-12T17:46:46.923Z
- 目录核对时间：2026-11-14T14:55:28Z
- 产品状态：v1 Action Type 基础页入口，无 Preview 标记

## 英文原文短摘录（每个来源不超过 25 词）

> “An action type represents a set of changes and logic that can be applied in the Ontology.”

## 摘录译文

Action Type 表示一组可应用于本体的变更与逻辑。

## 中文要点

v1 路由 `/action-types` 在目录中指向 Action Type 基础页。动作类型由 Ontology Manager 创建，描述一组可提交到本体的变更及其逻辑；实际参数、约束和状态由 Get Action Type 等接口查询。此页为概念导航入口，不是列出动作类型的端点。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Action Type | 动作类型 | 本体上可复用的一组变更与逻辑 |
| Get Action Type | 获取动作类型 | 查询单个动作定义的 API 操作 |
| List Action Types | 列出动作类型 | 分页发现本体动作定义的 API 操作 |

## 疑问与待验证项

- 本页不展示动作列表内容或创建/发布操作，不应与 List Action Types 端点混为一谈。
- 具体状态、参数和权限语义需从配套接口页补全。

## 复刻启示

- 导航页与操作端点分别记录，目录解析 canonical 路由以防将入口页误认为 API 操作。
- 画布动作目录需要支持搜索与状态过滤，并展示动作对哪些对象类型产生影响。
