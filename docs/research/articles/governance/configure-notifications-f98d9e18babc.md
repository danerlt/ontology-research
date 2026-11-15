<!-- 页面 URL：https://www.palantir.com/docs/foundry/functions/configure-notifications -->
<!-- 研读状态：已完成 -->

# Functions • 配置通知 • Configure notifications • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/functions/configure-notifications)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/functions/configure-notifications)（配对状态：matched）
- 页面语言：英文
- 主题栏目：functions
- 相关性：direct；本体函数文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:02:44Z
- 产品状态：函数可以构造通知内容或收件人，使用 Principal/User/Group 等类型表达平台身份。

## 英文原文短摘录（每个来源不超过 25 词）

> “Functions can be used to flexibly configure notifications that should be sent in the platform.”

## 摘录译文

可以使用函数灵活配置要在平台内发送的通知。

## 中文要点

- 通知函数可产生站内通知及发往用户邮箱的通知；其主要身份参数类型包括 Principal、User、Group，通知内容使用平台 notification 类型。
- 函数可以返回自定义通知内容，按对象和用户动态生成标题、正文、邮件 HTML 及对象链接。
- 另一条路线是返回收件人列表，由函数按业务规则选择一个或多个用户/组。
- 通知生成函数由 Action 等消费，平台仍需按通知权限规则确定哪些收件人可获得对象数据。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Principal | 主体 | 代表 User 或 Group 的身份接口类型 |
| Notification | 通知对象 | 包含站内/邮件内容与链接的结构化结果 |
| Recipient function | 收件人函数 | 动态计算通知接收者的函数 |

## 疑问与待验证项

- 函数生成的收件人/内容与严格脱敏、每个收件人对象数据授权的交互，应以通知 Action 专页为准。
- 用户与组返回值解析、空收件人以及无权数据的失败策略需在真实环境验证。

## 复刻启示

- 通知生成与收件人决策可由独立函数实现，但调用时保留用户/组 ID、数据引用和权限过滤轨迹。
- 通知预览显示按收件人裁剪后的正文、对象链接和邮件脱敏状态。
