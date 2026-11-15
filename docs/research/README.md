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

当前目录工具为直接相关页面生成了 676 张卡片文件；截至 2026-11-15，641 张已完成首轮研读，35 张仍待填写。最近一次覆盖检查结果为：已有卡片 676 张、缺卡 0、未完成 35、超出摘录限制 0。本轮累计新增 437 张研读卡，覆盖 v2 Action、对象与值类型、关系、集合、Query API、Ontology Interface、Agent SDK、AIP Assist、MCP、Ontology Augmented Generation 与语义搜索。接口卡记录接口契约、继承属性、实现对象类型、分页读取以及 API 处于 Preview 的状态；类型卡区分对象 schema、实例、集合和值类型作用域，并记录多类型对象集的接口投影；Action 卡解释动作定义、运行调用、预验证与最终写入的边界，特别标明预验证不读取现存对象状态，批量端点不承诺原子性；对象关系卡区分 schema 边与实例边，并记录 v1 linked-object 查询的分页不一致、OSv1 上限和缺失链接错误；本轮新增动作日志与撤销、接口/结构体动作、读写授权以及隔离级别卡，标记了日志覆盖边界、撤销副作用限制、授权 Beta 状态与快照隔离下的写偏斜；随后补充分支动作、提交标准、动作权限、指标、监控和并发冲突卡，覆盖分支副作用隔离、权限边界、条件表达式风险及安全重试；本轮再补 Ontology 与 Space 多组织边界、Ontology Manager 资源视图、变更恢复、时间序列派生绑定和 AIP Logic 编辑仿真评估卡；随后补充 v2 对象集合加载/聚合 API 与 TS/Python 自定义聚合，明确了近似精度、分页快照、接口视图限制、SDK 版本差异和示例预测假设；再补 ObjectSet 概念、临时集合、按集合加载和 TSv1 对象集查询，记录惰性执行、链接遍历、集合运算、加载上限、分页完整性和机器翻译提示；随后覆盖全局分支应用、OSDK 概览、本体对象上的模型推理及 FoundryTS 时间序列属性引用，补充了分支隔离评审、SDK 资源授权、模型部署调用与时间序列查询边界；随后补充 Developer Console 应用治理、TS OSDK 接入、OpenAPI 多语言生成与本地注册表配置，记录默认资源限权、应用权限类型、凭据处理、SDK 版本与 schema 绑定；随后完成 Java/Python OSDK 参考和 Python 1.x→2.x 迁移指南，记录 Java 属性投影限制、Python Beta 派生属性、分页快照语义、SDK 返回类型/链接基数变化，以及机器翻译和未确认中文配对的风险；本批覆盖 REST API v2 的本体/对象集概念、按主键读取、对象分页与过滤搜索，梳理最终一致、快照、null 属性省略、派生属性实验状态、OAuth 读范围和查询嵌套/相关性排序限制；本批补充 REST API v2 查询定义、执行与 Query Type 元数据卡，记录默认版本可能为预发布、分支/事务实验状态、嵌套返回类型和查询 schema 驱动工具调用。本批完成时间序列属性概念、首末点与流式读取卡，注明时间戳和值结构、时间窗/聚合、Arrow 大流量选择，以及普通链接推理与时序窗口计算的边界；随后补齐 Query Type 列表与基础概念、Time Series Value Bank 基础和最新值/流式读取卡，记录游标分页、最新版本可能为预发布、地理时序实时优先、时间窗请求以及未明确的流协议编码；本批补充 Value Bank 时序属性定义、Ontology v1 概念、附件生命周期及元数据 API 卡片，记录 API 最终一致、附件暂存后经 Action 关联、元数据与内容分端点，以及样例的 `sizeBytes` 类型差异；本批补齐附件元数据/内容与原始二进制上传 API，并记录一小时暂存清理、写入授权和元数据/下载分离；同时梳理 v1 对象主键读取、聚合指标与分组契约，注明空值忽略、近似 distinct、分组上限和 v1 RID 路径；本批完成 v1 对象分页与结构化搜索、本体及 Query Type 基础卡，记录数据变更导致的跨页遗漏/重复、OSv1 10,000 条限制、null 属性省略、搜索查询三层限制和本体发布传播延迟；随后梳理 v1 Query Type 概念、列表/详情与执行 API，记录游标分页、Function RID/语义版本、参数输出契约及 `DataValue` 的嵌套和多类型 JSON 表达，并标出 v1 缺少 v2 分支/版本读取上下文的差异；本批完成显式 v1 Query Type 基础、Ontology SQL Preview 端点及 v1 附件基础卡，记录 SQL 的 Arrow 同步输出、dryRun/行数限制、分支/场景输入、仅支持 OSv2 的限制与 Preview 状态，并标注重复路由的概念去重；随后完成显式 v1 附件元数据、内容、二进制上传和详细聚合卡，补充一小时/双周孤儿清理、二进制 Content-Type、元数据类型冲突、null 忽略与聚合分组语义；本批覆盖 v1 对象聚合、主键读取、列表与 JSON 搜索，记录不一致分页、OSv1 10,000 条上限、null 字段省略、三层查询深度及内存缩页时继续读令牌的规则；本批补齐显式 v1 Ontology/Query 基础路由和 Query 执行卡，记录对象图语义、最终一致传播、Query Type 参数映射与多类型 `DataValue` 响应，并标注重复基础页路径；本批逐篇完成 v1 Query Type 详情/列表及 v2 Ontology 概念、附件属性分组/基础卡，记录分页游标、Function RID/版本、最终一致、附件引用边界及 API 列表能力；随后补齐 v2 附件属性元数据/内容读取和 Attachment 生命周期基础，注明对象/属性/RID 归属校验、分支上下文、临时上传后经 Action 关联、元数据与文件内容分离，以及 `sizeBytes` schema/示例类型差异；再补通用附件资源读取及 CipherText 属性/解密卡，明确全局 RID 与对象属性两种访问上下文、密文字段的明文读取边界、敏感数据审计建议和内容响应格式待核验项；随后补齐时间序列首末点/最新值、时空序列窗口及媒体引用读取卡，记录 Preview 与冷存储限制、半开时间范围和分页、MediaReference 投影缺省语义，以及媒体 Range 请求的 206/416 行为；本批再补 Ontology API 路由、对象集/查询/Query Type 分组及 Time Series 属性定义，并梳理 Ontology SQL Preview 同步 Arrow 输出、试运行、分支/场景输入和查询边界；本批完成 v2 Time Series Stream Points/Stream Values、Value Bank 属性定义及附件二进制上传卡，记录 JSON/Arrow 格式差异、Branch 上下文、二阶段对象绑定与一小时/双周孤儿清理规则；本批新增 Developer Console 授权上限与应用指标、Ontology 索引计算成本、Gaia 本体对象创建、嵌入式离线本体应用、Java OSDK 启动及 Foundry 静态托管卡，覆盖 OAuth scope 交集、Beta 指标滞后与聚合粒度、changelog 索引优化、Gaia 接口迁移、离线同步边界、令牌保管和前端静态部署限制；其他卡片区分了确定性关系推理和概率式向量召回，并记录 OTDP 当前尚未普遍开放、自定义 embedding 路线已不再推荐、模型能力受 enrollment 影响等边界。

