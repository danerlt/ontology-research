<!-- 页面 URL：https://www.palantir.com/docs/zh/foundry/questions-answers/ontology -->
<!-- 研读状态：已完成 -->

# 问答 • Ontology • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/questions-answers/ontology)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/questions-answers/ontology)
- 页面语言：中文（官方机器翻译，准确性未验证）
- 主题栏目：questions-answers
- 相关性：direct；本体安全、属性标识、编辑冲突与附件关系
- 官方更新时间：2026-11-12T17:46:46.937Z
- 目录核对时间：2026-11-14T15:01:25Z
- 产品状态：问答附有 2024–2025 日期；具体版本和权限模式需对照当前主题文档

## 英文原文短摘录（不超过 25 词）

> “You need to explicitly parent the attachment through an action.”

## 摘录译文

需要通过 Action 显式建立附件的父子关系。

## 中文要点

- OSv2 对象类型若由物化 Restricted View 支撑，需在支撑它的 RV 上修改细粒度策略，策略再传播到物化 RV。
- 多个附件不能通过向属性写入 RID 数组来挂接；需要经 Action 显式将附件关联到对象。
- 在 MDO 对象的 Restricted View 间移动列不会改变属性 API name 或 RID；物化列名变化也不会改写存放于 OSv2 的对象编辑记录。
- “应用最新值”冲突策略按时间戳决定胜者；流水线时间戳较新时，用户把 null 改成值的编辑可能被流水线 null 覆盖。
- Restricted View 策略列未填全可能让 Action 新建对象对所有人不可见；布尔值可在 Action 表单中映射为“是/否”展示而保持布尔类型。
- 英文当前页另有旧 geohash 类型更名为 geopoint 的问答；此类 dated FAQ 应与当前类型参考交叉核对。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| materialized Restricted View | 物化限制视图 | OSv2 对象数据来源与安全策略承载位置 |
| object edit conflict resolution | 对象编辑冲突解决 | 管道写入和用户编辑并发时的胜者规则 |
| property API name / RID | 属性 API 名 / RID | 本体属性在 schema 与资源层的稳定标识 |
| parent an attachment | 建立附件归属 | 通过 Action 把附件关联到对象 |

## 疑问与待验证项

- 问答给出具体日期但未列明适用的平台版本；流程与策略应以当前权限、附件和 MDO 参考页为准。
- Restricted View 策略列缺失的对象可见性依具体策略表达式而定，需通过实际权限模拟核验。
- “最新值”冲突需要正确配置时间戳属性；若时间戳缺失，行为与数据源写入顺序须结合冲突策略文档验证。

## 复刻启示

- 附件写入应先上传暂存，再通过受控 Action 关联对象，不能把存储 RID 列表当成授权关系。
- 权限策略字段要参与对象创建预检，预演新对象对不同角色的可见性，避免创建后不可见。
- 属性标识与显示名分开保存；schema 名称迁移不得破坏已存编辑记录和 API 引用。