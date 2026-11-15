<!-- 页面 URL：https://www.palantir.com/docs/zh/foundry/pb-functions-expression/createOntologyGeopointV1 -->
<!-- 研读状态：已完成 -->

# PB函数表达式 • 转换为 Ontology GeoPoint • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/pb-functions-expression/createOntologyGeopointV1)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/pb-functions-expression/createOntologyGeopointV1)（中文路由译文以英文原文复核）
- 页面语言：中文
- 主题栏目：pb-functions-expression
- 相关性：direct；标题或简介提及本体、对象、动作、权限或 Agent 主题
- 官方更新时间：2026-11-12T17:46:46.927Z
- 目录核对时间：2026-11-14T15:01:08Z
- 产品状态：官方中文路由的译文准确性未逐句验证；术语和规则按英文原文复核。

## 原文短摘录与翻译

> “Convert a GeoPoint into a string that the Ontology will accept for a geo-indexed column (a geohash type column).”

## 摘录译文

将 GeoPoint 转为本体可用于地理索引列（geohash 类型列）的字符串。

## 中文要点

- 该表达式接收结构化 GeoPoint（包含 latitude 与 longitude），输出 Ontology GeoPoint 字符串，格式为 `纬度,经度`，合法范围分别是 -90..90 与 -180..180。
- 示例显示输出小数会格式化到最多约 7 位；输入 `null` 时输出 `null`。页面列出 Batch、Faster 和 Streaming 三种支持模式。
- 这是 Pipeline Builder 表达式层的类型适配，不代表对象链接或地理语义推理；存储字符串前仍需验证坐标顺序和范围。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| GeoPoint | 地理点结构 | 由 latitude/longitude 数值组成的结构化坐标。 |
| Ontology GeoPoint | 本体地理点 | 用于本体地理索引的 `lat,lon` 字符串。 |
| geohash type column | geohash 类型列 | 用于地理索引的目标列类型。 |

## 疑问与待验证项

- 文档示例可见数值被格式化到 7 位小数，但未充分说明四舍五入规则、边界值校验失败行为及不同运行模式的一致性。

## 复刻启示

- 在类型系统中区分结构化坐标和本体地理索引值，转换时显式固定纬度/经度顺序并处理 null。
- 表单和导入预览应展示坐标范围校验、精度变化及错误原因，不能仅按逗号拆分。
