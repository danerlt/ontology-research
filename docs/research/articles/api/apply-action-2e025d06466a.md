<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/v1/ontology-resources/actions/apply-action -->
<!-- 研读状态：已完成 -->

# Apply Action (v1) • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/v1/ontology-resources/actions/apply-action)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/v1/ontology-resources
- 相关性：direct；Ontology API v1 端点参考；保留作兼容性对照，并优先关注 v2
- 官方更新时间：2026-11-12T17:46:46.923Z
- 目录核对时间：2026-11-14T14:55:34Z
- 产品状态：v1 写入 API；OAuth2 第三方调用需读写两个 scope

## 英文原文短摘录（每个来源不超过 25 词）

> “Applies an action using the given parameters.”

## 摘录译文

使用给定参数应用一个动作。

## 中文要点

`POST /api/v1/ontologies/{ontologyRid}/actions/{actionType}/apply` 按动作类型和参数执行一次本体写入。OAuth2 第三方应用需要 `api:ontologies-read` 与 `api:ontologies-write`。此端点不支持参数默认值。写入 Object Storage v1 的对象/链接变更最终一致，可能延迟可见；写入 Object Storage v2 的编辑在动作完成后立即可见。接口成功响应示例为空对象 `{}`，调用成功本身不返回变更对象的完整快照。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Apply Action | 应用动作 | 对指定动作类型执行一次写入 |
| `actionType` | 动作类型 API 名 | 选择要执行的动作定义 |
| Eventual consistency | 最终一致性 | OSv1 的写入可在动作完成后延迟可见 |
| `api:ontologies-write` | 本体写入范围 | 第三方 OAuth2 写操作所需 scope |

## 疑问与待验证项

- 成功响应没有对象结果；需通过读对象 API 或 Action 回写对象标识来核对提交后的值。
- 页面没有定义幂等键、重试去重和并发冲突策略；网络超时后不能盲目重放非幂等动作。

## 复刻启示

- 执行端应把请求接受与数据实际可见分开表示，并对 OSv1 延迟刷新结果提供状态提示。
- Agent 写工具需要读写权限、参数默认值处理策略、重复提交保护及写后回读/审计。
