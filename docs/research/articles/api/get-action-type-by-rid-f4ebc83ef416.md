<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/action-types/get-action-type-by-rid -->
<!-- 研读状态：已完成 -->

# Get Action Type By Rid • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/action-types/get-action-type-by-rid)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/v2/ontologies-v2-resources
- 相关性：direct；本体动作文档
- 官方更新时间：2026-11-12T17:46:46.921Z
- 目录核对时间：2026-11-14T14:56:13Z
- 产品状态：常规 v2 读取接口；可选 branch 参数属于实验性功能。

## 英文原文短摘录（每个来源不超过 25 词）

> “Gets a specific action type with the given RID.”

## 摘录译文

按给定的 RID 获取一个指定的 Action Type。

## 中文要点

- GET `/api/v2/ontologies/{ontology}/actionTypes/byRid/{actionTypeRid}` 按资源 RID 获取 Action Type；OAuth 应用需要 `api:ontologies-read`。
- 响应仍为 `ActionTypeV2`，字段包括参数、发布状态、操作规则、`toolDescription` 和返回类型；因此可用 RID 详情接口补齐画布或 Agent 工具目录元数据。
- 接口可指定 branch，但分支属于实验性能力；未指定时从默认分支读取。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| RID | 资源标识符 | 用于其他 Foundry API 间稳定引用 Action Type。 |
| ActionTypeV2 | Action Type v2 结构 | 按 RID 获取时返回的定义模型。 |
| branch | 分支 | 可选的定义读取来源；当前为实验性功能。 |

## 疑问与待验证项

- 当 RID 在指定分支不存在、已删除或调用方无权读取时，具体错误和权限隐藏策略需要实测。
- 本页未说明 RID 在本体分支之间是否始终稳定。

## 复刻启示

- 在画布和内部服务间用不可变 RID 关联动作定义，用 API 名供用户阅读与调用。
- 为 RID 查询保留本体/项目授权检查，并将分支上下文纳入读请求与审计。
