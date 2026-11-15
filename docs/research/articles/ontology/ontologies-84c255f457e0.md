<!-- 页面 URL：https://www.palantir.com/docs/zh/foundry/ontologies -->
<!-- 研读状态：已完成 -->

# 本体 • 概述 • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/ontologies)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/ontologies)（已直接核验；页面声明未经验证的机器翻译）
- 页面语言：中文
- 主题栏目：ontologies
- 相关性：direct；本体管理与治理文档
- 官方更新时间：2026-11-12T17:46:46.937Z
- 目录核对时间：2026-11-14T15:00:03Z
- 产品状态：中文页为未经验证的 AIP 机器翻译；英文现行页另说明组织共享和项目角色边界。

## 原文短摘录与翻译

> “一个Ontology与一个空间是 1:1 映射的。”

**对应英文：** “An ontology is mapped 1:1 with a space.”

## 摘录译文

每个 Ontology 对应一个 Space；创建 Space 时会同步创建同名 Ontology，并继承组织标记。

## 中文要点

- Ontology 是保存本体资源/实体的工件，包括对象类型、链接类型、动作类型和接口。英文现行页还把共享属性、对象类型组列为资源种类。
- 一个 Ontology 可以私有并只属于单个组织，也可以在多个组织间共享。英文页的关键选择标准是：同一组织的多团队通常共享一个私有 Ontology；只有多个组织要共用同一套对象、链接和动作时才考虑共享 Ontology。不同团队的项目角色用于控制项目资源的可达权限。
- Ontology 与 Space 一对一：新 Space 同步创建同名 Ontology，并继承组织标记；私有 Space 对应私有 Ontology，共享 Space 对应共享 Ontology。英文页还说明同一用户可在有权限的多个 Ontology 间切换。
- 中文页解释共享本体支持跨组织安全共享数据与工作流，但省略了英文页按组织数量选择 private/shared 的具体规则及项目角色分权建议。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Ontology resource | 本体资源 | 对象类型、链接、动作、接口等可治理定义。 |
| Space | 空间 | 与 Ontology 一对一映射的容器和项目资源边界。 |
| private ontology | 私有本体 | 面向单个组织的本体资源集合。 |
| shared ontology | 共享本体 | 由多个组织成员共同访问同一组对象模型和动作。 |

## 疑问与待验证项

- 1:1 映射关系不能推导出每个团队或项目都必须新建 Ontology；英文页建议多团队在同一组织中使用项目角色管理资源访问。
- 中文页“组织权限标记”的翻译与当前角色模型的精确关系需结合 project-based permissions 与 Ontology roles 页面进一步核对。

## 复刻启示

- 多租户模型应显式拆分组织、项目/空间、Ontology 和资源权限；按空间/项目隔离成员与数据，同时支持跨组织共享的明确配置。
- 创建项目时可生成默认本体，但允许多个项目使用同一组织域本体；用资源级角色管理不同团队可见范围，不把租户和 Ontology 类型混为一层。
- 画布根上下文固定当前项目与 Ontology，显示私有/共享边界和参与组织；跨本体切换保留独立导航上下文。
