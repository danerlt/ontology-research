<!-- 页面 URL：https://www.palantir.com/docs/zh/foundry/ontology-sdk/oauth-clients -->
<!-- 研读状态：已完成 -->

# OSDK • OAuth 客户端 • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/developer-console/oauth-clients)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/ontology-sdk/oauth-clients)
- 页面语言：中文（官方机器翻译，准确性未验证）
- 主题栏目：ontology-sdk
- 相关性：direct；OAuth 应用身份、组织启用和迁移
- 官方更新时间：2026-11-12T17:46:46.932Z
- 目录核对时间：2026-11-14T15:00:52Z
- 产品状态：Standalone OAuth clients 已标记 Legacy，当前不能新建；新集成推荐迁移到自定义应用

## 英文原文短摘录（不超过 25 词）

> “Standalone OAuth clients are now legacy and can no longer be created.”

## 摘录译文

独立 OAuth 客户端现已属于 Legacy，不能再创建。

## 中文要点

- 中文旧页介绍 OAuth 客户端的管理、OAuth & Permissions 设置、显示信息编辑、删除和跨组织共享；它反映的是旧版控制台流程。
- 当前英文页将 standalone OAuth client 标记为 Legacy：不能新建，建议新集成使用 unrestricted custom application。
- 迁移向导将现有客户端转换为 Developer Console application，可获得 Ontology/Platform SDK、网站托管、应用限制、DevOps 和指标能力；迁移时选择 location/最高分类并检查用户权限。
- 迁移后已有工作流继续使用原 client；管理现存客户端需拥有其所属组织的 Manage OAuth 2.0 clients 权限。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| standalone OAuth client | 独立 OAuth 客户端 | 仅含授权客户端、能力较少的旧式应用原语 |
| unrestricted custom application | 不受限自定义应用 | Developer Console 新应用类型；不配置资源限制 |
| migration wizard | 迁移向导 | 将旧客户端迁入 Developer Console 应用的流程 |
| owning organization | 所属组织 | 决定谁可管理 OAuth 客户端的组织边界 |

## 疑问与待验证项

- 当前页面建议使用 unrestricted custom application；其访问范围与 restricted application 的差异应结合应用限制和权限卡理解。
- 旧中文文档描述的创建步骤已过时，应以 Legacy 状态页为准；现有客户端可继续运行不代表仍能新建。
- 文档说明迁移后已有工作流不受影响，但未覆盖各类回调 URI、密钥轮换和外部集成的逐项验证计划。

## 复刻启示

- 旧客户端需显示清楚的生命周期状态、停建提示、迁移向导和迁移前后权限差异。
- 新建 OAuth 应用时同时配置回调地址、资源最大范围、应用/用户权限及密钥轮换策略，并记录审计。
- 跨组织共享、目标组织启用与最终资源授权拆分为可追踪状态，不以一次分享操作替代全部授权。