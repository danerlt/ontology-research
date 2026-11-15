<!-- 页面 URL：https://www.palantir.com/docs/foundry/action-types/parameters-override -->
<!-- 研读状态：已完成 -->

# 动作类型 • 参数覆盖 • Overrides • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/action-types/parameters-override)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/action-types/parameters-override)（配对状态：matched）
- 页面语言：英文
- 主题栏目：action-types
- 相关性：direct；本体动作文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:01:57Z
- 产品状态：覆盖按条件改变参数约束、可见性、必填和默认值；多条命中时只有第一条生效。

## 英文原文短摘录（每个来源不超过 25 词）

> “if more than one is true, only the first one will be executed.”

## 摘录译文

如果多个覆盖条件同时为真，只会执行第一条。

## 中文要点

- 覆盖用于按用户/参数等条件改变参数行为，减少仅因表单略有不同而拆分多个 Action 的需要。
- 每个参数可有多个覆盖块；条件只可引用表单层级中位于当前参数之前的参数。
- 一个覆盖块可组合多项条件以及多项结果；结果可改变约束、显示/隐藏、必填状态和默认值。
- 多条覆盖条件同时成立时按配置顺序只执行第一条，必须把顺序视作业务逻辑。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Override block | 覆盖块 | 包含 if 条件与 then 参数配置变更的规则块 |
| Visibility override | 可见性覆盖 | 按条件控制参数显示或隐藏 |
| First-match behavior | 首条命中 | 多个覆盖同时成立时仅应用首个覆盖块 |

## 疑问与待验证项

- 配置顺序决定命中结果，界面重排是否影响优先级需要本地明确并做冲突提示。
- 条件仅允许引用前序参数，复杂角色授权仍应由服务端提交标准与权限规则完成。

## 复刻启示

- 参数覆盖可保存为有序决策表，编辑器检测重叠条件并显示命中顺序预览。
- 覆盖结果改变表单体验，不得替代后端对提交人、目标对象和最终变更的授权。
