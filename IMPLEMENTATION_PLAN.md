# Palantir Ontology / Agent 管理系统高保真复刻实施计划

> **执行方式：** 使用 `superpowers:executing-plans` 在当前会话逐阶段实现，并按测试驱动流程执行。

**目标：** 将当前演示工作台升级为以公开 Foundry 文档行为为基准的本体建模、变更治理、数据映射和 Agent 构建/运行管理系统。

**架构：** 保持 Vue 3、Ontology FastAPI、Agent FastAPI、PostgreSQL、Redis 的业务边界；本体 API 拥有 schema/object/action 权威数据，Agent 服务仅经授权 HTTP 工具调用 Ontology API。通过 schema snapshot 和 revision 乐观锁实现隔离分支、逐资源审查与安全合并。

**技术栈：** Vue 3 + TypeScript + Pinia；Python 3.12 + FastAPI + SQLAlchemy 2 + Alembic；PostgreSQL + Redis；Docker Compose；pytest + Vitest。

**设计说明：** `docs/superpowers/specs/2026-11-15-foundry-ontology-agent-parity-design.md`

## 全局约束

- 所有对老板可见的输出、界面、文档和日志用中文；代码标识符保持英文。
- 以公开文档确认的用户流程为目标，不复制闭源实现、原始全文、商标资产或逐像素界面。
- 每个用户可见的成功状态必须对应已持久化或实际执行的行为；未实现的外部连接能力明确显示边界。
- 所有数据库 schema 变化通过 `alembic revision` 生成骨架，再填写 upgrade/downgrade。
- 保留服务端身份、资源/对象/属性/Action/Agent/session 授权分层；不把 API key 放入数据库明文或审计日志。
- 每个阶段小步提交；提交前通过该阶段测试、构建和格式检查。

## 审查关注点

- 过期分支遇到 main 已变更：测试合并明确冲突并保持 main 不变。
- Action 和 Agent 预计算工具触发数据写入：测试 Preview 无副作用、正式会话仍执行服务端授权。
- Agent 新版本发布期间存在老会话：测试老会话仍固定原版本。
- 属性包含敏感策略而用户缺少标记：测试读取和事件 payload 均脱敏。
- CSV/JSON 导入中出现未知字段、重复主键或类型错误：测试可解释失败并且无部分数据写入。

---

## 阶段 1：本体领域模型、分支和 API 基础

**目标**：为隔离的 Ontology 编辑、资源检查、数据来源和 Agent 版本提供持久模型与稳定 API。
**成功标准**：branch snapshot 独立于 main；修改、验证、创建提案、逐资源评审、过期检查与事务合并端到端可用；新增资源字段有数据库迁移、校验和审计。
**测试**：分支基线、分支变更 schema 校验、并发 revision 冲突、审批/拒绝、Action 参数/规则、安全授权、无副作用 Preview。
**状态**：进行中

### 任务 1.1：分支快照、变更与合并 API

- [x] 先为创建分支、应用资源变更、schema 校验、proposal 审批/合并写失败测试；确认失败原因是接口/行为缺失。
- [x] 覆盖 `test_branch_changes_do_not_mutate_main_schema`、`test_branch_validation_reports_duplicate_api_name`、`test_merge_rejects_stale_branch_without_partial_writes`、`test_resource_review_required_before_merge`、`test_rebase_preserves_branch_changes_and_updates_base_revision` 和 `test_rebase_reports_resource_conflict_without_changing_branch`，置于 `tests/test_branches.py`。
- [x] 用 `alembic revision -m "新增本体分支与资源级评审"` 生成迁移骨架，再实现 `OntologyBranch` 快照/变更字段和 `ProposalResourceReview` 字段。
- [x] 实现 create/list/get/validate/propose/review/rebase/merge API；合并采用 base revision 检查和数据库事务。
- [x] 新增分支用例 6/6、后端全量 87/87 通过；PostgreSQL 18.7 上完成全部迁移升级、回滚一个 revision、再升级。

