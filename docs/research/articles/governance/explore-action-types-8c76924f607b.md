<!-- 页面 URL：https://www.palantir.com/docs/foundry/action-types/explore-action-types -->
<!-- 研读状态：已完成 -->

# 动作类型 • 探索其他动作能力 • Explore other action types • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/action-types/explore-action-types)
- 官方中文来源：尚未确认（配对状态：ambiguous）
- 页面语言：英文
- 主题栏目：action-types
- 相关性：direct；本体动作文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:01:50Z
- 产品状态：Action Type 的规则覆盖对象、链接、函数、副作用、构建和场景提交等不同写入形态。

## 英文原文短摘录（每个来源不超过 25 词）

> “Action types can express much more than a property edit.”

## 摘录译文

Action 类型能够表达远多于属性编辑的操作。

## 中文要点

- 规则可以新建、修改或删除对象，也可以建立或移除对象间的链接。
- 其他能力包括调用函数、调用外部系统的 webhook、预先写回 webhook、通知用户、触发构建、应用场景编辑，以及对接口实现类型操作。
- 新建向导配置首条规则，已有 Action 可在 Ontology Manager 的 Rules 页添加规则；一个 Action 可组合多条规则，但 Function 规则不能与其他 Ontology 规则组合。
- 要修改的对象类型须先配置为可编辑；选择规则应围绕业务目标和副作用边界。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Ontology rule | 本体规则 | 声明对象或关系的结构化变更 |
| Writeback webhook | 写回 Webhook | 在应用编辑前调用外部系统 |
| Apply scenario | 应用场景 | 提交场景中暂存的对象编辑 |

## 疑问与待验证项

- 各种规则之间的事务边界、失败补偿和外部副作用重试语义由各专题分别说明，不能假设统一原子。
- Apply scenario 的编辑集如何与分支、权限及并发冲突互动，需结合场景和 Action 分支文档。

## 复刻启示

- 画布和 Action 编辑器应区分对象属性变更、关系变更、函数逻辑和外部副作用，并在提交前显示影响图。
- 规则组合校验须显式拒绝 Function 与其他 Ontology 规则并存，并为外部调用标注不可回滚风险。
