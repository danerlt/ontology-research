# Foundry Ontology / Agent 公开功能对照矩阵

> 核对日期：2026-11-15。此矩阵以 Palantir 公开文档描述的用户流程为基线，不推测私有实现，也不代表与 Foundry 产品代码或逐像素界面等同。

## Ontology Manager

| 官方工作流 | 本项目映射 | 状态 | 与文档行为的主要差距 |
|---|---|---|---|
| 对象类型创建：元数据、数据源、属性、主键/标题键、生成 Actions | 分支向导创建复数名、说明、主键/标题键、别名、分组、图标和附加属性；数据源在独立映射页关联 | **部分具备** | 元数据和附加属性已贯通；还没有 Foundry 数据集 schema 探测、向导内数据源绑定、自动生成 Action 与创建时安全策略。 |
| 属性定义：基础类型、必填/唯一/敏感/只读约束 | `PropertyDefinition`、对象类型属性页、分支内新增/更新，以及派生属性定义、路径试算和评审发布 | **核心流程具备** | 尚无属性删除/字段数据迁移预览、展示格式、条件格式、共享属性及 struct/media 类型；派生属性只支持声明式链接路径与内置聚合器。 |
| 链接类型：定义源/目标类型与关系方向、基数 | 分支中新建链接、维护源/目标基数；画布展示有向关系，实例页显示实际关联 | **核心流程具备** | 源/目标类型创建后不可编辑；没有删除、反向显示名称、跨本体或外部关系。 |
| Action：参数、规则、提交条件、预览和执行 | 分支新建/更新 Action；服务端 schema 与条件校验、版本检查、权限校验、事务写入、审计及 Agent allowlist | **部分具备** | 普通对象属性写入路径可运行；未支持 Action 定义删除、函数型 Action、参数默认值/引用控件、批量操作、外部副作用及平台级 Action 权限策略。 |
| Ontology 分支与变更审阅 | 快照分支、资源更新、校验、rebase/冲突检测、提案、按资源评审、事务合并；项目成员角色限制访问 | **核心流程具备** | 治理规则为本地角色配置；没有 Foundry 项目策略、审批组编排、通知和评论线程。 |
| 对象/属性安全与权限 | 项目成员角色、项目级资源隔离、敏感属性过滤、Agent 工具二次授权 | **部分具备** | 尚无 Compass/组织权限继承、对象级策略、行/列/格标记与策略模拟。不能将项目角色和敏感字段过滤等同于 Foundry 的细粒度安全模型。 |
| 数据源映射与刷新 | 本地 CSV/JSON 映射、预览、类型检查、整批原子导入与状态记录 | **部分具备** | 没有 Foundry dataset、Pipeline Builder、增量构建、调度、血缘、重试/回滚与外部连接器。 |
| 资源搜索和对象浏览 | 全局资源命令面板；对象搜索、服务端分页/排序、类型与记录深链、关系与 Action 面板 | **核心流程具备** | 搜索当前是基于授权 API 拉取目录后组合；没有 Foundry 搜索索引、查询语言、保存的 object sets 或大型数据集性能保证。 |

