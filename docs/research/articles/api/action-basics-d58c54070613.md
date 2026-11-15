<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/actions/action-basics -->
<!-- 研读状态：已完成 -->

# Action basics (v2, latest) • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/actions/action-basics)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/v2/ontologies-v2-resources
- 相关性：direct；Ontology REST API v2 参考
- 官方更新时间：2026-11-12T17:46:46.921Z
- 目录核对时间：2026-11-14T14:56:15Z
- 产品状态：常规 v2 概念页；本页未标注预览状态。

## 英文原文短摘录（每个来源不超过 25 词）

> “An Action represents one application of an action type.”

## 摘录译文

Action 表示一次 Action Type 的应用。

## 中文要点

- Action 是一次实际应用动作类型的执行；Action Type 是被重复使用的定义，二者分别代表定义和运行时实例。
- API 的 Action 端点用于提交变更。概念页没有进一步给出参数、校验结果、持久化记录或执行状态模型。
- 读取此页时应与 Action Type basics 和 Apply Action 配套，不能将某一次 Action 当作新的动作定义。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Action | 动作执行 | Action Type 的一次实际应用。 |
| Action Type | 动作类型 | 描述可重复执行的变更与逻辑。 |
| Ontology edit | 本体编辑 | 动作可能产生的对象或链接变化。 |

## 疑问与待验证项

- 概念页没有说明所有执行是否都会形成可长期查询的运行记录。
- 幂等、重试、去重与并发冲突语义应从 Apply Action 及事务文档继续核验。

## 复刻启示

- 数据模型分离 `ActionType` 定义与 `ActionRun` 执行记录；运行记录保留操作者、参数、校验、影响对象与结果。
- 画布展示 Action Type 与对象读写边，运行详情展示具体一次 Action 的状态和审计时间线。
