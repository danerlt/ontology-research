<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/ontology-resources/query-types/get-query-type -->
<!-- 研读状态：已完成 -->

# Get Query Type (v1) • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/ontology-resources/query-types/get-query-type)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/ontology-resources/query-types
- 相关性：direct；Ontology API v1 端点参考，保留兼容性对照并优先关注 v2
- 官方更新时间：2026-11-12T17:46:46.923Z
- 目录核对时间：2026-11-14T14:55:27Z
- 产品状态：页面未标注 Preview；v1 返回类型模型较 v2 简化

## 英文原文短摘录（每个来源不超过 25 词）

> “Gets a specific query type with the given API name.”

## 摘录译文

按给定 API 名获取指定 Query Type。

## 中文要点

- `GET /api/v1/ontologies/{ontologyRid}/queryTypes/{queryApiName}` 读取单个查询类型元数据；OAuth2 第三方应用需要 `api:ontologies-read`。
- 响应 `QueryType` 包含 `apiName`、可选描述/显示名、参数映射、可选 output、RID 和语义版本。参数类型以 `baseType` 等 v1 结构表达，输出是 v1 union/原始类型模型。
- RID 指向 Function 资源，可用于和 Foundry 其他 API 交互；版本示例格式为 `major.minor.patch`，可有 prerelease tag。
- 页面没有版本或分支查询参数；v2 详情 endpoint 可选择版本、分支和 SDK 信息，因此跨版本取 schema 时不能假设参数等价。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| queryApiName | 查询 API 名 | 定位本体内查询类型的稳定名称 |
| parameters | 参数定义 | 每个输入参数的类型、描述和 required 标记 |
| output | 输出类型 | 查询执行结果的类型契约 |
| Function RID | 函数 RID | 关联此 Query Type 实现的 Foundry 资源 ID |

## 疑问与待验证项

- `output` 在 schema 中标记 optional；未声明输出时的执行响应/错误行为未在本页说明。
- 版本是否支持按版本查询由 v1 页面没有暴露；若消费者需要复现旧结果，应通过 v2 或版本锁定 SDK 验证。
- `version` 的语义是 Function 版本还是 Query Type 独立版本，文档以 Function 描述 RID，需以实际发布链路确认。

## 复刻启示

- 查询定义详情接口应返回完整参数和输出 schema，并包含实现 RID、版本与描述，供 UI 校验和 Agent 工具生成复用。
- v1/v2 数据传输模型应经显式适配器映射到统一内部 schema，保留原始字段以便兼容。
- 详情检查器展示“逻辑版本”和“实现版本”关系，不把 API 名当成版本锁定机制。
