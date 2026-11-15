<!-- 页面 URL：https://www.palantir.com/docs/foundry/action-types/parameters-filter -->
<!-- 研读状态：已完成 -->

# 动作类型 • 筛选参数下拉结果 • Filter results of a parameter dropdown menu • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/action-types/parameters-filter)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/action-types/parameters-filter)（配对状态：matched）
- 页面语言：英文
- 主题栏目：action-types
- 相关性：direct；本体动作文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:01:56Z
- 产品状态：参数下拉选项可由对象集、对象关系和参数过滤，并在提交前验证所选值。

## 英文原文短摘录（每个来源不超过 25 词）

> “The value selected is also validated before the action is executed.”

## 摘录译文

所选值也会在 Action 执行前经过验证。

## 中文要点

- 多选参数可以从对象集中取某个属性作为允许值；如果结果只有一个且参数必填，系统会自动预填该值。
- 从对象集生成选项时遵循用户对象可见权限，不会显示无权访问对象的属性。
- 对象引用参数可配置过滤器和 Search Around，以在不同 Action 界面中限制下拉对象；选中对象会在执行前再次校验。
- 筛选支持的操作因参数类型而异，应按页面的支持操作表配置。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Parameter dropdown filter | 参数下拉筛选 | 限制用户可选择的值/对象 |
| Search Around | 关系搜索 | 通过本体链接遍历缩小对象候选集 |
| Pre-submit validation | 提交前校验 | 执行 Action 前重新核对参数所选值 |

## 疑问与待验证项

- 候选对象变化或用户权限在表单打开后变化时，提交重验证可避免过期授权，但错误提示与重载体验需另行设计。
- Search Around 深度与循环关系在该页未作完整限制说明。

## 复刻启示

- 下拉候选项以带授权的对象集查询生成；提交时服务端重查所选对象仍满足过滤表达式。
- 对象集合的筛选语义需和动态表单依赖、敏感静态常量泄露防护一起审计。
