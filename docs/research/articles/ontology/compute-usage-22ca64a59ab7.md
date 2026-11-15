<!-- 页面 URL：https://www.palantir.com/docs/zh/foundry/ontologies/compute-usage -->
<!-- 研读状态：已完成 -->

# 本体 • Usage • 计算使用：Ontology 索引 • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/ontologies/compute-usage)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/ontologies/compute-usage)
- 页面语言：中文（官方机器翻译，准确性未验证）
- 主题栏目：ontologies
- 相关性：direct；Ontology 索引作业成本说明的中文路由
- 官方更新时间：2026-11-12T17:46:46.935Z
- 目录核对时间：2026-11-14T15:00:06Z
- 产品状态：使用与成本说明；非 API Preview 页

## 英文原文短摘录（每个来源不超过 25 词）

> “Ontology stores objects in an Ontology index, a storage format optimized for rapid access.”

## 摘录译文

Ontology 会将对象存储在 Ontology index 中，这种存储格式针对快速访问进行了优化。

## 中文要点

- 中文文档将 Ontology 索引描述为把任意数据集转成适合本体快速访问的对象格式，索引成本以计算秒计量，并通过并行 Spark 后端执行。
- 作业成本由 driver/executor 的 CPU、内存与总运行时间决定；任务在 Builds 应用中可见并关联到正在索引的对象。对象数、属性数、属性体量与上游刷新频率会影响成本。
- 页面建议减少输入记录/属性/属性大小，或配置 changelog 索引只处理与已存在对象相比的变化；变更日志策略需要正确更新策略和更多配置。
- 中文页在正文开头明确声明翻译未经过准确性验证，事实与术语以[英文原页](https://www.palantir.com/docs/foundry/ontologies/compute-usage)为准。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Ontology indexing | Ontology 索引 | 将源数据转换为可查询、可编辑对象 |
| Changelog strategy | 变更日志策略 | 通过变更差量减少重建对象 |
| Wall-clock time | 墙钟时间 | 索引作业实际运行时长 |
| Index export job | 索引导出任务 | 将对象直接编辑写回数据集的任务 |

## 疑问与待验证项

- 中文路线保留旧页面翻译，页面明示机器翻译准确性未经验证；本卡对应英文同一内容，避免把中文表达当作独立产品承诺。
- 计算秒示例依赖资源规格；当前价格、配额和成本核算需按部署信息另查。
- 本卡范围只包括索引作业，不覆盖查询执行和对象操作的计算费用。

## 复刻启示

- 连接器应支持可恢复的增量同步、变更检测和全量回填；变更策略需要包含更新、删除和 schema 变化的处理约定。
- 建立项目级索引作业记录和预算看板，以对象量、字段量、刷新频率及资源/运行时间估算导入成本。
- 将索引写入成本和运行时推理/查询成本分开埋点，便于定位“导入慢”还是“画布查询/派生属性计算”过重。
