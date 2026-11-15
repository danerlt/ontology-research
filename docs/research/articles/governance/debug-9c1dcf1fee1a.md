<!-- 页面 URL：https://www.palantir.com/docs/foundry/functions/debug -->
<!-- 研读状态：已完成 -->

# Functions • 调试函数（TypeScript v1） • Debug functions • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/functions/debug)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/functions/debug)（配对状态：matched）
- 页面语言：英文
- 主题栏目：functions
- 相关性：direct；本体函数文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:03:06Z
- 产品状态：TSv1 的 Code Repositories 调试器可在预览/单元测试暂停运行、设置断点并查看变量。

## 英文原文短摘录（每个来源不超过 25 词）

> “Use the debugger tool in Code Repositories to examine the behavior of your unit test while it runs.”

## 摘录译文

使用 Code Repositories 调试器检查单元测试运行时的行为。

## 中文要点

- 文档为 TypeScript v1 Functions 专页，并建议需要 OSDK 与可配置资源请求时迁移到 v2。
- 在 Authoring 的 Code Repositories 中可以给单元测试设置一个或多个断点；运行时暂停并检查变量和函数/库调用。
- 可从函数 Live Preview 或单元测试启动调试；编辑器高亮下一行，调试器支持继续、单步和终止。
- Live Preview 的 console 日志会连同时间戳显示，辅助分析逻辑正确性与性能。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Breakpoint | 断点 | 让函数暂停在指定代码行的调试标记 |
| Live Preview | 实时预览 | 在编辑阶段运行函数并查看输出的环境 |
| Variable inspection | 变量检查 | 暂停时读取当前作用域值 |

## 疑问与待验证项

- 调试日志和变量可能含有敏感对象字段，日志可见角色、保留时间和脱敏需在组织内核实。
- TSv1 工具链的调试能力与本地 IDE/TSv2 的差异应依据当前版本确认。

## 复刻启示

- 提供预览与测试共用的调试能力，支持断点、变量快照、逐步执行和带时间戳日志。
- 调试数据默认按对象权限脱敏并限制保留，显示函数版本、分支和调用参数来源。
