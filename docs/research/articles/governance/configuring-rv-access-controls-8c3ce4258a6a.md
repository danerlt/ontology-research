<!-- 页面 URL：https://www.palantir.com/docs/foundry/object-permissioning/configuring-rv-access-controls -->
<!-- 研读状态：已完成 -->

# Object permissioning • Configuring restricted-view-backed object types • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/object-permissioning/configuring-rv-access-controls)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/object-permissioning/configuring-rv-access-controls)（配对状态：matched）
- 页面语言：英文
- 主题栏目：object-permissioning
- 相关性：direct；本体对象权限文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:04:25Z
- 产品状态：OSv1/OSv2 对受限视图可见权限和策略更新传播有差异。

## 英文原文短摘录（每个来源不超过 25 词）

> “Restricted views (RVs) enable row-level access controls for ontology data.”

## 摘录译文

受限视图（RV）为本体数据提供行级访问控制。

## 中文要点

- Restricted View 可作为对象类型数据源，以其行策略控制对应 Ontology object 的可见性，比按数据集或对象类型整表授权更细。
- OSv1（Phonograph）要求对象类型可见并满足该行的 marking/read policy，但用户不一定需要 RV 本身查看权；OSv2 则要求用户能查看 backing RV。
- OSv2 的 RV/object security policy 比较操作数只能是 String 或 Boolean，不支持小于/大于等序比较；策略未引用的数值、日期、时间戳字段仍可索引。
- 若 Action 改写策略依赖属性，对象安全策略与 backing RV 行策略可能产生访问不一致。OSv1 策略变更需手动更新注册；OSv2 默认自动传播。
- 旧式 granular edit policy 只对部分 OSv1 对象类型可用；其他类型通过 Action Type 的编辑权限控制。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Restricted View (RV) | 受限视图 | 含行级读取策略、可作为对象类型数据源的视图。 |
| marking | 标记 | 决定用户能否访问受限数据的分类控制。 |
| object security policy | 对象安全策略 | 按对象/属性计算访问条件的策略。 |
| policy propagation | 策略传播 | 策略变更同步到对象存储/索引的过程。 |

## 疑问与待验证项

- 索引属性允许的类型和策略比较类型不同；不能根据可索引就推断该字段可安全用作策略操作数。
- Action 改写策略字段会影响用户之后能否继续读取该对象；部署需检查锁定/提升权限造成的访问变化。

## 复刻启示

- 以行/对象级策略约束画布预览、函数/Agent 查询和派生属性依赖遍历，避免通过链接/聚合侧向泄露不可见对象。
- 策略规则版本化，展示所依赖属性和变更影响；OSv1 兼容需显式注册更新状态，OSv2 则追踪自动传播完成状态。
