<!-- 页面 URL：https://www.palantir.com/docs/foundry/aip-evals/ontology-edits -->
<!-- 研读状态：已完成 -->

# AIP Evals • Evaluate Ontology edits • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/aip-evals/ontology-edits)
- 官方中文来源：未找到确定的一对一官方中文页（配对状态：ambiguous）
- 页面语言：英文
- 主题栏目：aip-evals
- 相关性：direct；Ontology 与 Agent 评估文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:04:36Z
- 产品状态：针对产生 Ontology 编辑的 AIP Logic 函数，评估需使用 Ontology simulation。

## 英文原文短摘录（每个来源不超过 25 词）

> “This ensures that the actual Ontology remains unchanged during testing and evaluation.”

## 摘录译文

仿真评估可确保测试过程中不更改实际 Ontology。

## 中文要点

- Evaluation suite 的每个测试用例都会执行对应 Logic function；若函数创建、编辑或删除对象，则测试运行在 Ontology simulation 中，真实本体保持不变。
- 产生本体编辑的 AIP Logic 函数必须配置 TypeScript 自定义评估函数，或使用 intermediate parameters。评估函数返回 Boolean 或数字；也可返回由 Boolean/数字组成的 struct，以一个函数输出多项指标。
- 创建的对象只存在于仿真本体，不能直接作为测试参数传入；应以可识别属性搜索仿真中的对象并断言其字段。被编辑对象原本存在于真实本体，可直接传给评估函数，在仿真中检查编辑结果。被删除对象不能直接传入，应按可识别属性搜索并确认不存在。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Evaluation suite | 评估套件 | 用测试用例批量运行 Logic 函数并计算指标。 |
| Ontology simulation | 本体仿真 | 隔离测试期间的本体编辑状态，不改变实际本体。 |
| intermediate parameters | 中间参数 | 作为 Logic block 输出评估输入的一种方案。 |
| custom evaluation function | 自定义评估函数 | 用 TypeScript 对仿真中的新增、修改或删除结果进行断言。 |

## 疑问与待验证项

- 页面聚焦 AIP Logic function 的编辑评估，未定义与 Action Type submit criteria 的 test run、Action branch test 之间的状态隔离是否共享。
- 仿真函数可读数据的安全边界、外部函数调用和副作用在 Evaluation suite 中如何处理，需结合运行套件与 AIP 安全页面核对。

## 复刻启示

- 为派生属性、Agent 计划和 Action 增加隔离试算：以快照复制本体读视图，拦截持久写入和副作用，并把模拟新增/修改/删除与预期结果分别呈现。
- 评估指标可返回多项结构化结果；每个用例保存输入快照、模拟编辑集、断言结果和模型/逻辑版本，支持回归比较。
- 新建、编辑、删除对象的评估器采用不同取证路径；删除断言按稳定标识查询“无匹配”，不可尝试读取已经删除的仿真对象。
