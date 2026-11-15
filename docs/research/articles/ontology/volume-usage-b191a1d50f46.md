<!-- 页面 URL：https://www.palantir.com/docs/zh/foundry/ontologies/volume-usage -->
<!-- 研读状态：已完成 -->

# 本体 • Usage • Ontology 占用量 • Palantir

- 英文来源：[当前英文原文](https://www.palantir.com/docs/foundry/ontologies/volume-usage)
- 官方中文来源：[中文原文](https://www.palantir.com/docs/zh/foundry/ontologies/volume-usage)
- 页面语言：中文（官方机器翻译，准确性未验证）
- 主题栏目：ontologies
- 相关性：direct；本体管理与治理文档
- 官方更新时间：2026-11-12T17:46:46.935Z
- 目录核对时间：2026-11-14T15:00:13Z
- 产品状态：Ontology 对象索引和链接存储规模说明

<!-- 研读状态：已完成 -->
# 英文原文短摘录（每个来源不超过 25 词）

> “Ontology volume is a measure of the total size of the indexed object sets and their links with each other.”

## 摘录译文

Ontology 占用量衡量已索引对象集及其相互链接的总大小。

## 中文要点

- Ontology volume 衡量对象索引中对象属性和链接的体积；瞬时单位为 GB，按月统计使用 GB-Month。
- 平台每小时采集对象体积，再对所选时间范围内的小时读数求平均；一个日历月的平均值对应 GB-Month。
- 本体数据不能像源数据一样压缩，索引还需额外空间加速访问，因此本体体积可能大于底层数据集。
- 主要驱动因素是对象数量、属性数量与大小，以及多对多 join table 中的链接数；Resource Management Application 展示总体积。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Ontology volume | 本体占用量 | 本体对象索引和链接的存储规模 |
| GB-Month | GB 月 | 按月平均 GB 用量表示的体积单位 |
| Join table | 连接表 | 多对多链接的键表，也计入本体索引体积 |
| Hourly measurement | 小时采样 | 每小时记录对象体积的指标粒度 |

## 疑问与待验证项

- 页面未提供不同属性类型、索引结构或数据压缩的容量系数。
- 月平均账期、刷新采样处理和合同单位价格需向部署环境核验。

## 复刻启示

- 为对象类型、属性和关系估算存储成本，并把多对多链接表计入本体成本。
- 管理台提供项目/本体/类型维度的小时趋势和月均视图，提示高基数链接与大文本字段的成本。