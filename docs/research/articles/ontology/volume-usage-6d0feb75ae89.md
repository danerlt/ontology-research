<!-- 页面 URL：https://www.palantir.com/docs/foundry/ontologies/volume-usage -->
<!-- 研读状态：已完成 -->

# Ontologies • Usage • Ontology volume • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/ontologies/volume-usage)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/ontologies/volume-usage)（目录配对状态：matched）
- 页面语言：英文
- 主题栏目：ontologies
- 相关性：direct；本体索引容量计量和资源治理
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:01:38Z
- 产品状态：使用按小时采样并按期间取平均的体量指标；计量单位按观察区间变化

## 英文原文短摘录（不超过 25 词）

> “Ontology volume is an average metric that has the unit of GB for an instantaneous reading”

## 摘录译文

Ontology volume 是平均体量指标，瞬时读数的单位为 GB。

## 中文要点

- Foundry Ontology 是支持查询、链接、场景与 Action 的快速访问存储层；对象集和链接经索引以支持交互访问与并发安全编辑。
- volume 衡量对象集索引及其链接相关索引的总体大小，不是源数据集的文件体积。
- 对每个对象类型，索引大小由对象数量及其每个已索引属性大小汇总；本体 volume 可能大于数据集体量，因为数据不压缩且索引需要额外空间。
- 平台每小时记录对象本体体量；按一个月计量时，将小时读数取平均并使用 GB-Month 单位。
- Ontology Manager 是对象类型、属性和链接的配置/监控入口；对象和对应链接的总 volume 显示在 Resource Management Application。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Ontology volume | 本体体量 | 对象类型/链接底层索引所占空间计量 |
| indexed property | 已索引属性 | 索引体量统计范围内的对象属性 |
| GB-Month | GB 月 | 对月度期间的平均 GB 体量进行的计量单位 |
| Resource Management Application | 资源管理应用 | 查看对象类型和链接总本体体量的入口 |

## 疑问与待验证项

- 页面未细分链接索引和属性索引的精确占比算法，也未说明哪些属性不纳入索引体量统计。
- GB-Month 的账单汇总、舍入、时间边界及项目分摊方式需结合合同/计量界面确认。
- 每小时采样会平滑短时间尖峰；容量告警仍需结合高水位或存储变化速度设计。

## 复刻启示

- 多项目工作台应分开显示源数据体积、本体索引体量和关系开销，并明确采样时间与统计区间。
- 对象类型和链接可按项目、系统来源和属性维度呈现资源估算，用于识别高基数或宽对象成本。
- 将当前/按月平均的不同单位写进指标模型，避免把瞬时 GB 与 GB-Month 混为一列。