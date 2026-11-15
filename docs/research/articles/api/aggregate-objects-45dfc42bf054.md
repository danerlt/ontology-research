<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/ontology-objects/aggregate-objects -->
<!-- 研读状态：已完成 -->

# Aggregate Objects (v2, latest) • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/ontology-objects/aggregate-objects)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/v2/ontologies-v2-resources
- 相关性：direct；Ontology REST API v2 参考
- 官方更新时间：2026-11-12T17:46:46.921Z
- 目录核对时间：2026-11-14T14:57:25Z
- 产品状态：常规 v2 读取接口；可选 branch 为实验性功能。

## 英文原文短摘录（每个来源不超过 25 词）

> “Perform functions on object fields in the specified ontology and object type.”

## 摘录译文

对指定 Ontology 和对象类型中的字段执行聚合函数。

## 中文要点

- POST `/api/v2/ontologies/{ontology}/objects/{objectType}/aggregate` 对对象类型字段执行聚合，输入可包含 aggregation、where、groupBy 和 accuracy。
- accuracy 默认 `ALLOW_APPROXIMATE`；要求 `REQUIRE_ACCURATE` 时，仅在结果可保证精确时返回，否则可能以 `AggregationAccuracyNotSupported` 失败。
- 响应会给出实际准确度、数据分组和指标，并可含排除项数量与 computeUsage；OAuth 需要 `api:ontologies-read`。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| aggregation | 聚合定义 | 指定对字段执行的统计函数及输出名。 |
| groupBy | 分组 | 按字段或范围拆分聚合结果。 |
| REQUIRE_ACCURATE | 要求精确 | 无法保证精确时失败。 |
| ALLOW_APPROXIMATE | 允许近似 | 默认准确度策略。 |

## 疑问与待验证项

- 哪些函数可用于不同字段类型、精度和最大分组数限制应由 schema 文档与运行测试补充。
- 近似值在界面中应显示准确度元数据，不应与精确计算结果混为一谈。

## 复刻启示

- 把派生属性中的多对象聚合映射到明确聚合算子、过滤条件和分组字段；预览结果返回准确度与排除项信息。
- 运行成本和精度可作为推理试算面板的指标，超过预算时提示用户收窄关系路径或数据范围。
