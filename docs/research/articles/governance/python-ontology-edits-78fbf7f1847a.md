<!-- 页面 URL：https://www.palantir.com/docs/zh/foundry/functions/python-ontology-edits -->
<!-- 研读状态：已完成 -->

# 函数 • Python functions • Ontology 更改 • Palantir

- 英文来源：[现行英文原文](https://www.palantir.com/docs/foundry/functions/python-ontology-edits)
- 官方中文来源：[官方中文页（AIP 机器翻译，准确性未独立验证）](https://www.palantir.com/docs/zh/foundry/functions/python-ontology-edits)
- 页面语言：中文（官方 AIP 机器翻译，需与英文原文交叉核对）
- 主题栏目：functions
- 相关性：direct；本体函数文档
- 官方更新时间：2026-11-12T17:46:46.935Z
- 目录核对时间：2026-11-14T14:59:39Z
- 产品状态：Python 本体编辑函数通过 OSDK 编辑容器收集创建/更新/链接更改，并需配置为 function-backed Action 才会提交；staged writes 提供读后写语义。

## 原文短摘录与翻译

> “For the edits created in a function to actually be applied, Ontology edit functions must be configured as a function-backed Action.”

## 摘录译文

函数中创建的编辑若要真正应用，Ontology 编辑函数必须配置成由函数支持的 Action。

## 中文要点

- 用 `@function(edits=[...])` 声明允许修改的对象类型；多对多链接还需声明其 link type，函数返回值应为 `list[OntologyEdit]`。
- Python 对象默认只读；通过 OSDK edits 容器获取 editable view、修改属性后返回编辑集合。原始只读对象不会随编辑视图改变。
- 更新数组属性必须先复制、修改，再重新赋回属性；直接原地改动列表不会登记编辑。既有对象主键不可修改。
- Staged writes 可在写后读取刚刚修改的数据并嵌套调用 staged-write 函数；Python struct 属性编辑目前标为 Beta。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| OntologyEdit | 本体编辑项 | 描述一次对象创建/更新/链接变化的写入对象 |
| editable view | 可编辑视图 | 由 edits 容器生成、用于收集修改的对象视图 |
| function-backed Action | 函数支持的 Action | 配置调用函数并应用其本体编辑结果的写入动作 |
| staged writes | 暂存写入 | 在函数执行中支持写后读和嵌套暂存调用的机制 |

## 疑问与待验证项

- 函数在 Action 外运行不会实际持久化这些编辑；产品需清楚区分“生成编辑计划”与“用户授权后提交”。
- 页面提醒刚写入后立即搜索可能得到意外结果；索引可见性与事务读后写语义需要分开理解。
- Struct property 标为 Beta；多对多链接登记、并发冲突和动作失败回滚需结合相关文档核对。

## 复刻启示

- 实现统一编辑计划层：函数输出待创建/变更对象和链接的差异，Action 对调用者、目标项目和对象字段做最终校验后应用。
- 画布实时试算只展示计划值和依赖轨迹；提交后才写入生产对象，并将编辑项与审核人/分支/发布版本一起审计。
- 数组、struct、主键与多对多链接各自提供显式差异预览和校验器，不把 Python 对象赋值等同于数据库写入。
