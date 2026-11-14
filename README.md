# 本体工作台

一个参考 Palantir Foundry Ontology 与 Agent 工作流实现的本地演示系统。它提供可版本化的本体定义、对象与关系、受控 Action、提案审阅、角色与敏感字段控制，以及通过本体 API 操作数据的独立 Agent 服务。

本项目是用于学习和验证架构的独立原型，不是 Palantir 产品或其源码的复刻。首版 Agent 使用确定性工具调用，不连接外部大模型。

## 快速启动

需要 Docker Desktop（包含 Docker Compose）。在仓库根目录运行：

```powershell
Copy-Item .env.example .env
docker compose up --build -d
docker compose ps
```

首次启动时，API 容器会运行 Alembic 迁移并写入演示数据。服务健康后打开 [http://localhost:5173](http://localhost:5173)。

| 角色 | 用户名 | 本地演示密码 |
|---|---|---|
| 管理员 | `admin@example.com` | `change-this-local-password` |
| 编辑者 | `editor@example.com` | `local-editor-password` |
| 只读用户 | `viewer@example.com` | `local-viewer-password` |

这些账号和密钥只供本地演示。部署到共享或生产环境前，请修改 `.env` 中的密码、JWT 密钥和数据库凭据，不要提交 `.env` 文件。

## 功能

- **本体建模：** Ontology revision、对象类型、属性定义、链接类型和 Action 定义。
- **提案治理：** 编辑者提交结构变更；管理员按基础 revision 审阅并合并或驳回；过期提案不能覆盖新版本。
- **对象工作台：** 类型/关键词检索、对象详情、关系浏览、对象新增和 Action 执行。
- **访问控制：** 管理员、编辑者、只读用户分权；敏感属性按角色隐藏，审计内容脱敏。
- **Agent 工作台：** 配置允许使用的工具和 Action，创建会话，检索/读取对象，按授权执行 Action，并查询事件。
- **审计：** 对象操作和 Action 记录操作者、时间、版本及变更摘要。

## 服务结构

| 服务 | 端口 | 职责 |
|---|---:|---|
| `web` | 5173 | Vue 3 + TypeScript 管理控制台，由 Nginx 提供静态文件并代理 API |
| `ontology-api` | 8000 | FastAPI 本体、身份、对象、提案、Action 与审计 API |
| `agent-service` | 8001 | FastAPI Agent 注册、工具权限、会话和事件 API |
| `postgres` | 容器网络 | 权威本体数据、治理状态、Agent 持久轨迹 |
| `redis` | 容器网络 | Agent 会话事件的短期缓存 |

本体 API 文档：<http://localhost:8000/docs>。Agent API 文档：<http://localhost:8001/docs>。`web` 通过 `/api/` 访问本体 API，通过 `/agent-api/` 访问 Agent API。

## 常用命令

```powershell
# 查看服务状态与日志
docker compose ps
docker compose logs -f ontology-api agent-service

# 停止服务，保留数据库卷
docker compose down

# 本地开发测试
.venv\Scripts\python.exe -m unittest discover -s tests -p "test_*.py" -v
cd frontend
npm ci
npm test -- --reporter=dot
npm run build
```

`docker compose down -v` 会删除数据库和 Redis 数据卷，请仅在确实需要清空本地演示数据时使用。

## 研究材料

- [Palantir Ontology 与 Agent 文档目录](docs/research/README.md)：682 个官方页面的元数据目录、相关性分类与官方链接。
- [本体管理系统需求基线](docs/research/replica-requirements.md)：将研究方向映射到当前原型的领域模型与边界。
- [Palantir 官方 Foundry 文档](https://www.palantir.com/docs/foundry/)；[官方中文文档](https://www.palantir.com/docs/zh/foundry/)。

目录脚本只记录官方页面元数据，不保存文章正文。研读卡片由 [覆盖检查工具](scripts/check_research_coverage.py) 检查；尚未完成的卡片会明确显示为未完成，不能将目录覆盖率误当成研读完成率。
