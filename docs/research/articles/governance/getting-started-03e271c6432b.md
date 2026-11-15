<!-- 页面 URL：https://www.palantir.com/docs/zh/foundry/functions/getting-started -->
<!-- 研读状态：已完成 -->

# 函数 • 入门 • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/functions/getting-started)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/functions/getting-started)
- 页面语言：中文
- 主题栏目：functions
- 相关性：direct；本体函数文档
- 官方更新时间：2026-11-12T17:46:46.935Z
- 目录核对时间：2026-11-14T14:59:18Z
- 产品状态：官方中文页标注为未经验证的 AIP 机器翻译；英文原文为核对依据。

## 英文原文短摘录（每个来源不超过 25 词）

> “There are three language options for getting started with functions in Foundry: TypeScript v1, TypeScript v2, and Python.”

## 摘录译文

在 Foundry 中开始使用 Functions 有三种语言选项：TypeScript v1、TypeScript v2 和 Python。

## 中文要点

- 创建函数仓库时选定语言，在 Code Repositories 或 VS Code workspace 编写；三种语言都具备运行、测试、提交和发布等基础平台流程。
- Live Preview 可在提交前填入输入值执行函数，但运行资源、内存和时长与发布环境不同。
- 代码提交后打版本标签并发布到函数注册表；发布后函数可在平台其他应用中调用，权限传播可能造成短暂搜索不可见。
- 官方中文页标注 AIP 机器翻译准确性未经验证；功能支持矩阵及每个语言的专属教程决定语言差异。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Functions repository | 函数仓库 | 承载函数源代码、依赖、资源导入与发布版本的项目资源。 |
| Live Preview | 实时预览 | 提交前在平台开发环境中运行函数的调试入口。 |
| Function registry | 函数注册表 | 汇总可被平台调用的已发布函数资源。 |

## 疑问与待验证项

- Live Preview 与生产环境的资源差异具体值、外部出站权限及写入隔离需逐运行时核实。
- 发布后因权限传播延迟不可搜索的时间窗和恢复途径未在本页明确。

## 复刻启示

- 产品需要仓库、分支、依赖导入、预览运行、版本发布和注册表等连续开发路径，而不只提供编辑器。
- 预览环境和生产环境分开展示身份、配额和副作用风险；发布状态应含构建检查和权限传播进度。
