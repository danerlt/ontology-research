<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/actions/apply-action -->
<!-- 研读状态：已完成 -->

# Apply Action (v2, latest) • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/actions/apply-action)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/ontologies-v2-resources/actions
- 相关性：direct；Ontology REST API v2 参考
- 官方更新时间：2026-11-12T17:46:46.921Z
- 目录核对时间：2026-11-14T14:53:32Z
- 产品状态：按页面现行表述整理；涉及分支/事务的能力以 Preview 或实验性限制为准。

## 英文原文短摘录（每个来源不超过 25 词）

> “See the validation result in the response body to determine if the action was applied successfully.”

## 摘录译文

应查看响应正文中的校验结果来判断动作是否成功应用。

## 中文要点

- POST `/api/v2/ontologies/{ontology}/actions/{action}/apply` 提交参数并执行指定动作；OAuth 第三方客户端需要本体读、写两个 scope。
- HTTP 200 只说明服务端接收并处理请求，不代表 Action 校验通过；调用方必须解析 validation 结果。参数默认值当前不受此端点支持。
- V1 存储的对象/链接变更最终一致、可稍后可见；V2 存储在动作完成后立即可见。可指定 transactionId、scenarioRid 或 branch，但事务与分支工作流有实验性限制。
- 响应可能包含 operationId、validation、edits 和 returnValue；返回值支持对象引用、集合、结构、聚合等多种本体类型。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| validation result | 校验结果 | 决定动作是否真正应用的业务状态。 |
| scenarioRid | 场景 RID | 将动作应用到指定 Ontology Scenario 的上下文。 |
| operationId | 操作标识 | Action 运行的服务端操作标识。 |

## 疑问与待验证项

- 对于 scenarioRid 与 branch 同时传入时的优先级，本页没有给出；实现前需校验互斥/组合规则。
- V1/V2 可见性时序不同，客户端如何轮询或订阅结果未在此端点说明。

## 复刻启示

- 执行 UI 应区分 HTTP 传输成功、业务校验通过和变更已可见三个状态，避免成功提示误导。
- 分支和场景调用必须在执行记录中保存上下文，并向评审者展示预期变更与 validation 结果。
