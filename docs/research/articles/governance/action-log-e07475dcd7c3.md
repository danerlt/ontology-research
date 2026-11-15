<!-- 页面 URL：https://www.palantir.com/docs/zh/foundry/action-types/action-log -->
<!-- 研读状态：已完成 -->

# 动作类型 • 操作日志 • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/action-types/action-log)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/action-types/action-log)
- 页面语言：中文
- 主题栏目：action-types
- 相关性：direct；本体动作文档
- 官方更新时间：2026-11-12T17:46:46.935Z
- 目录核对时间：2026-11-14T14:58:13Z
- 产品状态：官方中文页面明确提示为未经验证的 AIP 机器翻译；以英文现行页校对功能边界。

## 英文原文短摘录（每个来源不超过 25 词）

> “The action log models successful action submissions as object types to be analyzed and displayed in object-aware Foundry tooling.”

## 摘录译文

操作日志会将成功提交的操作建模为对象类型，供支持对象感知的 Foundry 工具分析和展示。

## 中文要点

- 中文页提供操作日志的建模目的、日志对象结构和时间线用途；一次动作可同时编辑多个对象，但对应一个日志对象并链接全部受影响对象。
- 日志包含动作标识、动作类型及版本、UTC 时间、用户、被编辑对象主键，以及可选的参数值和上下文属性。函数驱动操作需要配置 `Edits` 来源。
- 页面说明可将日志用于时间线审计，以回答谁在何时改了什么。它不等同于记录任意写入的全量编辑历史；日志仅在启用后生成。
- 该中文页提示是 AIP 自动翻译且准确性未经验证。英文现行页面还区分失败指标、撤销、未回填旧记录、媒体参数排除和若干日志摘要约束，遇到冲突应以英文现行页核对。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| 操作日志对象类型 | action log object type | 代表某个操作类型提交事件的对象类型，与 Action Type 一一对应。 |
| 操作时间线 | action log timeline | 将日志对象按时间呈现，用于审计变更背景。 |
| 编辑来源 | Edits provenance | 函数型操作生成日志所需的来源配置。 |

## 疑问与待验证项

- 本页是官方机器翻译，并提示准确性未经验证；英文页内容更完整。不要仅凭中文页“所有操作提交”的措辞推断所有写入都留痕，英文明确日志只记录成功且由 Action Type 发起的提交。
- 时间线和日志对象的访问权限、敏感参数是否落日志，需要在权限模型和字段安全设计中继续核对。

## 复刻启示

- 日志应作为带关联关系的一等领域对象建模，保存操作决策上下文，而不只是写一段不可查询的文本；时间线按对象可聚合多种操作日志。
- 审计界面要提示覆盖范围、启动时间和机器翻译不确定性；对参数、对象字段和 side effect provenance 实施字段级允许列表与授权检查。
