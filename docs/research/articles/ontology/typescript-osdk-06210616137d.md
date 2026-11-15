<!-- 页面 URL：https://www.palantir.com/docs/foundry/ontology-sdk/typescript-osdk -->
<!-- 研读状态：已完成 -->

# Ontology SDK • TypeScript • TypeScript OSDK • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/ontology-sdk/typescript-osdk)
- 官方中文来源：尚未确认（目录配对状态：ambiguous）
- 页面语言：英文
- 主题栏目：ontology-sdk
- 相关性：direct；TypeScript OSDK 对象、对象集、关系和 Action API
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:04:41Z
- 产品状态：当前示例以 TypeScript OSDK 2.x 为目标；具体应用可在 Developer Console 查看版本专属生成文档

## 英文原文短摘录（不超过 25 词）

> “This page provides generic documentation for the TypeScript OSDK based on an example `Restaurant` object and its associated actions and queries.”

## 摘录译文

本页以示例 Restaurant 对象及其关联 Action 和 Query 提供通用 TypeScript OSDK 文档。

## 中文要点

- 页面是通用 SDK 参考，示例以 `Restaurant` 对象类型演示读取、过滤、链接、对象集、Action 和 Query/Function；实际应用应看 Developer Console 中按已选 Ontology 资源生成的文档。
- 2.x 示例使用类型化客户端按主键或分页读取；对象集可迭代、过滤和排序，并能组合 union/intersect/subtract。
- 关系查询通过类型化链接访问器遍历；集合支持聚合，SDK 另提供 nearest-neighbor、Action 调用、Function 和 scenario-scoped client 用法。
- 页面专门包含分页一致性与快照章节，提醒开发者需要区分跨页时数据变化与稳定读取视图；1.x 升级需另查迁移指南。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| generated TypeScript SDK | 生成的 TypeScript SDK | 与应用选择的本体资源和 API 版本绑定的类型化包 |
| object set | 对象集 | 以惰性查询表达式构成的对象结果集合 |
| set operation | 集合操作 | union、intersect、subtract 等对象集运算 |
| scenario-scoped client | 场景范围客户端 | 按某个场景上下文访问对象数据的客户端 |

## 疑问与待验证项

- 通用页只覆盖示例对象，应用自己的资源可用范围、权限和类型定义需要从生成文档读取。
- 页内 2.x API 不应与 1.x 客户端语法混用；迁移期间需逐项检查返回类型、链接和 Action 响应。
- 快照和分页一致性的具体边界需按对应 fetch API 选项核对，不应推断任意遍历都是全程一致快照。

## 复刻启示

- 用 schema 生成强类型客户端与文档，让应用代码只调用被授权的对象、关系、Action 和查询。
- 对象集运算保留可组合查询计划，不要求 UI 一次加载所有对象；分页/快照策略通过 API 参数明确。
- 所有执行结果展示数据版本、场景上下文和访问范围，关系遍历沿本体定义边执行。