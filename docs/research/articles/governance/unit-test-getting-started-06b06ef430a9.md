<!-- 页面 URL：https://www.palantir.com/docs/zh/foundry/functions/unit-test-getting-started -->
<!-- 研读状态：已完成 -->

# 函数 • Unit testing • 入门指南 • Palantir

- 英文来源：[现行英文原文](https://www.palantir.com/docs/foundry/functions/unit-test-getting-started)
- 官方中文来源：[官方中文页（AIP 机器翻译，准确性未独立验证）](https://www.palantir.com/docs/zh/foundry/functions/unit-test-getting-started)
- 页面语言：中文（官方 AIP 机器翻译，需与英文原文交叉核对）
- 主题栏目：functions
- 相关性：direct；本体函数文档
- 官方更新时间：2026-11-12T17:46:46.935Z
- 目录核对时间：2026-11-14T14:59:41Z
- 产品状态：该 TSv1 单元测试入门页介绍使用 Jest 为函数仓库配置测试；模板默认带有测试文件，可在 `__tests__` 目录新增测试。

## 原文短摘录与翻译

> “Functions ships with support for Jest unit tests.”

## 摘录译文

Functions 提供对 Jest 单元测试的支持。

## 中文要点

- 模板仓库默认包含一个测试文件，并支持在 `__tests__` 目录内创建更多测试文件。
- 示例以纯函数 `addOne` 为被测逻辑，通过 Jest `expect(...).toEqual(...)` 验证输入输出。
- 该教程聚焦函数代码自身的单元测试，其他页面再说明如何 mock 对象查询、用户/组、时间/UUID，以及验证 Ontology edits。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Jest | Jest 测试框架 | 执行断言、mock 和测试用例的 JavaScript/TypeScript 工具 |
| `__tests__` | 测试目录 | 放置 Functions 仓库测试文件的约定目录 |
| assertion | 断言 | 验证实际结果与预期结果是否相符的语句 |

## 疑问与待验证项

- 导航路径标为 TSv1 Unit testing；该页不证明新版本 Python/TSv2 使用同一套 Jest 配置。
- 简单纯函数示例不会覆盖本体查询/写入、权限过滤、并发冲突和资源限额；需配合专门的函数测试工具页设计测试。

## 复刻启示

- 规则表达式/派生属性应有纯逻辑单测和对象关系集成试算两层；前者验证确定性，后者验证真实对象类型与链接语义。
- 新建函数模板就提供确定性 Jest/Python 测试样例和 stub 工具，让项目维护者先验证业务规则再发布。
- 把测试结果与函数源码提交、SDK schema 和 Ontology 分支绑定，保证审查者复现同一依赖版本。
