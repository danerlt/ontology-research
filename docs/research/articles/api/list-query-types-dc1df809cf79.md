<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/ontology-resources/query-types/list-query-types -->
<!-- 研读状态：已完成 -->

# List Query Types (v1) • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/ontology-resources/query-types/list-query-types)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/ontology-resources/query-types
- 相关性：direct；Ontology API v1 端点参考，保留兼容性对照并优先关注 v2
- 官方更新时间：2026-11-12T17:46:46.923Z
- 目录核对时间：2026-11-14T14:55:27Z
- 产品状态：页面未标注 Preview；默认页大小为 100

## 英文原文短摘录（每个来源不超过 25 词）

> “Lists the query types for the given Ontology.”

## 摘录译文

列出给定本体中的 Query Type。

## 中文要点

- `GET /api/v1/ontologies/{ontologyRid}/queryTypes` 列出当前用户可读本体的 Query Type；分页参数为 `pageSize`（默认 100）和 `pageToken`，响应包含 `data` 和可选 `nextPageToken`。
- 页可以小于请求页大小，但只要还有结果就保证至少返回一条。客户端应依据令牌继续读取而非以返回行数是否达到 pageSize 判断结束。
- 返回项是 QueryType 元数据对象，含 API 名、描述、参数、输出、RID 和版本。OAuth2 第三方应用需要 `api:ontologies-read`。
- v1 列表不含 v2 的 `branch` 参数，也没有“最新发布版本可能是 prerelease”的特定说明；样例本身仍展示 prerelease 版本字符串。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| List Query Types | 列出查询类型 | 获取一个本体中的查询逻辑定义集合 |
| pageSize | 页大小 | 请求期望的每页条目数，默认 100 |
| pageToken | 分页令牌 | 指定下一页读取起点 |
| QueryType | 查询类型元数据 | 含参数/输出 schema 和版本的资源定义 |

## 疑问与待验证项

- 分页期间 Query Type 新增、修改时是否保证快照一致性，本页没有说明。
- 样例含 prerelease 版本，但列表 API 未定义排序或稳定版筛选规则；生产锁定应使用详情接口/SDK 的版本控制能力。
- v1 无 branch 查询参数；从分支读取元数据应改用支持该功能的 v2 API 并核对实验状态。

## 复刻启示

- 列表使用游标分页并保留条目版本信息；客户端分页流程保持请求上下文稳定并容忍短页。
- 在本体管理台同时提供逻辑目录和版本状态，显示 prerelease；Agent 工具发布需固定 schema/版本，避免列表结果随发布自动改变。
- 权限按本体资源范围检查，未授权 Query Type 不应泄露名称、描述或参数 schema。
