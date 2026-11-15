<!-- 页面 URL：https://www.palantir.com/docs/foundry/object-permissioning/ontology-permissions -->
<!-- 研读状态：已完成 -->

# Object permissioning • Ontology permissions • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/object-permissioning/ontology-permissions)
- 官方中文来源：无精确对应页面；参照英文原文
- 页面语言：英文
- 主题栏目：object-permissioning
- 相关性：direct；本体对象权限文档
- 官方更新时间：页面未提供
- 目录核对时间：2026-11-15
- 产品状态：当前项目权限文档；新本体默认采用此路线，替代旧角色及数据源派生权限。

## 英文原文短摘录（每个来源不超过 25 词）

> “Ontology resources are saved into a project, and the selected project determines who can view, edit, and manage them.”

## 摘录译文

本体资源保存在项目中；所选项目决定谁可以查看、编辑和管理这些资源。

## 中文要点

- 对象类型、链接类型、动作、接口和共享属性等定义资源保存在具体项目，并继承 Compass 项目权限；实例权限另由支撑数据源或对象/属性策略控制。
- 看见对象类型 schema 不代表有权看对象实例；查看实例通常要同时有类型定义访问权和数据权限。无数据源类型必须使用项目权限与对象安全策略。
- 链接编辑要求有权编辑链接和两侧对象类型；动作编辑还要求对其编辑范围内的本体资源有相应权限。安全页用于解释定义、实例读取和动作执行分别需要什么权限。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| project-based permissioning | 项目权限 | 本体定义资源归入项目并继承项目访问控制。 |
| object security policy | 对象安全策略 | 无来源数据策略时限制对象实例可见性的规则。 |
| schema permission | 模式权限 | 查看/编辑对象类型定义和元数据的权利。 |

## 疑问与待验证项

- 页面说明新本体默认采用项目授权；已有本体仍需管理员开启并迁移，部署环境可能有历史差异。
- 执行本体查询需综合项目资源访问和来源数据规则；权限不足的派生路径应该是拒绝或明确缩减结果，不能悄悄泄漏。

## 复刻启示

- 以项目/文件夹 RBAC 管理本体定义资源，同时用数据源或对象/属性 ACL 保护实例；API 的每个请求都显式校验两层权限。
- 权限检查结果提供可读解释（缺失哪个项目角色、来源数据权或动作授权），并用于画布、推理预览、Agent 工具发现和执行。