### 任务 1.2：资源定义、数据源与 Action 规则

- [ ] 为 Action 参数 schema、提交条件、效果摘要、数据源连接、字段映射、同步任务状态和资源来源关系写失败测试。
- [ ] 覆盖 `test_action_parameters_must_match_declared_schema`、`test_action_preview_does_not_write_record_or_audit`、`test_submission_criteria_blocks_invalid_state`，扩展 `tests/test_objects_actions.py`。
- [ ] 通过 Alembic 自动生成字段/表迁移，添加 Pydantic request/response schema 和服务层规则校验。
- [ ] Action 执行返回受控差异预览；正式执行验证参数、目标资源、当前用户和提交条件后事务写入。
- [ ] 运行新增测试与全部后端测试。

## 阶段 2：Ontology Manager 产品工作流

**目标**：把资源导航、对象类型多页面、数据映射与变更审查做成高密度、可操作的管理控制台。
**成功标准**：用户无需进入演示路由即可完成资源搜索/创建、属性/链接/Action 编辑、分支校验提案、对象数据/来源/安全/使用浏览；所有成功提示有后端响应支撑。
**测试**：路由守卫、资源搜索与筛选、类型页标签路由、分支草稿/差异审查组件行为、加载/错误/无数据态、Vue build。
**状态**：未开始

### 任务 2.1：全局 shell 与资源目录

- [ ] 添加路由/组件测试，覆盖工作区分组导航、全局搜索、资源类型过滤、当前 ontology/branch 和未保存状态。
- [ ] 将导航与全局搜索分别固定在 `frontend/src/router.spec.ts` 和 `frontend/src/components/AppShell.spec.ts`。
- [ ] 重构 `AppShell.vue` 和 `router.ts`，建立 Discover、目录、分支、数据源、Agent、会话和审计路由。
- [ ] 将内容区重排为资源树/列表、面包屑和详情；补键盘焦点、窄屏导航和 reduced-motion。
- [ ] 运行 Vitest 与 `npm run build`。

### 任务 2.2：对象类型及资源详情页

- [ ] 为对象类型 Overview/Properties/Links/Actions/Data/Dependents/Usage/Security/History 标签与各表单校验写组件测试。
- [ ] 覆盖资源子页路由、空数据与 API 错误；新增 `frontend/src/views/ObjectTypeDetail.spec.ts`。
- [ ] 实现属性、链接和 Action 配置面板，显示参数/规则、来源映射、数据状态与可解释权限。
- [ ] 用真实 API 结果和明确的空态/错误态替换静态卡片；删除临时 smoke seed 数据。
- [ ] 运行 Vitest、构建、前后端关键 API 流程验证。

### 任务 2.3：数据源接入与对象浏览

- [ ] 为 CSV/JSON 预览、字段映射、重复主键、校验错误、导入事务、数据过滤和详情关系面板写测试。
- [ ] 覆盖重复主键无部分提交、未知属性映射拒绝、详情关系按类型授权；后端置于 `tests/test_data_sources.py`。
- [ ] 实现本地文件连接器、对象类型映射、导入任务状态/审计；不对真实外部 Foundry connector 作虚假声明。
- [ ] 补对象搜索过滤器、排序/分页、属性表格、关系跳转、血缘和同步状态。
- [ ] 运行后端和前端测试、build，并走一遍数据导入到对象浏览流程。

## 阶段 3：Agent Builder、发布版本和 Agent Manager

**目标**：建立完整可配置、可版本化、可调试且受授权的 Agent 构建和运行控制台。
**成功标准**：Agent 草稿保存为不可变发布版本；从版本创建 session，要求输入有效；事件/上下文/工具 trace/日志可检索；会话拒绝访问和 Action 执行有明确授权结果；Preview 不改 Ontology。
**测试**：配置 schema、版本固定、必填 inputs、Preview dry-run、tool allowlist + role、会话访问边界、事件顺序和状态转换。
**状态**：未开始

