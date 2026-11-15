<!-- 页面 URL：https://www.palantir.com/docs/zh/foundry/action-types/set-up-notification -->
<!-- 研读状态：已完成 -->

# 动作类型 • Side effects • 设置通知 • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/action-types/set-up-notification)
- 官方中文来源：尚未确认（配对状态：not_applicable）
- 页面语言：中文
- 主题栏目：action-types
- 相关性：direct；本体动作文档
- 官方更新时间：2026-11-12T17:46:46.935Z
- 目录核对时间：2026-11-14T14:58:27Z
- 产品状态：官方中文页标注为未经验证的 AIP 机器翻译；英文原文为核对依据。

## 原文短摘录与翻译

> 英文原文：This tutorial demonstrates how to set up an action with a notification.

> 中文译文：本教程演示如何为操作配置通知。

## 摘录译文

以上为英文短摘录及中文译文。官方中文页面为 AIP 机器翻译，准确性未经验证。

## 中文要点

- 示例将 Alert 对象上的 assignee 用户属性作为通知收件人；收件人属性必须存储 Foundry user ID，普通邮件地址字符串不会触发平台通知。
- 通知内容可用模板插入参数值和对象属性，例如向收件人称呼并显示变更前后的优先级/状态。
- 教程依赖对象可编辑、动作已配置且对象上有负责人的前置条件；可先用固定收件人验证消息逻辑。
- 官方中文页提示 AIP 机器翻译未经验证，收件人 ID 类型和配置步骤需以英文原文核对。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Recipient from object property | 从对象属性取收件人 | 动作从目标对象属性读取接收通知的用户标识。 |
| Foundry user ID | Foundry 用户 ID | 平台通知系统识别用户的标识符。 |
| Notification template | 通知模板 | 由静态文本、参数与对象属性组成的消息内容。 |

## 疑问与待验证项

- 用户 ID 无效、用户停用或用户无通知权限时如何反馈，页面未说明；需检查通知执行日志与错误路径。
- 通知的送达/重试/幂等由何服务负责，应查通知副作用和平台监控文档。

## 复刻启示

- 通知配置应提供强类型收件人，不接受任意字符串误作 user ID；发送前校验目标用户/组。
- 模板只能引用获授权且明确列出的动作参数/对象属性，发送记录包含模板版本、收件人解析和结果状态。
