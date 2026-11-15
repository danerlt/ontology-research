<!-- 页面 URL：https://www.palantir.com/docs/foundry/functions/python-staged-writes -->
<!-- 研读状态：已完成 -->

# Functions • Python • Staged writes • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/functions/python-staged-writes)
- 官方中文来源：尚未确认（配对状态：ambiguous）
- 页面语言：英文
- 主题栏目：functions
- 相关性：direct；本体函数文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:02:59Z
- 产品状态：Beta；本地开发和 VS Code workspace 不支持该页所述预览能力。

## 英文原文短摘录（每个来源不超过 25 词）

> “Python staged-write functions use a generated `WriteableClient` instead of the standard `FoundryClient`.”

## 摘录译文

Python staged-write 函数使用生成的 WriteableClient，而不是标准 FoundryClient。

## 中文要点

- 执行内查询/聚合可读到当前函数和调用方已暂存的修改；执行外用户仍看不到未提交内容。
- 函数成功后自动提交；异常会丢弃整批变更。它不要求返回 `OntologyEdit`，可返回其他平台支持类型。
- 由 `WriteableClient` 创建暂存编辑容器；对象和链接编辑 API 类似常规 Python 编辑，提交由 Action 执行流程管理。
- Beta 功能；函数预览仅支持 Code Repositories，不支持本地开发或 VS Code workspace。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| staged writes | 分阶段写入 | 执行内暂存并在成功后提交的写入模式。 |
| WriteableClient | 可写客户端 | 执行本体 staged writes 的客户端。 |
| write-after-read consistency | 写后读一致性 | 同一执行内后续查询可见此前写入。 |

## 疑问与待验证项

- Action 重试时若代码已经执行了外部调用，需自行确认幂等性。
- 支持版本和 enrollment 开关以产品状态为准。

## 复刻启示

- 把规则计算、暂存写入、业务校验、权限评审和原子提交做成可追踪的运行阶段。
- 嵌套函数共享变更上下文；异常时整体回滚并保留失败审计。
