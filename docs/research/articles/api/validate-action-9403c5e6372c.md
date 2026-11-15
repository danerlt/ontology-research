<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/ontology-resources/actions/validate-action -->
<!-- 研读状态：已完成 -->

# Validate Action • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/ontology-resources/actions/validate-action)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/ontology-resources/actions
- 相关性：direct；Ontology API 兼容参考
- 官方更新时间：2026-11-12T17:46:46.923Z
- 目录核对时间：2026-11-14T14:55:01Z
- 产品状态：v1 Validate Action 兼容入口，执行前预验证 API

## 英文原文短摘录（每个来源不超过 25 词）

> “Validates if an action can be run with the given set of parameters.”

## 摘录译文

验证给定参数能否用于运行某个动作。

## 中文要点

该兼容路径对应 v1 的动作预验证端点：检查参数和提交条件，返回整体有效性与逐参数评估，但不应用变更。它为了性能不读取现有对象数据，因而不验证主键唯一性或用户引用是否存在；未给参数按 null，Action 参数默认值当前不受支持。端点使用 `api:ontologies-read` OAuth2 范围。目录 canonical 路由为 `/api/v1/ontology-resources/actions/validate-action`。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Validation | 验证 | 对动作输入与提交条件做预检查 |
| Submission criteria | 提交条件 | 额外的动作可提交性判断 |
| `VALID` / `INVALID` | 有效 / 无效 | 返回的验证结论 |
| Side effect | 副作用 | 验证阶段不会执行的本体写入 |

## 疑问与待验证项

- 验证通过不是提交成功的承诺；对象状态变化可能在验证后发生，执行阶段必须重新校验。
- 本页未说明数据相关检查的其他范围，需查看 Apply Action 和对象权限文档。

## 复刻启示

- 前端将 dry-run 状态和最终写入状态并列呈现，明确解释验证没有读取的运行时条件。
- 为 Agent 工具设计“validate → 人类确认 → apply → 读取结果”链路，并在 apply 服务端做最后防线。