本批补齐 Ontology 代码依赖导入、Code Workspaces 中的 OSDK 生成与使用、动态排程对象/资源模型、地理时间序列对象引用、Marketplace 类型分发边界，以及查询计算和索引占用模型；同步梳理 Ontology 作为语义与执行层的定位、多语言 SDK 的权限传播限制和 React OSDK 组件路线。

本批新增时间序列属性配置与传感器对象端到端建模、Ontology 搜索语法、TypeScript OSDK 迁移/测试/实时订阅/类型限制，以及 Action 类型和附件生命周期卡片。复刻设计会结合对象链接、时序绑定和 SDK 能力边界，避免将搜索、订阅或附件访问误建模成通用关系。

本批完成 Action 表单分区、对象下拉筛选的信息暴露、动作规则类型、函数支持动作与批量执行、动作入门和行内编辑卡片。重点记录 Function 规则不可与其他本体规则组合、自动升级时函数权限与 Action 权限分离，以及批量/行内编辑的冲突和顺序差异。

本批完成 Action 参数概述、默认值与覆盖、下拉筛选和性能、规则语义、规模/属性限制、通知配置及 Marketplace 打包卡片。重点记录全局默认与宿主覆盖优先级、对象集授权过滤、批次配额以及通知收件人必须是 Foundry 用户 ID。

本批完成函数支持动作、Webhook 写回与副作用、排程构建、Action 测试运行、附件/媒体上传、跨应用动作入口以及 Developer Console 权限卡片。特别区分了“模拟不写 Ontology”与仍可能触发的函数/外部调用、外部写回与本体编辑并非跨系统原子事务，以及附件/媒体权限继承本体对象或 Action 条件的边界。

本批完成 TypeScript v1 依赖与装饰器、对象/链接 API、本体编辑和调试，以及跨版本外部 API、分支函数、自定义别名、通知函数和 UUID 卡片。卡片标清 TSv1/TSv2/Python 的版本边界，并强调外部出站访问默认关闭、函数写入要经 Action、分支函数版本仅在当前分支可见。

本批完成函数的本体编辑机制、对象资源导入、函数接口、指标与执行模式、模型函数、扩展权限、SemVer 发布和函数仓库入门卡片。卡片强调对象写入通过 Action 应用、无服务器与长期部署能力/成本差异、LLM 函数接口发现机制，以及扩展调用 Action/长效令牌的白名单控制。

本批补齐函数遥测、语言支持矩阵、本地 OSDK、已发布函数治理与 Marketplace 发布，以及媒体读写和 LLM 代理/模型别名卡。重点区分语言能力差异、旧版模型迁移、仓库资源快照、函数执行可观测性、版本/API 名冲突与临时媒体持久化边界。

本批补齐官方中文 Action Types 路由的首组 10 张卡：表单分区、对象下拉筛选的侧信道风险、函数支持动作、入门教程、行内批量编辑、Marketplace 打包、通知、动作语义、参数契约和默认值优先级。中文页面均标注为未经验证的 AIP 机器翻译，卡片保留配对英文源的短摘录并据英文原文复核。

