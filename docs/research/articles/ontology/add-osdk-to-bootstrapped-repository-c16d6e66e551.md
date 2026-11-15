<!-- 页面 URL：https://www.palantir.com/docs/foundry/ontology-sdk/add-osdk-to-bootstrapped-repository -->
<!-- 研读状态：已完成 -->

# Ontology SDK • TypeScript • Add an OSDK to a bootstrapped repository • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/ontology-sdk/add-osdk-to-bootstrapped-repository)
- 官方中文来源：尚未确认；近似页面候选需人工判断
- 页面语言：英文
- 主题栏目：ontology-sdk
- 相关性：direct；Ontology SDK 文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:04:43Z
- 产品状态：待核对 Beta、预览、弃用或更名信息

## 英文原文短摘录（每个来源不超过 25 词）

> “This guide explains how to add an OSDK to a repository that was originally bootstrapped without one.”

## 摘录译文

本指南介绍如何为最初未包含 OSDK 的代码库补入本体 SDK。

## 中文要点

- 本指南针对已从 Developer Console 或 `@osdk/create-app` 启动、但起初未接入 OSDK 的 TypeScript 仓库；自定义脚手架可能需要调整步骤。
- 页面要求在 `index.html` meta tag 和环境变量中配置 Ontology RID，并在客户端从 meta tag 读取 RID 后用 `createClient(foundryUrl, ontologyRid, auth)` 初始化。
- 需把应用对应的 SDK package 加入 `package.json`；本地启动的仓库还要在 `.npmrc` 配置 Foundry registry 并通过 `FOUNDRY_TOKEN` 鉴权。Foundry 托管仓库跳过本地 registry 配置。
- 常见安装 401/403/404 与 token 环境变量、NPM registry 覆盖或 `.npmrc` 包名配置错误有关；不要将个人 token 提交进版本控制。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| bootstrapped repository | 已脚手架化仓库 | 已创建基础应用但未集成本体 SDK 的项目。 |
| Ontology RID | 本体 RID | 创建客户端时用于选择目标 Ontology 的资源标识。 |
| `FOUNDRY_TOKEN` | Foundry 访问令牌 | 本地 npm 注册表认证使用的环境变量。 |
| `.npmrc` | npm 配置文件 | 指向应用专属 SDK registry 并配置认证。 |

## 疑问与待验证项

- 本指南假设仓库采用官方脚手架；它没有覆盖其他 bundler 的环境变量展开与 meta tag 注入方式。
- SDK package 依赖写为 `latest` 的示例适合入门，但团队发布时仍需确定版本锁定和更新策略。

## 复刻启示

- 前端在运行时显式绑定 Ontology RID，应用配置应分别管理项目环境、RID、SDK 版本和 OAuth 客户端，避免跨环境串接本体。
- 将 schema 变更与 SDK 重新生成关联，并对浏览器可见配置与私密令牌分离；Agent 工具也须绑定明确的本体资源范围。