官方依据：[创建对象类型](https://www.palantir.com/docs/foundry/object-link-types/create-object-type)、[Ontology Manager 保存变更](https://www.palantir.com/docs/foundry/ontology-manager/save-changes)、[分支本体](https://www.palantir.com/docs/foundry/ontologies/branching-ontology)、[Action Types](https://www.palantir.com/docs/foundry/action-types/overview)、[对象权限](https://www.palantir.com/docs/foundry/object-permissioning/overview)。

## 项目、本体画布与派生属性

| 官方工作流 | 本项目映射 | 状态 | 与文档行为的主要差距 |
|---|---|---|---|
| 多个业务项目各自维护 Ontology、数据和成员 | 项目与成员角色；项目可有多个本体和数据源；HTTP 请求显式携带活动项目，ORM 查询按项目范围过滤 | **核心边界具备** | 目前是单工作区部署，没有组织层级、SSO、外部身份目录、项目配额和平台级权限继承。 |
| 在图形画布上浏览对象类型和关系 | Vue Flow 画布呈现真实 ObjectType、LinkType、SourceMapping 与 ActionAssociation；支持图层筛选、搜索定位、缩放、小地图、检查器和个人布局 | **核心流程具备** | 当前聚焦单个本体的建模资源图，不是对象实例网络浏览器；没有大型图的服务端增量布局与协作式实时光标。 |
| 使用链接与已有属性推导新属性 | 分支内声明 1–3 跳路径；单值路径读值，多对象路径需要类型匹配的聚合器；只读试算并返回逐跳证据，敏感终点受角色控制 | **核心流程具备** | 当前为同步试算，最多处理 1000 条路径记录；无后台物化、缓存更新策略、函数表达式或通用本体查询语言。 |
| 在审批后发布本体结构变更 | 派生定义使用现有属性 JSONB 元数据保存，纳入分支快照、资源提案、逐资源评审与合并事务 | **核心流程具备** | 没有 Foundry 环境升级、发布通道、版本化安全策略迁移或原生通知。 |

官方依据：[派生属性概览](https://www.palantir.com/docs/foundry/ontology/derived-properties)、[派生属性配置](https://www.palantir.com/docs/foundry/object-link-types/derived-properties)、[聚合与类型参考](https://www.palantir.com/docs/foundry/ontology/derived-properties-reference)。画布使用 [Vue Flow](https://vueflow.dev/guide/) 呈现本项目自己的本体资源。

## Agent Builder / Agent Manager

| 官方工作流 | 本项目映射 | 状态 | 与文档行为的主要差距 |
|---|---|---|---|
| 输入、预计算变量、提示词、工具和完成配置 | Builder 的输入/变量/模型提示/工具权限/结构化输出面板 | **部分具备** | 变量目前为受限表达式，不支持任意 Ontology 查询、函数计算、Action 组合或完整依赖图。 |
| 工具访问 Ontology 数据或执行 Action | OpenAI 兼容函数调用进入 Agent 服务，再由 Ontology API 做权限校验 | **部分具备** | 目前只有对象查找/读取与白名单 Action；没有 no-code 自定义工具、Ontology SQL、Foundry 函数或 AIP 原生工具注册。 |
| 保存草稿与发布版本 | 草稿配置存储、服务端校验、不可变 `AgentVersion` | **核心流程具备** | 没有 Foundry Agent SDK 项目、代码编辑工作流、版本回滚/环境发布与平台模型路由。 |
| 从固定版本创建会话并提供输入、继续消息、取消会话 | Manager 版本选择、必填输入、来源、消息表单与结束状态 | **核心流程具备** | 没有 Foundry 应用内嵌启动参数、共享/委派运行身份及真实 AIP session semantics。 |
| 跨应用筛选与调查 session | 跨 Agent 会话表、状态/来源/关键词筛选，固定版本检查器、事件载荷与模型用量 | **部分具备** | 尚无历史时点的上下文/Agent 状态重放、结构化 trace span、平台日志与底层代码跳转。 |
| 模型运行时配置 | 可选 Chat Completions 兼容接口；地址/密钥仅由 Agent 服务环境读取 | **部分具备** | 未使用 Palantir AIP，不接 Foundry OAuth、权限标记传播、模型选择/预算/队列、区域策略或供应商注册。没有配置密钥时不会伪装成真实 Agent 推理。 |

官方依据：[Agent Builder 核心概念](https://www.palantir.com/docs/foundry/agent-builder/core-concepts)、[Agent Builder 入门](https://www.palantir.com/docs/foundry/agent-builder/getting-started)、[Agent Manager 概览](https://www.palantir.com/docs/foundry/agent-manager/overview)、[调查 Agent 会话](https://www.palantir.com/docs/foundry/agent-manager/session-debugging)。

## 当前版本可复核范围

- 新增和已支持的元数据更新只在分支中暂存，经过校验和资源级评审后才能合并到 main；过期快照不能静默覆盖新 revision。
- Action 与 Agent 工具最终都通过 Ontology API 的角色、对象版本和允许范围检查；Action 执行与审计在事务中完成。
- Agent 会话固定不可变发布版本；会话输入展示时脱敏，事件持久化不包含模型 API key。
- 模型 Provider 能发起兼容接口调用并进行函数工具调用循环。没有服务端配置时只允许本地 dry-run 与显式工具调试。
- 数据源能力只覆盖本地 CSV/JSON 文件流入演示本体；它不连接 Palantir Foundry，也不声称复刻真实平台同步任务。
- 项目隔离、关系画布和派生属性试算均已落到本地工作流；派生属性在提案批准并合并前仅存在于分支定义中。

## 不能声称 1:1 的部分

Foundry 属于闭源商业平台，公开文档能验证的是已描述的产品功能和工作流程，无法据此还原内部数据存储、调度/索引算法、部署与权限服务、故障语义或未公开 UI 状态。本项目因此以“公开文档工作流高保真复现”作为可检验目标，并逐项披露未覆盖能力；不复制 Palantir 商标、私有源码或未授权正文镜像。
