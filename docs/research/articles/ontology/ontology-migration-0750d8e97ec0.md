<!-- 页面 URL：https://www.palantir.com/docs/zh/foundry/ontologies/ontology-migration -->
<!-- 研读状态：已完成 -->

# 本体 • 在Ontologies之间迁移本体资源 • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/ontologies/ontology-migration)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/ontologies/ontology-migration)
- 页面语言：中文
- 主题栏目：ontologies
- 相关性：direct；本体管理与治理文档
- 官方更新时间：2026-11-12T17:46:46.935Z
- 目录核对时间：2026-11-15
- 产品状态：官方中文页标注为未经验证的 AIP 机器翻译；已对照英文原文。

## 英文原文短摘录（每个来源不超过 25 词）

> “Migrating resources between ontologies also changes the permissions on the resources.”

## 摘录译文

在本体之间迁移资源会改变资源权限。

## 中文要点

- 迁移可选择对象类型、链接、动作和工作流，并在提交前对照来源本体与目标本体资源清单。
- 依赖资源需要一起选择，否则迁移失败；对象编辑默认保留。
- 迁移改变本体资源授权但不会改变输入数据源权限；因此移动后仍须检查数据可见性与目标本体访问权。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| resource selection | 资源选择 | 迁移时明确纳入的本体资源清单。 |
| dependency closure | 依赖闭包 | 为保持引用完整而需要一起移动的资源集合。 |
| permission boundary | 权限边界 | 资源所属本体变动所涉及的授权上下文。 |

## 疑问与待验证项

- 中文页是未经验证的机器翻译；本卡采用英文原文确认迁移约束。
- 默认保留对象编辑并不表示外部系统状态或跨本体链接也会自动转移。

## 复刻启示

- 迁移前在图上高亮选中资源的依赖闭包、跨本体链接限制和访问策略变更。
- 迁移完成后重建项目 ACL 缓存，并检验对象数据权限仍然受来源数据授权保护。