本批完成 10 张官方中文 Action Types 卡，覆盖参数筛选与优先覆盖规则、动作执行规则、提交规模限制、通知/webhook 配置、副作用时序、附件生命周期，以及 Object Views、Object Explorer、Workshop 的动作入口。跨系统 webhook 卡明确区分写回和尽力而为副作用，记录非原子双写窗口；中文路由均保留配对英文短摘录并注明机器翻译未校验。

本批完成 10 张 Functions 官方中文路由卡，覆盖 npm 依赖、附件与媒体、TSv1 对象/链接访问、本体编辑 API、语义检索文本分块、函数通知、断点调试、TypeScript 装饰器和对象唯一 ID。卡片特别记录 TSv1 与 TSv2/Python 的运行时差异、附件临时/持久生命周期、媒体旧路由、函数写入必须经 Action，以及 PDF chunk 回链证据语义。

本批完成 10 张 Functions 中文研读卡，涵盖本体编辑写集、执行上限、外部系统访问、面向对象的函数/资源导入、模型部署包装、仓库开发发布流程、函数类型契约、TSv1 LLM 接入与 Marketplace 分发。重点记录外呼默认关闭及来源别名、模型部署和本体版本依赖、函数类型跨语言差异与发布后权限传播。若目录旧英文路由已迁移或失效，卡片链接到现行官方规范页并保留迁移/404 疑问。

本批完成 10 张 Functions 官方中文路由卡，覆盖模型函数、对象标识、代码仓库的本体资源导入、函数性能、函数概览、语义搜索、PDF 文档处理、函数权限、Python 类型映射和 Query。旧中文路由迁移到当前英文文档的情况均在卡片中标出；重点记录项目级资源依赖、对象身份复合键、对象集的性能特点、检索证据回链、函数输出的权限传播风险，以及 Query 只读与 Action 写入的分界。

本批完成 10 张 Python Functions 中文研读卡，覆盖外部 API/source alias、Pipeline Builder 逐行 UDF、Python OSDK 对象读取、本体编辑与 staged writes、Workshop 函数部署/计算列、Query、资源导入、undefined 处理和时间/UUID mock。卡片标清 TSv1/TSv2 差异及 Beta 范围，并将本体写入限制为经 Action 提交的授权变更。

本批完成 10 张 Functions 测试/消费及语义搜索卡，涵盖函数单测调试、Jest 入门、对象集查询 stub、本体编辑断言、对象与用户/组 mock、平台宿主调用、用户可见错误，以及平台模型和自定义模型两种语义搜索工作流。复刻提示区分 mock 逻辑测试与真实权限/事务验证、查询函数与 Action、副作用，以及语义召回与关系推理；自定义模型流程已在官方页标注为不再推荐。

**页面编目完成不等于逐篇研读完成。**

可用以下命令复核：

```powershell
python scripts/check_research_coverage.py
```

- [本体管理系统复刻需求基线](replica-requirements.md)
- [本体管理系统设计说明](../superpowers/specs/2026-11-14-ontology-management-system-design.md)


本批完成 OSDK React 开发/排障、Python 与 TypeScript 应用启动、服务用户及跨组织权限、Developer Console 导航、旧 OAuth 客户端迁移和 TypeScript OSDK 1.x→2.0 卡片。卡片对照现行英文路由，注明官方中文机翻未经验证、OAuth client 已进入 Legacy、PR 预览为 Beta，并将个人 token 与服务端机密凭据分开。


本批完成 Developer Console 应用托管、Marketplace 本体类型打包与应用安装、Code Workspace SDK 生成、Node.js 版本固定，以及英文版 Python/TypeScript 启动、跨组织服务用户和 OAuth Legacy 原文卡。重点记录托管应用类型/域名审批、安装参数映射与 API name 冲突、数据源依赖闭包、SDK 发布态，以及目标环境 secret 轮换和 Compass 权限 Beta 边界。


本批补齐 Ontology 与 OSDK 问答、Pipeline Builder 本体输出、Object Set Service 执行/分页上限、WebSocket 对象集增量订阅、对象索引体量、2026 查询计算归因、TypeScript OSDK 集成测试/客户端参考，以及 Dynamic Scheduling 的 Schedule/Resource 模型。问答卡对照机器翻译与当前英文更新，标出 Python 版本冲突、OSv1 计划下线日期已过待核验；实时订阅卡区分增量 UI 更新与不完整的 join 订阅。


本批完成 10 张对象权限、Ontology GeoPoint 表达式、Functions 类型参考、VS Code 发布流程和函数监控卡。对象权限卡分开记录 schema 与实例数据授权、Restricted View 的 OSv1/OSv2 差异及策略传播；GeoPoint 卡梳理正反转换、格式验证、空值和坐标顺序；旧 OSDK 权限路由返回 404，卡片并列保留旧中文机翻与当前 Developer Console 权限规范，标注 Compass 用户权限 Beta 和模型迁移差异；Functions 卡记录跨语言类型映射、仓库全量函数发布范围、动态监控范围及失败分类。
