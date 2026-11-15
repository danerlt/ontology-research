<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/action-types/action-type-basics -->
<!-- 研读状态：已完成 -->

# Action Type basics (v2, latest) • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/action-types/action-type-basics)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/ontologies-v2-resources/action-types
- 相关性：direct；本体动作文档
- 官方更新时间：2026-11-12T17:46:46.921Z
- 目录核对时间：2026-11-14T14:53:27Z
- 产品状态：按页面现行表述整理；涉及分支/事务的能力以 Preview 或实验性限制为准。

## 英文原文短摘录（每个来源不超过 25 词）

> “An action type represents a set of changes and logic that can be applied in the Ontology.”

## 摘录译文

Action Type 表示一组可应用到 Ontology 的变更和逻辑。

## 中文要点

- Action Type 是动作的定义资源，包含一组变更及其逻辑；它在 Ontology Manager 中创建。
- 该基础页没有定义具体规则字段、校验顺序或副作用语义，应继续参考 Action Type 用户文档与相关 API schema。
- Action 与 Action Type 不同：前者是某次执行，后者是可重复应用的定义。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Action Type | 动作类型 | 定义可提交的本体变更及逻辑。 |
| Action | 动作执行 | 某次动作类型应用。 |
| Ontology Manager | 本体管理器 | 创建和配置动作类型的界面。 |

## 疑问与待验证项

- 基础页没有说明同一动作的并发冲突处理或事务原子性。
- 各类规则与 side effects 是否支持跨对象/外部操作，需按具体规则文档确认。

## 复刻启示

- 把动作定义和执行记录分成不同资源；画布中动作节点关联其影响的对象属性/链接及参数。
- 评审页应显示规则、输入参数、校验与副作用，使审批者能理解提交动作的业务影响。
