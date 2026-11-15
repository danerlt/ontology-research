<!-- 页面 URL：https://www.palantir.com/docs/foundry/functions/python-getting-started -->
<!-- 研读状态：已完成 -->

# Functions • Python • Getting started • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/functions/python-getting-started)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/functions/python-getting-started)（配对状态：matched）
- 页面语言：英文
- 主题栏目：functions
- 相关性：direct；本体函数文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:02:53Z
- 产品状态：页面未标注 Beta/预览/弃用；仓库路径和分支示例受模板配置影响。

## 英文原文短摘录（每个来源不超过 25 词）

> “Even if you declare the type of an argument with the API type, your function will be passed the corresponding Python type at runtime.”

## 摘录译文

即使参数声明使用 API 类型，运行时传入函数的仍是对应的 Python 类型。

## 中文要点

- Python 函数使用 `@function` 装饰器注册；输入和输出须声明平台支持类型，可写 Functions API 类型或对应 Python 类型。运行时传入原生 Python 类型。
- 入门流程为创建仓库、使用 Live Preview、提交并打版本标签；一个 Python 文件可包含多个函数，但只有带装饰器的函数注册。
- 指南建议把 Workshop/本体应用共用函数放在同一仓库以减少开销；仍需同时考虑项目权限、资源导入和发布边界。
- 这是基础教程；Ontology 对象读写、Pipeline Builder UDF 和 Workshop 使用各有独立能力/权限限制。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| @function | 函数装饰器 | 标记 Python 函数供平台发现与注册。 |
| live preview | 实时预览 | 发布前试运行函数的开发工具。 |
| function registry | 函数注册表 | 发布后供平台应用发现调用的函数目录。 |

## 疑问与待验证项

- 模板文件路径及 `master` 分支示例可能随仓库版本变化。
- 类型注解定义 registry 契约，运行时值的 Python 原生类型应与 API 声明区分。

## 复刻启示

- 保存输入输出 schema、仓库版本、运行环境和已发布版本；预览与发布使用同一授权验证逻辑。
- 发布向导分别呈现代码提交、检查、版本标签和权限传播状态。
