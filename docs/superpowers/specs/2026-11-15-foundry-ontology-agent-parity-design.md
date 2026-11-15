# Foundry 本体与 Agent 管理工作台高保真复刻设计

## 目标与适用范围

把当前演示级本体工作台升级成一套面向真实建模与运行治理的系统。产品行为以 Palantir Foundry 公开文档中 Ontology Manager、Global Branching、对象权限、Agent Builder 和 Agent Manager 的工作流为参照，提供对应的可操作能力和可追踪状态。

“高保真”指公开功能与用户工作流的对应关系，不承诺复刻 Palantir 的闭源代码、内部服务、专有数据格式、商标、素材或逐像素界面。每个有意缩小的范围都应在页面或文档中说明；不以静态样例或无法持久化的按钮冒充已实现能力。

主要用户与任务：

- 本体建模者：浏览本体资源，编辑类型、属性、链接、Action 与 Function 元数据，在隔离分支中校验、提交评审并合并。
- 数据工程师：将可用数据源映射为对象类型和链接，查看同步/索引状态、数据预览、来源与下游依赖。
- Agent 作者：配置模型、提示词、输入、预计算变量、工具与完成条件；在无副作用预览中调试，保存和发布版本。
- 运行管理员：跨 Agent 筛选会话，查看输入、事件、上下文、工具调用、执行结果、状态变化和追踪，按独立权限检查会话访问。
- 安全管理员：分别管理资源级角色、对象可见性和属性级可见性，并能解释一次读取或 Action 为什么被允许/拒绝。

## 公开产品行为基线

- Ontology Manager 有持久顶栏与导航，可搜索资源、创建资源、切换或创建分支；资源页覆盖对象类型、属性、链接、Action 与 Function。
- 对象类型视图聚合元数据、属性、Action、关系图、依赖、数据和使用情况；资源有独立的配置和观察视图。
- Ontology 编辑先进入工作中状态；保存前逐资源审阅，呈现阻止项与警告，允许丢弃单项或全部修改。并发更新要提示更新或冲突解决。
- 分支隔离本体修改；提案运行合并检查，经过逐资源评审后才合并至主分支。
- 资源权限与对象/链接数据访问分层；对象策略与属性策略可控制行和列级可见性。Agent 资源权限与会话权限也分开判断。
- Agent Builder 配置系统提示、初始消息、输入、预计算变量、工具、完成条件和输出；支持预览与调试，保存后发布版本。
- Agent Manager 浏览已发布 Agent、创建指定版本会话、发送事件或取消运行，并检查会话上下文、事件详情、状态历史、追踪和日志。
- Agent 工具能读取 Ontology 或调用预定义 Action；配置中的允许工具必须和当前用户对资源/数据/Action 的权限共同生效。

官方基线链接：

