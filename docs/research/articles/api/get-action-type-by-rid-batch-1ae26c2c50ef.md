<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/action-types/get-action-type-by-rid-batch -->
<!-- 研读状态：已完成 -->

# Get Action Type By Rid Batch • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/action-types/get-action-type-by-rid-batch)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/v2/ontologies-v2-resources
- 相关性：direct；本体动作文档
- 官方更新时间：2026-11-12T17:46:46.921Z
- 目录核对时间：2026-11-14T14:56:13Z
- 产品状态：预览接口；请求必须加 `preview=true`，可选 branch 仍为实验性功能。

## 英文原文短摘录（每个来源不超过 25 词）

> “Gets a list of action types by RID in bulk.”

## 摘录译文

按 RID 批量获取 Action Type 列表。

## 中文要点

- POST `/api/v2/ontologies/{ontology}/actionTypes/getByRidBatch` 批量查询 Action Type；请求 query 必须传 `preview=true`，最大批次为 100，OAuth 需要 `api:ontologies-read`。
- 响应会过滤不存在或当前令牌无权限访问的类型，因此缺少某项不能直接区分“资源不存在”和“无权查看”。
- 可选 branch 会读取指定分支的定义，分支本身仍标为实验性功能。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| batch lookup | 批量查询 | 一次请求按多个 RID 取回动作定义。 |
| preview | 预览标记 | 启用此预览 API 所必需的 query 参数。 |
| permission filtering | 权限过滤 | 不存在或调用方无权访问的类型都不会出现在响应中。 |

## 疑问与待验证项

- 响应过滤会隐藏资源是否存在；调用端需避免把未返回项误报为确定的 404。
- 页面没有展开单项失败、重复 RID 和超大请求的错误结构。

## 复刻启示

- 批量详情 API 需限流并校验批次上限；本地预览 API 应显式提示权限过滤造成的结果不完整。
- 不要把预览接口当作正式集成依赖；内部先用普通单项读取实现，再将批量优化作为可替换适配器。
