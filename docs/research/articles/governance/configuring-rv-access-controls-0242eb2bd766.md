<!-- 页面 URL：https://www.palantir.com/docs/zh/foundry/object-permissioning/configuring-rv-access-controls -->
<!-- 研读状态：已完成 -->

# 对象权限管理 • 配置受限视图支持的对象类型 • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/object-permissioning/configuring-rv-access-controls)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/object-permissioning/configuring-rv-access-controls)（中文路由译文以英文原文复核）
- 页面语言：中文
- 主题栏目：object-permissioning
- 相关性：direct；本体对象权限文档
- 官方更新时间：2026-11-12T17:46:46.936Z
- 目录核对时间：2026-11-14T14:59:57Z
- 产品状态：官方中文路由的译文准确性未逐句验证；术语和规则按英文原文复核。

## 原文短摘录与翻译

> “Restricted views (RVs) enable row-level access controls for ontology data.”

## 摘录译文

受限视图（RV）为本体数据提供行级访问控制。

## 中文要点

- 对象类型可由 Restricted View（RV）作为支持数据源；对象可见性继承 RV 行策略，从而把数据集级访问细化到单行/单对象。
- OSv1（Phonograph）下用户需能查看对象类型，并满足该行标记与读取策略；未必需要 RV 本身的查看权限。OSv2 则要求用户能查看该 RV。
- OSv2 的 RV/对象安全策略比较操作数限于 String 或 Boolean，且不支持大小比较；若策略不引用字段，数值、日期和时间戳属性仍可索引。
- 若 Action 编辑了策略依赖的对象属性，Ontology 对象可见性会与支持行的可见性分离。OSv1 策略改动需手动更新注册；OSv2 默认自动传播。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Restricted View (RV) | 受限视图 | 带行级策略的数据视图，可作为对象类型的数据源。 |
| row-level access control | 行级访问控制 | 按行策略控制对应对象实例的可见性。 |
| policy propagation | 策略传播 | 策略修改同步到对象存储/索引的过程。 |

## 疑问与待验证项

- OSv1/OSv2 的授权差异及策略传播细节会影响实际访问结果；迁移兼容性和策略更新时序应在目标部署中核对。
- 当策略所依赖属性被 Action 改写时，行权限与对象权限短暂或长期不一致的处理方式需结合具体数据源验证。

## 复刻启示

- 支持把来源系统的行策略映射为对象访问策略，并在对象详情、画布预览、派生属性和 Agent 读取路径上统一执行。
- 将策略依赖字段纳入变更影响图；策略更新、对象属性写回和索引注册需要提供版本、传播状态与审计记录。
