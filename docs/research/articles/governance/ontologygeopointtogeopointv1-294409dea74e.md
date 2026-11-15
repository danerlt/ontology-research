<!-- 页面 URL：https://www.palantir.com/docs/zh/foundry/pb-functions-expression/ontologyGeopointToGeopointV1 -->
<!-- 研读状态：已完成 -->

# PB函数表达式 • 从Ontology GeoPoint转换 • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/pb-functions-expression/ontologyGeopointToGeopointV1)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/pb-functions-expression/ontologyGeopointToGeopointV1)
- 页面语言：中文
- 主题栏目：pb-functions-expression
- 相关性：direct；标题或简介提及本体、对象、动作、权限或 Agent 主题
- 官方更新时间：2026-11-12T17:46:46.926Z
- 目录核对时间：2026-11-14T15:01:09Z
- 产品状态：官方中文路由的译文准确性未逐句验证；术语和规则按英文原文复核。

## 英文原文短摘录（每个来源不超过 25 词）

> “Convert an Ontology GeoPoint into a regular GeoPoint.”

## 摘录译文

将 Ontology GeoPoint 转换为普通 GeoPoint。

## 中文要点

- 该表达式把 `纬度,经度` 字符串解析为结构化 GeoPoint，输出包含 latitude 与 longitude 两个字段。
- 无法解析的输入（例如字段数量错误、混入字母）以及 null 在文档示例中都会返回 null；支持 Batch、Faster 和 Streaming。
- 它与正向转换表达式构成往返映射，但正向输出会规范化精度；不能假设往返后保留原始文本格式。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Ontology GeoPoint | 本体地理点 | 以逗号分隔的纬度/经度字符串。 |
| GeoPoint | 地理点结构 | 包含 latitude、longitude 的结构化坐标。 |
| null propagation | 空值传播 | 空值或解析失败时输出 null 的行为。 |

## 疑问与待验证项

- 页面列出若干无效示例但没有完整文法；是否区分空输入、格式错误与越界坐标需进一步核验。
- 转换是否同时验证数值范围还是仅解析格式，需用边界和越界样例试算确认。

## 复刻启示

- 导入与派生逻辑应将 parse error、越界和显式 null 区分为不同状态，避免都静默折叠成空值。
- 对于地理属性，保存规范化值时保留来源原文与转换错误，以支持回溯。
