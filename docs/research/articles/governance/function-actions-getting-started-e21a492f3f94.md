<!-- 页面 URL：https://www.palantir.com/docs/zh/foundry/action-types/function-actions-getting-started -->
<!-- 研读状态：已完成 -->

# 动作类型 • Function-backed actions • 入门 • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/action-types/function-actions-getting-started)
- 官方中文来源：尚未确认（配对状态：not_applicable）
- 页面语言：中文
- 主题栏目：action-types
- 相关性：direct；本体动作文档
- 官方更新时间：2026-11-12T17:46:46.935Z
- 目录核对时间：2026-11-14T14:58:13Z
- 产品状态：官方中文页标注为未经验证的 AIP 机器翻译；英文原文为核对依据。

## 原文短摘录与翻译

> 英文原文：This tutorial explains how to create an action type that is backed by an Ontology Edit function.

> 中文译文：本教程介绍如何创建由 Ontology Edit 函数支持的操作类型。

## 摘录译文

以上为英文短摘录及中文译文。官方中文页面为 AIP 机器翻译，准确性未经验证。

## 中文要点

- 先在 TypeScript 函数仓库导入相关对象类型，编写并发布 Ontology Edit 函数，再把发布版本接入动作规则。
- 操作规则选择一个函数规则并映射函数输入；函数的输入会自动形成动作参数，可再配置对象引用或表单展示。
- 用于该路线的函数必须使用 `@OntologyEditFunction()`，不能用普通 `@Function()`；函数规则也不能与其他规则混搭。
- 函数逻辑更新后，动作不会自动改指新版本；需在动作规则中主动升级引用版本。中文页面为未校验的机器翻译。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Function-backed action | 函数支持的操作 | 以已发布的本体编辑函数执行业务编辑的动作类型。 |
| Ontology Edit function | 本体编辑函数 | 通过专用声明执行本体对象编辑的函数。 |
| Function version | 函数版本 | 动作规则显式绑定的已发布函数版本。 |

## 疑问与待验证项

- 函数入参的 schema 变化如何影响已配置的参数默认值、权限和提交条件，需在版本升级时逐项对比。
- 本教程基于 TSv1 样例模板；当前新建仓库和 OSDK 版本的具体用法需查现行函数指南。

## 复刻启示

- 动作与函数间保存不可变版本绑定及输入映射；升级时提供 schema diff、兼容性检查和显式确认。
- 区分普通查询函数与可写本体的编辑函数，权限模型不得因“由函数执行”而跳过 Action 级校验。
