# 本体管理系统实施计划

> **执行要求：** 按阶段小步交付；业务行为先写失败测试。每阶段完成后更新状态。本计划所有阶段完成后删除。

**目标：** 实现可通过 Docker Compose 本地启动的本体管理与 Agent 工具工作台。

**架构：** Vue 3 控制台访问独立的 FastAPI 本体 API 与 Agent 运行服务。PostgreSQL 保存权威业务状态，Redis 保存 Agent 短期会话/事件；服务间通过受限 HTTP API 通信。

**技术栈：** Vue 3、TypeScript、Vite、Pinia、Python 3.12、FastAPI、SQLAlchemy 2、Pydantic、Alembic、PostgreSQL、Redis、Docker Compose。

**设计文档：** `docs/superpowers/specs/2026-11-14-ontology-management-system-design.md`

## 全局约束

- 中文产品界面、文档、日志和提交信息；代码标识符使用英文。
- `.env.example` 可提交；实际 `.env`、密码、JWT 密钥不得提交。
- PostgreSQL 为生产开发数据库；所有 schema 变更由 `alembic revision` 生成迁移。
- 管理 API 是本体结构和对象写入的唯一权威入口；Agent 服务只能调用授权 API。
- Agent 工具按 Agent 授权和当前操作者角色双重校验；服务端拒绝未授权操作。
- API 和 Agent 服务对外分别提供健康检查；Compose 使用持久化卷和健康依赖。
- 仅实现可本地演示的确定性 Agent 工具调用，不要求外部模型密钥。

## 审查重点

- 非管理员批准结构提案：必须拒绝，覆盖于阶段 2 的 `test_editor_cannot_merge_schema_proposal`。
- 过期版本的提案：不得覆盖较新结构，覆盖于阶段 2 的 `test_stale_schema_proposal_is_rejected`。
- Action 尝试修改未授权属性：整笔事务拒绝且对象不变，覆盖于阶段 2 的 `test_action_rejects_properties_outside_allowlist`。
- Agent 调用未授权工具或越权 Action：拒绝并记录审计，覆盖于阶段 3 的 `test_agent_cannot_call_ungranted_tool` 与 `test_agent_action_respects_actor_role`。
- Redis 暂时不可用或首次数据库初始化：服务提供可诊断健康状态，Compose 重启后持久业务数据仍在，覆盖于阶段 5 的启动与重启冒烟检查。

---

## 阶段 1：后端骨架、身份与本体数据模型

**目标**：搭好 API、数据库、登录/角色和核心 SQLAlchemy 模型，建立可迁移、可测试的本地运行骨架。
**成功标准**：健康检查、登录和角色依赖可用；本体、对象类型、属性、链接、对象、Action、提案及审计模型可在测试数据库建表；Alembic 迁移由命令生成。
**测试**：`python -m unittest discover -s tests -p "test_*.py" -v`；已验证登录、viewer/editor/admin 角色依赖、领域约束与 PostgreSQL 迁移。
**状态**：已完成

### Task 1：服务脚手架与认证

**文件**：新增 `backend/ontology_service/app/{main.py,config.py,database.py,security.py}`、`backend/ontology_service/app/routers/auth.py`、`backend/requirements.txt`、`tests/test_auth.py`。

- [x] 写测试：登录成功签发 JWT、错误凭据返回 401、JWT 过期被拒绝、viewer 不能调用管理员依赖。
- [x] 运行测试，确认因 app/登录接口缺失失败。
- [x] 实现环境配置、SQLAlchemy session 依赖、密码哈希、JWT 和角色依赖。
- [x] 运行测试确认通过；`python -m compileall backend/ontology_service`。

### Task 2：领域模型与 Alembic

**文件**：新增 `backend/ontology_service/app/models/` 下的 `ontology.py`、`objects.py`、`governance.py`、`audit.py`，`backend/ontology_service/alembic.ini`、`backend/ontology_service/alembic/env.py`、`tests/test_models.py`。

- [x] 写测试：属性 API 名唯一、对象记录关联类型、审计事件保存操作者与时间、提案状态约束、Action API 名唯一和对象版本类型。
- [x] 运行测试确认缺少领域模型导出及两项约束测试失败。
- [x] 实现模型、PostgreSQL JSONB（测试使用兼容 JSON 类型）和 Alembic 元数据加载。
- [x] 用 `alembic revision --autogenerate -m "初始化本体管理模型"` 生成迁移，不手写 revision 文件。
- [x] 在 PostgreSQL 上执行升级；41 项完整测试、迁移差异检查与 Python 编译均通过。

## 阶段 2：本体管理、对象操作、Action 与提案治理

**目标**：交付可审阅的本体结构变更、对象查询和受校验 Action 写入。
**成功标准**：提案审批以版本检查保护 schema；对象/链接 API 可用；Action 按属性白名单、类型和角色校验并原子写审计。
**测试**：`backend/tests/test_governance.py`、`test_objects_actions.py`、`test_audit.py`；阶段 1 全套回归。
**状态**：进行中

### Task 3：本体元数据和提案审阅

**文件**：新增 `backend/ontology_service/app/routers/ontology.py`、`proposals.py`、`backend/ontology_service/app/services/governance.py`、`backend/ontology_service/app/schemas/ontology.py`、`backend/tests/test_governance.py`。

