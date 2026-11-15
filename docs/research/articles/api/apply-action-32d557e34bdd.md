<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/actions/apply-action -->
<!-- 研读状态：已完成 -->

# Apply Action (v2, latest) • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/actions/apply-action)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/v2/ontologies-v2-resources
- 相关性：direct；Ontology REST API v2 参考
- 官方更新时间：2026-11-12T17:46:46.921Z
- 目录核对时间：2026-11-14T14:56:19Z
- 产品状态：常规 v2 写入接口；可选 transactionId 与 branch 为实验性功能。

## 英文原文短摘录（每个来源不超过 25 词）

> “Applies an action using the given parameters.”

## 摘录译文

使用给定参数应用一个 Action。

## 中文要点

- POST `/api/v2/ontologies/{ontology}/actions/{action}/apply` 使用参数执行 Action Type；OAuth 应用同时需要 `api:ontologies-read` 与 `api:ontologies-write`。
- 请求体包含参数；响应可含 operationId、validation、edits 与 returnValue。HTTP 200 只说明服务器处理了请求，必须读取 validation 才能判断动作是否成功。
- 此端点当前不支持 Action 参数默认值。Object Storage v1 的对象/链接编辑最终一致；Object Storage v2 的编辑在动作完成后立即可见。
- 可选 scenarioRid 指定情景；transactionId 和 branch 是实验性能力，文档提醒并非所有事务/分支工作流均受支持。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| validation | 校验结果 | 判断动作是否实际应用成功的响应字段。 |
| edits | 编辑集 | 动作产生的对象或链接变化。 |
| returnValue | 返回值 | 动作定义输出的数据，可使用多种 JSON 编码。 |
| scenarioRid | 情景 RID | 指定动作应用到哪个本体情景。 |

## 疑问与待验证项

- 一次失败校验是否总有 HTTP 200 及稳定的 validation 结构，客户端应按完整错误 schema 处理。
- 本页未承诺 Action 的通用原子性、幂等键或重放安全；不能把 HTTP 成功响应等同于业务提交成功。
- V1 最终一致的可见延迟没有给出时间上限。

## 复刻启示

- 执行界面按参数 schema 生成表单，并在提交后分别呈现 HTTP 处理状态、业务 validation、变更列表与返回值。
- 情景和分支作为明确的执行上下文写入审计；为 V1/V2 数据源显示一致性提示，避免成功后读回旧值引起误判。
- Agent 调用动作前展示 toolDescription 和参数确认；高影响操作通过权限校验与审批记录保护。
