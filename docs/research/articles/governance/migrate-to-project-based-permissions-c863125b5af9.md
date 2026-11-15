<!-- 页面 URL：https://www.palantir.com/docs/foundry/ontology-manager/migrate-to-project-based-permissions -->
<!-- 研读状态：已完成 -->

# Ontology Manager • Migrate to project-based permissions • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/ontology-manager/migrate-to-project-based-permissions)
- 官方中文来源：无对应中文页
- 页面语言：英文
- 主题栏目：ontology-manager
- 相关性：direct；本体管理器文档
- 官方更新时间：页面未提供
- 目录核对时间：2026-11-15
- 产品状态：当前权限迁移路线；项目权限取代旧本体角色与数据源派生模型。

## 英文原文短摘录（每个来源不超过 25 词）

> “Ontology resources can be saved within specific projects and automatically inherit permissions from those projects.”

## 摘录译文

本体资源可保存在特定项目中，并自动继承该项目的权限。

## 中文要点

- 对象类型、动作、链接、接口和共享属性等本体资源可保存到具体项目，并继承项目权限；对象/链接实例仍按支撑数据源位置控制访问。
- 迁移工具会建议资源放置项目，以帮助保留适当权限；迁移完成后通过 Compass 管理查看、编辑和管理权。
- 从旧权限迁至项目权限不可逆；迁移前要检查目标项目角色、标记分类及资源落位，目标项目权限可能比系统服务项目更严格。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| project-based permissions | 项目权限模型 | 本体定义资源保存到项目并继承其授权的方式。 |
| resource placement | 资源落位 | 为本体资源选择目标项目。 |
| backing datasource | 支撑数据源 | 实例读写权限仍需依据其来源授权的位置。 |

## 疑问与待验证项

- 项目权限适用于资源 schema；实例数据仍有自己的来源授权，API 必须同时判定两种访问。
- 迁移不可逆，因此本地是否提供项目迁移、资源搬迁和冲突回滚需设计清楚。

## 复刻启示

- 项目作为首要隔离上下文，提供成员角色和资源目录；对象类型、链接等 schema 资源可分配项目。
- 把本体资源 ACL 与实例数据 ACL 拆开检查；可见性、定义编辑权、对象读取权和动作执行权分别解释。
