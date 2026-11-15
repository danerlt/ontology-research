<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/v1/ontology-resources/query-types/query-type-basics -->
<!-- 研读状态：已完成 -->

# Query Type basics (v1) • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/v1/ontology-resources/query-types/query-type-basics)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/v1/ontology-resources
- 相关性：direct；Ontology API v1 概念参考，保留兼容性对照并优先关注 v2
- 官方更新时间：2026-11-12T17:46:46.923Z
- 目录核对时间：2026-11-14T14:56:00Z
- 产品状态：基础说明页；与非显式 v1 路由内容相同

## 英文原文短摘录（每个来源不超过 25 词）

> “A query type represents a logic that can be run in the Ontology.”

## 摘录译文

Query Type 表示一段可在本体中运行的逻辑。

## 中文要点

- v1 基础页以一句话定义 Query Type：本体内可运行的查询逻辑；同页说明可通过 Query Functions 创建。
- 与同内容、不同路径的 `/api/ontology-resources/query-types/query-type-basics` 相比，此 URL 显式包含 `/v1`；目录分别保留，功能理解应归并到相同概念。
- 本页不定义参数结构、版本读取或运行结果格式；需查看 List/Get Query Type 与 Execute Query 端点。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Query Type | 查询类型 | 可在本体中执行的命名逻辑 |
| Query Function | 查询函数 | 创建查询类型的函数实现入口 |
| query logic | 查询逻辑 | 被封装为可调用资源的业务逻辑 |

## 疑问与待验证项

- 页面没有说明函数怎样转换为 Query Type、发布与权限的关系；需查 Query Functions 与 Ontology Manager 工作流。
- 这张卡对应的路径是否只是 REST v1 文档版本镜像，需依 canonical 规则确认；内容本身短且与同组定义重复。

## 复刻启示

- 将 Query Type 抽象为独立本体资源，元数据与执行 API 分层，参数/输出 schema 供控制台和 Agent 调用。
- 对不同文档版本路径做语义去重，但保留源 URL 与版本标记，避免目录统计掩盖真实 API 版本差异。
- Agent 工具注册只引用已发布、明确授权的查询逻辑，不能因 Query Function 存在就默认暴露。
