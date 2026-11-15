<!-- 页面 URL：https://www.palantir.com/docs/foundry/developer-console/permissions -->
<!-- 研读状态：已完成 -->

# Developer Console • 权限 • Permissions • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/developer-console/permissions)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：developer-console
- 相关性：direct；开发者控制台与本体集成文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:05:01Z
- 产品状态：Developer Console 应用可采用用户或应用权限；Compass 管理用户权限当前为 Beta，Client-facing 应用要求用户权限。

## 英文原文短摘录（每个来源不超过 25 词）

> “Client-facing applications must use the user permissions option and the Authorization code grant OAuth workflow.”

## 摘录译文

面向客户端的应用必须使用用户权限和 OAuth 授权码流程。

## 中文要点

- Developer Console 应用继承父项目/文件夹的角色、标记和组织权限；Viewer 可查看/使用 SDK 开发但不能编辑或生成新 SDK，Editor 可修改并生成，Owner 还可分享应用。
- 用户权限以当前用户身份读取/写入本体，使用 OAuth Authorization Code；应用权限使用生成服务用户，采用 Client Credentials；两种权限可组合。
- 面向终端用户的应用必须走用户权限与授权码流程；若改用应用权限，服务用户会按应用级授权读取数据。
- Compass 管理的用户权限仍为 Beta，适用租户受限；旧应用迁移至项目时既有权限结构不会沿用，网站查看范围按目标项目权限重算。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| User permissions | 用户权限 | 以登录用户权限读写本体的 OAuth 模式 |
| Application permissions | 应用权限 | 以生成服务用户权限读写本体的 OAuth 模式 |
| Compass-managed permissions | Compass 管理权限 | 随项目/文件夹继承的应用授权方式 |

## 疑问与待验证项

- 用户权限 Beta 的租户可用性会变化，需按目标 enrollment 检查，不把 Beta 机制当稳定假设。
- 迁移会以目标项目权限替换原应用权限；执行前应预览 Viewer 和网站访客范围，避免扩大访问面。

## 复刻启示

- 默认面向用户的交互客户端采用用户授权并透传当前用户；后台服务单独使用最小范围服务身份。
- 项目权限继承、应用角色、OAuth scope 和本体数据权限分层展示；迁移向导对比迁移前后的用户可见范围。
