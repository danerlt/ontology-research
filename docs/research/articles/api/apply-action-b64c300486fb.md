<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/ontology-resources/actions/apply-action -->
<!-- 研读状态：已完成 -->

# Apply Action (v1) • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/ontology-resources/actions/apply-action)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/ontology-resources/actions
- 相关性：direct；Ontology API v1 端点参考；保留作兼容性对照，并优先关注 v2
- 官方更新时间：2026-11-12T17:46:46.923Z
- 目录核对时间：2026-11-14T14:55:01Z
- 产品状态：v1 Apply Action 兼容入口；执行写入需要读写 scope

## 英文原文短摘录（每个来源不超过 25 词）

> “Applies an action using the given parameters.”

## 摘录译文

使用给定参数应用一个动作。

## 中文要点

此兼容入口对应 v1 单次 Action 执行端点。它接受本体 RID、动作类型 API 名和参数，执行本体写入；OAuth2 需要 `api:ontologies-read` 与 `api:ontologies-write`。参数默认值不受支持。OSv1 编辑最终一致，OSv2 编辑在动作完成后立即可见。该请求的成功示例返回 `{}`，canonical 路由为 `/api/v1/ontology-resources/actions/apply-action`。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Apply Action | 应用动作 | 单次本体写入调用 |
| Object Storage v1/v2 | 对象存储 v1/v2 | 写入可见一致性行为不同 |
| `api:ontologies-write` | 本体写入范围 | 调用所需的 OAuth2 scope |
| Canonical URL | 规范地址 | 目录标记的主要 v1 路由 |

## 疑问与待验证项

- `{}` 响应不包含对象快照，调用方需要单独读取目标对象或查看审计记录。
- 文档未说明客户端可安全重试的情形；超时后应先查询结果或使用业务幂等键。

## 复刻启示

- 将写操作状态与本体读模型更新时间分开追踪，并针对 OSv1 最终一致提供刷新/等待机制。
- 外部 Agent 工具禁止直接暴露无约束的写请求；采用参数 schema 校验、幂等策略和审计日志。
