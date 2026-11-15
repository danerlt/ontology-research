<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/query-types -->
<!-- 研读状态：已完成 -->

# Query Type basics (v2, latest) • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/query-types)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/ontologies-v2-resources/query-types
- 相关性：direct；Ontology REST API v2 参考
- 官方更新时间：2026-11-12T17:46:46.921Z
- 目录核对时间：2026-11-14T14:54:27Z
- 产品状态：Ontology REST API v2 的查询类型概念页；对应定义和运行接口分别由 Get Query Type、Execute Query 提供

## 英文原文短摘录（每个来源不超过 25 词）

> “A query type represents a logic that can be run in the Ontology.”

## 摘录译文

Query Type 表示可在本体中运行的一段逻辑。

## 中文要点

- 本页定义 Query Type 为可在 Ontology 中运行的逻辑，并说明其可由 Query Functions 创建。
- 它是简短的概念说明，不是 Query Type 的 JSON schema 或发布教程；实际元数据包括 apiName、展示名/描述、参数、输出联合类型、函数 RID、版本和可选的类型引用映射。
- 与 Query Type 对应的 Execute Query 端点负责按 `queryApiName` 执行，并接受参数与版本/分支/场景上下文；这两个能力在 API 中分开暴露。
- 文档中的 v2 Query Type basics 正文与 Query basics 页面相同，应将重复内容当成文档导航结构，而非额外对象语义。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| `Query Type` | 查询类型 | 查询逻辑的可发现、可调用接口定义。 |
| `Query Function` | 查询函数 | 创建 Query Type 的逻辑资源。 |
| `ParameterId` | 参数 ID | 查询调用和元数据中参数的 API 标识。 |
| `QueryDataType` | 查询数据类型 | 参数/输出联合类型中的 Ontology 类型描述。 |

## 疑问与待验证项

- 概念页没有约束输入参数的校验时机、函数副作用、执行超时或资源消耗，这些需到函数运行和治理文档核实。
- 区分 Query Function 实现资源 RID 与 Query Type API 名，外部调用用 API 名，其他 Foundry 资源关联可用函数 RID。
- 版本默认行为会包含预发布版本，需与 Execute Query/Get Query Type 的具体 endpoint 参数一起理解。

## 复刻启示

- 为查询资源保存定义版本、实现版本、输入输出类型及可调用权限，查询画布节点可据此生成稳定端口与类型检查。
- 执行前展示版本/预发布标记、参数约束和副作用说明；查询节点沿数据流输出对象集或类型化聚合结果，可连接到画布中的对象/关系节点。
- 让 Agent 的工具 schema 使用 Query Type 作为来源，输出调用轨迹和运行版本供评审与审计。
