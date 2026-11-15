<!-- 页面 URL：https://www.palantir.com/docs/zh/foundry/pb-functions-expression/isValidOntologyGeopointV1 -->
<!-- 研读状态：已完成 -->

# PB函数表达式 • 是否为有效的Ontology GeoPoint • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/pb-functions-expression/isValidOntologyGeopointV1)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/pb-functions-expression/isValidOntologyGeopointV1)
- 页面语言：中文
- 主题栏目：pb-functions-expression
- 相关性：direct；标题或简介提及本体、对象、动作、权限或 Agent 主题
- 官方更新时间：2026-11-12T17:46:46.927Z
- 目录核对时间：2026-11-14T15:01:08Z
- 产品状态：官方中文路由的译文准确性未逐句验证；术语和规则按英文原文复核。

## 英文原文短摘录（每个来源不超过 25 词）

> “Returns true if the input is a valid Ontology GeoPoint.”

## 摘录译文

输入值是有效 Ontology GeoPoint 时返回 true。

## 中文要点

- 表达式输入为 String，输出 Boolean；格式要求是 `纬度,经度`，纬度在 -90 到 90 之间、经度在 -180 到 180 之间。
- 页面示例中坐标顺序颠倒、括号包裹、非坐标文本和 null 均返回 false；规范小数串返回 true。示例包含有空格分隔的合法形式。
- 该函数适合作为数据清洗/写入前的格式筛查；通过校验只说明符合函数认可的坐标形式，不代表位置业务规则满足。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| valid Ontology GeoPoint | 有效本体地理点 | 符合纬度、经度字符串格式与数值范围的值。 |
| Boolean | 布尔值 | 校验函数的 true/false 输出类型。 |
| coordinate order | 坐标顺序 | 本页采用纬度在前、经度在后的顺序。 |

## 疑问与待验证项

- 文档未明确字符串解析是否接受所有空白、符号、科学计数法或超长精度；示例不能代替完整输入语法规范。
- 本函数针对字段格式的判定，与地理索引器自身的拒绝/归一化规则是否完全一致，需要用目标环境试算确认。

## 复刻启示

- 把格式校验设计为类型级约束函数，并在数据导入、编辑表单和 Action 提交前复用。
- 错误消息可分别指出坐标顺序、纬度范围、经度范围和无法解析，而不是统一提示“无效”。
