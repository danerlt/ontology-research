<!-- 页面 URL：https://www.palantir.com/docs/foundry/action-types/set-up-webhook -->
<!-- 研读状态：已完成 -->

# 动作类型 • 配置 Webhook • Set up a webhook • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/action-types/set-up-webhook)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/action-types/set-up-webhook)（配对状态：matched）
- 页面语言：英文
- 主题栏目：action-types
- 相关性：direct；本体动作文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:02:10Z
- 产品状态：Action 中的 Webhook 可选编辑前写回或编辑后副作用，并把动作参数映射到外部请求输入。

## 英文原文短摘录（每个来源不超过 25 词）

> “By default, the newly added webhook is configured as a side effect.”

## 摘录译文

新添加的 Webhook 默认配置为副作用。

## 中文要点

- 先准备基础 Action，再由有权限的管理员配置连接外部系统的 Webhook；在 Logic/Rules 中添加 Webhook 规则。
- 默认采用编辑后副作用；选择 Writeback 则会在本体对象编辑前调用外部系统。
- 选择 Webhook 及其版本，并将每个输入映射到 Action 参数；若名称相同会自动复用参数，否则会生成新参数。
- 确认写回阶段后保存；添加 Webhook 时生成但未使用的参数可以清理。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Webhook rule | Webhook 规则 | Action 调用外部系统的规则 |
| Writeback | 写回 | 在 Foundry 对象编辑之前调用外部系统 |
| Webhook input mapping | Webhook 输入映射 | 把 Action 参数绑定到外部请求输入 |

## 疑问与待验证项

- 连接外部系统需要的管理员配置与凭据生命周期由 Data Connection 管理；本教程不定义密钥轮换流程。
- 教程说明新增 Webhook 的版本可选，但未阐明版本升级与既有 Action 的兼容策略。

## 复刻启示

- 在动作编辑器中先明确外部调用发生于对象变更之前还是之后，再配置参数映射，保存时展示执行顺序。
- Webhook 版本、凭据引用、输入来源和错误处理均纳入动作审计；未使用的自动参数给出清理提示。
