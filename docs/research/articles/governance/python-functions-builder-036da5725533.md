<!-- 页面 URL：https://www.palantir.com/docs/zh/foundry/functions/python-functions-builder -->
<!-- 研读状态：已完成 -->

# 函数 • Python functions • 在Pipeline Builder中使用Python函数 • Palantir

- 英文来源：[现行英文原文](https://www.palantir.com/docs/foundry/functions/python-functions-builder)
- 官方中文来源：[官方中文页（AIP 机器翻译，准确性未独立验证）](https://www.palantir.com/docs/zh/foundry/functions/python-functions-builder)
- 页面语言：中文（官方 AIP 机器翻译，需与英文原文交叉核对）
- 主题栏目：functions
- 相关性：direct；本体函数文档
- 官方更新时间：2026-11-12T17:46:46.935Z
- 目录核对时间：2026-11-14T14:59:33Z
- 产品状态：Python 函数可作为 Pipeline Builder 的 UDF 边车容器运行；它逐行处理映射列并为输出表生成新列，不要求单独部署。

## 原文短摘录与翻译

> “Pipeline Builder invokes the function for every row, passing that row's cell values as the parameter arguments.”

## 摘录译文

Pipeline Builder 会为每一行调用函数，并把该行的单元格值作为参数传入。

## 中文要点

- Python UDF 随 Pipeline Builder 流水线以 sidecar 容器运行，按流水线数据规模动态扩展，也可像其他 transform 一样预览。
- 调用粒度是一行：将输入列映射到函数参数，函数返回单个标量并写入输出列；它不会接收整个 pandas 或 Spark DataFrame。
- 要返回多个相关值可用自定义 struct，之后再通过 Get struct field 拆列；Ontology 类型不在 Pipeline Builder UDF 可用类型之列。
- Pipeline Builder UDF 不支持调用 LLM；需要 LLM 时应使用专门的 Use LLM 节点。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| UDF | 用户定义函数 | 在流水线中按行调用的自定义计算逻辑 |
| sidecar container | 边车容器 | 随 Pipeline Builder transform 一起运行的 Python 函数容器 |
| scalar | 标量 | 每行函数输出的单个值，如字符串或数值 |
| struct | 结构体 | 可作为单个结构化输出列的多字段自定义类型 |

## 疑问与待验证项

- 逐行执行的成本与批量向量化计算不同；高基数数据、外部调用或复杂循环可能放大运行时间。
- Python Ontology 函数类型参考与 Pipeline Builder 的可用类型不同；某个类型能在 Ontology 函数中使用，并不代表 UDF 可以导入。
- 文档建议用专用 LLM 节点；节点输入输出、提示版本和隐私治理需结合 Pipeline Builder 页面继续核对。

## 复刻启示

- 在系统内区分逐行数据流水线函数与 Ontology 对象集/Action 函数，分别定义输入 schema、扩展方式、超时与计算计量。
- 对 UDF 可视化列到参数、参数到返回列的映射；在数据预览里展示样例输入输出和错误行。
- 大规模输入优先考虑批处理或原生 transform，禁止在逐行函数内隐式做 N 次网络请求；LLM 调用走显式编排节点。
