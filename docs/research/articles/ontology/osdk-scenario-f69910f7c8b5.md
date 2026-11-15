<!-- 页面 URL：https://www.palantir.com/docs/foundry/ontology/osdk-scenario -->
<!-- 研读状态：已完成 -->

# Use scenarios with OSDK • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/ontology/osdk-scenario)
- 官方中文来源：尚未确认（配对状态：ambiguous）
- 页面语言：英文
- 主题栏目：ontology
- 相关性：direct；本体模型与治理文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:04:07Z
- 产品状态：页面标注 Experimental；TypeScript 和 Python OSDK 均有 Scenario client，但 API、版本要求和部分操作限制仍在变动。

## 英文原文短摘录（每个来源不超过 25 词）

> “All reads are automatically scoped to the scenario.”

## 摘录译文

所有读取会自动限定在该场景范围内。

## 中文要点

- OSDK 可创建场景或按 RID 连接现有场景；场景 client 的读取、查询、聚合和 Action 会自动针对隔离场景状态执行。创建的场景继承基础 client 的 Ontology 和 branch。
- TypeScript 版本要求 @osdk/client 2.27.0+；Python OSDK 要 2.209.0+，枚举编辑对象/链接需 2.221.0+，并在 AllowBetaFeatures 上下文中运行。
- 支持通过 Apply Scenario Action rule 将场景合入主本体；也可枚举场景内已编辑类型、对象和链接，以展示修改集。编辑 link 的接口仅返回多对多链接，一对多变化通过持有外键的对象体现。
- 不支持场景内批量 Action、嵌套 Scenario 或同事务组合；API 使用不稳定模块，文档明确标记实验状态。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| scenario-scoped client | 场景范围客户端 | 自动把查询和编辑路由到对应场景。 |
| edited entities | 已编辑实体 | 在场景中变更过的对象/链接标识集合。 |
| scenario RID | 场景 RID | 用于再次连接特定场景的引用标识。 |

## 疑问与待验证项

- - 使用不稳定 API 前需锁定 SDK 版本并加兼容适配层；不能把示例接口承诺为稳定长期契约。
- - link diff 的一对多/多对多表达不同，需要统一归一成画布边的变更模型，避免漏掉基于外键的关系修改。

## 复刻启示

- - 本地领域服务提供 ScenarioContext，使 object query、derived preview、Action edits 都显式携带 project、ontology、branch 和 scenario。
- - 提供按类型分页的 edited-entity manifest，并在画布上展示新增/改动/删除对象及关系；大批次通过游标读取而不是一次加载全量。
