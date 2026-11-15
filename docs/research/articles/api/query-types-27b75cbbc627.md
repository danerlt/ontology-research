<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/ontology-resources/query-types -->
<!-- 研读状态：已完成 -->

# Query Type basics (v1) • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/ontology-resources/query-types)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/ontology-resources/query-types
- 相关性：direct；Ontology API v1 查询类型概念参考，保留兼容性对照并优先关注 v2
- 官方更新时间：2026-11-12T17:46:46.923Z
- 目录核对时间：2026-11-14T14:55:25Z
- 产品状态：分组基础路由；定义由同组可读官方 Query Type basics 子页确认

## 英文原文短摘录（每个来源不超过 25 词）

> “A query type represents a logic that can be run in the Ontology.”

摘录来源：[Query Type basics (v1)](https://www.palantir.com/docs/foundry/api/ontology-resources/query-types/query-type-basics)。

## 摘录译文

Query Type 表示一段可以在本体中运行的逻辑。

## 中文要点

- 本体中的 Query Type 是可执行的查询逻辑定义；同组页面说明可以通过 Query Functions 创建。
- 该分组根路由与 `/query-type-basics` 子页内容重叠；卡片分别保留目录中的不同 URL，不把重复编目误作不同产品能力。
- 实际接口能力分成列表、详情和执行：List Query Types 返回定义列表；Get Query Type 返回单个 schema；Execute Query 输入参数并给出结果值。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Query Type | 查询类型 | 本体中的命名查询逻辑 |
| Query Function | 查询函数 | Query Type 的函数式创建入口 |
| query type schema | 查询类型结构 | 参数、输出及资源元数据定义 |
| query result | 查询结果 | Execute Query 的运行时返回值 |

## 疑问与待验证项

- 页面定义非常简短，未说明 Query Type 的权限规则、发布步骤和生命周期；需看配套 API 和产品操作文档。
- 根路由是否仅为侧栏目录/版本切换入口，当前 API 文档读取结果无法证明。

## 复刻启示

- 在管理系统里将定义与执行解耦，但使用稳定 API 名将画布逻辑节点、Function 实现、输入 schema 和输出 schema 关联。
- 为 Agent 提供有限且版本固定的 Query Type 工具注册；每次调用保存所用 ontology、逻辑版本和参数 schema 版本。
- 对重复/别名路由做 canonical 去重展示，目录索引仍保留原始官方路由以追溯来源。
