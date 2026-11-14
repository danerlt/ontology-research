# 本体管理系统实施计划

> 本计划由当前会话原生执行，逐任务按测试驱动完成；任务以方框跟踪。

**目标：** 交付一套通过 Docker Compose 本地启动的 Ontology 管理与 Agent 工具工作台。

**架构：** Vue 3 单页控制台访问独立的 FastAPI 本体 API 与 Agent 运行服务。PostgreSQL 保存权威数据，Redis 保存 Agent 活跃会话和事件；Agent 服务通过受限 HTTP API 操作本体。

**技术栈：** Vue 3、TypeScript、Vite、Pinia、FastAPI、SQLAlchemy 2、Pydantic、Alembic、PostgreSQL、Redis、Docker Compose。

**Spec：** `docs/superpowers/specs/2026-11-14-ontology-management-system-design.md`

## 全局约束

- 中文界面、文档、日志、提交信息；代码标识符保持英文。
- 密码、JWT 私钥和实际 `.env` 不进入版本控制；`.env.example` 只含本地演示默认值。
- PostgreSQL 是关系/对象主存储；schema 变更必须由 `alembic revision` 生成 revision。
- 本体 API 是业务写入的权威入口；Agent 不直连 PostgreSQL。
- Agent 工具需要同时满足 Agent 工具授权与操作者权限，服务端最终拒绝越权操作。
- 首版不调用外部模型，不引入尚无用例的向量库、图数据库和对象存储。
- 所有 Compose 服务需健康检查；初始化迁移与演示数据可重复执行。

## 审查重点

- 非管理员批准本体提案：预期拒绝，阶段 2 `test_editor_cannot_merge_schema_proposal`。
- 提案所基于版本已过期：预期冲突且 schema 不变，阶段 2 `test_stale_schema_proposal_is_rejected`。
- Action 写入不在白名单内的属性：预期整笔回滚，阶段 2 `test_action_rejects_properties_outside_allowlist`。
- Agent 调用未获授权工具/越权 Action：预期拒绝并留痕，阶段 3 `test_agent_cannot_call_ungranted_tool`、`test_agent_action_respects_actor_role`。
- PostgreSQL 或 Redis 未就绪：Compose 服务保持不可用并报告原因，阶段 5 `test_compose_health_checks_cover_stateful_dependencies` 与启动冒烟。

---

## 文件边界

- `backend/ontology_service/app/`：本体 API 配置、数据库、身份、领域模型、schema、业务服务和路由。
- `backend/ontology_service/alembic/`：Alembic 环境与命令生成的 revision。
- `backend/agent_service/app/`：Agent 注册、工具授权、会话/事件与本体 API 客户端。
- `tests/`：继承现有 unittest 风格，覆盖目录工具和系统服务的业务契约。
- `frontend/src/`：Vue 路由、状态、API 客户端、共用布局和产品页面。
- 根目录 `docker-compose.yml`、服务 Dockerfile、`.env.example` 和中文 `README.md`：本地可重复部署。

## 阶段 1：本体 API 骨架、身份与数据模型

### Task 1：FastAPI 骨架和登录/角色

**文件：** 新增 `backend/ontology_service/app/{main.py,config.py,database.py,security.py}`、`routers/auth.py`、`backend/requirements.txt`、`tests/test_auth.py`。

**接口：** `get_current_user()` 解析 Bearer JWT 并返回 actor/role；`require_role(*roles)` 生成路由依赖；`Settings` 从环境变量加载数据库/JWT/管理员种子配置。

- [x] 写 `test_login_returns_bearer_token`、`test_invalid_credentials_are_rejected`、`test_expired_token_is_rejected`、`test_viewer_is_rejected_by_admin_dependency`。
- [x] 运行 `python -m unittest discover -s tests -p "test_auth.py" -v`，先因应用模块缺失而失败；后续调试修正 EmailStr 测试域和异步清理钩子。
- [x] 实现哈希口令、签发/校验 JWT、角色依赖和 `/health/live`、`/health/ready`。
- [x] 运行本任务测试和 `python -m compileall backend/ontology_service`。

