<!-- 页面 URL：https://www.palantir.com/docs/zh/foundry/action-types/notifications -->
<!-- 研读状态：已完成 -->

# 动作类型 • Side effects • 通知 • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/action-types/notifications)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/action-types/notifications)
- 页面语言：中文
- 主题栏目：action-types
- 相关性：direct；本体动作文档
- 官方更新时间：2026-11-12T17:46:46.935Z
- 目录核对时间：2026-11-14T14:58:19Z
- 产品状态：官方中文页标注为未经验证的 AIP 机器翻译；英文原文为核对依据。

## 英文原文短摘录（每个来源不超过 25 词）

> “Notifications can be added to an action through the Add new rule dropdown menu.”

## 摘录译文

可通过“添加新规则”下拉菜单向 Action 添加通知。

## 中文要点

- 通知作为 Action 的副作用规则配置，至少包含接收人和内容；接收人可静态指定用户/组，也可以通过动作参数动态提供。
- 通知对每个接收人分别发送；电子邮件通知不支持 CC 收件人。
- 动态接收人的来源类型受参数类型限制，应确保执行用户无权向任意用户群体扩散敏感信息。
- 英文页面完整说明收件人和内容配置；官方中文页标有 AIP 机器翻译准确性未验证。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Notification side effect | 通知副作用 | 动作提交后发送的通知行为。 |
| Recipient | 接收人 | 接收动作通知的平台用户或组。 |
| CC recipient | 抄送收件人 | 电子邮件中的抄送字段；此处不受支持。 |

## 疑问与待验证项

- 通知是否随动作事务成功后发送、失败重试及去重策略需查看设置通知专页。
- 向动作参数指定用户/组作为接收人时，哪些角色可以配置该参数或改变默认值需结合权限模型检查。

## 复刻启示

- 将通知作为动作提交后的独立副作用配置，保存接收人来源、模板、发送状态和重试记录。
- 对动态收件人应用白名单/策略校验并记录审计；不要默认为邮件 CC 提供支持。
