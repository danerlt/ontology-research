<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/v1/ontology-resources/action-types/list-action-types -->
<!-- 研读状态：已完成 -->

# List Action Types (v1) • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/v1/ontology-resources/action-types/list-action-types)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/v1/ontology-resources
- 相关性：direct；Ontology API v1 端点参考；保留作兼容性对照，并优先关注 v2
- 官方更新时间：2026-11-12T17:46:46.923Z
- 目录核对时间：2026-11-14T14:55:34Z
- 产品状态：v1 只读分页 API；OAuth2 第三方应用需 `api:ontologies-read`

## 英文原文短摘录（每个来源不超过 25 词）

> “Lists the action types for the given Ontology.”

## 摘录译文

列出指定本体中的动作类型。

## 中文要点

`GET /api/v1/ontologies/{ontologyRid}/actionTypes` 分页枚举本体动作类型。路径使用本体 RID；默认页大小 500，可通过 `pageSize` 调整，并用响应 `nextPageToken` 作为下一次请求的 `pageToken`。服务允许单页少于请求大小，但如果还有结果则至少返回一条。OAuth2 第三方调用要求 `api:ontologies-read`。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| List Action Types | 列出动作类型 | 本体级动作定义发现端点 |
| `pageSize` | 页大小 | 默认 500，实际页可能更小 |
| `nextPageToken` | 下一页令牌 | 传回后续请求的 `pageToken` |
| `ontologyRid` | 本体 RID | 限定列举范围的资源标识 |

## 疑问与待验证项

- 页面没有承诺跨页快照一致性；动作类型并发变更时同步器需防止重复和遗漏。
- 列表结果是只读发现，不说明哪些类型当前用户实际有权执行。

## 复刻启示

- 动作目录采用分页加载和增量同步，并展示状态过滤；执行权限仍按调用人逐项服务端校验。
- 多项目场景按项目授权映射到本体 RID，不能用同一动作目录缓存替代项目隔离。
