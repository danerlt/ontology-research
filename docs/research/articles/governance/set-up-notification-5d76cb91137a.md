<!-- 页面 URL：https://www.palantir.com/docs/foundry/action-types/set-up-notification -->
<!-- 研读状态：已完成 -->

# 动作类型 • 配置通知 • Set up a notification • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/action-types/set-up-notification)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/action-types/set-up-notification)（配对状态：matched）
- 页面语言：英文
- 主题栏目：action-types
- 相关性：direct；本体动作文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:02:06Z
- 产品状态：通知教程将对象属性中的 Foundry 用户 ID 用作收件人，并用模板填充内容及对象视图链接。

## 英文原文短摘录（每个来源不超过 25 词）

> “the recipient must always be a Foundry user ID.”

## 摘录译文

收件人必须始终是 Foundry 用户 ID。

## 中文要点

- 教程以前置 Alert 对象可编辑以及优先级 Action 为基础，在 Rules 中加入 Notification。
- 收件人可从被编辑对象的 Case Managers 属性读取，但该字段必须存 Foundry 用户 ID；普通邮件地址不会产生通知。
- 模板内容可以引用收件人、当前用户、对象参数和属性，组成主题、正文及指向对象视图的按钮链接。
- 教程建议先用测试收件人验证逻辑与内容，再以测试对象触发 Action 检查最终送达。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Recipient from object property | 从对象属性取收件人 | 按目标对象中存储的用户身份字段发送 |
| Notification template | 通知模板 | 不编写函数即可配置主题/正文引用 |
| Object View link | 对象视图链接 | 通知中跳转至目标对象详情的按钮 |

## 疑问与待验证项

- 教程样例要求属性存用户 ID；组织账号禁用、用户离组或通知偏好关闭时的失败/投递状态需另查通知概览页。
- 模板引用的旧优先级应使用执行前对象快照还是显式旧值参数，需与 Action 规则时序一致。

## 复刻启示

- 收件人字段建立类型约束，使用 Foundry user identity 而非任意邮箱字符串；在测试发送界面验证解析结果。
- 通知预览应显示最终收件人、敏感字段权限、引用值来源和对象跳转目标。
