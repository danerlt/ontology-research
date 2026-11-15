<!-- 页面 URL：https://www.palantir.com/docs/zh/foundry/functions/configure-notifications -->
<!-- 研读状态：已完成 -->

# 函数 • 配置通知 • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/functions/configure-notifications)
- 官方中文来源：尚未确认（配对状态：not_applicable）
- 页面语言：中文
- 主题栏目：functions
- 相关性：direct；本体函数文档
- 官方更新时间：2026-11-12T17:46:46.935Z
- 目录核对时间：2026-11-14T14:58:53Z
- 产品状态：官方中文页标注为未经验证的 AIP 机器翻译；英文原文为核对依据。

## 原文短摘录与翻译

> 英文原文：Functions can be used to flexibly configure notifications that should be sent in the platform.

> 中文译文：可以使用函数灵活配置要在平台中发送的通知。

## 摘录译文

以上为英文短摘录及中文译文。官方中文页面为 AIP 机器翻译，准确性未经验证。

## 中文要点

- 函数可返回平台内短通知和邮件通知内容；接收主体使用 `Principal`（User 或 Group），正文/标题可引用对象和关联链接。
- 通知模板以函数定义，可从对象状态构建动态内容；平台内通知与邮件正文是不同的结构化内容类型。
- 是否能向用户邮箱发外部邮件取决于租户权限/功能可用性，调用前需检验平台配置。官方中文页面为 AIP 机器翻译，准确性未经验证。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Principal | 主体 | 可表示用户或用户组的通知接收方。 |
| Short notification | 短通知 | 平台内显示的简短通知内容。 |
| Email notification content | 邮件通知内容 | 包含邮件标题、正文及对象链接的通知载荷。 |

## 疑问与待验证项

- 组主体如何展开为成员、邮件地址/外部邮件是否需要额外许可与发送速率限制未在此段完整说明。
- 函数构造通知与 Action notification side effect 在权限、审计、模板能力上的边界需跨文档比较。

## 复刻启示

- 通知能力支持多渠道内容模型和强类型主体；将用户/组解析与实际发送解耦并有失败状态。
- 为敏感对象内容做接收者权限过滤，发送后保留模板版本、对象链接和交付审计。
