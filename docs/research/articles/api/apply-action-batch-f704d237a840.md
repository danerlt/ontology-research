<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/actions/apply-action-batch -->
<!-- 研读状态：已完成 -->

# Apply Action Batch (v2, latest) • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/actions/apply-action-batch)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/v2/ontologies-v2-resources
- 相关性：direct；Ontology REST API v2 参考
- 官方更新时间：2026-11-12T17:46:46.921Z
- 目录核对时间：2026-11-14T14:56:19Z
- 产品状态：常规 v2 批量写入接口；可选 branch 为实验性功能。

## 英文原文短摘录（每个来源不超过 25 词）

> “Applies multiple actions (of the same Action Type) using the given parameters.”

## 摘录译文

使用给定参数批量应用多个同一 Action Type 的 Action。

## 中文要点

- POST `/api/v2/ontologies/{ontology}/actions/{action}/applyBatch` 通过 `requests` 一次提交同一个 Action Type 的多组参数；OAuth 应用需要读写两个 scope。
- 单次最多应用 20 个 Action；如果只修改 Object Storage v2 对象且不调用 Functions，可能获得更高上限，但文档没有给出固定扩容值。
- Object Storage v1 编辑最终一致、v2 编辑在动作完成后立即可见；此端点当前不支持 notifications。
- 请求可指定 scenarioRid 和 branch（实验性）；响应类型提供 edits。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| applyBatch | 批量应用 | 一个端点按多组参数执行同一 Action Type。 |
| requests | 请求项列表 | 每项包含一次动作的参数。 |
| notifications | 通知 | 批量端点目前不支持的动作能力。 |
| Object Storage v1/v2 | 对象存储 v1/v2 | 两种存储的编辑可见性时序不同。 |

## 疑问与待验证项

- 文档没有给出超出 20 条时可获得的固定批次上限，调用方应按 20 设计并处理限制错误。
- 批次内单项失败、整批回滚和返回 edits 的粒度没有在本页展开，不能假设整批原子提交。
- 通知不支持范围可能影响依赖通知的业务工作流，需要单独验证。

## 复刻启示

- 批量提交界面默认限制 20 项，逐项展示参数和校验状态；只有真实部署能力确认后再开放更高上限。
- 保存批次级与单项级审计，并在设计中明确原子性边界；不要将批量请求简单包装成一个不可解释的整体。
- 对依赖通知的流程切换到逐项 Action 或在本地明确编排通知步骤。
