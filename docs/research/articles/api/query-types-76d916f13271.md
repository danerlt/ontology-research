<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/query-types -->
<!-- 研读状态：已完成 -->

# Query Type basics (v2, latest) • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/query-types)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/v2/ontologies-v2-resources
- 相关性：direct；Ontology REST API v2 Query Type 分组入口
- 官方更新时间：2026-11-12T17:46:46.922Z
- 目录核对时间：2026-11-14T14:57:50Z
- 产品状态：分组入口未标注 Preview；具体查询定义状态以端点页为准

## 英文原文短摘录（每个来源不超过 25 词）

> “Query Types”

## 摘录译文

查询类型。

## 中文要点

- 该路由是 v2 Query Type API 分组入口，官方导航列出 Query Type basics、List Query Types 和 Get Query Type。
- Query Type 描述可被发现和执行的查询接口；列表用于发现某本体下的契约，单条读取则按查询 API 名加载具体参数/输出 schema。它不同于一次查询执行结果。
- v1 也有同名资源，但 v2 端点可能增加 SDK、branch/scenario 或 transaction 上下文；实际差异以两个版本的各接口卡为准。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Query Type | 查询类型 | 已发布查询接口的元数据/契约 |
| API name | API 名称 | 查询定义的稳定程序化标识 |
| Query execution | 查询执行 | 某一次带参数运行 |
| Output schema | 输出 schema | 描述返回值形状的契约 |

## 疑问与待验证项

- 分组入口依据官方[v2 Ontology API 导航](https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources)；同名 v1 路由和 v2 路由存在版本差异，不能合并成一张端点卡。
- Query Type 和底层 Function 的发布绑定、版本升级/回滚策略需结合 Query Type basics 与详情接口确认。
- 该分组本身不说明 Agent 可见性、工具暴露策略、运行费用或权限继承。

## 复刻启示

- 将 Query Type 当作可机器调用的工具契约，包含输入 schema、输出 schema、版本、授权 scope 和执行器引用。
- Agent 工具注册中心可从 Query Type 生成受限工具描述，但每次运行仍要独立校验调用者、资源权限和参数。
- 在设计画布中，查询类型可作为操作/工具节点展示，与领域对象节点和关系边使用不同视觉编码。
