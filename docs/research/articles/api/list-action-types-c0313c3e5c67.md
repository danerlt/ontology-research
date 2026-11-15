<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/action-types/list-action-types -->
<!-- 研读状态：已完成 -->

# List Action Types (v2, latest) • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/action-types/list-action-types)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/v2/ontologies-v2-resources
- 相关性：direct；本体动作文档
- 官方更新时间：2026-11-12T17:46:46.921Z
- 目录核对时间：2026-11-14T14:56:15Z
- 产品状态：常规 v2 列表接口；可选 branch 参数属于实验性功能。

## 英文原文短摘录（每个来源不超过 25 词）

> “Lists the action types for the given Ontology.”

## 摘录译文

列出给定 Ontology 中的 Action Type。

## 中文要点

- GET `/api/v2/ontologies/{ontology}/actionTypes` 列出本体内动作定义，OAuth 应用需要 `api:ontologies-read`。
- `pageSize` 默认 500，并使用分页令牌继续读取；实际返回页可能小于请求大小，但有更多结果时保证至少返回一项。
- 可选 branch 用于列出分支上的定义；分支功能当前为实验性。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| pageSize | 页大小 | 希望返回的页面条数，默认值为 500。 |
| nextPageToken | 下一页令牌 | 继续读取分页结果的游标。 |
| ActionTypeV2 | Action Type v2 结构 | 列表结果中的动作定义。 |

## 疑问与待验证项

- 若目录快照期间定义发生变化，分页读取是否能提供一致快照，本页没有说明。
- 页面强调返回页可小于 pageSize，实现时不能用短页推断遍历结束，应检查分页令牌。

## 复刻启示

- 管理台目录采用游标分页并以 `apiName`、显示名、发布状态和 Agent 工具说明支持搜索筛选。
- 对列表缓存标记本体与分支维度；消费方必须按照 nextPageToken 完成遍历。
