<!-- 页面 URL：https://www.palantir.com/docs/zh/foundry/functions/python-function-types -->
<!-- 研读状态：已完成 -->

# 函数 • Python functions • 类型参考 • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/functions/types-reference)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/functions/python-function-types)
- 页面语言：中文（官方 AIP 机器翻译，需与英文原文交叉核对）
- 主题栏目：functions
- 相关性：direct；本体函数文档
- 官方更新时间：2026-11-12T17:46:46.935Z
- 目录核对时间：2026-11-14T14:59:31Z
- 产品状态：中文旧路由已重定向至统一 Functions 类型参考；该表比较 TSv1、TSv2 与 Python 的注册类型映射，且部分类型仅由特定语言支持。

## 英文原文短摘录（每个来源不超过 25 词）

> “their corresponding language types”

## 摘录译文

它们对应的语言类型

## 中文要点

- 类型参考将平台函数注册类型映射到 TSv1、TSv2、Python 的代码类型；对象集、Ontology 编辑、媒体、用户、结构体和聚合类型均有差异。
- Python 内置 `int` 注册成 Integer、`float` 默认注册成 Float；需要 Long 或 Double 语义时应使用 `functions.api` 提供的类型别名。
- Python 函数并不支持全部注册类型，例如 Interface 与 Interface ObjectSet 不支持；Pipeline Builder UDF 还有额外限制，不能接受或返回 Ontology 对象类型。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| function registry type | 函数注册类型 | Functions 平台用于校验参数/返回值的逻辑类型 |
| type alias | 类型别名 | 明确区分整数/长整数或单/双精度的 API 类型 |
| ObjectSet | 对象集 | 函数对一组 Ontology 对象进行查询或聚合的类型 |
| struct | 结构体 | 按字段组成的自定义复合参数或返回类型 |

## 疑问与待验证项

- 类型表会随 SDK/函数注册能力演进；实现时应把能力表按运行时版本维护，避免根据 Python 基础类型自行推断平台 schema。
- Decimal、Binary、Interface 等条目的语言可用性不对称；跨语言迁移需逐项核对，而非只转换语法。

## 复刻启示

- 为函数参数与返回值保存平台 schema 和语言映射，发布前校验类型、可空性、集合基数及跨版本可用性。
- 数值类型使用明确的 Integer/Long/Float/Double 标识，避免语言运行时默认类型造成静默精度或范围变化。
- 将 Pipeline UDF 限定为表格行输入及标量/结构体输出的独立执行类型；它与面向 Ontology 对象集的函数 API 分开建模。
