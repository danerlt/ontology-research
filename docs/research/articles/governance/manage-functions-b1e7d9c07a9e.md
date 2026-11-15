<!-- 页面 URL：https://www.palantir.com/docs/foundry/functions/manage-functions -->
<!-- 研读状态：已完成 -->

# Functions • Function management • Manage published functions • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/functions/manage-functions)
- 官方中文来源：尚未确认（配对状态：ambiguous）
- 页面语言：英文
- 主题栏目：functions
- 相关性：direct；本体函数文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:02:30Z
- 产品状态：未见本页另标 Beta、预览或弃用状态。

## 英文原文短摘录（每个来源不超过 25 词）

> Once published, all types of functions can be viewed and managed using the Ontology Manager.

## 摘录译文

函数发布后，可在 Ontology Manager 中查看和管理所有类型的函数。

## 中文要点

- 管理器支持按名称、描述、API 名称、RID 等元数据搜索函数；详情页展示输入、输出、使用历史和成功/失败次数、P95 执行时长等指标。
- 支持的函数类型可在配置页按版本设置 timeout、memory 等资源覆盖；发布新版本时配置继承依赖模板版本，部分发布路径也可能需要重新配置。
- 文档区分一致性快照、禁用快照和强制快照，并指出默认快照选项及函数涉及写入/外部调用时的风险；还列出不同语言的执行时限、内存和对象集加载约束。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Function configuration | 函数配置 | 按函数版本配置运行资源或快照选项。 |
| Consistent snapshot | 一致性快照 | 一次函数执行中的多次本体读取共享一致的数据视图。 |
| P95 duration | P95 执行时长 | 95 百分位的执行耗时，用于观察尾延迟。 |

## 疑问与待验证项

- 函数的资源限制和默认值因语言、serverless/deployed 模式与平台版本而不同；页面上的数值应标注时点并可配置。
- 快照是否适合某个动作取决于隔离级别、读写模式和外部副作用；不应仅因性能而强制启用。

## 复刻启示

- 为函数建立可搜索的发布目录，保留不可变版本、输入输出 schema、版本级资源配置、使用记录与 P95/失败率。
- 在动作函数中明确记录读取快照和隔离级别；配置覆盖的继承与默认差异应在发布比较视图中呈现。
