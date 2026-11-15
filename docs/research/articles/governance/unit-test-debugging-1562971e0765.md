<!-- 页面 URL：https://www.palantir.com/docs/zh/foundry/functions/unit-test-debugging -->
<!-- 研读状态：已完成 -->

# 函数 • Unit testing • 调试 • Palantir

- 英文来源：[现行英文原文](https://www.palantir.com/docs/foundry/functions/unit-test-debugging)
- 官方中文来源：[官方中文页（AIP 机器翻译，准确性未独立验证）](https://www.palantir.com/docs/zh/foundry/functions/unit-test-debugging)
- 页面语言：中文（官方 AIP 机器翻译，需与英文原文交叉核对）
- 主题栏目：functions
- 相关性：direct；本体函数文档
- 官方更新时间：2026-11-12T17:46:46.935Z
- 目录核对时间：2026-11-14T14:59:41Z
- 产品状态：该页介绍在 Code Repositories 调试器中暂停运行中的函数单元测试，设置断点并检查变量；页面属于 TSv1 单元测试文档体系。

## 原文短摘录与翻译

> “Use the debugger tool in Code Repositories to examine the behavior of your unit test while it runs.”

## 摘录译文

使用 Code Repositories 中的调试器，可在单元测试运行时检查其行为。

## 中文要点

- 调试器可在测试执行中停在断点，检查当前变量并理解函数及依赖库行为。
- 本页将具体的断点配置、启动调试和变量检查链接到独立函数调试指南，当前页只说明测试执行时的调试入口。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| debugger | 调试器 | 暂停代码执行并检查当前运行状态的工具 |
| breakpoint | 断点 | 测试执行到指定代码行时暂停的位置 |
| unit test | 单元测试 | 对单个函数或逻辑单元运行的自动化验证 |

## 疑问与待验证项

- 页面聚焦 TSv1 的单元测试调试器；TSv2/Python 的测试运行模式和本地调试接口是否一致，需查各语言指南。
- 调试会话中的本体数据、权限和实时预览与离线单元测试的隔离程度没有在此页说明。

## 复刻启示

- 为本体函数提供可复现的试算输入和断点/调用轨迹；调试信息显示对象主键、属性路径和编辑计划，而不泄露无权字段。
- 将测试运行与本体数据服务隔离，允许用 stub 固定对象查询响应；任何连接生产数据的调试操作需显式授权。
- 调试器定位逻辑问题，运行监控定位部署延迟/失败，两类信息在界面上应分开。
