<!-- 页面 URL：https://www.palantir.com/docs/foundry/developer-console/oauth-clients -->
<!-- 研读状态：已完成 -->

# Developer Console • Core concepts • Standalone OAuth clients (legacy) • Palantir

- 英文来源：[现行英文原文（Standalone OAuth clients，Legacy）](https://www.palantir.com/docs/foundry/developer-console/oauth-clients)
- 官方中文来源：[中文候选（旧 OSDK OAuth 页面，待人工复核）](https://www.palantir.com/docs/zh/foundry/ontology-sdk/oauth-clients)
- 页面语言：英文
- 主题栏目：developer-console
- 相关性：direct；OAuth 客户端生命周期、权限和迁移
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:05:05Z
- 产品状态：Standalone OAuth client 已进入 Legacy，不能新建；现有客户端可以迁入 Developer Console application

## 英文原文短摘录（不超过 25 词）

> “Standalone OAuth clients are now legacy and can no longer be created.”

## 摘录译文

Standalone OAuth 客户端现已属于 Legacy，不能再创建。

## 中文要点

- 当前文档建议新建 unrestricted custom application；Standalone OAuth client 作为旧式轻量授权原语，缺少应用限制、SDK 生成、托管、DevOps 和指标等能力。
- 现有客户端可用迁移向导转换成 Developer Console 应用，选择 location/最高分类并审查用户权限；迁移后旧工作流仍可使用原客户端。
- 管理现有 OAuth client 需要在其所属组织拥有 Manage OAuth 2.0 clients 权限；可编辑名称、描述、logo，或在 Danger zone 删除。
- OAuth & Permissions 页面管理客户端细节，也可以把应用共享给其他组织，让目标组织为自己的用户启用。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| standalone OAuth client | 独立 OAuth 客户端 | 仅提供授权能力的旧式应用资源 |
| custom application | 自定义应用 | 关联 OAuth、SDK、权限及可选托管的完整应用 |
| unrestricted | 不受限 | 不设置应用资源白名单上限的权限模式 |
| Manage OAuth 2.0 clients | 管理 OAuth 2.0 客户端 | 由所属组织控制的管理权限 |

## 疑问与待验证项

- 页面建议 unrestricted custom application，但不表示它自动获得用户或服务用户可访问的所有资源；仍需按权限和 scope 规则核验。
- 迁移保留已有客户端工作流，文档未逐项说明回调 URL、secret 和第三方依赖如何处置。
- 相邻中文页反映旧流程，需人工区分仍有效的管理步骤与已经停止的新建能力。

## 复刻启示

- OAuth 客户端资源应有 deprecated 状态、迁移流程、权限要求和兼容期限；禁止旧种类继续新建。
- 应用范围、用户授权、OAuth 操作 scope 和客户端访问配置分别展示并联合校验。
- 跨组织共享需要目标方启用，旧应用迁移应生成差异清单与审计事件。