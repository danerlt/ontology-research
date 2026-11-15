<!-- 页面 URL：https://www.palantir.com/docs/foundry/functions/edits-overview -->
<!-- 研读状态：已完成 -->

# Functions • 本体编辑概述 • Ontology edits • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/functions/edits-overview)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/functions/edits-overview)（配对状态：matched）
- 页面语言：英文
- 主题栏目：functions
- 相关性：direct；本体函数文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:02:42Z
- 产品状态：TypeScript v1/v2 与 Python 函数都可产出本体对象/链接编辑，Action 来源元数据用于权限判定。

## 英文原文短摘录（每个来源不超过 25 词）

> “An Ontology edit is the act of creating, modifying, or deleting an object.”

## 摘录译文

本体编辑是创建、修改或删除对象的操作。

## 中文要点

- 函数可返回对象属性、对象和链接编辑，供 function-backed Action 应用；不同语言的编辑 API 不同。
- TSv1 使用 @OntologyEditFunction 与 @Edits；TSv2 通过 @osdk/functions 的 createEditBatch 和 Edits 类型；Python 使用 Ontology SDK 的 FoundryClient edits 容器和 decorator edits 参数。
- 来源元数据描述函数可修改哪些对象类型，Action 可据此执行权限检查；链接编辑也属于本体编辑，外键型关系需声明持有外键的对象类型。
- Automate 的普通 function effect 不会自动应用函数返回的本体编辑；要通过自动化写本体，需配置 function-backed Action。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Ontology edit | 本体编辑 | 创建/更改/删除对象或关系的编辑记录 |
| Provenance | 来源范围 | 函数声明的可编辑对象/链接范围 |
| Edit batch | 编辑批次 | 聚合并提交一组本体变更的容器 |

## 疑问与待验证项

- 不同语言的编辑批次 API 和声明形式并不相同，需要分别做类型和权限校验。
- Automate effect 与 function-backed Action 的写入语义不同，调用方设计不能仅按函数返回值推断已提交。

## 复刻启示

- 编辑函数统一生成有来源范围的变更集；应用入口再由 Action 执行授权、提交条件、写入和审计。
- 画布追踪函数到对象类型/链接类型的可写边，并阻止未声明类型的运行时编辑。
