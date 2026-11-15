<!-- 页面 URL：https://www.palantir.com/docs/zh/foundry/ontologies/ontology-permissions -->
<!-- 研读状态：已完成 -->

# 本体 • 权限 • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/object-permissioning/ontology-permissions-legacy)
- 官方中文来源：[中文页面](https://www.palantir.com/docs/zh/foundry/ontologies/ontology-permissions)
- 页面语言：中文
- 主题栏目：ontologies
- 相关性：direct；本体管理与治理文档
- 官方更新时间：2026-11-12T17:46:46.935Z
- 目录核对时间：2026-11-15
- 产品状态：旧中文权限页；它把 Ontology roles 描述为新方案，已被当前 Compass 项目权限文档取代。

## 英文原文短摘录（每个来源不超过 25 词）

> “The Ontology roles are the new and improved solution for authorizing Ontology resources.”

## 摘录译文

本体角色是当时用于本体资源授权的改进方案。

## 中文要点

- 该中文页面解释历史两种授权方式：从支撑数据源继承权限，或在对象类型、链接和动作资源上直接设置 Ontology roles。
- 旧角色区分 Owner、Editor、Viewer、Discoverer；这些角色控制资源 schema/元数据，不直接授予对象实例数据访问。
- 这份中文文档没有体现当前项目权限路线。现行英文资料规定本体定义资源存入项目、继承项目授权，实例数据继续按数据源或对象安全策略授权。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| ontology roles | 本体角色 | 曾直接授予资源级查看/编辑权限的旧授权模型。 |
| Discoverer | 发现者 | 旧角色中仅能看到资源名称和元数据的权限。 |
| project-based permissions | 项目权限 | 当前由项目/文件系统管理本体定义资源授权的模型。 |

## 疑问与待验证项

- 此中文页面与当前权限文档存在时效差异；页面自述是旧模型向 roles 迁移，当前又已从 roles 转向项目授权。
- 迁移顺序、旧环境兼容性和新的项目落位需分别依据对应英文迁移指南确认。

## 复刻启示

- 在研究卡和产品差异矩阵中为权限文档标注“旧路线/当前路线”，不要让旧页面覆盖新权限模型。
- 对 Agent、推理和画布资源读取分别判定项目本体定义权与对象数据权；不使用单一角色布尔值替代多层安全判断。
