<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/query-types/query-type-basics -->
<!-- 研读状态：已完成 -->

# Query Type basics (v2, latest) • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/query-types/query-type-basics)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/ontologies-v2-resources/query-types
- 相关性：direct；Ontology REST API v2 参考
- 官方更新时间：2026-11-12T17:46:46.922Z
- 目录核对时间：2026-11-14T14:54:34Z
- 产品状态：页面未标注 Beta/Preview；本卡的定义由同组官方 v2 查询基础页交叉核对

## 英文原文短摘录（每个来源不超过 25 词）

> “A query type represents a logic that can be run in the Ontology.”

摘录来源：[Query basics (v2, latest)](https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/queries)（同组官方说明；本卡目标路由无法从文档读取端单独载入）。

## 摘录译文

Query Type 表示一段可以在本体中运行的逻辑。

## 中文要点

- 本页主题是 Query Type 的基础概念。同组 v2 Query basics 官方说明将其定义为可在本体中执行的逻辑，并说明可通过 Query Functions 创建。
- 与普通对象属性读取不同，Query Type 具有参数与输出契约，可将查询逻辑封装为命名资源供应用或 SDK 调用。相邻的 v2 列表/详情 API 返回参数、输出、RID 与版本等元数据。
- 目标基础页 URL 在本次文档读取中返回不可访问；因此本卡不推断其是否还列有 UI 配置步骤、额外限制或版本差异，以上定义以可读取的同组 v2 说明交叉确认。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Query Type | 查询类型 | 可在本体上执行的命名逻辑资源 |
| Query Function | 查询函数 | 创建 Query Type 的函数实现入口 |
| query parameter | 查询参数 | 调用逻辑时提供的输入 |
| output type | 输出类型 | Query Type 运行结果的数据类型契约 |

## 疑问与待验证项

- 当前可读取的同组说明很简短；目标基础页是否补充定义边界、运行限制或示例，仍待页面可访问时复核。
- Function 与 Query Type 的发布、版本绑定及兼容策略需结合 Function/Query API 页面与具体环境继续核实。

## 复刻启示

- 把 Query Type 建模为受版本管理的逻辑资源：API 名、展示名、描述、输入参数 schema、输出 schema、实现引用、版本、发布状态与适用分支。
- 对 Agent 暴露时，应由 schema 驱动工具参数校验，并记录执行采用的逻辑版本；画布中显示逻辑输入输出与所依赖的对象类型。
- 预览器需区分“元数据定义”与“运行结果”，并显示执行上下文，方便审阅者复现查询。