### 任务 3.1：Agent 配置与版本 API

- [ ] 写配置 CRUD、保存版本、发布和版本 pinning 的失败测试。
- [ ] 覆盖 `test_published_agent_version_is_immutable`、`test_new_session_pins_published_agent_version`、必填输入缺失拒绝，置于 `tests/test_agent_versions.py`。
- [ ] Alembic 生成 Agent config/version 模型迁移；只在环境配置层读取 LLM 凭据。
- [ ] 实现 inputs、prompt、初始消息、variables、tools、Action scopes、completion/output schema 校验与 publish API。
- [ ] 运行 Agent Service 测试及数据库迁移升级/回滚验证。

### 任务 3.2：Agent Builder 编辑器

- [ ] 写 Builder 各配置面板、预览启动、Debug 事件渲染、工具授权控件的 Vue 测试。
- [ ] 覆盖配置保存/发布状态和 Preview 不应用 Action 变更，置于 `frontend/src/views/AgentBuilder.spec.ts`。
- [ ] 实现模型/提示词、输入、变量链、工具/Action、输出设置、dry-run Preview 与 debug trace。
- [ ] 实现保存草稿、发布确认结果与版本回看；无模型配置时明确提示并允许使用显式标注的确定性本地预览。
- [ ] 运行 Vitest 和前端 build。

### 任务 3.3：Agent Manager 会话检查器

- [ ] 写会话筛选、按发布版本启动、事件/上下文/工具 trace 读取、继续/取消和访问控制测试。
- [ ] 覆盖访问边界、事件顺序、敏感值脱敏，扩展 `tests/test_agent_tools.py`。
- [ ] 实现密集会话表、详情时间线、payload/context/state snapshots、logs/traces 和敏感值脱敏。
- [ ] 运行全套后端/前端测试并验证 Agent Builder→Publish→Manager→tool trace 路径。

## 阶段 4：端到端治理、文档和交付

**目标**：保证跨服务事务、授权、迁移、部署与操作指南形成可复核交付。
**成功标准**：全新数据库启动时自动迁移和示例初始化；关键核心工作流通过 API/浏览器验证；README 与 parity matrix 准确披露完成项与差异；main 提交并推送。
**测试**：pytest、Vitest、前端构建、Alembic upgrade/downgrade、Compose 服务健康、主要用户流程和浏览器检查。
**状态**：未开始

### 任务 4.1：安全审计和差异矩阵

- [ ] 写资源/对象/属性/Action/Agent/会话访问策略及解释 API 测试。
- [ ] 实现拒绝理由、字段脱敏和关联追踪 ID；确保 audit/event 均不存储 credential。
- [ ] 更新 README、运行手册、官方来源映射及功能差异矩阵。
- [ ] 执行静态检查、格式化、完整测试、构建与 Compose 检查。

### 任务 4.2：体验审查、提交与推送

- [ ] 浏览器验证主要工作流、桌面和窄屏界面、空态/错误态与控制台无异常。
- [ ] 自查 diff、迁移链、Secret、临时数据、功能占位和可访问性；修复阻塞缺陷。
- [ ] 分阶段中文 commit message 提交并推送分支，然后按既有授权合并/推送 `main`。

## 阶段完成状态更新

| 阶段 | 状态 | 证据 |
|---|---|---|
| 1 本体领域模型、分支和 API 基础 | 进行中 | Task 1.1：分支/评审 API 6/6、后端 87/87；PostgreSQL 18.7 迁移升级/回滚/再升级通过。 |
| 2 Ontology Manager 产品工作流 | 未开始 | — |
| 3 Agent Builder、发布版本和 Agent Manager | 未开始 | — |
| 4 端到端治理、文档和交付 | 未开始 | — |
