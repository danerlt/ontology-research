<!-- 页面 URL：https://www.palantir.com/docs/zh/foundry/action-types/use-actions -->
<!-- 研读状态：已完成 -->

# 动作类型 • 在平台中使用操作 • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/action-types/use-actions)
- 官方中文来源：尚未确认（配对状态：not_applicable）
- 页面语言：中文
- 主题栏目：action-types
- 相关性：direct；本体动作文档
- 官方更新时间：2026-11-12T17:46:46.935Z
- 目录核对时间：2026-11-14T14:58:33Z
- 产品状态：官方中文页标注为未经验证的 AIP 机器翻译；英文原文为核对依据。

## 原文短摘录与翻译

> 英文原文：Action types can be seamlessly integrated across applications in Foundry.

> 中文译文：操作类型可以无缝集成到 Foundry 的各类应用中。

## 摘录译文

以上为英文短摘录及中文译文。官方中文页面为 AIP 机器翻译，准确性未经验证。

## 中文要点

- Action 可接入 Object Views、Object Explorer 和 Workshop；消费端只显示适用于当前单对象或所选对象集合的动作。
- Object View 可将动作配置为按钮、改标签/颜色、设参数默认值、覆盖参数可见性，并可选择直接应用默认值或先打开表单。
- Object Explorer 会按当前对象/集合上下文生成单条或批量操作入口；Workshop Button Group 还能触发事件、URL 或对象集导出。
- 官方中文页是未经验证的 AIP 机器翻译。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Single action type | 单对象动作类型 | 以单个对象引用参数为目标的操作。 |
| Bulk action type | 批量动作类型 | 以对象引用列表为目标、对当前选择集执行的动作。 |
| Button group | 按钮组 | Workshop 中用于呈现并应用动作的组件。 |

## 疑问与待验证项

- 立即应用动作时若隐藏参数无效，隐藏/禁用行为何时计算需要按消费端确认。
- 批量上下文下参数映射和对象集选择能否保证逐对象授权，需与 action limits 和对象安全文档交叉核验。

## 复刻启示

- Action 定义与各消费端实例应分离：同一动作可创建多个带不同默认值、文案和按钮样式的入口。
- 运行前基于对象类型、选择集和权限过滤动作目录；同时支持单个和批量操作而不复制业务逻辑。