- [Ontology Manager 概览](https://www.palantir.com/docs/foundry/ontology-manager/overview)
- [保存 Ontology 修改](https://www.palantir.com/docs/foundry/ontology-manager/save-changes)
- [Ontology 分支](https://www.palantir.com/docs/foundry/ontologies/branching-ontology)
- [Ontology 权限](https://www.palantir.com/docs/foundry/object-permissioning/ontology-permissions)
- [管理对象安全](https://www.palantir.com/docs/foundry/object-permissioning/managing-object-security)
- [Agent Builder 入门](https://www.palantir.com/docs/foundry/agent-builder/getting-started)
- [Agent Builder 核心概念](https://www.palantir.com/docs/foundry/agent-builder/core-concepts)
- [Agent Manager 概览](https://www.palantir.com/docs/foundry/agent-manager/overview)
- [Action 提交条件](https://www.palantir.com/docs/foundry/action-types/submission-criteria)

## 产品信息架构

### 全局工作区

- 固定的资源搜索、资源创建、Ontology 选择器、分支选择器、版本/保存状态、用户和服务状态。
- 左侧分组导航：Discover、Object types、Link types、Action types、Functions、Data sources、Branches & proposals、Agents、Sessions、Audit。
- 资源目录支持名称/API 名称搜索、资源类型筛选、最近使用、收藏和项目/文件夹归属。空态提供实际创建入口。
- 主工作区采用高密度三栏资源管理布局：资源目录、选中资源信息/页面导航、详情面板。表格、属性面板和差异审查为主要界面，不用指标卡片替代核心数据。

### 流程图式本体画布

本体画布是结构探索与编辑入口，使用 Vue Flow 的可组合图形编辑能力；节点和边必须来自当前项目、来源系统、本体分支中的真实资源，不使用静态示例关系。

```text
┌ 项目 / 来源系统 / 本体 / 分支 / revision / 保存状态 ─────────────────────────┐
├ 资源目录 ─────────┬ 关系画布：对象类型节点 + 有向链接 + 来源映射 ─┬ 资源检查器 ┤
│ 搜索、类型筛选    │ 属性、派生属性、Action 可见性图层               │ 字段/路径  │
│ 对象/链接/动作    │ 拖动、缩放、平移、框选、小地图、保存布局           │ 校验/审计  │
├───────────────────┴───────────────────────────────────────────────┴───────────┤
│ 推理试算：起点对象 → 最多 3 跳链接 → 目标属性 → 取值/聚合 + 逐跳对象轨迹       │
└───────────────────────────────────────────────────────────────────────────────┘
```

- 项目、来源系统、本体和分支选择器固定在画布上方。切换项目时后端重新授权并只返回该项目资源。
- Object type 是主节点；Link type 是带方向和基数的边。来源系统以独立节点表示，通过数据映射连接到对象类型；Action 可按图层显示为关联节点。画布的开关只改变视图，不改变资源定义。
- 属性与派生属性列在对象节点内；派生属性使用独立标记。选择派生属性时，画布按定义高亮链接路径，检查器展示源属性、基数、聚合方式和版本状态。
- 节点位置按 `project + ontology + branch` 保存在浏览器 `localStorage`，不作为业务 schema 合并；手工拖动后自动保存，刷新时恢复。
- 画布支持按资源名/API 名称搜索并定位、缩放/平移/小地图、聚焦资源、图层筛选、键盘可达的检查器。窄屏收起目录/检查器抽屉，画布支持缩放与横向浏览。
- 画布采用石墨 `#25312F`、松针 `#2E6658`、雾白 `#F3F6F4`、雾蓝 `#496F91`、琥珀 `#B8793B`、石英紫 `#7668A6`；对象节点以松针识别，来源系统以雾蓝、Action 以琥珀、派生属性以石英紫标记，颜色同时配合图标/文本，避免仅靠颜色传达类型。

### 多项目与多来源系统

- Project 是访问隔离边界；用户通过 ProjectMembership 获得 `admin/editor/viewer` 项目角色。Ontology、来源系统、分支、提案、对象、Action、Agent、会话和审计记录都归属项目。
- 每个项目可有多个本体和多个来源系统；来源系统至少区分连接器类型、连接状态、映射、最近同步状态和同步记录。本地首版连接器为 CSV/JSON，外部连接器显示真实未配置/未连接状态。
- API 使用明确的活动项目上下文。列表只返回活动项目数据；任何通过 ID 读取、变更或关联的资源都要校验项目归属。跨项目本体、对象、链接、数据映射和 Agent 调用返回拒绝，且不泄露目标资源内容。
- 演示管理员可以切换/新建项目；普通成员只能访问有成员资格的项目。项目成员角色约束本体结构写入、评审合并、来源系统管理、Agent 配置与对象 Action。

### 派生属性推理与发布

- 支持 Ontology 定义级派生属性：从本体类型出发，经过 1–3 个有向链接，读取末端对象的原生属性；链接基数为多的一侧时，必须选择聚合。首版实现 `count`、`sum`、`average`、`minimum`、`maximum`、`collect_list`、`collect_set`；表达式型派生属性、引用其他派生属性、筛选 DSL 和预计算索引留待后续。
- 定义包含 API/显示名称、结果类型、起始对象类型、链接 API 名及遍历方向、目标属性、聚合器、空值处理和描述。服务端校验路径连续性、最多三跳、终点属性类型、聚合类型兼容、基数/聚合要求、唯一 API 名称和只读特征。
- 推理引擎只执行服务端允许的声明式操作，不接受用户 SQL、Python 或可执行表达式。试算为只读 API；返回结果、匹配对象数、每一跳的对象/链接 ID、末端属性来源、被忽略的空值和聚合解释。
- 试算对象、每个中间对象和末端属性均按当前操作者的项目与敏感字段权限过滤；无法读到任何中间对象时不泄露其 ID、数量或属性值。
- 派生属性定义保存在本体分支快照中，通过现有分支校验、逐资源评审和合并流程发布。提案变更以 `derived_property:<object_type_api_name>:<api_name>` 作为资源键；合并后成为主本体定义，派生值仍按查询时数据实时计算、不写入对象记录。
- 行为依据：[派生属性概览](https://www.palantir.com/docs/foundry/ontology/derived-properties)、[配置说明](https://www.palantir.com/docs/foundry/object-link-types/derived-properties)、[聚合与类型参考](https://www.palantir.com/docs/foundry/ontology/derived-properties-reference)。公开文档说明本体级定义最多遍历三层；可达多个对象的路径必须聚合；本地首版只实现经过明确标注的子集。

### Ontology 资源

- Object type：Overview、Properties、Actions、Links、Functions、Data、Dependents、Usage、Security、History 页面。
- Property：API 名称、显示名称、描述、类型、主键/必填/唯一/编辑能力、敏感分级、来源映射、访问策略与依赖。
- Link type：起点与终点类型、方向与基数、主键映射、来源、数据样本和反向引用。
- Action type：参数 schema、写入目标、提交条件、效果预览、权限要求、执行观察指标与运行记录。
- Function type：版本、配置来源、消费方/使用历史、调用指标；代码仓库外部依赖显示为明确状态，不做虚假编辑。
- 数据面板：关联数据源、映射字段、最近同步/索引构建时间、行数/错误数、抽样对象、字段级血缘和下游使用。

### 变更与发布

- `main` 只接受经本地校验与权限检查的合并结果。分支在创建时记录基线 revision 和 Schema Snapshot，分支写入不修改 main。
- 编辑操作作为分支上的资源变更记录；保存审查显示新增、修改和删除摘要、错误、警告及依赖影响。
- 提案包括标题、说明、修改资源、检查结果、评审状态和评审意见。审批人可逐资源批准或拒绝；合并前再次比较 base revision，检测 stale branch 并阻止覆盖。
- 支持从当前分支刷新 main 基线；冲突按资源路径显示 main 与 branch 两侧值，由操作者选择后再校验。

### Agent Builder 与 Manager

- Builder 编辑器：版本状态、模型提供方和模型名、System prompt、Initial user message、输入声明、预计算变量有向步骤、工具与 Action allowlist、会话完成模式、结构化输出 schema。
- Preview 为独立 dry-run；Action 产生候选变更但不提交对象数据。Debug 显示预计算步骤、提示词变量展开、模型消息、工具请求/结果与错误。
- 保存形成不可变版本快照，发布令 Agent Manager 只能启动该版本。正在运行的会话固定其 agent version。
- Manager 以表格管理会话：Agent、版本、来源、发起用户、状态、开始/更新时间。详情分栏展示事件时间线、事件 payload、上下文与状态快照、工具 trace 和日志；取消、继续对话均检查权限。
- 大模型适配使用可替换 Provider 接口。无 Provider 凭据时，可用显式标记的本地脚本预览核心 UI/工具流，不把它描述为生成式 Agent。

#### Agent 控制台界面方向

Agent Builder 与 Agent Manager 采用桌面优先的操作台布局，优先让作者快速看到配置、发布版本与运行证据：

```text
┌ Agent/版本目录 ─┬ 配置编辑器或会话表格 ───────────┬ Preview / Debug / 运行详情 ┐
│ 搜索、状态筛选  │ 提示词、输入、变量、工具、输出  │ 输入、解析结果、事件、Trace │
└────────────────┴───────────────────────────────┴───────────────────────────┘
```

界面颜色使用石墨 `#25312F`、松针 `#2E6658`、雾白 `#F3F6F4`、薄荷 `#DCEAE4`、琥珀 `#B8793B` 和灰绿 `#66746F`；正文使用清晰的系统无衬线字，API 名、版本号和时间使用等宽字。表格、紧凑分隔线和运行时间线承载信息；仅对发布、失败和警告使用状态色，不堆叠等尺寸指标卡片。操作文案保持中文句式，避免只作装饰的全大写眉题。

在窄屏上将目录收为可切换抽屉，配置与 Preview 按顺序纵向排列；所有编辑器保持可键盘操作，并尊重系统减少动态效果偏好。

### 安全、审计与数据

- Ontology 资源授权、对象授权、属性授权、Action 执行授权、Agent 发布权限、会话查看权限分开判定。
- 对象/属性策略先采用可解释的角色与属性标签规则，记录命中策略和拒绝原因；策略配置变更审计。
- Action 与 Agent 工具只经 Ontology API 执行；写入按一次事务校验与持久化，并写入操作者、目标资源、前后值摘要和关联 session id。
- 机密只使用部署环境变量或本地密钥存储，不返回前端，不写进事件或审计正文。
- 数据源采用连接器接口；第一阶段提供本地 CSV/JSON 导入与映射、运行状态、数据预览和索引模拟。真实外部数据库/Foundry 兼容、流式接入和云凭据需要单独连接器实现，不伪称覆盖。

## 技术架构

- Vue 3 + TypeScript + Vue Router + Pinia + `@xyflow/vue`：资源路由、图画布、细粒度编辑状态、列表筛选和 Agent 调试器。画布使用官方提供的自定义节点、交互视口、背景、控制器和 MiniMap。
- FastAPI Ontology API：资源定义、对象查询、动作、分支/变更/评审、数据映射、权限解释、审计；PostgreSQL 为权威数据源。
- FastAPI Agent Service：Agent 草稿和不可变版本、发布、会话编排、工具授权、事件与 trace；通过 HTTP 调用 Ontology API，不直接写本体对象。
- PostgreSQL：项目/成员、关系结构、JSONB 分支快照与派生定义、Agent 配置/版本、会话历史、审计和同步状态。画布布局保存在浏览器本地；schema 变更必须通过 Alembic 生成 revision。
- Redis：仅用于可重建的运行队列、短期运行状态、限流与缓存；不作为 Agent 事件或 Ontology 版本的唯一存储。
- Docker Compose：本地启动 web、ontology-api、agent-service、postgres、redis；健康检查和迁移顺序显式化。
- 维持两个业务微服务，不按页面拆空服务；数据源连接器用服务内接口及独立 worker 边界，后续有负载时可拆出。

## 成功标准

1. 操作者能在完整资源目录发现并创建 Object type、Property、Link type 与 Action type，并从 Overview 深入配置、数据、安全、使用和历史。
2. 分支修改能独立读取、校验、审阅、批准、检测过期基线并安全合并；错误和警告可定位到资源与字段。
3. Object type 能绑定本地数据源、映射属性、导入样本，查看同步/索引状态和下游关系。
4. Action 参数/提交条件有后端强校验，权限拒绝可解释、执行有事务及审计。
5. Agent 配置可保存、创建不可变版本并发布；发布版本可启动 session，正确记录 inputs、events、tool traces、context 和 errors；Preview 不落库变更。
6. 项目成员只能访问有资格的项目；每个项目可有多个本体和来源系统，资源 ID 不能绕过项目授权。
7. 画布节点/有向边对应真实本体资源；搜索、聚焦、拖动、缩放、平移、图层、小地图、检查器和布局保存都可用。
8. 1–3 跳派生属性在分支中可定义、校验、只读试算、展示逐跳计算轨迹，并经过逐资源评审合并后发布；多对象路径要求兼容聚合。
9. 后端、前端、Compose 验证均通过；界面无静态假成功按钮、错误控制台异常或小屏不可用的核心导航；更新中文 README 和功能差异矩阵。

## 关键风险与取舍

- Palantir 文档描述的很多功能依赖 Foundry 专有资源、权限体系、管道、函数代码仓库和 SDK。项目提供可用的对应工作流，不模拟无法验证的后端实现或连接器。
- 业务 schema snapshot 和关系操作可能跨多个资源。合并采用 PostgreSQL 事务与乐观 revision 检查；冲突以资源为粒度，禁止静默 last-write-wins。
- Agent 执行任何 Action 都是业务写入。Preview 永远只生成候选结果；正式会话使用已发布版本、授权工具和当前操作者权限。
- 运行时派生属性读取了多个对象时，权限必须逐跳套用；试算证据只包含操作者可以读取的数据，防止推理结果泄露被拒绝访问对象。
- 画布布局属于视图偏好，派生属性定义属于 schema 资源；两者必须分别存储，避免调整节点位置触发业务评审。
- 现有演示数据带有随机 smoke 类型；必须清理重复/临时演示数据并补充一致、可信、可浏览的业务模型。
