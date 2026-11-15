<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/ontology-objects/search-objects -->
<!-- 研读状态：已完成 -->

# Search Objects (v2, latest) • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/ontology-objects/search-objects)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/v2/ontologies-v2-resources
- 相关性：direct；Ontology REST API v2 参考
- 官方更新时间：2026-11-12T17:46:46.921Z
- 目录核对时间：2026-11-14T14:57:30Z
- 产品状态：常规 v2 搜索接口；分支与 OTDP 参数有实验性限制。

## 英文原文短摘录（每个来源不超过 25 词）

> “Queries can be at most three levels deep.”

## 摘录译文

查询最多可以嵌套三层。

## 中文要点

- POST `/api/v2/ontologies/{ontology}/objects/{objectType}/search` 以查询树筛选对象，支持比较、相等、空值、数组包含、文本词项及 AND/OR/NOT 组合；查询最多三层。
- 请求可设置字段排序或相关性排序。相关性排序适用于部分文本查询和 nearest-neighbor 查询，但跨页结果顺序不稳定，完整性要求高时应限制为单页。
- 支持属性投影、分页和 `executeInMemoryOnly`（无法在内存中完成则快速失败）；OTDP 可随结果返回但当前属实验性、尚未普遍开放。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| where | 筛选条件 | 由比较或逻辑查询构成的过滤树。 |
| orderBy | 排序规则 | 按字段或相关性排序。 |
| executeInMemoryOnly | 仅内存执行 | 遇到无法以内存方式完成的查询时直接报错。 |
| nearestNeighbors | 近邻查询 | 与相关性排序关联的一类搜索条件。 |

## 疑问与待验证项

- 具体查询支持矩阵会随属性数据类型变化，前端构造器应由 schema 驱动，而不是让所有字段共用同一操作符。
- 相关性分页可能重复或漏过对象；需要完整结果的场景应改用稳定排序或单页策略。
- OTDP 的查询、排序或过滤能力没有在本页逐项保证。

## 复刻启示

- 把查询编辑器做成有类型的过滤树，限制三层嵌套并依据字段类型提供合法操作符。
- 相关性排序标注为非稳定分页；大结果集采用稳定字段排序和快照策略。
- 派生属性进入搜索前，需在本地验证其可筛选、可排序和可索引语义，并显示推导路径。
