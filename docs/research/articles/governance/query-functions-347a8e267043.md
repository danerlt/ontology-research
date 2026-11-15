<!-- 页面 URL：https://www.palantir.com/docs/foundry/functions/query-functions -->
<!-- 研读状态：已完成 -->

# Functions • Language-agnostic features • Publish and call query functions through API gateway • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/functions/query-functions)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/functions/query-functions)（配对状态：matched）
- 页面语言：英文
- 主题栏目：functions
- 相关性：direct；本体函数文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:02:44Z
- 产品状态：页面当前未标注特定 Beta/预览/弃用状态；关联功能状态按引用子页复核。

## 英文原文短摘录（每个来源不超过 25 词）

> “Queries are the read-only subsets of functions that may be optionally exposed through the API gateway.”

## 摘录译文

Query 是函数的只读子集，可以选择通过 API gateway 暴露。

## 中文要点

- Query 适用于只读逻辑，可通过 API gateway 作为查询 API 发布；若需要修改本体或外部系统副作用，应采用 Action。
- API-named Query 需要符合 lowerCamelCase、少于 100 字符、不以数字开头，并在仓库导入的 Ontology 集合中唯一；TSv1、TSv2 与 Python 的声明语法不同。
- API 名调用始终指向最新已标记版本，不使用普通函数相同的语义版本选择方式；更改/移除 API 名会破坏消费者。需要并行升级时复制查询并提供新的 API 名。
- TSv1 函数调用 Query 时平台会静态分析依赖；分析偶尔漏检需用 `@Uses` 声明查询依赖。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Query | 查询函数 | 只读的函数类型，可通过平台或 API gateway 调用。 |
| API name | API 名称 | 对外稳定调用的查询标识符。 |
| @Uses | 依赖声明装饰器 | 为 TSv1 函数补充平台静态分析未发现的查询依赖。 |

## 疑问与待验证项

- API-named Query 采用最新 tag 而非版本范围，独立 API 兼容策略需由发布流程负责。
- Query 与 Action 的类型边界必须在 API 层强制校验，不能只依赖函数作者的命名约定。

## 复刻启示

- 对 Agent 公开工具分成只读 Query 与写入 Action；为工具 schema 固定 API 名、版本策略、主体权限和输入校验。
- 变更 API 名前生成消费者影响图，允许保留 v1/v2 两个 API 名并安排弃用周期。
