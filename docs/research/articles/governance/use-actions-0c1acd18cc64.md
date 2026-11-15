<!-- 页面 URL：https://www.palantir.com/docs/foundry/action-types/use-actions -->
<!-- 研读状态：已完成 -->

# 动作类型 • 在平台中使用 Action • Use actions in the platform • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/action-types/use-actions)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/action-types/use-actions)（配对状态：matched）
- 页面语言：英文
- 主题栏目：action-types
- 相关性：direct；本体动作文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:01:51Z
- 产品状态：Action 类型可在对象视图、对象浏览器和 Workshop 复用；系统根据当前对象选择自动筛选适用动作。

## 英文原文短摘录（每个来源不超过 25 词）

> “Action types can be seamlessly integrated across applications in Foundry.”

## 摘录译文

Action 类型可以无缝集成到 Foundry 的多个应用中。

## 中文要点

- 单对象 Action 使用 Object Reference 参数；批量 Action 使用 Object Reference List 参数，应用只呈现匹配当前选择对象类型的动作。
- Object View 可添加带标签/颜色的动作按钮，选择打开表单或用有效默认值立即提交，也可按隐藏参数无效状态隐藏或禁用按钮。
- Object Explorer 在对象集、对象详情与已链接对象视图中按当前选择自动呈现适用的单体/批量动作。
- Workshop Button Group 还支持不同布局、图标/标签样式，并可触发 Workshop 事件、URL 或对象集导出。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Single action type | 单对象动作 | 通过单对象引用参数操作一个目标对象的 Action |
| Bulk action type | 批量动作 | 通过对象引用列表参数批量操作的 Action |
| Applicable action | 适用动作 | 与当前选择对象类型和参数基数匹配的 Action |

## 疑问与待验证项

- 各消费应用对默认值、隐藏参数、提交失败提示和批量执行的差异应独立校验。
- 按钮启用条件仅用于界面体验，不能替代提交时的权限与提交条件检查。

## 复刻启示

- 将 Action 的业务定义与各应用中的入口配置分开，可复用同一动作同时提供列表批量和对象详情单体调用。
- 入口根据对象集类型和基数筛选，提交前仍重新验证参数、权限、对象状态和默认值。
