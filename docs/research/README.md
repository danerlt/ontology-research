# Palantir Ontology 与 Agent 文档目录

> 目录快照：2026-11-14。仅保存公开页面元数据、分类和链接，不保存文章正文。

## 官方入口

- [Foundry 英文文档](https://www.palantir.com/docs/foundry/)
- [Foundry 官方中文文档](https://www.palantir.com/docs/zh/foundry/)
- [官方文档 sitemap](https://www.palantir.com/docs/sitemap.xml)

## 覆盖情况

本次从官方 sitemap 的主题路由和 10 个 Ontology/Agent 种子页开始发现页面，再沿官方侧边栏补充导航链接。站点 sitemap 达到 5,000 条 URL 上限；主题筛选和导航补充共得到 682 个唯一页面。

| 项目 | 数量 | 说明 |
|---|---:|---|
| 唯一页面 | 682 | sitemap 路由与导航去重后的结果 |
| 英文页面 | 527 | 英文页面为研读卡片的主要来源 |
| 中文页面 | 155 | 官方中文页面候选 |
| 直接相关 | 676 | Ontology、管理、动作/函数、权限、Agent、SDK/MCP 与相关 API |
| 补充参考 | 6 | 数据连接代理运行时 4 页、Gaia 地理空间消费示例 2 页 |
| 抓取成功 | 682 | 标题与 canonical URL 均存在 |
| 抓取失败 | 0 | 抓取时间：2026-11-14 |

### 官方中文配对

英文页面按规范化路由与中文页面精确配对；近似 slug 只作为复核候选，不直接认定为译文。

| 配对状态（英文页） | 数量 | 含义 |
|---|---:|---|
| 已配对 | 99 | 英中规范路由一致 |
| 未发现中文页 | 330 | 当前 Foundry sitemap 中没有同路由或近似路由 |
| 多个候选 | 72 | slug 相似的中文候选不止一个，需人工判断 |
| 单个近似候选 | 26 | 只有 slug 近似，需人工判断 |

“未发现中文页”不等于确认没有中文译文；若英文与中文页面使用不同路由，仍需人工核对。卡片会保留英文官方链接，并在可确认时加入官方中文链接。

## 分类边界

- `direct`：本体结构与治理、对象/链接类型、Action Types、Functions、对象权限、Ontology Manager、Ontology SDK/API、Agent Builder/Manager/SDK、Agent/MCP 集成，以及相关写入/读取 API。
- `supplement`：Foundry 数据连接代理运行时配置（这里的 agent 不是 AIP Agent），以及 Gaia 地理空间应用对本体数据的下游消费示例。
- Ontology API v1 仍列为直接相关的兼容性参考；新实现优先比较 v2 页面，并在卡片中标注版本差异。
- `classification_status=needs_review` 与 `zh_pair_status=ambiguous|needs_review` 的项目不应被自动规则静默定案。

## 目录字段

`data/palantir_docs_catalog.jsonl` 每行对应一页，包含 URL、canonical URL、英文/中文语言、栏目、标题、描述、sitemap 更新时间、发现来源、抓取状态、相关性及理由、分类置信度、官方中文配对状态和核对时间。页面响应只用于提取 head 与导航元数据，文章正文不写入文件。

## 研读卡片

卡片按主题存放在 `docs/research/articles/`。每篇保留官方原文链接，英文短摘录及中文译文总计不超过 25 个英文词，并提供原创中文摘要、术语、疑问/待验证项和本体管理系统复刻启示。

- [本体管理系统复刻需求基线](replica-requirements.md)（阶段五交付）
- [阶段实施计划](../../IMPLEMENTATION_PLAN.md)
