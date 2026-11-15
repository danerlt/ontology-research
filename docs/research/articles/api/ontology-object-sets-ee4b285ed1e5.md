<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/ontology-object-sets -->
<!-- 研读状态：已完成 -->

# Ontology Object Set basics • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/ontology-object-sets)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/v2/ontologies-v2-resources
- 相关性：direct；Ontology REST API v2 ObjectSet API 分组入口
- 官方更新时间：2026-11-12T17:46:46.922Z
- 目录核对时间：2026-11-14T14:57:16Z
- 产品状态：分组入口未标注 Preview；具体操作状态以各端点为准

## 英文原文短摘录（每个来源不超过 25 词）

> “Ontology Object Sets”

## 摘录译文

本体对象集。

## 中文要点

- 这是 REST API v2 ObjectSet 资源分组页，分组路由未能独立读取正文。官方 v2 API 导航列出对象集基础、创建临时对象集、加载对象集、多对象类型加载、对象/接口加载和聚合等操作。
- ObjectSet 是查询/加载的对象集合上下文；它与对象类型 schema 不同，也不意味着把全体对象立即物化到客户端。具体惰性执行、分页和对象数限制需参考各操作页。
- 该分组覆盖从构造输入集合到按需加载/聚合的查询链路，是对象浏览、筛选与统计的 API 入口；它本身不是持久化对象类型定义。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| ObjectSet | 对象集 | 查询所作用的对象集合表达式 |
| Temporary ObjectSet | 临时对象集 | 通过 API 创建的临时集合输入 |
| Load | 加载 | 将集合按字段/类型取成响应数据 |
| Aggregate | 聚合 | 对集合执行统计/分组操作 |

## 疑问与待验证项

- 分组入口正文未独立可读；条目结构依据官方[v2 Ontology API 导航](https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources)，各接口具体能力需逐页核对。
- 临时对象集的存活时间、跨请求复用、分页快照和服务端资源回收规则不在目录页说明中。
- ObjectSet 表达式的跨类型、接口投影和链接遍历限制不能只依据分组名称判断。

## 复刻启示

- 前端可把筛选条件、关系遍历与集合运算编译成服务端 ObjectSet 查询计划，避免一次性下载全量对象。
- 类型 schema、集合查询和加载结果使用不同模型：分别代表定义、查询表达式和当前数据快照。
- 画布的对象节点/边是 schema 浏览视图；对象集的运行结果应作为可追踪查询上下文展示，而不是改写 schema 图。
