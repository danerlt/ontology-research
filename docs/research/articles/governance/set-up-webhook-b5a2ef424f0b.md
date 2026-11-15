<!-- 页面 URL：https://www.palantir.com/docs/zh/foundry/action-types/set-up-webhook -->
<!-- 研读状态：已完成 -->

# 动作类型 • Side effects • 设置 Webhook • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/action-types/set-up-webhook)
- 官方中文来源：尚未确认（配对状态：not_applicable）
- 页面语言：中文
- 主题栏目：action-types
- 相关性：direct；本体动作文档
- 官方更新时间：2026-11-12T17:46:46.935Z
- 目录核对时间：2026-11-14T14:58:27Z
- 产品状态：官方中文页标注为未经验证的 AIP 机器翻译；英文原文为核对依据。

## 原文短摘录与翻译

> 英文原文：This makes the webhook run after objects are edited in Foundry.

> 中文译文：这会使 webhook 在 Foundry 中的对象编辑之后运行。

## 摘录译文

以上为英文短摘录及中文译文。官方中文页面为 AIP 机器翻译，准确性未经验证。

## 中文要点

- 动作可添加已配置的 Data Connection webhook，并把 webhook 输入映射到动作参数；同名输入参数会自动复用，缺少时才新建。
- Webhook 默认为副作用，在本体对象编辑后运行；切换为 writeback 后会先调用外部系统再执行对象编辑。
- writeback/副作用选择决定用户看到成功时点和失败处理：外部写回失败可阻止 Foundry 编辑；副作用可能在用户收到成功提示后才运行。
- 中文官方页为 AIP 机器翻译，执行顺序及错误语义须以英文为准。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Webhook | Webhook | 向外部 HTTP/连接器系统发起请求的已配置资源。 |
| Writeback | 写回 | 在本体对象变更之前执行的外部调用。 |
| Side effect | 副作用 | 本体编辑后执行的外部调用。 |

## 疑问与待验证项

- “一定程度的事务性”不意味着跨系统原子提交；外部成功而本体写入失败的补偿流程需业务自行设计。
- 入参映射、响应字段以及 webhook 版本升级策略应和 Data Connection webhook 契约一起复核。

## 复刻启示

- 外部写回建立状态机：待调用、外部成功/失败、本体提交成功/失败、待补偿；保留请求 ID 与重放能力。
- 动作设计器要明确展示 webhook 相对本体写入的先后、用户可见失败语义和可能的不一致窗口。
