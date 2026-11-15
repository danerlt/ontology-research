<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/action-types/action-type-basics -->
<!-- 研读状态：已完成 -->

# Action Type basics (v2, latest) • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/action-types/action-type-basics)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/v2/ontologies-v2-resources
- 相关性：direct；本体动作文档
- 官方更新时间：2026-11-12T17:46:46.921Z
- 目录核对时间：2026-11-14T14:56:13Z
- 产品状态：常规 v2 概念页；本页未标注预览状态。

## 英文原文短摘录（每个来源不超过 25 词）

> “An action type represents a set of changes and logic that can be applied in the Ontology.”

## 摘录译文

Action Type 表示一组可应用于 Ontology 的变更和逻辑。

## 中文要点

- Action Type 是可复用的定义层，描述一组可应用到本体的变更与逻辑；定义在 Ontology Manager 中创建。
- 它对应“允许做什么”的模型，与某次实际提交的 Action 执行实例分离。具体参数、规则和结果结构需结合 Action Type schema 与 Apply Action 接口阅读。
- 该基础页没有展开动作校验、副作用、并发冲突或事务保证，不能仅凭“set of changes and logic”推断这些行为。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Action Type | 动作类型 | 可复用的本体变更与逻辑定义。 |
| Ontology Manager | 本体管理器 | 创建 Action Type 的产品界面。 |
| Action | 动作执行 | 一次应用 Action Type 的实际操作。 |

## 疑问与待验证项

- 规则在运行时的校验顺序、失败策略和副作用范围，要结合具体 LogicRule 文档与产品实测确认。
- 基础页没有声明定义版本、并发写入或原子提交的语义。

## 复刻启示

- 把 Action Type 建成独立的可版本化本体资源；画布节点显示参数、规则及其读写的对象/链接。
- 将定义、分支评审与运行记录分开呈现，并让 Agent 可发现的动作说明与人工说明各有明确字段。
