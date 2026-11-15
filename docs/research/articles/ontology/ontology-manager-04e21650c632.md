<!-- 页面 URL：https://www.palantir.com/docs/zh/foundry/ontology-manager -->
<!-- 研读状态：已完成 -->

# 本体管理器 • 概述 • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/ontology-manager/overview)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/ontology-manager)（已直接核验；页面声明未经验证的机器翻译）
- 页面语言：中文
- 主题栏目：ontology-manager
- 相关性：direct；本体管理器文档
- 官方更新时间：2026-11-12T17:46:46.937Z
- 目录核对时间：2026-11-14T15:00:13Z
- 产品状态：中文页面为 AIP 机器翻译；英文现行页展示资源视图与可观测性入口。

## 原文短摘录与翻译

> “Ontology Manager使您能够搭建和维护组织的Ontology。”

**对应英文：** “Ontology Manager enables you to build and maintain your organization’s Ontology.”

## 摘录译文

Ontology Manager 是用于搭建和维护组织本体的管理应用。

## 中文要点

- 管理器支持创建对象类型和动作类型、把数据接入 Ontology、调查用户应用的数据更新状态。文档列出 Discover、对象类型、属性编辑器、链接类型、动作类型和函数类型等主要视图。
- 顶部栏用于搜索/创建本体资源以及切换或新建分支；侧边栏在资源和应用之间导航。Discover 页面可配置收藏对象类型、最近访问对象类型和分组等内容。
- 对象类型概览包含元数据、属性、动作、链接类型图、依赖资源、数据与使用情况；从链接类型图可以进入链接类型视图。动作类型视图提供 Overview、Logic 与 Observability；后者展示近实时指标与监控规则。
- 本页描述的是资源管理器和类型关系图入口，未将全局本体自由画布列为该概览的 UI 组成项。需要把“对象类型页中的 Link type graph”和用户提出的全域流程图式模型画布区分开。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Ontology Manager / OMA | 本体管理器 | 创建、连接数据、查看和维护本体资源的管理应用。 |
| Discover view | 发现视图 | 可自定义的资源入口，展示收藏、最近浏览和分组。 |
| Link type graph | 链接类型图 | 对象类型概览中的关系导航视图。 |
| Observability | 可观测性 | 动作/函数运行指标与规则入口。 |

## 疑问与待验证项

- 中文页与英文页的视图清单略有差异，英文当前对象类型概览还列出 Dependents；UI 名称和页面分区会随产品版本演进。
- 本页没有说明画布的编辑布局、跨对象类型连接编辑或关系自动布局能力，需分别查找 Graph/Vertex 和设计图工具页面。

## 复刻启示

- 管理器壳层需要全局搜索、资源导航、创建入口、分支选择器、收藏/最近使用和资源类型页；对象详情页按元数据、属性、关系、动作、数据、依赖、使用组织信息。
- 在全域画布里保留类型图中的关系跳转语义，并让画布节点能打开对应属性、链接、动作、函数检查器；图边引用持久化关系定义，而非只画 UI 连线。
- 监控和动作审计由动作资源详情页提供上下文入口，连接同一 action ID 的定义、调用指标与日志。
