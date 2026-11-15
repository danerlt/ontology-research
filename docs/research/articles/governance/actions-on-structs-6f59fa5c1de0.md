<!-- 页面 URL：https://www.palantir.com/docs/foundry/action-types/actions-on-structs -->
<!-- 研读状态：已完成 -->

# Action types • Actions on structs • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/action-types/actions-on-structs)
- 官方中文来源：未找到确定的一对一官方中文页（配对状态：ambiguous）
- 页面语言：英文
- 主题栏目：action-types
- 相关性：direct；本体动作文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:02:02Z
- 产品状态：页面未标注 Beta 或 Preview；复合参数和属性字段映射有明确约束。

## 英文原文短摘录（每个来源不超过 25 词）

> “Struct property values can be created and modified with actions, through values supplied in a struct parameter.”

## 摘录译文

结构体参数以 `STRUCT` 为基础类型，包含具名且有独立基础类型的嵌套字段；这些字段整体映射到对象的结构属性。

## 中文要点

- Action 可通过结构体参数创建或修改结构属性；结构属性的每个字段须与参数字段逐一映射，字段基础类型必须相符，映射必须完整。
- 表单将结构体参数字段作为一个字段组呈现；默认值逐字段从指定对象类型的结构属性字段读取，字段约束也逐项配置，所有子字段都满足约束时整个参数才有效。
- 支持的参数字段基础类型列举为 Boolean、Date、Double、Geopoint、Integer、Long、String、Timestamp。结构属性不能从静态值或对象属性引用写入，也不能由多个结构体参数分别写入；结构字段不能拆开写入普通非结构属性。
- 对结构属性新增/删除字段或更改基础类型会影响相关 Action Type，必须一并更新动作映射。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| struct parameter | 结构体参数 | 将相关嵌套字段作为一个 Action 输入整体提交。 |
| struct property | 结构属性 | 对象类型上由多个具名字段组成的属性。 |
| field mapping | 字段映射 | 结构属性字段与 Action 参数字段的一对一映射。 |

## 疑问与待验证项

- 结构属性字段变化会使动作映射失配；上线时的模式迁移顺序、版本兼容和已有数据补齐需要结合结构属性类型编辑文档再核对。
- 列表中的基础类型集合可能受平台版本或 enrollment 变化影响，若要兼容更多类型需避免将当前清单写死为不可扩展的数据库枚举。

## 复刻启示

- 画布节点可把 Struct 当作可展开的复合属性；在属性检查器中显示字段类型、映射、默认来源和约束，表单按组提交完整对象。
- 发布分支前校验字段映射完整性、类型兼容、默认值来源和所有子字段约束；结构模式变化时生成受影响 Action Type 清单，并阻止不兼容的发布。
