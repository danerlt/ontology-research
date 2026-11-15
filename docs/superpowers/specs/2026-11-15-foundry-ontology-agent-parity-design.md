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

### 安全、审计与数据

- Ontology 资源授权、对象授权、属性授权、Action 执行授权、Agent 发布权限、会话查看权限分开判定。
- 对象/属性策略先采用可解释的角色与属性标签规则，记录命中策略和拒绝原因；策略配置变更审计。
- Action 与 Agent 工具只经 Ontology API 执行；写入按一次事务校验与持久化，并写入操作者、目标资源、前后值摘要和关联 session id。
- 机密只使用部署环境变量或本地密钥存储，不返回前端，不写进事件或审计正文。
- 数据源采用连接器接口；第一阶段提供本地 CSV/JSON 导入与映射、运行状态、数据预览和索引模拟。真实外部数据库/Foundry 兼容、流式接入和云凭据需要单独连接器实现，不伪称覆盖。

## 技术架构

- Vue 3 + TypeScript + Vue Router + Pinia：资源路由、细粒度编辑状态、列表筛选和 Agent 调试器。
- FastAPI Ontology API：资源定义、对象查询、动作、分支/变更/评审、数据映射、权限解释、审计；PostgreSQL 为权威数据源。
- FastAPI Agent Service：Agent 草稿和不可变版本、发布、会话编排、工具授权、事件与 trace；通过 HTTP 调用 Ontology API，不直接写本体对象。
- PostgreSQL：关系结构、JSONB schema snapshot、Agent 配置/版本、会话历史、审计和同步状态。schema 变更必须通过 Alembic 生成 revision。
- Redis：仅用于可重建的运行队列、短期运行状态、限流与缓存；不作为 Agent 事件或 Ontology 版本的唯一存储。
- Docker Compose：本地启动 web、ontology-api、agent-service、postgres、redis；健康检查和迁移顺序显式化。
- 维持两个业务微服务，不按页面拆空服务；数据源连接器用服务内接口及独立 worker 边界，后续有负载时可拆出。

## 成功标准

1. 操作者能在完整资源目录发现并创建 Object type、Property、Link type 与 Action type，并从 Overview 深入配置、数据、安全、使用和历史。
2. 分支修改能独立读取、校验、审阅、批准、检测过期基线并安全合并；错误和警告可定位到资源与字段。
3. Object type 能绑定本地数据源、映射属性、导入样本，查看同步/索引状态和下游关系。
4. Action 参数/提交条件有后端强校验，权限拒绝可解释、执行有事务及审计。
5. Agent 配置可保存、创建不可变版本并发布；发布版本可启动 session，正确记录 inputs、events、tool traces、context 和 errors；Preview 不落库变更。
6. 后端、前端、Compose 验证均通过；界面无静态假成功按钮、错误控制台异常或小屏不可用的核心导航；更新中文 README 和功能差异矩阵。

## 关键风险与取舍

- Palantir 文档描述的很多功能依赖 Foundry 专有资源、权限体系、管道、函数代码仓库和 SDK。项目提供可用的对应工作流，不模拟无法验证的后端实现或连接器。
- 业务 schema snapshot 和关系操作可能跨多个资源。合并采用 PostgreSQL 事务与乐观 revision 检查；冲突以资源为粒度，禁止静默 last-write-wins。
- Agent 执行任何 Action 都是业务写入。Preview 永远只生成候选结果；正式会话使用已发布版本、授权工具和当前操作者权限。
- 现有演示数据带有随机 smoke 类型；必须清理重复/临时演示数据并补充一致、可信、可浏览的业务模型。
