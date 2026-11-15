<!-- 页面 URL：https://www.palantir.com/docs/foundry/ontology/ontology-structural-guidance -->
<!-- 研读状态：已完成 -->

# Ontology design: Structural guidance • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/ontology/ontology-structural-guidance)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：ontology
- 相关性：direct；本体模型与治理文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:03:45Z
- 产品状态：页面说明属性规范化、派生值、struct 结构和访问控制的建模指导，并区分预计算值与运行时动态值。

## 英文原文短摘录（每个来源不超过 25 词）

> “Store each fact once. Use derived properties for convenience.”

## 摘录译文

每个事实只存一份；使用派生属性提供便捷访问。

## 中文要点

- 源值稳定且由同一 pipeline 更新时，可在 transform 中预计算；若依赖链接对象或会被 Action/Automation 等本体操作改变，应使用 runtime derived property，避免多处复制导致过期。
- 派生属性在查询时计算；文档建议低至中等规模（约每次查询少于 10k 对象）可直接使用，超过该规模可能增加延迟，应有意识地权衡选择性反规范化。
- 多字段且语义关联的数据宜建为 struct；可设 main field、reducer，并把来源、置信度、时间戳等元数据与主值放在同一结构中。
- 页面也覆盖访问控制结构，强调数据可见性边界需融入模型设计。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| normalization | 规范化 | 每个事实放在语义上归属的单一位置。 |
| derived property | 派生属性 | 查询时从对象属性或关联对象动态计算的值。 |
| struct | 结构体 | 将具备共同语义的多个子字段组合为一个属性。 |
| reducer | 归约器 | 从多值 struct 中选出最相关的一项。 |

## 疑问与待验证项

- - ~10k 是页面的经验分界而非硬限制；具体延迟依赖关系深度、过滤、基数、索引和查询量，需要以目标数据试算。
- - 复杂 struct、多值 reducer 和访问控制组合方式需另查属性/API 的类型限制。

## 复刻启示

- - 派生属性编辑器应提示属性来源、链接路径、集合基数、运行时计算范围和性能风险；对高基数路径提供预览样本及明确告警。
- - 保留 source-of-truth 属性映射并区分 materialized 与 dynamic；若用户选择复制值，要求填写同步策略和理由。
- - 支持 struct 字段及 metadata 子字段，使 AI 输出能一起保存主结果、引用来源、置信度和解释。
