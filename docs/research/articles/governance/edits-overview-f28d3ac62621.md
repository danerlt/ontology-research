<!-- 页面 URL：https://www.palantir.com/docs/zh/foundry/functions/edits-overview -->
<!-- 研读状态：已完成 -->

# 函数 • Ontology edits • 概述 • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/functions/edits-overview)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/functions/edits-overview)
- 页面语言：中文
- 主题栏目：functions
- 相关性：direct；本体函数文档
- 官方更新时间：2026-11-12T17:46:46.935Z
- 目录核对时间：2026-11-14T14:59:12Z
- 产品状态：官方中文页标注为未经验证的 AIP 机器翻译；英文原文为核对依据。

## 英文原文短摘录（每个来源不超过 25 词）

> “An Ontology edit is the act of creating, modifying, or deleting an object.”

## 摘录译文

Ontology 编辑是创建、修改或删除对象的操作。

## 中文要点

- 本体编辑函数会返回可供 Function-backed Action 应用的编辑；TSv1 用 `@OntologyEditFunction`/`@Edits`，TSv2 用 `createEditBatch`/`Edits` 类型，Python 用 FoundryClient edits 容器。
- 创建/修改对象属性和增删链接都属于本体编辑。为完整数据来源追踪，需声明会编辑的对象类型；外键关系的一对一/一对多编辑要声明承载外键的对象类型。
- 本页将函数实现与 Action 执行边界分开：函数构造写入，Action 提供权限及操作上下文。各语言对编辑对象和写入表达存在不同 API。
- 中文官方页为未经验证的 AIP 机器翻译。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Ontology edit | 本体编辑 | 创建/修改/删除对象或链接的变更表达。 |
| Provenance | 数据来源追踪 | 记录编辑来自哪个函数、对象类型和动作的元数据。 |
| Edit batch | 编辑批次 | TSv2 组织多个本体变更的容器。 |

## 疑问与待验证项

- 声明不完整时平台推断写集的覆盖率/安全后果需进一步确认；权限策略不应依赖不完整静态推断。
- 本体编辑函数在不同语言中的原子性、读后写和 staged writes 能力需单独按执行版本查看。

## 复刻启示

- 编辑函数应返回明确的对象/属性/链接写集，随后交给授权 Action 校验并提交。
- 把写集及来源声明纳入静态检查和审计图，跨语言 SDK 保持操作语义一致。
