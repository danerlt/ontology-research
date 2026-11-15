<!-- 页面 URL：https://www.palantir.com/docs/zh/foundry/functions/unit-test-ontology-edits -->
<!-- 研读状态：已完成 -->

# 函数 • Unit testing • 验证Ontology编辑 • Palantir

- 英文来源：[现行英文原文](https://www.palantir.com/docs/foundry/functions/unit-test-ontology-edits)
- 官方中文来源：[官方中文页（AIP 机器翻译，准确性未独立验证）](https://www.palantir.com/docs/zh/foundry/functions/unit-test-ontology-edits)
- 页面语言：中文（官方 AIP 机器翻译，需与英文原文交叉核对）
- 主题栏目：functions
- 相关性：direct；本体函数文档
- 官方更新时间：2026-11-12T17:46:46.935Z
- 目录核对时间：2026-11-14T14:59:45Z
- 产品状态：TSv1 函数测试使用 `verifyOntologyEditFunction()` 检查函数计划创建、修改、删除对象及添加/移除链接的编辑结果。

## 原文短摘录与翻译

> “You can use the verifyOntologyEditFunction() API to verify edits performed by your function.”

## 摘录译文

可以使用 `verifyOntologyEditFunction()` API 验证函数生成的编辑。

## 中文要点

- 验证器提供对象创建/修改/删除、链接添加/移除等断言；单数断言接受一个编辑，复数断言接受多个同类编辑。
- 单数与复数方法不可互换，传错形态会产生类型错误；链接编辑还可通过回调引用同一函数中新建的对象。
- 该验证器适合测试“函数计划写什么”，与 Action 的最终权限验证、事务冲突和真实持久化结果分开。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| `verifyOntologyEditFunction()` | 本体编辑验证器 | 检查 TSv1 函数生成的本体编辑计划 |
| `.createsObject()` | 验证创建对象 | 断言一个对象类型及其创建属性 |
| `.modifiesObjects()` | 验证修改多个对象 | 对数组形式的对象编辑进行批量断言 |
| link edit | 链接编辑 | 新增或移除对象关系的编辑项 |

## 疑问与待验证项

- 验证器方法名和单/复数形态为 TSv1 的测试 API；TSv2/Python 的编辑测试方式需按相应 SDK 页面核实。
- 通过测试断言函数编辑计划正确，不等于确认用户可执行该 Action，也不验证数据库提交后的索引延迟和并发冲突。

## 复刻启示

- 在本体分支评审界面提供“变更计划单元测试”：按对象创建/属性变更/链接编辑逐条对比期望与实际。
- 测试通过只是逻辑正确的证据；发布前仍需权限与冲突预检查，并在执行后审计真实事务结果。
- 支持批量新增/删除边的测试回调关联临时创建的节点，验证复杂对象图更新路径。
