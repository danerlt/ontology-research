<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/action-types/list-action-types -->
<!-- 研读状态：已完成 -->

# List Action Types (v2, latest) • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/action-types/list-action-types)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/ontologies-v2-resources/action-types
- 相关性：direct；本体动作文档
- 官方更新时间：2026-11-12T17:46:46.921Z
- 目录核对时间：2026-11-14T14:53:30Z
- 产品状态：按页面现行表述整理；涉及分支/事务的能力以 Preview 或实验性限制为准。

## 英文原文短摘录（每个来源不超过 25 词）

> “Each page may be smaller than the requested page size.”

## 摘录译文

每一页的结果数可能少于请求的页大小。

## 中文要点

- GET `/api/v2/ontologies/{ontology}/actionTypes` 列出指定本体下的动作类型；OAuth scope 为 `api:ontologies-read`。
- 可以选择本体分支；分支为实验能力且并非所有工作流都支持。默认页大小为 500，使用 pageToken/nextPageToken 游标分页。
- 服务器可返回小于请求大小的一页，但若仍有结果，保证至少返回一条，客户端应以是否存在下一页令牌作为结束条件。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| pageSize | 页大小 | 默认 500；控制期望的返回条数。 |
| pageToken | 分页令牌 | 读取下一页时使用的游标。 |
| nextPageToken | 下一页令牌 | 告诉客户端是否仍有后续页。 |

## 疑问与待验证项

- 页面引用通用 page sizes 限制，具体允许的最大值应以通用 API 说明为准。
- 本端点是列表而非搜索；大量资源的筛选与检索策略需结合查询接口。

## 复刻启示

- 画布首次加载应采用游标分页并支持增量装载，避免假定一页等于完整图谱。
- 用户切换分支时缓存键必须包含 ontology 与 branch，防止混用主线和实验定义。
