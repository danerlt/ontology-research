<!-- 页面 URL：https://www.palantir.com/docs/zh/foundry/functions/python-functions-on-objects -->
<!-- 研读状态：已完成 -->

# 函数 • Python functions • 对象上的函数 • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/functions/python-functions-on-objects)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/functions/python-functions-on-objects)
- 页面语言：中文（官方 AIP 机器翻译，需与英文原文交叉核对）
- 主题栏目：functions
- 相关性：direct；本体函数文档
- 官方更新时间：2026-11-12T17:46:46.935Z
- 目录核对时间：2026-11-14T14:59:33Z
- 产品状态：Python Ontology 函数通过为仓库导入对象/链接并生成、安装 Python OSDK 来访问本体；对象和对象集由生成的类型绑定提供。

## 英文原文短摘录（每个来源不超过 25 词）

> “You can write functions that interact with the Ontology using the Python Ontology SDK.”

## 摘录译文

你可以使用 Python Ontology SDK 编写与 Ontology 交互的函数。

## 中文要点

- 先在 Resource Imports 中选择 Ontology 及要使用的对象、链接，之后在 SDK Generation 生成并安装包；后续增补资源或修改类型时需生成新 SDK 版本。
- 函数可将一个类型化对象作为输入，也可通过 `FoundryClient` 查询并返回对象集；代码补全来自生成的 OSDK。
- Python OSDK 支持部分 Beta 能力，例如对象集转 pandas DataFrame；查询对象集的语法由 SDK 类型和过滤表达式构成。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Python Ontology SDK | Python Ontology SDK | 由当前导入的本体资源生成的 Python 客户端和类型 |
| ObjectSet | 对象集 | 通过本体查询获得、可过滤和聚合的对象集合 |
| SDK generation | SDK 生成 | 根据已导入对象/链接类型生成语言包的过程 |
| Beta | Beta | 文档标明仍处于测试阶段的 OSDK 能力 |

## 疑问与待验证项

- 生成 SDK 包名在首次版本后不能更改，更新资源需要生成并安装新版本；自动发布节奏和旧版本兼容策略需另查 SDK 页面。
- 文档的 pandas DataFrame 互操作标为 Beta，尚不能将其当作稳定函数契约。
- 此页面示例依赖项目已正确选择目标 Ontology；只导入对象类型而未选 Ontology 会造成代码生成导入错误。

## 复刻启示

- 对本体 schema 的代码投影需绑定确定的 SDK 生成版本与导入快照；本体有变更时在项目分支生成候选 SDK 并审查差异。
- 画布节点和 Python 函数编辑器共享对象/链接 schema 来源，避免 UI 展示定义与运行时 SDK 脱节。
- Beta API 和 SDK 能力表显式标记预览/稳定状态，生产部署可设兼容检查门槛。
