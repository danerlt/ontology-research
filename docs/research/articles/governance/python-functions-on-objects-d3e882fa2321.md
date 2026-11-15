<!-- 页面 URL：https://www.palantir.com/docs/foundry/functions/python-functions-on-objects -->
<!-- 研读状态：已完成 -->

# Functions • Python • Functions on objects • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/functions/python-functions-on-objects)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/functions/python-functions-on-objects)（配对状态：matched）
- 页面语言：英文
- 主题栏目：functions
- 相关性：direct；本体函数文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:02:56Z
- 产品状态：Python OSDK 的部分 DataFrame 互操作功能为 Beta。

## 英文原文短摘录（每个来源不超过 25 词）

> “You can write functions that interact with the Ontology using the Python Ontology SDK.”

## 摘录译文

可使用 Python Ontology SDK 编写与本体交互的函数。

## 中文要点

- Python 函数通过生成的 Ontology SDK 引用对象类型、对象集和链接；从 Resource imports 导入资源后还需生成并安装 SDK。
- 函数可把对象当作参数，也能用 `FoundryClient` 查询对象集并筛选、聚合和遍历链接。
- 新增导入资源或对象 schema 变化后需重新生成并安装 SDK；首个生成包名确定后不可修改。
- 对象集转换为 pandas DataFrame 等互操作能力属于 Beta，需关注数据规模、内存和 enrollment 支持。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Ontology SDK (OSDK) | 本体 SDK | 根据本体资源生成的客户端与类型绑定。 |
| FoundryClient | Foundry 客户端 | Python 函数中访问对象 API 的客户端。 |
| ObjectSet | 对象集 | 可筛选、聚合或迭代的本体对象集合。 |

## 疑问与待验证项

- SDK 绑定依赖导入资源快照；版本升级需检查函数/应用仍引用的 schema。
- DataFrame 互操作处于 Beta，不适合作为默认的大规模查询方式。

## 复刻启示

- 画布展示函数依赖的对象类型与链接，并固定其 SDK/schema 版本。
- 推理预览优先用对象集筛选和聚合下推查询，避免全量载入 Python 进程。
