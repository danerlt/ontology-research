<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/object-types/get-object-type-edits-history -->
<!-- 研读状态：已完成 -->

# Get Object Type Edits History • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/object-types/get-object-type-edits-history)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/v2/ontologies-v2-resources
- 相关性：direct；对象类型与本体建模文档
- 官方更新时间：2026-11-12T17:46:46.921Z
- 目录核对时间：2026-11-14T14:56:58Z
- 产品状态：正式 API（页面未标注 Preview）

## 英文原文短摘录（每个来源不超过 25 词）

> “Returns the history of edits for objects of a specific object type.”

## 摘录译文

返回特定对象类型下对象的编辑历史。

## 中文要点

- 该接口查询的是对象实例的变更事件：新增、修改、删除；它不是对象类型定义本身的 schema 版本历史。
- 默认按最近到最早排序，可通过 `sortOrder` 反转；给出 `objectPrimaryKey` 时限定到单个对象，否则查询该类型的对象。
- 支持 filters、每页数量与分页令牌，也可传 `scenarioRid` 或 `branch` 查询对应上下文；默认 pageSize 为 100。OSv1 对象类型会忽略 filters。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Edits history | 编辑历史 | 对象实例的动作变更记录 |
| Primary key | 主键 | 将历史范围限制为某个对象 |
| Scenario | 情景 | 指定情景中的对象变更上下文 |

## 疑问与待验证项

- 返回记录是否带操作者身份、动作类型、字段级前后值和时间精度，需结合 ObjectEditHistoryEntry 完整结构与权限规则继续核对。
- 文档指出 OSv1 忽略 filters，但没有说明过滤器被忽略时响应是否返回提示。

## 复刻启示

- 审计界面应区分“定义变更历史”和“对象数据变更历史”，本接口只支持后者。
- 可在对象检查器提供按主键过滤、按时间倒序浏览和分页，并把 scenario/branch 作为明确的查询范围展示。
- 权限过滤、敏感字段脱敏及历史留存周期仍需自行设计，不能仅凭此读取接口推断。
