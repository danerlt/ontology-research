<!-- 页面 URL：https://www.palantir.com/docs/foundry/functions/unit-test-debugging -->
<!-- 研读状态：已完成 -->

# Functions • Unit testing (TSv1) • Debug • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/functions/unit-test-debugging)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/functions/unit-test-debugging)（配对状态：matched）
- 页面语言：英文
- 主题栏目：functions
- 相关性：direct；本体函数文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:03:45Z
- 产品状态：本页是 TSv1 函数开发/单测调试说明。

## 英文原文短摘录（每个来源不超过 25 词）

> “Use the debugger tool in Code Repositories to examine the behavior of your unit test while it runs.”

## 摘录译文

可在 Code Repositories 中使用调试器检查单元测试运行行为。

## 中文要点

- Code Repositories authoring debugger 可在实时预览或单测运行时暂停执行、检查变量并逐步执行；断点可以放在多个文件中。
- 调试面板展示当前堆栈帧、下一条执行语句和变量；console 在选中的 frame 上下文执行，访问其他 frame 的局部变量会报错。
- `console.log` 输出可用于正确性和性能排查；单测面板显示日志，Live Preview 中还展示时间戳。
- 断点调试适用于观察本地/预览执行路径，不自动提供生产用户权限或外部系统状态。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| authoring debugger | 代码编写调试器 | Code Repositories 中交互式暂停与检查函数运行的工具。 |
| breakpoint | 断点 | 让执行在指定代码行前暂停的标记。 |
| stack frame | 堆栈帧 | 当前调用链中一个函数调用的变量作用域。 |
| console.log | 控制台日志 | 函数执行期间输出的调试消息。 |

## 疑问与待验证项

- 本页为 TSv1 专属说明，TSv2/VS Code 的调试工具与断点能力需按对应开发环境指南核对。
- 日志内容可能包含对象属性值；真实调试时应遵循数据分类和访问控制。

## 复刻启示

- 本体推理试算应给出每一步输入、查询结果、过滤和聚合中间值，并提供可复现的断点/步骤重放。
- 调试日志与审计记录分开管理，避免敏感对象字段进入普通开发日志。
