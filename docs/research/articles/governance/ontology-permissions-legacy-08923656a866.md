<!-- 页面 URL：https://www.palantir.com/docs/foundry/object-permissioning/ontology-permissions-legacy -->
<!-- 研读状态：已完成 -->

# Object permissioning • Legacy ontology permissions • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/object-permissioning/ontology-permissions-legacy)
- 官方中文来源：无精确对应页面；参照英文原文
- 页面语言：英文
- 主题栏目：object-permissioning
- 相关性：direct；本体对象权限文档
- 官方更新时间：页面未提供
- 目录核对时间：2026-11-15
- 产品状态：遗留权限参考；新实现应以 Compass 项目权限为准。

## 英文原文短摘录（每个来源不超过 25 词）

> “This replaces the previous ontology roles and datasource-derived permission models.”

## 摘录译文

该项目权限模型取代了此前的本体角色和数据源派生权限模型。

## 中文要点

- 本页归纳两种历史模式：Ontology roles 直接给 schema 资源授予角色；数据源派生权限把本体资源访问与支撑数据源权限绑定。
- 旧角色只控制本体资源和元数据编辑，不会自动授予底层实例数据权限；数据源派生模式则将资源元数据授权耦合到输入数据源。
- 当前权限页面指出项目权限已取代两种旧模式；这份资料适用于解释兼容环境与迁移边界，不应作为新项目的默认配置说明。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Ontology Viewer | 本体查看者 | 旧角色模型中只读查看本体定义的角色。 |
| Ontology Editor | 本体编辑者 | 旧角色模型中编辑本体定义的角色。 |
| datasource-derived | 数据源派生授权 | 由支撑数据源权限推导本体定义权限的旧方式。 |

## 疑问与待验证项

- 旧版各角色细节会随遗留安装环境不同而异；应用不能只靠角色名称猜测实例数据权限。
- 新旧授权模型之间迁移涉及项目落位和分类标记，权限不能仅通过角色名机械映射。

## 复刻启示

- 只在导入兼容配置时识别旧角色授权，并提供迁移检查报告；核心权限模块采用项目 RBAC 与数据 ACL 分层。
- 给 Agent 暴露“可发现定义”“可查询对象”“可运行动作”三种独立权限判断，防止对象 schema 可见就扩大数据读取权。
