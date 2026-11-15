# 项目化本体画布与派生属性实施记录

**目标：** 在现有 Ontology/Agent 工作台中交付项目隔离、本体关系画布，以及可解释、可评审发布的 1–3 跳派生属性。

**技术栈：** Vue 3、TypeScript、`@xyflow/vue`、FastAPI、SQLAlchemy 2、Pydantic、Alembic、PostgreSQL、Redis、Docker Compose。

**资料边界：** 按 Palantir 公开文档复现可验证工作流；不镜像文档全文，不声称还原闭源内部实现。

## 已完成实现

1. **多项目与成员隔离：** 增加 Project、ProjectMembership 和 admin/editor/viewer 角色；本体、Agent 与审计事件归属项目；请求头携带活动项目，ORM 查询受项目范围过滤；迁移回填已有数据。来源连接和对象映射沿本体归属项目。
2. **链接基数与分支定义：** 链接增加源/目标基数；分支支持增删派生属性、连续路径和类型/聚合校验；派生定义复用 `PropertyDefinition.options` JSONB 和现有提案机制，不新增派生定义表。
3. **只读推理 API：** 支持最多 3 跳关系读取及 count/sum/average/minimum/maximum/collect_list/collect_set；按基数约束聚合，忽略数值 null；返回匹配数、结果和逐跳对象/链接/属性证据，并对受限属性拒绝试算。
4. **本体资源画布：** Vue Flow 显示从 API 读取的对象类型、链接、来源系统映射和 Action；可筛选/搜索、拖动、缩放、定位、检查资源、小地图浏览；个人节点坐标和视口按项目/本体/分支保存在 localStorage。
5. **定义、试算与发布界面：** 分支页面编辑链接基数和派生路径；画布检查器选择派生属性，读取示例对象并发起试算，高亮路径并显示返回证据；既有分支提案流程负责审阅与合并。

## 集成验收结果

- 后端全量 unittest：130 项通过。
- 前端 Vitest：56 项通过；Vue 类型检查与生产构建通过。
- 文档覆盖脚本：676 张直接相关研读卡，缺卡 0、未完成 0、超限摘录 0。
- `docker compose config --quiet` 通过；五个容器健康；`/health/ready` 返回就绪。
- Alembic 数据库当前版本与迁移链头均为 `8ef7708b3491`；项目回填与链接基数迁移已在 Compose 数据库应用。
- 更新后的应用主导航可见“本体画布”；页面请求 `/api/ontology/canvas` 返回 HTTP 200。

## 尚待人工目检

浏览器自动化能登录工作区并打开画布路由，但页面状态和截图采集连续遇到 `Emulation.setFocusEmulationEnabled` / `DOMSnapshot.captureSnapshot` 超时。服务日志确认 Ontology、Branch 与 Canvas API 均已返回 200；由于没有成功取得画布截图，本轮不声称完成视觉目检或整条浏览器端新建项目到评审发布流程的手工验收。代码级测试、构建和服务健康检查均已通过。

## 公开功能范围

本地数据源只支持 CSV/JSON 导入；没有真实 Foundry/AIP 连接、Foundry OAuth、Ontology MCP/PMCP、外部连接器、物化派生属性、完整对象/行列格级权限或 Foundry 级协作治理。这些边界详见[公开功能对照矩阵](../../research/palantir-public-parity-matrix.md)。
