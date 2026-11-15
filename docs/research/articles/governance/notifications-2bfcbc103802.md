<!-- 页面 URL：https://www.palantir.com/docs/foundry/action-types/notifications -->
<!-- 研读状态：已完成 -->

# 动作类型 • 通知副作用 • Notifications • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/action-types/notifications)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/action-types/notifications)（配对状态：matched）
- 页面语言：英文
- 主题栏目：action-types
- 相关性：direct；本体动作文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:02:05Z
- 产品状态：通知是 Action 的副作用，收件人、通知内容和数据可见权限共同决定是否成功发送。

## 英文原文短摘录（每个来源不超过 25 词）

> “Notifications will be sent to each recipient individually.”

## 摘录译文

通知将分别发送给每位收件人。

## 中文要点

- 通知规则由 Action 的 Rules 添加；配置需要收件人和内容，可通过静态用户/组、对象属性或参数决定收件人。
- 通知内容可用模板或已发布函数生成，包含主题、正文、可选链接及邮件专用 HTML；收件人可按个人偏好接收站内或邮件通知。
- 收件人必须有权查看通知渲染的数据；默认要求所有收件人有权限，否则 Action 失败且编辑与通知均不发生；另一模式允许任一收件人有权并只通知有权限者。
- 开启严格/组级邮件脱敏时，自定义邮件内容会被通用脱敏消息替代；动态内容超长时会截断。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Notification side effect | 通知副作用 | 随 Action 执行向用户发送站内/邮件信息 |
| Recipient resolution | 收件人解析 | 把配置的用户、组或对象属性解析为接收对象 |
| Strict redaction | 严格脱敏 | 阻止邮件发送明文自定义内容的组织策略 |

## 疑问与待验证项

- 多收件人权限默认策略会改变整个 Action 是否成功；本地复刻需明确设置默认值并在 UI 展示影响。
- 通知产生时使用编辑前/后的对象快照，应按规则文档进一步核实；本概览仅说明各项配置与安全策略。

## 复刻启示

- 通知内容在发送前按每个收件人的对象权限过滤，并可选择全员权限门槛或仅向有权人员发送。
- 将邮件脱敏策略、长度截断、渠道偏好和 Action 编辑事务结果作为独立通知状态记录。
