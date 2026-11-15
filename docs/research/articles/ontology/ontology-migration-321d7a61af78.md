<!-- 页面 URL：https://www.palantir.com/docs/foundry/ontologies/ontology-migration -->
<!-- 研读状态：已完成 -->

# Ontologies • Migrating between ontologies • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/ontologies/ontology-migration)
- 官方中文来源：[中文页面](https://www.palantir.com/docs/zh/foundry/ontologies/ontology-migration)
- 页面语言：英文
- 主题栏目：ontologies
- 相关性：direct；本体管理与治理文档
- 官方更新时间：页面未提供
- 目录核对时间：2026-11-15
- 产品状态：本体资源跨本体迁移向导；需保留相互依赖的资源集合。

## 英文原文短摘录（每个来源不超过 25 词）

> “Migrating resources between ontologies also changes the permissions on the resources.”

## 摘录译文

在本体之间迁移资源会改变资源权限。

## 中文要点

- 管理员选择来源本体和目标本体，再勾选对象类型、链接、动作与工作流；迁移对话框提供迁移前后的资源对照预览。
- 关联资源必须成组迁移，否则因引用缺失而失败；从私有本体迁往默认本体还有来源创建位置限制。
- 迁移会改变资源的本体权限，但不改变支撑数据源的权限；对象编辑默认保留。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| ontology migration | 本体迁移 | 在不同本体边界间移动模型资源。 |
| dependent resource | 依赖资源 | 引用待迁移对象/链接/动作的关联资源。 |
| target ontology | 目标本体 | 资源迁移后所属的本体。 |

## 疑问与待验证项

- 公开流程强调本体资源权限变化与数据权限不变；跨项目授权发生变化时仍要重新验证实例可见性。
- 迁移页面只允许选择对象类型、链接、动作和工作流，引用到其他服务的外部依赖是否自动迁移要另查。

## 复刻启示

- 资源移动应展示依赖闭包和迁移前后权限差异，并检查每个来源系统数据授权不因 schema 移动而改变。
- 执行迁移采用可审阅变更集；保留对象主键与用户编辑并审计目标项目及授权变化。
