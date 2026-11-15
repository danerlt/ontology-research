<!-- 页面 URL：https://www.palantir.com/docs/foundry/functions/unit-test-getting-started -->
<!-- 研读状态：已完成 -->

# Functions • Unit testing (TSv1) • Getting started • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/functions/unit-test-getting-started)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/functions/unit-test-getting-started)（配对状态：matched）
- 页面语言：英文
- 主题栏目：functions
- 相关性：direct；本体函数文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:03:24Z
- 产品状态：TSv1 单元测试指引；本轮仅研读，不运行测试。

## 英文原文短摘录（每个来源不超过 25 词）

> “Functions ships with support for Jest unit tests.”

## 摘录译文

Functions 仓库内置对 Jest 单元测试的支持。

## 中文要点

- 函数仓库默认提供 Jest 测试文件，可在 `__tests__` 目录创建测试；测试逻辑可直接构造函数类并调用纯逻辑。
- 可在 Code Repositories UI 运行单个测试或整个测试集；提交时 checks 也会运行相关测试。
- 本页给出标量函数最小例子，并指向 stub 对象、验证 Ontology edits、模拟搜索/聚合等后续专题。
- 此类 mock 单测验证函数逻辑，不替代真实运行时权限、Ontology 事务或数据索引集成验证。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Jest | Jest 测试框架 | TSv1 函数仓库用于编写和执行单元测试的工具。 |
| __tests__ | 测试目录 | 存放自动发现单测文件的仓库目录。 |
| Checks | 提交检查 | 随提交执行的构建/质量校验流程。 |

## 疑问与待验证项

- 测试文件识别规则和运行命令与旧 TSv1 仓库模板有关，需区分现代 Code Workspace/TSv2 测试工作流。
- 单测覆盖不能证明部署函数的真实权限上下文和查询一致性。

## 复刻启示

- 为派生属性/Action规则提供确定性单元测试和 mock 数据，并单独保留真实数据库/权限集成验收。
- 分支提交时自动执行规则测试，将测试结果链接到变更评审与发布审批。