- [ ] 写测试：editor 可提交新增类型/属性/链接提案；admin 可批准或拒绝；viewer/editor 不可合并；旧 revision 提案冲突返回 409；成功合并只递增一个版本并产生审计。
- [ ] 运行测试确认失败。
- [ ] 实现元数据读取、提案状态流转、事务化应用与版本冲突检查。
- [ ] 运行治理测试确认通过。

### Task 4：对象、链接和 Action

**文件**：新增 `backend/ontology_service/app/routers/objects.py`、`actions.py`、`backend/ontology_service/app/services/action_engine.py`、`backend/ontology_service/app/schemas/objects.py`、`backend/tests/test_objects_actions.py`。

- [ ] 写测试：对象类型校验、按类型/关键词分页查询、对象详情/链接、Action 成功更新、错误字段/无权限时拒绝且不部分写入。
- [ ] 运行测试确认失败。
- [ ] 实现对象检索、详情、链接查询和事务化 Action 执行；记录变更前后值。
- [ ] 运行测试确认通过。

## 阶段 3：Agent 注册、授权工具、会话与事件

**目标**：实现独立 Agent 服务，可在显式权限范围内发现本体对象、读取对象、执行 Action 并检查调用轨迹。
**成功标准**：工具授权与操作者角色都在服务端校验；会话短期状态/事件进入 Redis，执行结果和审计进入 PostgreSQL；Redis 错误有明确响应。
**测试**：`agent_service/tests/test_agent_tools.py`、`test_sessions.py`；工具调用联测本体 API 测试服务。
**状态**：未开始

### Task 5：Agent API 和会话存储

**文件**：新增 `backend/agent_service/app/{main.py,config.py,redis_store.py,api_client.py}`、`routers/agents.py`、`sessions.py`、`tools.py`、`backend/agent_service/pyproject.toml`、`backend/agent_service/tests/test_agent_tools.py`、`test_sessions.py`。

- [ ] 写测试：无效 JWT 被拒绝；Agent 仅能运行显式授权工具；越权 Action 返回拒绝并留审计；会话创建、事件写入/读取和结束状态可观测。
- [ ] 运行测试确认失败。
- [ ] 实现 Agent/工具配置、Redis 活跃会话与事件、受控本体 API 客户端和健康路由。
- [ ] 运行 Agent 服务测试与本体 API 回归。

## 阶段 4：Vue 管理控制台

**目标**：实现中文 Web 控制台，覆盖本体建模、数据、提案、Agent 和审计的端到端工作流。
**成功标准**：登录后能浏览/筛选对象类型和对象、创建并审批提案、执行 Action、创建 Agent 会话并调用工具、查看事件/审计；错误/空/加载状态清楚。
**测试**：`npm run build`；组件测试覆盖路由守卫、提案审批权限和 Agent 未授权工具不可点用；API 联调冒烟。
**状态**：未开始

### Task 6：Vue 项目与控制台页面

**文件**：新增 `frontend/package.json`、`vite.config.ts`、`src/{main.ts,router.ts,stores/auth.ts,api/client.ts}`，布局/组件和 `views/` 下 `Overview.vue`、`Ontology.vue`、`Objects.vue`、`Proposals.vue`、`Agents.vue`、`Audit.vue`。

- [ ] 先写关键组件测试：匿名访问跳登录、viewer 无审批按钮、未授权工具不可触发、错误 API 显示中文提示。
- [ ] 运行测试确认失败。
- [ ] 实现登录态、侧栏导航、六个工作视图和服务 API 接入；提供演示数据友好的默认概览。
- [ ] 运行组件测试和 `npm run build`。

## 阶段 5：Compose 集成、演示数据、说明和交付

**目标**：一条命令启动全部服务并能完成演示工作流；完成配置与中文文档，提交并推送。
**成功标准**：`docker compose up --build` 后各健康检查通过；数据库迁移/种子可重复；前端可访问；Compose 重启保留本体和审计数据；测试/构建通过；提交推送至 `danerlt` 目标仓库。
**测试**：后端单测、前端组件测试与构建、`docker compose config`、Compose 冒烟（登录、提案审批、对象 Action、Agent 工具调用、审计、重启后数据保留）。
**状态**：未开始

### Task 7：容器化与可重复初始化

**文件**：新增 `Dockerfile`（前端、本体服务、Agent 服务）、`docker-compose.yml`、`.env.example`、`backend/ontology_service/app/seed.py`、中文 `README.md`。

- [ ] 写启动契约检查：Compose 服务清单/健康检查/依赖顺序/环境变量缺项和实际密钥不得被版本控制。
- [ ] 运行 `docker compose config` 确认初始化约束测试先失败。
- [ ] 实现服务镜像、持久卷、Redis、启动迁移与幂等演示数据；文档说明本地账号、地址、模块和 API。
- [ ] 启动完整 Compose，修复启动/迁移问题，执行端到端冒烟和重启数据持久性检查。
- [ ] 运行全部测试、前端构建、格式/编译检查；审查 `git diff` 与密钥扫描。
- [ ] 配置 SSH remote `git@github.com:danerlt/ontology-research.git`，本地分支命名 `main`，提交中文信息并推送。

## 交付顺序与检查点

1. 阶段 1 完成后得到可登录、数据库可迁移的服务骨架。
2. 阶段 2 完成后得到有权限与审计保护的本体管理闭环。
3. 阶段 3 完成后得到 Agent 会话和授权工具服务。
4. 阶段 4 完成后得到可操作的浏览器端应用。
5. 阶段 5 完成后得到一条命令启动、可重启保留数据、可推送的完整交付。
