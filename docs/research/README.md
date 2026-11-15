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

卡片按主题存放在 `docs/research/articles/`。目标格式是保留官方原文链接、合规短摘录及中文译文，并记录原创中文摘要、术语、疑问/待验证项和本体管理系统复刻启示。

当前目录工具为直接相关页面生成了 676 张卡片文件；截至 2026-11-15，401 张已完成首轮研读，275 张仍待填写。最近一次覆盖检查结果为：已有卡片 676 张、缺卡 0、未完成 275、超出摘录限制 0。本轮累计新增 197 张研读卡，覆盖 v2 Action、对象与值类型、关系、集合、Query API、Ontology Interface、Agent SDK、AIP Assist、MCP、Ontology Augmented Generation 与语义搜索。接口卡记录接口契约、继承属性、实现对象类型、分页读取以及 API 处于 Preview 的状态；类型卡区分对象 schema、实例、集合和值类型作用域，并记录多类型对象集的接口投影；Action 卡解释动作定义、运行调用、预验证与最终写入的边界，特别标明预验证不读取现存对象状态，批量端点不承诺原子性；对象关系卡区分 schema 边与实例边，并记录 v1 linked-object 查询的分页不一致、OSv1 上限和缺失链接错误；本轮新增动作日志与撤销、接口/结构体动作、读写授权以及隔离级别卡，标记了日志覆盖边界、撤销副作用限制、授权 Beta 状态与快照隔离下的写偏斜；随后补充分支动作、提交标准、动作权限、指标、监控和并发冲突卡，覆盖分支副作用隔离、权限边界、条件表达式风险及安全重试；本轮再补 Ontology 与 Space 多组织边界、Ontology Manager 资源视图、变更恢复、时间序列派生绑定和 AIP Logic 编辑仿真评估卡；随后补充 v2 对象集合加载/聚合 API 与 TS/Python 自定义聚合，明确了近似精度、分页快照、接口视图限制、SDK 版本差异和示例预测假设；再补 ObjectSet 概念、临时集合、按集合加载和 TSv1 对象集查询，记录惰性执行、链接遍历、集合运算、加载上限、分页完整性和机器翻译提示；随后覆盖全局分支应用、OSDK 概览、本体对象上的模型推理及 FoundryTS 时间序列属性引用，补充了分支隔离评审、SDK 资源授权、模型部署调用与时间序列查询边界；随后补充 Developer Console 应用治理、TS OSDK 接入、OpenAPI 多语言生成与本地注册表配置，记录默认资源限权、应用权限类型、凭据处理、SDK 版本与 schema 绑定；随后完成 Java/Python OSDK 参考和 Python 1.x→2.x 迁移指南，记录 Java 属性投影限制、Python Beta 派生属性、分页快照语义、SDK 返回类型/链接基数变化，以及机器翻译和未确认中文配对的风险；本批覆盖 REST API v2 的本体/对象集概念、按主键读取、对象分页与过滤搜索，梳理最终一致、快照、null 属性省略、派生属性实验状态、OAuth 读范围和查询嵌套/相关性排序限制；本批补充 REST API v2 查询定义、执行与 Query Type 元数据卡，记录默认版本可能为预发布、分支/事务实验状态、嵌套返回类型和查询 schema 驱动工具调用。本批完成时间序列属性概念、首末点与流式读取卡，注明时间戳和值结构、时间窗/聚合、Arrow 大流量选择，以及普通链接推理与时序窗口计算的边界；随后补齐 Query Type 列表与基础概念、Time Series Value Bank 基础和最新值/流式读取卡，记录游标分页、最新版本可能为预发布、地理时序实时优先、时间窗请求以及未明确的流协议编码；本批补充 Value Bank 时序属性定义、Ontology v1 概念、附件生命周期及元数据 API 卡片，记录 API 最终一致、附件暂存后经 Action 关联、元数据与内容分端点，以及样例的 `sizeBytes` 类型差异；本批补齐附件元数据/内容与原始二进制上传 API，并记录一小时暂存清理、写入授权和元数据/下载分离；同时梳理 v1 对象主键读取、聚合指标与分组契约，注明空值忽略、近似 distinct、分组上限和 v1 RID 路径；本批完成 v1 对象分页与结构化搜索、本体及 Query Type 基础卡，记录数据变更导致的跨页遗漏/重复、OSv1 10,000 条限制、null 属性省略、搜索查询三层限制和本体发布传播延迟；随后梳理 v1 Query Type 概念、列表/详情与执行 API，记录游标分页、Function RID/语义版本、参数输出契约及 `DataValue` 的嵌套和多类型 JSON 表达，并标出 v1 缺少 v2 分支/版本读取上下文的差异；本批完成显式 v1 Query Type 基础、Ontology SQL Preview 端点及 v1 附件基础卡，记录 SQL 的 Arrow 同步输出、dryRun/行数限制、分支/场景输入、仅支持 OSv2 的限制与 Preview 状态，并标注重复路由的概念去重；随后完成显式 v1 附件元数据、内容、二进制上传和详细聚合卡，补充一小时/双周孤儿清理、二进制 Content-Type、元数据类型冲突、null 忽略与聚合分组语义；本批覆盖 v1 对象聚合、主键读取、列表与 JSON 搜索，记录不一致分页、OSv1 10,000 条上限、null 字段省略、三层查询深度及内存缩页时继续读令牌的规则；其他卡片区分了确定性关系推理和概率式向量召回，并记录 OTDP 当前尚未普遍开放、自定义 embedding 路线已不再推荐、模型能力受 enrollment 影响等边界。**页面编目完成不等于逐篇研读完成。**

可用以下命令复核：

```powershell
python scripts/check_research_coverage.py
```

- [本体管理系统复刻需求基线](replica-requirements.md)
- [本体管理系统设计说明](../superpowers/specs/2026-11-14-ontology-management-system-design.md)
