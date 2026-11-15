<!-- 页面 URL：https://www.palantir.com/docs/zh/foundry/functions/python-getting-started -->
<!-- 研读状态：已完成 -->

# 函数 • Python functions • 起始步骤 • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/functions/python-getting-started)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/functions/python-getting-started)
- 页面语言：中文（官方 AIP 机器翻译，需与英文原文交叉核对）
- 主题栏目：functions
- 相关性：direct；本体函数文档
- 官方更新时间：2026-11-12T17:46:46.935Z
- 目录核对时间：2026-11-14T14:59:38Z
- 产品状态：Python 函数仓库的入门路径为创建模板仓库、编写类型完整的 `@function`、Live Preview、提交变更、打 tag 并发布。

## 英文原文短摘录（每个来源不超过 25 词）

> “The following documentation will guide you through the initial steps to prepare Python functions for use in the Palantir platform.”

## 摘录译文

以下文档将指导你完成在 Palantir 平台使用 Python 函数前的准备步骤。

## 中文要点

- 建议把供 Workshop 或本体应用使用的 Python 函数集中在一个仓库，以减少运行/治理成本；仓库由 Project 内的 Python functions 模板创建。
- 只有以 `functions.api` 的 `@function` 装饰器注册且输入输出声明类型的函数才会被识别；声明 API 类型时，运行时仍传递对应的 Python 值类型。
- 通过 Functions helper 进行 Live Preview，再提交仓库变更，创建 release tag 并在发布后从函数面板执行。
- 文档示例还展示用 `datetime` 和 `timedelta` 把毫秒参数换算为 ISO 时间字符串。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| `@function` decorator | 函数装饰器 | 注册 Python 函数并声明平台识别入口 |
| live preview | 实时预览 | 在发布前以交互方式运行函数的环境 |
| release tag | 发布标签 | 为可发布的函数源码版本打标 |
| functions helper | 函数助手 | 在代码仓库中预览和运行函数的工具面板 |

## 疑问与待验证项

- 入门文档以基础函数和发布操作为主；真实函数的权限、对象类型导入、依赖管理和运行模式还需结合后续文档。
- 页面示例引用 master 分支流程；主分支保护、代码评审与发布审批策略应按组织治理需要另定。

## 复刻启示

- 为函数注册保存明确输入输出 schema、源码提交和发布标签；Live Preview 与正式发布使用不同运行环境和权限。
- 函数创建流程用可视状态串起仓库初始化、依赖/本体资源导入、预览、代码评审、release tag 和发布验证。
- 新建项目模板提供最小 Python 函数，并在本体画布中关联函数依赖的对象类型和 Action。
