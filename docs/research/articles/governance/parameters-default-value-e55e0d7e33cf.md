<!-- 页面 URL：https://www.palantir.com/docs/foundry/action-types/parameters-default-value -->
<!-- 研读状态：已完成 -->

# 动作类型 • 设置参数默认值 • Set parameter default value • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/action-types/parameters-default-value)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/action-types/parameters-default-value)（配对状态：matched）
- 页面语言：英文
- 主题栏目：action-types
- 相关性：direct；本体动作文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:01:56Z
- 产品状态：默认值由 Action 参数配置统一定义，但宿主应用的本地覆盖优先级更高。

## 英文原文短摘录（每个来源不超过 25 词）

> “Default values for action type parameters are used to prefill parameters in the action form.”

## 摘录译文

Action 参数默认值用于预填动作表单中的参数。

## 中文要点

- 参数可使用固定常量或从对象参数读取属性；默认值配置在 Action 层，因此 Workshop、Object Explorer、Object Views、Quiver 和 Slate 可复用。
- 对象属性默认只允许引用在输入列表中排于当前参数之前的对象引用参数。
- 宿主应用的本地默认值/变量总是优先于 Action 全局默认值；迁移到全局默认前要清理原有局部覆盖。
- UUID、当前用户等特殊值可通过 type class 预填；为防用户手改，文档建议多数场景把该参数设为隐藏。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Static default | 静态默认值 | 对参数预置固定常量 |
| Object property default | 对象属性默认值 | 从选中的本体对象属性取值 |
| Type class | 类型类 | 用于自动生成 UUID、当前用户等特殊参数值的标记 |

## 疑问与待验证项

- 宿主级局部覆盖优先于全局配置会造成表单行为差异，改造时应能定位覆盖来源。
- 特殊值参数设为隐藏只是交互建议；最终值合法性和身份授权仍由服务端验证。

## 复刻启示

- 把默认值作为 Action 参数的共享配置，运行时保留“全局默认/宿主覆盖/用户编辑”三层来源。
- 提交摘要需区分用户主动修改与默认预填，并为旧值覆盖提供迁移诊断。
