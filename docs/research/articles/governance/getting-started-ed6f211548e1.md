<!-- 页面 URL：https://www.palantir.com/docs/foundry/functions/getting-started -->
<!-- 研读状态：已完成 -->

# Functions • 入门 • Getting started with functions • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/functions/getting-started)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/functions/getting-started)（配对状态：matched）
- 页面语言：英文
- 主题栏目：functions
- 相关性：direct；本体函数文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:02:25Z
- 产品状态：Foundry 提供 TypeScript v1、TypeScript v2 和 Python 函数仓库；基础运行/测试/发布流程一致但能力矩阵不同。

## 英文原文短摘录（每个来源不超过 25 词）

> “There are three language options for getting started with functions in Foundry: TypeScript v1, TypeScript v2, and Python.”

## 摘录译文

在 Foundry 中可以使用 TypeScript v1、TypeScript v2 或 Python 开始编写函数。

## 中文要点

- 三种语言都能运行、测试和发布函数，但具体特性支持不同，需查语言矩阵并选择对应教程。
- 函数仓库可从 Project 或 Code Repositories 创建；可在 Code Repositories 或 VS Code Workspaces 开发，后者推荐并提供预览、资源导入、SDK 生成、分支和发布管理。
- Live Preview 可在提交前用输入参数运行函数，但与已发布 runtime 的 CPU、内存和超时资源不同。
- 提交后通过 Tag version 创建发布，函数进入 Registry；权限传播可能导致函数名称暂时无法搜索到。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Functions repository | 函数仓库 | 包含源代码、资源依赖和发布配置的函数项目 |
| Live Preview | 实时预览 | 提交前用输入参数运行代码的预览环境 |
| Function registry | 函数注册表 | 平台可发现和复用已发布函数的目录 |

## 疑问与待验证项

- Live Preview 与发布 runtime 差异可能掩盖资源限制问题，生产可运行性需在目标执行模式复核。
- 页面示例提交到 master 分支；当前代码仓库默认分支可能不同，实际按仓库分支配置执行。

## 复刻启示

- 为函数仓库建立创建→导入 Ontology/SDK→预览/测试→提交→语义版本发布→应用消费的明确生命周期。
- 按语言/版本维护能力矩阵；预览结果记录资源差异、当前分支、函数版本和授权的数据源依赖。
