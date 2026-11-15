<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/ontology-interfaces/list-interface-types -->
<!-- 研读状态：已完成 -->

# List Interface Types • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/ontology-interfaces/list-interface-types)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/v2/ontologies-v2-resources
- 相关性：direct；Ontology REST API v2 参考
- 官方更新时间：2026-11-12T17:46:46.921Z
- 目录核对时间：2026-11-14T14:57:16Z
- 产品状态：Preview；调用需传 `preview=true`，分页可能返回少于请求页大小的结果

## 英文原文短摘录（每个来源不超过 25 词）

> “Lists the interface types for the given Ontology.”

## 摘录译文

列出指定本体中的接口类型。

## 中文要点

`GET /api/v2/ontologies/{ontology}/interfaceTypes` 列出本体中的接口类型。接口 API 当前处于 Preview，查询需带 `preview=true`；可选实验性分支。分页默认 `pageSize=500`，使用响应 `nextPageToken` 继续读取；单页可能小于请求数量，但若仍有后续数据，响应至少包含一条。第三方 OAuth2 应用需 `api:ontologies-read`。响应含接口简要结构及 `nextPageToken`，继续拉取时需原样带回令牌。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| List Interface Types | 列出接口类型 | 本体级接口类型枚举读取端点 |
| `pageSize` | 页大小 | 可请求的单页数量，默认 500，不保证恰好返回该数量 |
| `pageToken` / `nextPageToken` | 分页令牌 | 从响应取下一页令牌并放入后续请求 |
| Preview | 预览功能 | 请求需显式启用，接口可能调整或移除 |

## 疑问与待验证项

- 文档没有承诺分页快照一致性；如果并发发生接口变更，跨页枚举是否重复或遗漏需要用实际服务验证。
- `branch` 被标为实验性且并非所有工作流支持；页面未逐一列出兼容能力。

## 复刻启示

- 本地画布加载大量接口时应采用服务端分页、可取消请求和稳定排序；不要把每次响应页当作完整图谱。
- 目录同步保存本体、分支、分页游标和抓取时间，检测变化后更新节点和继承/实现边；授权按当前项目本体作用域校验。
