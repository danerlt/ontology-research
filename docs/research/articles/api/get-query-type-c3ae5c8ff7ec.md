<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/query-types/get-query-type -->
<!-- 研读状态：已完成 -->

# Get Query Type (v2, latest) • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/query-types/get-query-type)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/ontologies-v2-resources/query-types
- 相关性：direct；Ontology REST API v2 参考
- 官方更新时间：2026-11-12T17:46:46.922Z
- 目录核对时间：2026-11-14T14:54:27Z
- 产品状态：v2 元数据 GET；默认取最近发布版本（可含预发布），branch 支持仍属实验性

## 英文原文短摘录（每个来源不超过 25 词）

> “Gets a specific query type with the given API name.”

## 摘录译文

该端点按 API 名读取单个 Query Type 的元数据。

## 中文要点

- 端点为 `GET /api/v2/ontologies/{ontology}/queryTypes/{queryApiName}`，其中 Ontology 可用 API 名或 RID，查询类型以 API 名定位。OAuth2 第三方应用需 `api:ontologies-read`。
- `version` 可指定查询元数据版本；省略时读取最近发布版本，包括预发布版本。可选 `branch` 从本体分支加载元数据，但分支属于实验能力且并非所有工作流均支持。
- 返回 `QueryTypeV2`，包含 `apiName`、可选 `displayName`/`description`、参数映射、输出类型联合、Function RID、语义版本和可选 `typeReferences`。
- 参数和输出使用共享 Ontology 数据类型系统；示例将必填 `city:string` 映射为数组对象输出，表明该元数据可用于自动生成调用表单、类型化 SDK 与结果解析器。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| `queryApiName` | 查询 API 名称 | 定位需要读取的查询接口。 |
| `QueryTypeV2` | V2 查询类型元数据 | 描述查询参数、输出、Function RID 和版本的结构。 |
| `typeReferences` | 类型引用映射 | 为查询参数/输出使用的类型提供引用信息。 |
| `version` | 查询版本 | 指定查询定义版本，默认最近发布版本，包括预发布。 |
| `Function RID` | 函数资源标识 | 将查询类型元数据关联到 Foundry 函数资源。 |

## 疑问与待验证项

- 默认版本可能是预发布版本，因此读取元数据与执行查询时都应明确一致的版本策略，避免 UI 按一个版本生成表单却调用另一个版本。
- 元数据 `output` 为联合类型且可能嵌套，具体类型编码需查看 Execute Query 的返回值说明。
- `typeReferences` 可选，页面未提供所有复杂类型引用与 schema 解析示例。

## 复刻启示

- 实现可发现的查询注册表：以 `(project, ontology, apiName, version)` 为查询键并缓存输入输出 schema；分支上下文应独立隔离。
- Query Builder 与 Agent 工具参数表单均从 `parameters` 生成；输出预览按 `output` 类型构造适配器，未解析类型时拒绝静默降级为任意 JSON。
- 将函数 RID、API 名和语义版本分开保存，便于版本漂移诊断、审计追溯和兼容迁移。
