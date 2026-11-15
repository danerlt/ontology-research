<!-- 页面 URL：https://www.palantir.com/docs/foundry/developer-console/how-to-create-backend-service-app-different-org -->
<!-- 研读状态：已完成 -->

# Developer Console • How-to guides • Create an application in a different organization • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/developer-console/how-to-create-backend-service-app-different-org)
- 官方中文来源：[中文候选（旧 OSDK 路由，需人工复核）](https://www.palantir.com/docs/zh/foundry/ontology-sdk/how-to-create-backend-service-app-different-org)
- 页面语言：英文
- 主题栏目：developer-console
- 相关性：direct；服务用户跨组织可见性与权限配置
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:05:12Z
- 产品状态：指南针对 legacy permissions；Compass-managed permissions 可能采用不同继承流程

## 英文原文短摘录（不超过 25 词）

> “You must grant the service user any necessary permissions to read and write to the Ontology.”

## 摘录译文

必须向服务用户授予读写本体所需的权限。

## 中文要点

- confidential client 应用会创建关联服务用户；服务用户的本体读写权限需单独授予。
- 在 legacy permissions 模式下，服务用户最初是 Developer Console 选定组织的 guest；组织选择器只包含当前 location 已标记的组织。
- 目标组织不是默认组织时，先共享应用给目标组织，再由该组织在 Control Panel 启用应用，之后才能看到并授权服务用户。
- 开启 CBAC 时，服务用户不会自动继承应用最高分类，须加入正确组和分类；客户端与服务用户标记或组织成员不一致时，控制台会提醒。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| confidential client | 机密客户端 | 服务端持有 secret 的 OAuth 客户端 |
| guest user | 来宾用户 | 在目标组织中获得 guest 身份的服务用户 |
| Compass-managed permissions | Compass 管理的权限 | 通过父项目/文件夹组织权限的新权限模式 |
| marking mismatch | 标记不匹配 | 客户端与服务用户的分类/组织权限配置差异 |

## 疑问与待验证项

- 本文直接注明只涵盖 legacy permissions；在 Compass-managed 环境中应按权限说明重新确认，不应照抄分享和启用步骤。
- 即使应用成功分享和启用，仍需单独授予对象、Action、分类等授权。
- 目录将中文候选标为待复核；本卡链接同主题中文旧文，但不把它标记为已经证实的逐路由配对。

## 复刻启示

- 多组织边界应分别建模应用可见性、成员资格、资源授权和分类授权；流程面板按依赖顺序展示。
- 组织间启用需要目标方管理员动作和审计日志，创建应用者的权限不能隐式转移给服务身份。
- Agent/服务用户需可追踪其授权来源、当前组织和 marking，权限不一致时阻止部署或明确警示。