<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/actions/apply-action-batch -->
<!-- 研读状态：已完成 -->

# Apply Action Batch (v2, latest) • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/actions/apply-action-batch)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/ontologies-v2-resources/actions
- 相关性：direct；Ontology REST API v2 参考
- 官方更新时间：2026-11-12T17:46:46.921Z
- 目录核对时间：2026-11-14T14:53:33Z
- 产品状态：按当前 API 参考整理；批量与分支能力以页面限制为准。

## 英文原文短摘录（每个来源不超过 25 词）

> “Applies multiple actions (of the same Action Type) using the given parameters.”

## 摘录译文

使用给定参数批量应用多个同类型 Action。

## 中文要点

- POST `/api/v2/ontologies/{ontology}/actions/{action}/applyBatch` 对同一个 Action Type 批量提交多组参数。
- 通常一次最多 20 个动作；仅修改 OSv2 对象且不调用 Functions 的动作可能有更高上限。通知副作用当前不支持此端点。
- OSv1 对象/链接编辑最终一致，OSv2 在动作完成后立即可见；支持 scenarioRid 或 branch，上述 branch 工作流仍有实验限制。第三方 OAuth 需本体读写 scope。
- 请求体包含 requests 数组；文档例子响应为空对象，未在本页展示逐项校验详情。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| applyBatch | 批量应用 | 对同一动作类型提交多条参数组。 |
| Object Storage v1/v2 | 对象存储 v1/v2 | 两种存储的可见时序不同。 |
| notification side effect | 通知副作用 | 此批量 API 当前不支持通知。 |

## 疑问与待验证项

- 较高批量上限的具体阈值和适用条件未在本页给出。
- 部分失败时是否逐条成功、回滚或原子提交，需要实测或查更具体事务文档。

## 复刻启示

- 批量执行界面应显示每条输入行的结果，并明确是否具有原子性；不能从空响应推断全部成功。
- 数量限制、对象存储可见时序和副作用支持应写入 Action 类型的运行约束。
