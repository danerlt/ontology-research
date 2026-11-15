<!-- 页面 URL：https://www.palantir.com/docs/foundry/functions/functions-versioning -->
<!-- 研读状态：已完成 -->

# Functions • 函数版本管理 • Function versioning • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/functions/functions-versioning)
- 官方中文来源：尚未确认（配对状态：ambiguous）
- 页面语言：英文
- 主题栏目：functions
- 相关性：direct；本体函数文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:02:27Z
- 产品状态：函数发布版本由发布者指定且不可修改；遵循语义化版本并用兼容性约束保护消费者。

## 英文原文短摘录（每个来源不超过 25 词）

> “Versions for function releases are chosen by their publishers and are immutable after creation.”

## 摘录译文

函数发布版本由发布者选择，创建后不可更改。

## 中文要点

- 版本发布后不可变，消费者以固定版本依赖时可获得稳定行为；开发者需要判断哪些更改会影响既有消费者。
- 向后兼容示例：添加可选输入、保持预期行为的性能优化和修复不改变预期行为的 bug。
- 破坏性示例：新增必填输入、改变输出类型、删除函数；消费方必须注意或改变调用方式的变更就应作为 breaking change。
- 版本采用 SemVer 的 X.Y.Z 形式，可带 prerelease 标识；版本约定是跨应用可靠消费的基础。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Immutable release | 不可变发布版 | 创建后版本和行为不再修改的发布资源 |
| Backward compatible | 向后兼容 | 不干扰现有函数消费者的变更 |
| Breaking change | 破坏性变更 | 要求已有消费者显式处理或修改调用的变化 |

## 疑问与待验证项

- 兼容性取决于调用者行为，新增可选字段若改变运行逻辑也可能影响消费者，发布者仍需评估行为变更。
- SemVer 的 major/minor/patch 规则需要在团队发布规范里明确并通过自动兼容检查支撑。

## 复刻启示

- 函数版本是本体 Action/应用依赖图中的不可变构建产物；发布策略需明确 semver、prerelease 与依赖范围。
- 依赖图对输出/必需输入变化进行 breaking-change 检测，并在更新消费者前展示影响函数、Action 和 Agent。
