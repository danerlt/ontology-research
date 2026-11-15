<!-- 页面 URL：https://www.palantir.com/docs/foundry/functions/python-ontology-edits -->
<!-- 研读状态：已完成 -->

# Functions • Python • Ontology edits • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/functions/python-ontology-edits)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/functions/python-ontology-edits)（配对状态：matched）
- 页面语言：英文
- 主题栏目：functions
- 相关性：direct；本体函数文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:02:57Z
- 产品状态：Python 函数中的 struct 属性编辑和 staged writes 为 Beta。

## 英文原文短摘录（每个来源不超过 25 词）

> “Ontology objects in Python functions are read-only by default.”

## 摘录译文

Python 函数中的本体对象默认是只读的。

## 中文要点

- Python 编辑函数用 `@function(edits=[...])` 声明可写对象/链接类型，并返回 `list[OntologyEdit]`；变更通过 `FoundryClient().ontology.edits()` 累积。
- 对象默认只读；需从编辑容器获取 editable view 后修改属性或链接。主键不能更新，多对多链接需声明 `OntologyLinkType` 保留完整 provenance。
- 数组属性需复制后重新赋回；原地修改不会被记录。Struct 属性编辑为 Beta，字段修改后需把完整 struct 重新赋值给属性。
- 常规编辑函数只有通过 function-backed Action 执行才会写入；页面提醒刚编辑后立即搜索可能出现预期外结果。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| OntologyEdit | 本体编辑值 | 描述创建、更新或删除操作的类型。 |
| editable object | 可编辑对象视图 | 编辑容器提供的变更记录代理。 |
| OntologyLinkType | 本体链接声明 | 声明函数会修改的多对多链接。 |

## 疑问与待验证项

- 编辑后搜索的 caveats 涉及的具体延迟/一致性行为需要结合对象存储和索引说明。
- 数组/struct 原地更新可能被静默忽略，API 使用方应通过验证避免丢失编辑。

## 复刻启示

- Action 声明实体和属性写集；试算显示每个对象/链接的新旧值和待提交状态。
- 显式提示未登记的数组原地修改或结构体字段修改不会写入持久化编辑集。
