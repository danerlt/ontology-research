<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/ontology-resources/action-types/list-action-types -->
<!-- 研读状态：已完成 -->

# List Action Types (v1) • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/ontology-resources/action-types/list-action-types)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/ontology-resources/action-types
- 相关性：direct；Ontology API v1 端点参考；保留作兼容性对照，并优先关注 v2
- 官方更新时间：2026-11-12T17:46:46.923Z
- 目录核对时间：2026-11-14T14:54:55Z
- 产品状态：v1 List Action Types 兼容入口，分页 API

## 英文原文短摘录（每个来源不超过 25 词）

> “Lists the action types for the given Ontology.”

## 摘录译文

列出指定本体中的动作类型。

## 中文要点

此兼容路径映射到 v1 List Action Types：用本体 RID 列举动作类型，默认 `pageSize=500`，通过 `pageToken` 与 `nextPageToken` 延续分页。返回页面可以少于请求大小；有后续结果时保证至少返回一条。OAuth2 第三方应用需要 `api:ontologies-read`。其 canonical 路由为 `/api/v1/ontology-resources/action-types/list-action-types`。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| `pageToken` | 分页令牌 | 请求中指定读取位置 |
| `nextPageToken` | 下一页令牌 | 响应中返回的续页位置 |
| `pageSize` | 页大小 | 默认 500，非固定返回条数 |
| OAuth2 scope | OAuth2 作用域 | `api:ontologies-read` |

## 疑问与待验证项

- 文档没有说明多页读取期间的快照和排序约定；需要在目录同步时对变化执行增量扫描。
- 路由兼容关系不等于动作执行权限，执行授权需独立判定。

## 复刻启示

- 大型动作工具目录按页懒加载，保存 cursor 和同步时间，前端搜索不应默认只用首页结果。
- 在多本体产品中把操作目录缓存与 `ontologyRid`、项目和用户授权绑定。
