<!-- 页面 URL：https://www.palantir.com/docs/foundry/functions/unit-test-ontology-edits -->
<!-- 研读状态：已完成 -->

# Functions • Unit testing (TSv1) • Verify Ontology edits • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/functions/unit-test-ontology-edits)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/functions/unit-test-ontology-edits)（配对状态：matched）
- 页面语言：英文
- 主题栏目：functions
- 相关性：direct；本体函数文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:03:25Z
- 产品状态：TSv1 Jest 单测辅助 API；区分验证单项编辑与多项编辑的方法。

## 英文原文短摘录（每个来源不超过 25 词）

> “You can use the `verifyOntologyEditFunction()` API to verify edits performed by your function.”

## 摘录译文

可使用 verifyOntologyEditFunction() API 验证函数执行产生的本体编辑。

## 中文要点

- `verifyOntologyEditFunction()` 从 `@foundry/functions-testing-lib` 导入，将函数实际生成的 edits 与预期创建/修改/删除对象和链接进行比较。
- 编辑验证 API 区分 singular 与 plural 方法；单项方法收一个值，多项方法收数组，不能混用，否则类型检查失败。
- 测试可链式断言多个 edits，也支持异步编辑函数；重点验证函数产生的编辑集，不是把数据写入真实 Ontology。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| verifyOntologyEditFunction() | 验证本体编辑函数 | 捕获并核对 TSv1 edit function 产生的编辑。 |
| singular verifier | 单项验证器 | 断言一种编辑的一条记录。 |
| plural verifier | 多项验证器 | 断言同类编辑的多条记录。 |

## 疑问与待验证项

- 验证器对链接添加/移除和多阶段编辑的支持需按当前测试库完整 API 核对。
- 测试可确认编辑意图，但不会覆盖 Action 权限、提交条件、冲突或落库传播。

## 复刻启示

- 把预期写集作为版本评审的一部分，评审者能对照本体 schema看到每个对象/链接的变化。
- 规则单测与 Action 提交/安全/并发集成测试分层，并把验证结果挂到分支提案。
