<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/action-types/get-action-type-by-rid-batch -->
<!-- 研读状态：已完成 -->

# Get Action Type By Rid Batch • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/action-types/get-action-type-by-rid-batch)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/ontologies-v2-resources/action-types
- 相关性：direct；本体动作文档
- 官方更新时间：2026-11-12T17:46:46.921Z
- 目录核对时间：2026-11-14T14:53:29Z
- 产品状态：按当前 API 参考整理；批量与分支能力以页面限制为准。

## 英文原文短摘录（每个来源不超过 25 词）

> “Gets a list of action types by RID in bulk.”

## 摘录译文

按 RID 批量获取 Action Type。

## 中文要点

- POST `/api/v2/ontologies/{ontology}/actionTypes/getByRidBatch` 批量读取动作定义；请求体是 RID 请求列表，响应为 `data` 列表。
- 端点为 Preview，必须传 `preview=true`；单次最多 100 项，OAuth scope 为 `api:ontologies-read`。
- 不存在或调用令牌无权访问的动作会从响应中过滤掉，而不是分别返回错误项；可选 branch，但分支工作流支持有限。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| getByRidBatch | 按 RID 批量获取 | 一次请求读取多个动作定义。 |
| filtered response | 过滤后的响应 | 无资源或无权限项不会返回。 |
| preview | 预览能力 | 该端点处于可能变更的预览阶段。 |

## 疑问与待验证项

- 过滤掉无权限资源会让客户端无法区分不存在与无权访问；不要将缺项直接显示为已删除。
- 分支读取能力不代表所有 branch 工作流都可用。

## 复刻启示

- 读权限过滤行为应在批量图谱加载中保留，避免通过错误信息泄漏无权查看的资源。
- 对批次大小做 100 项上限校验，页面上区分部分结果和请求项数量。
