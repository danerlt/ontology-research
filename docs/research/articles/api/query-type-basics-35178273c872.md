<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/query-types/query-type-basics -->
<!-- 研读状态：已完成 -->

# Query Type basics (v2, latest) • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/query-types/query-type-basics)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/v2/ontologies-v2-resources
- 相关性：direct；Ontology REST API v2 参考
- 官方更新时间：2026-11-12T17:46:46.922Z
- 目录核对时间：2026-11-14T14:57:51Z
- 产品状态：常规 v2 概念页；Query Function 是其创建入口。

## 英文原文短摘录（每个来源不超过 25 词）

> “A query type represents a logic that can be run in the Ontology.”

## 摘录译文

Query Type 表示一段可在 Ontology 中运行的逻辑。

## 中文要点

- Query Type 是可在本体中执行的一段逻辑，通过 Query Functions 创建。此概念页与 `Query basics` 页面文字一致。
- 页面本身没有补充 schema 或运行细节；应结合 Get Query Type、List Query Types、Execute Query 读取版本、参数与返回类型。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Query Type | 查询类型 | 可执行的本体逻辑定义。 |
| Query Function | 查询函数 | 创建 Query Type 的产品能力。 |
| Ontology | 本体 | Query Type 运行所处的语义模型。 |

## 疑问与待验证项

- 两个不同路由的基础页表述相同；为何分别保留 Query 与 Query Type 导航层级，文档未解释。
- Query Function 的发布及权限边界需要转到相应用户文档核验。

## 复刻启示

- 产品侧合并重复概念说明，但在目录卡中保留两个官方入口以便追踪文档导航。
- Query Type 详情呈现版本、参数、返回值和创建来源，并与本体对象及 Agent 可用工具建立可审查的引用。