### Task 2：领域模型和数据库迁移

**文件：** 新增 `backend/ontology_service/app/models/{ontology.py,objects.py,governance.py,audit.py}`、`alembic.ini`、`alembic/env.py`、`tests/test_models.py`。

**接口：** 模型包含 Ontology revision、ObjectType/PropertyDefinition/LinkType、ObjectRecord/ObjectLink、ActionDefinition、ChangeProposal 和 AuditEvent；JSON 字段测试可用 SQLite，部署目标是 PostgreSQL JSONB。

- [x] 写 `test_property_api_names_are_unique_per_type`、`test_object_record_references_type`、`test_audit_event_has_actor_and_timestamp`，并补上 Action 唯一性和对象版本整数测试。
- [x] 运行测试确认模型导出缺失；随后两项新约束测试按预期失败。
- [x] 实现 SQLAlchemy 模型、session scope 和 Alembic `target_metadata`。
- [x] 启动 PostgreSQL，再运行 `alembic revision --autogenerate -m "初始化本体管理模型"`；执行 `alembic upgrade head`，禁止手写 revision 骨架。
- [x] 运行模型测试、迁移状态检查与 Python 编译；PostgreSQL 验证 JSONB 与整数列类型。

## 阶段 2：本体建模、提案治理、对象和 Action

### Task 3：Ontology 元数据与变更提案

**文件：** 新增 `routers/ontology.py`、`routers/proposals.py`、`services/governance.py`、`schemas/ontology.py`、`tests/test_governance.py`。

**接口：** `GET /api/ontology`；`GET /api/object-types`；`POST /api/proposals`；`POST /api/proposals/{id}/submit`；`POST /api/proposals/{id}/merge`；`POST /api/proposals/{id}/reject`。提案保存 base_revision 与 JSON 变更集合。

- [x] 写 `test_editor_can_submit_object_type_proposal`、`test_editor_cannot_merge_schema_proposal`、`test_stale_schema_proposal_is_rejected`、`test_merge_increments_revision_and_writes_audit`，并覆盖属性/链接、驳回和回滚。
- [x] 运行治理测试确认提案路由缺失而失败。
- [x] 实现对象类型/属性/链接定义提案、权限校验、版本乐观锁和事务化合并。
- [x] 运行 8 项治理测试确认通过。

### Task 4：对象检索、关系与 Action

**文件：** 新增 `routers/objects.py`、`routers/actions.py`、`services/action_engine.py`、`schemas/objects.py`、`tests/test_objects_actions.py`、`tests/test_audit.py`。

**接口：** `GET /api/objects` 支持 type/query/page/page_size；`GET /api/objects/{id}` 返回属性和出入链接；`POST /api/actions/{api_name}/execute` 校验参数并事务写回。

- [x] 写对象类型/属性校验、主键唯一性、检索分页、关系方向、Action 白名单、版本冲突、原子回滚、审计与敏感属性测试。
- [x] 运行对象/Action 测试确认接口缺失而失败；随后逐项实现并通过。
- [x] 实现对象过滤/搜索/分页 API、关系详情、原子 Action、权限角色与敏感值脱敏。
- [x] 运行对象/Action/审计测试、全量 Python 回归、编译检查；PostgreSQL Alembic 迁移升级并确认无差异。

## 阶段 3：Agent 服务、工具授权与会话事件

### Task 5：Agent 注册、会话和工具执行

**文件：** 新增 `backend/agent_service/app/{main.py,config.py,redis_store.py,api_client.py}`、`routers/{agents.py,sessions.py,tools.py}`、`tests/test_agent_tools.py`、`tests/test_sessions.py`。

**接口：** `GET/POST /api/agents`；`POST /api/agents/{id}/sessions`；`POST /api/sessions/{id}/tools/{tool_name}`；`GET /api/sessions/{id}/events`；`POST /api/sessions/{id}/close`。工具为 `search_objects`、`get_object`、`execute_action`。

