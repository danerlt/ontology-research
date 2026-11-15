<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/ontology-resources/actions/apply-action-batch -->
<!-- 研读状态：已完成 -->

# Apply Action Batch (v1) • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/ontology-resources/actions/apply-action-batch)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/ontology-resources/actions
- 相关性：direct；Ontology API v1 端点参考；保留作兼容性对照，并优先关注 v2
- 官方更新时间：2026-11-12T17:46:46.923Z
- 目录核对时间：2026-11-14T14:55:01Z
- 产品状态：v1 批量写入 API；默认上限 20，特定 OSv2 场景可能更高

## 英文原文短摘录（每个来源不超过 25 词）

> “Applies multiple actions (of the same Action Type) using the given parameters.”

## 摘录译文

使用给定参数应用多个同一 Action Type 的动作。

## 中文要点

`POST /api/v1/ontologies/{ontologyRid}/actions/{actionType}/applyBatch` 用一组请求批量运行同一 Action Type。通常每次最多 20 个动作；仅修改 Object Storage v2 且不调用 Functions 的动作可能有更高上限。该端点不支持参数默认值和 notifications；第三方 OAuth2 需要 `api:ontologies-read` 与 `api:ontologies-write`。OSv1 写入最终一致、OSv2 完成后即时可见。页面未承诺整批请求原子提交，不能把 batch 误当数据库事务。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Apply Action Batch | 批量应用动作 | 同一 Action Type 的多组参数请求 |
| `requests` | 请求列表 | 每项包含一个 Apply Action 参数对象 |
| Batch limit | 批量上限 | 通常最多 20，部分纯 OSv2/no-Function 场景可能更高 |
| Notification | 通知 | 此 batch API 当前不支持的副作用配置 |

## 疑问与待验证项

- 更高 batch 上限的具体数值与触发条件依文档和租户限制，须在目标环境核实。
- API 文档没有描述部分失败、逐项结果映射和原子性承诺；需要依赖响应 schema 与实际行为验证。

## 复刻启示

- 批量执行器根据目标存储和是否调用 Function 做容量控制，不能固定采用任意大 batch。
- 本地微服务应逐项关联输入、验证结果和写入结果；只有明确保证时才能提供“整批原子”的 UI 表述。
