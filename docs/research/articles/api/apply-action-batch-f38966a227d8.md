<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/v1/ontology-resources/actions/apply-action-batch -->
<!-- 研读状态：已完成 -->

# Apply Action Batch (v1) • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/v1/ontology-resources/actions/apply-action-batch)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/v1/ontology-resources
- 相关性：direct；Ontology API v1 端点参考；保留作兼容性对照，并优先关注 v2
- 官方更新时间：2026-11-12T17:46:46.923Z
- 目录核对时间：2026-11-14T14:55:34Z
- 产品状态：v1 批量写入 API；默认上限 20，notifications 不支持

## 英文原文短摘录（每个来源不超过 25 词）

> “Applies multiple actions (of the same Action Type) using the given parameters.”

## 摘录译文

使用给定参数应用多个同一 Action Type 的动作。

## 中文要点

v1 batch 端点用 `requests` 数组批量执行同一动作类型。通常一批最多 20 个；纯 Object Storage v2 且不调用 Functions 时可能有更高限制。默认参数和通知不支持；OAuth2 需要 ontology 读写范围。与单次 Apply Action 一样，OSv1 变更最终一致而 OSv2 在动作完成后即时可见。canonical 路由为 `/api/v1/ontology-resources/actions/apply-action-batch`。页面没有声明批处理事务原子性。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| `requests` | 请求列表 | 每个元素是一组同类型动作参数 |
| `applyBatch` | 批量应用 | 批量写入端点路径 |
| Eventual consistency | 最终一致性 | OSv1 对象修改的可见延迟 |
| OAuth2 scopes | OAuth2 作用域 | `api:ontologies-read` 与 `api:ontologies-write` |

## 疑问与待验证项

- 页面未明确部分失败、重试、逐条错误及事务回滚细节；应以响应结构和目标租户试运行确定。
- 更高批量限额不是普遍承诺，调用前需依据实际 Action 类型能力检查。

## 复刻启示

- 批量工具接口暴露最大请求数、每项结果和错误归属；超限拆批需可追踪而不伪装为原子事务。
- 对 Agent 的批量写操作增加逐项验证、用户确认和批次审计，并限制可批量调用的动作类型。
