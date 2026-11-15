<!-- 页面 URL：https://www.palantir.com/docs/zh/foundry/ontology-sdk/how-to-create-backend-service-app-different-org -->
<!-- 研读状态：已完成 -->

# OSDK • 使用不同的组织创建应用程序 • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/developer-console/how-to-create-backend-service-app-different-org)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/ontology-sdk/how-to-create-backend-service-app-different-org)
- 页面语言：中文（官方机器翻译，准确性未验证）
- 主题栏目：ontology-sdk
- 相关性：direct；跨组织服务用户启用与访问授权
- 官方更新时间：2026-11-12T17:46:46.932Z
- 目录核对时间：2026-11-14T15:00:52Z
- 产品状态：指南针对 legacy permissions；Compass 管理权限的环境继承规则可能不同

## 英文原文短摘录（不超过 25 词）

> “Developer Console creates a service user with your application.”

## 摘录译文

Developer Console 会为应用创建一个服务用户。

## 中文要点

- 创建使用 confidential client 的应用时会一并创建服务用户；服务用户需要对本体读写资源获得显式授权。
- 指南描述 legacy permissions 工作流：服务用户初始作为 Developer Console 选定组织的 guest；组织下拉框只列出当前 location 已标记的组织。
- 若目标组织与默认组织不同，先在 Developer Console 分享应用给该组织，再在目标组织的 Control Panel 启用应用；完成后服务用户作为 guest 出现，才可进一步授权。
- 开启 classification-based access control 时，应用的最高分类不会自动赋给服务用户，需显式加入适当组与分类；控制台会提示客户端和服务用户的 marking/组织成员关系不一致。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| guest organization | 来宾组织 | 服务用户可被纳入并授权的外部/目标组织 |
| location marking | 位置标记 | 决定 Developer Console 组织选择器能显示哪些组织 |
| classification-based access control | 基于分类的访问控制 | 按组织分类和组成员限制服务用户可见数据 |
| enablement settings | 启用设置 | 目标组织启用共享应用并允许服务用户加入 |

## 疑问与待验证项

- 本页明确限定 legacy permissions；Compass-managed 权限从父项目/文件夹继承，分享步骤可能不同，不应照搬旧向导。
- 应用分享和服务用户加入组织仍不等于得到对象权限；对象、Action 和分类授权仍需逐项授予。
- 文档未解释目标组织应用启用策略与审计要求的全部细节，实际部署需由目标组织管理员核对。

## 复刻启示

- 多项目/多组织系统需要区分应用可见性、成员资格、对象权限、Action 权限和数据分类授权，状态逐级展示。
- 共享应用应要求目标组织管理员启用，并记录发起方、目标组织、所选 location 与审批/生效时间。
- 对服务身份显示权限差异和分类不匹配告警；不得把应用所有者的权限自动继承给 Agent 或服务用户。