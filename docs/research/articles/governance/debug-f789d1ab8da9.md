<!-- 页面 URL：https://www.palantir.com/docs/zh/foundry/functions/debug -->
<!-- 研读状态：已完成 -->

# 函数 • TypeScript basics • 调试函数 • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/functions/debug)
- 官方中文来源：尚未确认（配对状态：not_applicable）
- 页面语言：中文
- 主题栏目：functions
- 相关性：direct；本体函数文档
- 官方更新时间：2026-11-12T17:46:46.935Z
- 目录核对时间：2026-11-14T14:59:08Z
- 产品状态：官方中文页标注为未经验证的 AIP 机器翻译；英文原文为核对依据。

## 原文短摘录与翻译

> 英文原文：Use the debugger tool in Code Repositories to examine the behavior of your unit test while it runs.

> 中文译文：使用 Code Repositories 中的调试器，可以检查单元测试运行时的行为。

## 摘录译文

以上为英文短摘录及中文译文。官方中文页面为 AIP 机器翻译，准确性未经验证。

## 中文要点

- 本页是 TSv1 专属调试文档；Code Repositories 调试器可在 live preview 或单元测试期间通过断点暂停，并检查变量、调用帧和执行位置。
- 调试操作包括继续运行、step over/into/out、停止执行与清理断点；断点可跨多个文件设置。
- 该工具帮助定位代码正确性与性能问题，但调试本身仍在受控预览/测试环境中运行；发布到生产的排错应结合 telemetry 与日志。
- 官方中文路由标注为未经验证的机器翻译；新运行时是否提供相同调试能力需查看 TSv2/Python 文档。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Breakpoint | 断点 | 调试时暂停程序执行的位置。 |
| Call frame | 调用帧 | 表示当前暂停所在函数、文件和行号的执行上下文。 |
| Step into | 步入 | 进入当前调用的内部函数继续单步。 |

## 疑问与待验证项

- Live Preview 调试调用是否访问真实权限数据、是否副作用隔离，需通过环境配置验证。
- TypeScript v2 和 Python 的本地调试与平台预览支持程度未由此 TSv1 页说明。

## 复刻启示

- 提供仅限开发/测试环境的断点调试、函数帧和变量检查；生产故障定位走 trace/log，不混用写入数据。
- 把调试运行绑定到分支、代码版本和 schema 快照，记录停止/超时状态，限制敏感变量的查看权限。
