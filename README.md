# 本体工作台

一个以 Palantir Foundry Ontology 与 Agent 公开文档为功能基线的本地高保真工作台。它提供本体资源目录、隔离分支、结构检查与逐资源评审、本地数据映射导入、受控 Action、Agent 草稿与不可变发布版本、可调试会话及跨资源全局搜索。

这是独立实现，按公开文档复现用户工作流；不包含 Palantir 私有服务、源代码、商标资产或逐像素界面。公开材料无法验证的内部算法和闭源连接器不会标成已复刻。

## 快速启动

需要 Docker Desktop（包含 Docker Compose）。在仓库根目录运行：

```powershell
Copy-Item .env.example .env
docker compose up --build -d
docker compose ps
```

首次启动时，API 容器会运行 Alembic 迁移并写入演示数据。服务健康后打开 [http://localhost:5173](http://localhost:5173)。如果要启用模型对话，在本地 `.env` 设置 `AGENT_MODEL_BASE_URL`、`AGENT_MODEL_API_KEY`、`AGENT_MODEL_DEFAULT_NAME` 后重建 Agent 服务；凭据只通过服务端环境读取，不会保存在 Agent 配置或事件中。留空时 Builder 会禁用外部模型选项，会话页只显示本地 dry-run 和手动工具调试。

| 角色 | 用户名 | 本地演示密码 |
|---|---|---|
| 管理员 | `admin@example.com` | `change-this-local-password` |
| 编辑者 | `editor@example.com` | `local-editor-password` |
| 只读用户 | `viewer@example.com` | `local-viewer-password` |

这些账号和密钥只供本地演示。部署到共享或生产环境前，请修改 `.env` 中的密码、JWT 密钥和数据库凭据，不要提交 `.env` 文件。

## 功能

- **本体建模：** 资源目录、对象类型、属性、链接与 Action 定义；支持按类型页签查看数据、依赖、使用、安全和历史。
- **变更治理：** 隔离分支快照、结构校验、rebase、过期冲突保护、资源级评审和事务合并。
- **数据映射：** 本地 CSV/JSON 字段映射、导入预览、类型校验、失败无部分写入和运行状态记录。
- **对象工作台：** 全局关键词搜索、类型/记录直达、分页与服务端排序、对象详情/关系、Action 影响预览与确认执行。
- **访问控制：** 管理员、编辑者、只读用户分权；敏感属性按角色隐藏，审计内容脱敏。
- **Agent Builder / Manager：** 配置模型、提示词、启动输入、预计算变量、工具/Action 范围、完成与输出；发布不可变版本、固定版本启动会话、消息对话、工具 trace、模型用量与事件检查。
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

### 启用兼容模型

在个人 `.env` 中填入服务端可访问的 Chat Completions 兼容地址和模型凭据：

```dotenv
AGENT_MODEL_BASE_URL=https://api.openai.com/v1
AGENT_MODEL_API_KEY=你的服务端模型密钥
AGENT_MODEL_DEFAULT_NAME=你的模型名称
AGENT_MODEL_TIMEOUT_SECONDS=60
```

随后运行 `docker compose up --build -d agent-service web`。模型服务由服务器调用；浏览器无法读取密钥。请求失败时只持久化安全错误摘要和 trace 元信息，不保存授权头或响应正文。该适配器目前遵循 OpenAI Chat Completions 兼容格式，未接入 Palantir AIP、Foundry OAuth 或其模型路由。

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
- [公开功能对照矩阵](docs/research/palantir-public-parity-matrix.md)：按官方文档主题列出已覆盖工作流、缺口与闭源边界。
- [Palantir 官方 Foundry 文档](https://www.palantir.com/docs/foundry/)；[官方中文文档](https://www.palantir.com/docs/zh/foundry/)。

目录脚本只记录官方页面元数据，不保存文章正文。研读卡片由 [覆盖检查工具](scripts/check_research_coverage.py) 检查；尚未完成的卡片会明确显示为未完成，不能将目录覆盖率误当成研读完成率。
