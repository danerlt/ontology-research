# 本体管理系统复刻需求基线

> 这是对公开产品文档方向的需求归纳及本地原型的范围说明，不代表 Palantir 内部实现细节。核对日期：2026-11-15。

## 从文档主题归纳的核心能力

研究目录将 682 个页面按本体、管理器、权限、Action、函数、SDK/API、Agent 与 MCP 等主题分类；其中 676 页标记为直接相关。分类用于发现材料，仍需结合原文复核，不代表每个 API 页面具有同等优先级。

| 领域 | 对系统设计的要求 | 本地原型实现 |
|---|---|---|
| Ontology 模型 | 让对象类型、属性、链接和可执行业务动作共享稳定的业务语义 | `Ontology`、`ObjectType`、`PropertyDefinition`、`LinkType`、`ActionDefinition` |
| 结构治理 | 结构修改可审阅、可追踪，并防止基于旧版本的变更覆盖新结构 | `ChangeProposal`、基础版本检查、管理员合并/驳回和审计 |
| 对象与关系 | 对象按类型校验；关系有明确源类型、目标类型和方向 | `ObjectRecord`、`ObjectLink`、对象检索与详情 API |
| Action | 将业务写入收敛为有参数、有权限、有版本检查的受控操作 | `ActionDefinition` 白名单、角色检查、乐观锁和事务审计 |
| 权限与敏感数据 | 不仅控制能否进入系统，还要约束对象读取、字段可见性和写入动作 | `admin/editor/viewer` 角色、敏感属性过滤、Agent 工具双重授权 |
| Agent | 让 Agent 通过受控工具使用本体，并能审查其会话和操作轨迹 | 独立 Agent 服务、工具允许列表、PostgreSQL 事件记录、Redis 短期缓存 |
| API / SDK 边界 | 应用和 Agent 经稳定 API 消费本体，不直接操作底层数据库 | Vue 控制台及 Agent 服务均通过 FastAPI 服务边界访问本体 |

## 对照官方文档

- [Ontology 核心概念](https://www.palantir.com/docs/foundry/ontology/core-concepts)：本体作为业务对象语义层的研究入口。
- [Ontology Manager 概览](https://www.palantir.com/docs/foundry/ontology-manager/overview)：本体管理与维护方向。
- [Ontology Manager 保存变更](https://www.palantir.com/docs/foundry/ontology-manager/save-changes)：结构编辑和变更管理方向。
- [Action Types 概览](https://www.palantir.com/docs/foundry/action-types/overview)：受控业务写入方向。
- [对象权限概览](https://www.palantir.com/docs/foundry/object-permissioning/overview)：本体对象安全方向。
- [Agent Builder 核心概念](https://www.palantir.com/docs/foundry/agent-builder/core-concepts)：Agent 构建与工具使用方向。
- [Agent Manager 概览](https://www.palantir.com/docs/foundry/agent-manager/overview)：Agent 运行管理方向。
- [Ontology MCP 认证与授权](https://www.palantir.com/docs/foundry/ontology-mcp/authentication-and-authorization)：外部 Agent 接入本体时的身份与权限方向。
- [Ontology API v2 参考](https://www.palantir.com/docs/foundry/api/ontologies-v2-resources)：本体 API 资源建模和版本接口方向。

以上链接用于定位原始材料。每篇页面的中文研读卡片应单独记录来源、要点、术语、待验证问题及其设计启示；这份需求基线不能替代逐篇研读。

### Agent / MCP 的两个边界

- **Ontology MCP（OMCP）**：将应用中显式纳入的对象类型、Action 类型和查询函数暴露为 Agent 工具。Agent 读业务对象或调用预定义 Action；资源范围由应用限制与授权控制。
- **Palantir MCP（PMCP）**：面向开发者操作本体结构和 Foundry 资源。结构变更需经过提案审阅并由人批准合并到主本体。
- 本地原型中的 Agent API 是受授权的 HTTP 工具服务，尚未实现 MCP 协议、OAuth scope、外部客户端接入或本体结构工具；不能把它等同于 OMCP/PMCP。

## 当前实现的范围与边界

当前实现增加了隔离本体分支、按资源逐项评审、分支重基与合并、对象类型和属性/链接/Action 定义更新、Action 参数与提交条件、CSV/JSON 本地映射导入、Agent 草稿与不可变发布版本、会话过滤/固定版本/消息、模型工具调用轨迹，以及可选的 OpenAI Chat Completions 兼容运行时。通过 Docker Compose 可启动 Vue、Ontology FastAPI、Agent FastAPI、PostgreSQL 和 Redis。

当前仍未实现真实 Foundry/AIP 连接、Foundry OAuth、Ontology MCP/PMCP、外部 Foundry 数据连接器与流水线、资源/对象/行列/格细粒度安全、函数/派生属性、函数型 Action、历史状态重放和完整上下文快照。对象类型、属性、链接与 Action 的结构变更覆盖度也低于官方 Ontology Manager；详细差距见[公开功能对照矩阵](palantir-public-parity-matrix.md)。不要把工作流接近称为产品本身完全等同。

## 研读未完成项

当前目录统计为 682 个唯一页面，其中 676 页为直接相关页面。已有 20 张卡片完成首轮研读，另有 656 张待填写；应按核心概念、治理、权限、Action、Agent/MCP、API/SDK 分批研读，在不保存全文的前提下保留官方链接与合规短摘录。
