<!-- 页面 URL：https://www.palantir.com/docs/zh/foundry/functions/api-object-sets -->
<!-- 研读状态：已完成 -->

# 函数 • Functions on objects • API：对象集 • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/functions/api-object-sets)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/functions/api-object-sets)（同路由中文版本；页面注明机器翻译未经准确性验证）
- 页面语言：中文
- 主题栏目：functions
- 相关性：direct；本体函数文档
- 官方更新时间：2026-11-12T17:46:46.935Z
- 目录核对时间：2026-11-14T14:58:48Z
- 产品状态：中文对照页覆盖 TypeScript v1（TSv1）；TSv2 与 Python 改用 Ontology SDK。

## 原文短摘录与翻译

> “对象集表示单一类型对象的无序集合。”

## 摘录译文

对象集是一种针对同类对象的无序集合表达。

## 中文要点

- 中文页解释 TSv1 对象集支持搜索、属性筛选、基于链接的周边搜索、集合运算和聚合；对象集可惰性传入函数，必要时再加载为具体对象。
- 使用筛选、排序和聚合前，属性需启用 `Searchable`。同类型集合可取并集、交集、差集；TSv2/Python 查询走 Ontology SDK，需查看对应 SDK 文档，不可将 TSv1 调用方式直接照搬。
- `.all()` 完整加载有对象数和超时限制；大量数据应尽量用服务端聚合。`.take(n)` 是截断上限而非分页；完整读取会受分页一致性与快照生命周期约束。
- 页面提示中文翻译由 AIP 自动生成且准确性未经验证；本卡重要运行限制以英文页复核。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| 对象集 | object set | 同类对象的查询集合，可做筛选、遍历和聚合。 |
| 周边搜索 | Search Around | 沿已定义链接从一类对象查询相关对象。 |
| 可搜索提示 | Searchable render hint | TSv1 中执行过滤、排序和聚合的必要属性提示。 |
| 集合操作 | set operation | 对同类型对象集执行 union、intersect、subtract。 |

## 疑问与待验证项

- 中文翻译页标明机器翻译未经验证；对象数上限、函数超时、快照异常等关键数值应以英文页和对应 SDK 版本为准。
- `take(n)` 会舍弃剩余匹配对象；对完整推理链应避免误把截断输出作为总量。

## 复刻启示

- 把对象集当作可执行、可回放的查询表达而非结果数组，并在画布上将链接跳转与集合运算可视化，支持检查每一步输入/输出规模。
- 面向 Agent 的工具返回值需携带分页完整性、截断与快照状态；遇到不完整页面时阻止 Agent 将其宣称为全量结论。
