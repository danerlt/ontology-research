<!-- 页面 URL：https://www.palantir.com/docs/zh/foundry/functions/python-functions-workshop -->
<!-- 研读状态：已完成 -->

# 函数 • Python functions • 在Workshop中使用Python函数 • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/functions/python-functions-workshop)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/functions/python-functions-workshop)
- 页面语言：中文（官方 AIP 机器翻译，需与英文原文交叉核对）
- 主题栏目：functions
- 相关性：direct；本体函数文档
- 官方更新时间：2026-11-12T17:46:46.935Z
- 目录核对时间：2026-11-14T14:59:34Z
- 产品状态：Workshop 可调用 serverless 或 deployed Python 函数；对象表的函数计算列使用对象集参数和按对象映射的返回字典。

## 英文原文短摘录（每个来源不超过 25 词）

> “This guide assumes you have already authored and published a Python function.”

## 摘录译文

本指南假定你已经编写并发布了 Python 函数。

## 中文要点

- 在 Workshop Variables 中搜索已发布 Python 函数；serverless 函数可使用任意版本，不需单独部署，deployed 函数则区分 Running、Stopped、Upgrading 状态。
- 部署版本可在 Ontology Manager 升级；切换仓库部署版本可能带来短暂中断，文档建议通过增加版本化函数名降低改动风险。
- 函数计算列要求输入包含对象集，返回 `dict[ObjectType, ColumnType]`，或返回按对象映射的多字段自定义类型；使用 `list[ObjectType]` 也可但较低效。
- 部署异常可从版本状态和 Ontology Manager Deployment 日志排查。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| serverless | 无服务器 | 由平台运行且无需手工启停某个部署版本的模式 |
| deployed function | 已部署函数 | 需要在 Ontology Manager 管理运行状态和版本的函数 |
| function-backed column | 函数计算列 | 以函数输出为对象表新增属性列的 Workshop 配置 |
| deployment status | 部署状态 | Running、Stopped、Upgrading 等函数服务状态 |

## 疑问与待验证项

- 文档称每个仓库同一时刻只有一个版本托管；通过并行增加版本化 API 名减少迁移耦合，但具体蓝绿发布能力仍需租户环境验证。
- 函数计算列返回映射需定义对象键覆盖率、缺失对象和空值展示语义；本页示例未完整规定这些边界。
- Workshop 的用户权限、函数仓库权限和对象数据权限仍应按 Permissions 文档组合判定。

## 复刻启示

- 在函数版本发布中将源码提交、release tag、部署状态和下游 Workshop 引用关联成发布记录，升级前列出受影响应用并支持回退。
- 对象表计算列用 ObjectSet 批量输入，返回对象 ID 到值的映射；画布预览展示参与计算的对象数和缺失值。
- 将 serverless 适用于快速交互的查询，与部署服务的运行状态、资源配额和可用性监控区分呈现。
