<!-- 页面 URL：https://www.palantir.com/docs/foundry/object-permissioning/object-security-policies -->
<!-- 研读状态：已完成 -->

# Object permissioning • Object security policies • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/object-permissioning/object-security-policies)
- 官方中文来源：尚未确认（配对状态：ambiguous）
- 页面语言：英文
- 主题栏目：object-permissioning
- 相关性：direct；本体对象权限文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:04:28Z
- 产品状态：当前页面介绍对象级行权限和属性级列权限的组合；权限在读取时强制执行，导出/下游传播需配合 markings 或 CBAC。

## 英文原文短摘录（每个来源不超过 25 词）

> “Object and property security policies filter what a user can read.”

## 摘录译文

对象与属性安全策略会筛选用户可以读取的内容。

## 中文要点

- 用户查看对象需有 object type Viewer 权限，并通过配置的 object policy、marking、organization、classification 等检查；属性值还需通过对应 property policy。
- 未通过对象策略时对象不可见；通过对象策略但未通过某属性策略时，该属性值显示 null。对象策略默认作用于所有属性，属性策略在此基础上再加限制。
- 项目权限模型下配置策略通常要求对象类型所在项目的 Owner。legacy datasource-derived 模型仍要求底层 datasource Viewer，且下载权限另行评估。
- 属性策略要求先有对象策略，不能保护主键，同一非主键属性至多加入一条属性策略；限制条件不宜用 group/marking/org membership 的 NOT。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| object security policy | 对象安全策略 | 控制对象实例行是否可见。 |
| property security policy | 属性安全策略 | 在对象可见基础上进一步控制属性值。 |
| mandatory control property | 强制控制属性 | 用对象字段携带每行所需的 markings 等访问条件。 |

## 疑问与待验证项

- - 页面明确说明 granular policies 是 read-time only，下载、导出及派生数据需要检查传播模型；不能仅测试 API 的单对象读取。
- - Derived property 可见性测试在此页面列为限制，因为源对象权限会参与计算；试算引擎要按路径上的每个对象逐跳执行权限检查。

## 复刻启示

- - 数据 API 应返回“对象隐藏”与“属性值脱敏为 null”两种明确授权结果；不要把前端隐藏当权限边界。
- - 权限试算器按用户、对象、属性和 marking 评估并逐项解释；派生值必须计算路径上所有源对象的有效权限。
