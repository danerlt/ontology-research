<!-- 页面 URL：https://www.palantir.com/docs/foundry/action-types/action-log -->
<!-- 研读状态：已完成 -->

# Action types • Action log • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/action-types/action-log)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/action-types/action-log)（配对状态：matched）
- 页面语言：英文
- 主题栏目：action-types
- 相关性：direct；本体动作文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:02:22Z
- 产品状态：页面未标注 Beta 或 Preview；函数型 Action 日志要求 `Edits` 来源标记。

## 英文原文短摘录（每个来源不超过 25 词）

> “The action log models successful action submissions as object types to be analyzed and displayed in object-aware Foundry tooling.”

## 摘录译文

操作日志把成功提交的 Action 建模为本体对象，供对象感知工具展示、分析和后续决策流程使用。

## 中文要点

- Action log 回答“谁在何时基于什么上下文作出了什么操作决定”；对象编辑历史负责完整记录各类编辑，Action metrics 负责成功率、失败和耗时，撤销能力负责回滚 Action 的对象编辑，四者不能互相替代。
- 每种 Action Type 对应一个日志 Object Type；一次成功提交创建一条日志对象，并链接该次 Action 修改的所有对象。日志可记录 Action RID、类型 RID/版本、UTC 时间、用户、对象主键、参数、通知/Webhook、scenario 与撤销信息，也可保存未被修改对象的上下文属性。
- 日志仅覆盖经 Action Type 提交的编辑；直接写入底层数据源不会产生 Action log。日志从启用配置后开始，不会为过去的提交补历史。日志对象本身需要相应对象权限。
- OSv2 中日志时间戳与 edit history 使用同一提交时间戳，但它表示准备提交存储的时间，不保证是查询中可见的准确时刻；撤销时保留原日志时间并另记撤销时间。
- 函数驱动 Action 要配置 `Edits` 来源。摘要最多 20 个组成部分，每个字面量最多 50 个字符，不能引用对象类型参数；媒体引用不写入日志，多值对象引用参数也不能记录其属性值。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Action log | 操作日志 | 将一次成功的动作提交建模成可查询的本体对象。 |
| Edit history | 编辑历史 | 对对象的编辑轨迹进行记录，覆盖面与 Action log 不同。 |
| commit timestamp | 提交时间戳 | OSv2 日志和编辑历史采用的时间，不等同于查询可见时刻。 |
| Edits provenance | Edits 来源标记 | 函数驱动 Action 生成操作日志所需的编辑来源配置。 |

## 疑问与待验证项

- 该页把 action log、edit history、metrics 和 revert 分成不同问题域；实现时需要避免把“有操作日志”误当作“所有数据写入都有完整审计”。
- 运行时若日志对象创建失败，Action 主体写入和日志写入的事务边界、失败重试与可见性应结合写入模式和存储后端进一步验证。

## 复刻启示

- 为每个 Action Type 维护单独的审计配置与日志模型，记录 action/version、操作者、提交时间、关联对象、参数摘要、side effect 标识、scenario 和撤销事件；一批对象修改仍可对应一条可关联多个对象的事件。
- 在控制台明确区分审计事件、逐字段编辑历史、运行指标和撤销记录；让管理员设置对象类型是否强制所有编辑动作产生日志，并提示配置启用前的历史不会回填。
- Agent 执行动作时复用同一 Action 提交路径及审计模型，明确记录调用来源和上下文，不能因调用入口是 SDK/API 而漏记。
