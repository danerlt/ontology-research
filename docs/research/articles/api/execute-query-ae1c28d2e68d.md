<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/queries/execute-query -->
<!-- 研读状态：已完成 -->

# Execute Query (v2, latest) • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/queries/execute-query)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/ontologies-v2-resources/queries
- 相关性：direct；Ontology REST API v2 参考
- 官方更新时间：2026-11-12T17:46:46.922Z
- 目录核对时间：2026-11-14T14:54:25Z
- 产品状态：v2 执行默认使用最近发布版本（可能是预发布）；branch 与 transaction 上下文为实验功能

## 英文原文短摘录（每个来源不超过 25 词）

> “By default, the latest version of the Query is executed.”

## 摘录译文

默认情况下，执行最近发布版本的 Query。

## 中文要点

- 端点为 `POST /api/v2/ontologies/{ontology}/queries/{queryApiName}/execute`。请求体可传参数 ID 到 `DataValue` 的映射；路径使用本体 API 名/RID 与 Query API 名。
- 如果不指定 `version`，系统运行最近发布的 Query 版本；文档特别指出它可能是预发布版本。指定语义版本范围时，执行引擎会选择满足范围的版本。
- 可附加 `branch` 在分支上下文执行，未指定 version 时选该分支最新版（可包括预发布）；也可传 `scenarioRid` 在本体场景执行。branch 与 transaction 支持实验性且并非所有工作流适用。
- 响应主体为 `value:any`，但值必须按 Ontology 类型编码解码，可包含嵌套数组/Struct、附件 RID、对象/接口引用、对象集、二维/三维聚合和时间序列引用等。
- OAuth2 第三方客户端需 `api:ontologies-read`。该权限范围虽然叫 read，查询函数也可能执行其定义的业务逻辑；是否存在写入应由查询实现本身及其权限单独评审。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| `queryApiName` | 查询 API 名称 | 用于选择在 Ontology 中执行的已发布查询。 |
| `version` | 语义版本范围 | 执行时从满足条件的版本中选择一个版本。 |
| `scenarioRid` | 本体场景 RID | 将查询的本体上下文指向指定 Scenario。 |
| `ExecuteQueryResponse.value` | 查询结果值 | 按输出 Ontology 类型编码的任意/嵌套结果。 |
| `api:ontologies-read` | 本体读取范围 | OAuth2 第三方应用执行此查询端点的操作范围。 |

## 疑问与待验证项

- “latest”允许选中预发布版本；对生产调用而言，版本选择是否锁定、何时更新需由调用方明确，而非假设永远指向稳定版本。
- `value:any` 不代表未类型化输出；必须查 Query Type 或生成 SDK 得到参数/输出 schema，并正确编码 Decimal、Long、引用等特殊类型。
- 查询执行端点要求 `api:ontologies-read`，但本页没有描述 Query Function 内部调用其他资源时的逐项授权和副作用，需独立核查。

## 复刻启示

- Agent 工具目录根据 Query Type schema 暴露参数表单和返回类型；工具调用时要记录查询 API 名、锁定版本、分支/场景、输入参数和结果摘要。
- Query 执行结果按本体类型做 JSON 编码/解码，API 网关不能仅处理简单 JSON 原语；对象引用、对象集、聚合和时间序列需有专门的类型适配器。
- 设计版本策略：开发/预览可追踪最新分支版本，生产默认固定发布版本范围，变更经评审后显式升级。
- 将 API read scope 与查询内部副作用权限分开治理，防止只看到“read”就忽略可执行逻辑的风险。