- [x] 写 `test_agent_cannot_call_ungranted_tool`、`test_agent_action_respects_actor_role`、`test_agent_tool_calls_ontology_api`、`test_session_events_are_ordered`、`test_redis_failure_is_reported`。
- [x] 运行 Agent 测试确认模型与路由缺失而失败。
- [x] 实现 Agent 权限检查、HTTP 本体 API 客户端、Redis 短期状态/事件及 PostgreSQL 会话/执行轨迹。
- [x] 运行 Agent 测试与本体 API 回归。

## 阶段 4：Vue 管理工作台

### Task 6：登录、Ontology、对象、治理、Agent 和审计视图

**文件：** 新增 `frontend/package.json`、`vite.config.ts`、`src/{main.ts,router.ts,api/client.ts,stores/auth.ts}`、布局组件和 `src/views/{Overview.vue,Ontology.vue,Objects.vue,Proposals.vue,Agents.vue,Audit.vue}`；测试放 `frontend/src/**/*.spec.ts`。

**接口：** API 客户端统一注入 Bearer token，将 401 带回登录页；Pinia 保存本地登录态；页面调用阶段 1-3 API。

- [x] 写登录路由守卫、viewer 不可见审批操作、未授权工具禁用、API 错误中文反馈组件测试。
- [x] 运行组件测试确认失败。
- [x] 实现中文控制台、对象类型/对象浏览、提案提交/审阅、Action 执行、Agent 工具会话/事件和审计视图。
- [x] 运行组件测试（7 项）和 `npm run build`。

## 阶段 5：Docker Compose、数据初始化、全量验证和推送

### Task 7：容器启动与端到端交付

**文件：** 新增 `.env.example`、`.gitignore` 条目、`docker-compose.yml`、前端/本体/Agent Dockerfile、幂等 `backend/ontology_service/app/seed.py`、中文 `README.md`。

**接口：** Compose 服务 `web`、`ontology-api`、`agent-service`、`postgres`、`redis`；本地入口 `http://localhost:5173`；本地管理员账号由 `.env.example` 提供，JWT/数据库可在 `.env` 覆盖。

- [x] 写 Compose 静态配置测试：五个服务、健康检查、Postgres 卷、必填服务环境变量；`.env` 被忽略。
- [x] 运行检查确认 Compose 配置，并为默认管理员邮箱补充回归测试。
- [x] 实现服务镜像、Compose 编排、启动迁移、幂等演示数据和中文 README。
- [x] 运行 `docker compose config`、全量 81 项 unittest、7 项前端测试/构建、Python 编译检查。
- [x] 启动完整栈并冒烟登录、提案审阅、对象 Action、Agent 工具调用、审计；重启后确认数据保留。
- [x] 自查差异与敏感文件，提交中文 commit；设置 SSH `origin`、将分支改名 `main` 并推送。

---

## 阶段状态

| 阶段 | 状态 | 结果 |
| --- | --- | --- |
| 阶段 1：本体 API 骨架、身份与数据模型 | 已完成 | 登录/角色与 PostgreSQL 迁移 |
| 阶段 2：本体建模、提案治理、对象和 Action | 已完成 | 结构提案、对象链接、Action、敏感字段与审计闭环 |
| 阶段 3：Agent 服务、工具授权与会话事件 | 已完成 | Agent 双重授权、HTTP 工具调用、Redis 事件与 PostgreSQL 轨迹 |
| 阶段 4：Vue 管理工作台 | 已完成 | 7 项组件测试与生产构建通过 |
| 阶段 5：Docker Compose、演示数据和交付 | 已完成 | 五个服务健康；端到端流程、重启持久性和 GitHub main 推送通过 |

> 说明：本体工作台代码交付与逐篇研究卡片是不同的完成条件。676 张直接相关卡片中，20 张已完成，656 张仍待研读。当前系统是基于核心文档启发的本地原型，不代表完成全量文档研读或完整复刻 Palantir 功能。
