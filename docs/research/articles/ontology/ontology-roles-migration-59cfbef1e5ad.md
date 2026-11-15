<!-- 页面 URL：https://www.palantir.com/docs/foundry/ontology-manager/ontology-roles-migration -->
<!-- 研读状态：已完成 -->

# Ontology Manager • Ontology roles migration [Legacy] • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/ontology-manager/ontology-roles-migration)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/ontology-manager/ontology-roles-migration)
- 页面语言：英文
- 主题栏目：ontology-manager
- 相关性：direct；本体管理器文档
- 官方更新时间：页面未提供
- 目录核对时间：2026-11-15
- 产品状态：旧版迁移文档；Ontology roles 已让位于项目权限模型，应以当前迁移文档为准。

## 英文原文短摘录（每个来源不超过 25 词）

> “Ontology resources can now be permissioned using the Compass filesystem.”

## 摘录译文

本体资源现在可以通过 Compass 文件系统进行权限管理。

## 中文要点

- 本页记录历史的 ontology roles 及来源数据权限迁移路径；旧模型把 schema 资源权限与来源数据集权限耦合。
- 角色模型曾允许在对象类型、链接、动作资源上授予本体查看/编辑/所有者角色，但对象实例和链接实例仍受输入数据源权限约束。
- 从数据源继承授权迁移时需要逐项校验资源和动作权限；旧角色迁移是不可逆操作。当前文档已指向 Compass 项目权限，应优先采用最新模型。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Ontology role | 本体角色 | 旧版资源查看、编辑和所有者权限。 |
| datasource-derived permissions | 数据源派生权限 | 旧模型中从支撑数据源继承本体资源权限。 |
| Compass | Compass | Foundry 资源与项目权限管理文件系统。 |

## 疑问与待验证项

- 这是标记为 Legacy 的页面；权限角色名称和迁移流程不应被误当成当前默认行为。
- 本体 schema 的可见权限与对象数据权限是两个不同授权面，迁移时必须分开核对。

## 复刻启示

- 将历史兼容层与当前项目 RBAC 隔离；新建本体资源遵循项目/文件夹授权。
- 对项目角色、资源定义查看权限、实例数据权限分别做解释和审计；不从项目级编辑权推导源系统数据权。
