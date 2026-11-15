<!-- 页面 URL：https://www.palantir.com/docs/foundry/action-types/configure-sections -->
<!-- 研读状态：已完成 -->

# 动作类型 • 配置表单分区 • Configure sections • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/action-types/configure-sections)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/action-types/configure-sections)（配对状态：matched）
- 页面语言：英文
- 主题栏目：action-types
- 相关性：direct；本体动作文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:02:11Z
- 产品状态：Action 表单可按参数分组，并配置列、说明、折叠、隐藏和条件展示行为。

## 英文原文短摘录（每个来源不超过 25 词）

> “These sections provide a logical grouping of parameters to organize an action form.”

## 摘录译文

这些分区可将参数按逻辑分组，用于组织 Action 表单。

## 中文要点

- 分区可配置标题、单列或双列布局及用户可见说明；说明始终显示在分区内，不像参数说明那样只出现在提示气泡。
- 分区可以折叠或隐藏，并可设置条件覆盖；例如先隐藏，在用户填入前序参数后再展示后续输入。
- 可在分区配置页新建/移动参数，也可在 Form 总览中拖动调整；分区及参数按表单内容中的顺序呈现。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Action form section | 动作表单分区 | 用于组织一组相关参数的表单容器 |
| Conditional override | 条件覆盖 | 根据其他参数状态改变分区显示/配置 |
| Form content | 表单内容 | 定义分区和参数显示顺序的结构 |

## 疑问与待验证项

- 条件覆盖的求值时机、嵌套分区约束和参数验证联动需在编辑器中验证。
- 分区布局属于表单呈现层，不应改变参数 schema 或服务端授权结果。

## 复刻启示

- Action 参数 schema 与表单布局分层存储；布局支持拖动排序、折叠和条件显示，并保留可访问性和窄屏适配。
- 条件展示只负责降低表单复杂度，隐藏输入不能替代服务端提交条件或权限校验。
