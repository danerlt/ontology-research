<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/actions/action-basics -->
<!-- 研读状态：已完成 -->

# Action basics (v2, latest) • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/actions/action-basics)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/ontologies-v2-resources/actions
- 相关性：direct；Ontology REST API v2 参考
- 官方更新时间：2026-11-12T17:46:46.921Z
- 目录核对时间：2026-11-14T14:53:32Z
- 产品状态：按页面现行表述整理；涉及分支/事务的能力以 Preview 或实验性限制为准。

## 英文原文短摘录（每个来源不超过 25 词）

> “An Action represents one application of an action type.”

## 摘录译文

Action 表示一次 Action Type 的应用。

## 中文要点

- Action 是某次应用动作类型以修改 Ontology 的执行；API 使用 Action 端点提交变更。
- Action Type 保存可复用规则和参数定义，单次 Action 则携带执行参数并产生校验与编辑结果。
- 该概念页很短，具体执行体、验证结果和异步状态需查看 Apply Action 等 API。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| application of an action type | 动作类型的一次应用 | 把一个定义落实为一次执行。 |
| action execution | 动作执行 | 一次实际提交和响应记录。 |
| Ontology edit | 本体编辑 | Action 可能造成的对象或链接变更。 |

## 疑问与待验证项

- API 概念页没有说明每个 Action 是否都必须创建持久化运行记录。
- 失败校验、重试和重复提交的幂等语义需查 Apply Action 文档。

## 复刻启示

- 保留每次动作的发起人、输入、验证结果、变更对象、时间和幂等键以形成完整审计链。
- 在图中以 Action Type 展示定义，以运行时间线展示 Action 实例，不把两个层次合并。
