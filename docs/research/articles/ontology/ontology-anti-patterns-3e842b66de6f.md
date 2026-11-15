<!-- 页面 URL：https://www.palantir.com/docs/foundry/ontology/ontology-anti-patterns -->
<!-- 研读状态：已完成 -->

# Ontology design: Anti-patterns • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/ontology/ontology-anti-patterns)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：ontology
- 相关性：direct；本体模型与治理文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:03:45Z
- 产品状态：当前页面整理八类常见设计反模式及解决方式：系统孤岛、厨房水槽、部门孤岛、上帝对象、万能工具、Action 泛滥、时间机器和误导命名。

## 英文原文短摘录（每个来源不超过 25 词）

> “Creating separate object types for each source system.”

## 摘录译文

为每个来源系统分别创建对象类型。

## 中文要点

- 多来源系统中的同一现实实体应通过管道合并到统一类型，并定义跨系统主键及冲突字段优先级，避免用户面对多个源系统版本。
- 对象类型应有意筛选业务属性，ETL 元数据保留在底层数据集；同一个类型不要囊括多种实体，也不要把一切问题强行交给一个工具。
- Action 应围绕完整业务操作组合，历史变化通常以实体加历史/修订链接或时间序列表达；名称要具体并准确反映实体、属性和关系。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| System Silos | 系统孤岛 | 同一实体按不同源系统被建成多个对象类型。 |
| The Kitchen Sink | 厨房水槽反模式 | 将大量无关技术字段暴露为本体属性。 |
| The God Object | 上帝对象 | 一个对象类型混合多种不同领域实体。 |
| Action Sprawl | Action 泛滥 | 把业务操作拆成许多零散的单属性 Action。 |

## 疑问与待验证项

- - 文档建议将多来源数据合并，但不同业务场景可能保留来源特有字段；需用 source lineage 属性/界面呈现来源，不要为每个来源复制实体类型。
- - 选择 pipeline、Action、Automation、Function 的界限需与实时性和人机决策要求联合评估。

## 复刻启示

- - 多项目系统注册表要把不同来源映射到共享领域实体，并维护键匹配、字段优先级和冲突处理，而不是生成系统前缀对象类型。
- - 画布/模型检查应发现重复实体、未使用技术字段、过宽对象和多条同义关系，并用可解释的建议提示修复。
