<!-- 页面 URL：https://www.palantir.com/docs/zh/foundry/ontology-sdk-react-applications/development -->
<!-- 研读状态：已完成 -->

# 本体SDK React应用 • 开发环境 • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/ontology-sdk-react-applications/development)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/ontology-sdk-react-applications/development)
- 页面语言：中文（官方机器翻译，准确性未验证）
- 主题栏目：ontology-sdk-react-applications
- 相关性：direct；OSDK React 应用的开发、预览与部署
- 官方更新时间：2026-11-12T17:46:46.930Z
- 目录核对时间：2026-11-14T15:00:41Z
- 产品状态：PR 预览为 Beta；仅覆盖通过 Foundry Code Repositories 和 Developer Console Web Hosting 托管的 OSDK React 应用

## 英文原文短摘录（不超过 25 词）

> “The repository template will include a basic React application integrated with authorization and the Ontology SDK.”

## 摘录译文

代码仓库模板包含一个集成授权能力和 Ontology SDK 的基础 React 应用。

## 中文要点

- 开发入口是 Developer Console 中的 client-facing application；从应用创建代码仓库后，默认模板提供 React、授权和 OSDK 接入，并可在平台内 VS Code 工作区编辑、实时预览。
- 文档把编辑、提交推送、带标签发布、检查通过后显示托管应用串成一个生命周期；Ontology 面板提供生成 SDK 的文档和代码片段。
- 默认 CSP 限制非 Foundry URI；在工作区做的临时 CSP 只对当前用户生效，工作区暂停或重启后失效，验证后还需更新应用级策略。
- PR 预览仅适用于符合托管条件的 OSDK React 应用，预览 7 天后过期；Owner/Editor 管理变更，Viewer 可通过托管站点权限查看。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| client-facing application | 面向客户端的应用 | Developer Console 中允许创建代码仓库的应用类型 |
| Code Repositories | 代码仓库 | 连接应用代码、分支、提交和发布流程 |
| Content Security Policy (CSP) | 内容安全策略 | 限制前端可访问的 URI |
| PR preview | 拉取请求预览 | 合并前查看应用变更的临时托管版本 |

## 疑问与待验证项

- 文档将 PR 预览标为 Beta，且限定于特定仓库与托管组合；其他应用形态不能据此推断也有预览能力。
- 工作区 CSP 与应用 CSP 是两处配置，具体允许源的语法和生产校验规则需结合托管配置页核对。
- 预览过期时间为文档当前值，平台后续可能调整。

## 复刻启示

- 将应用构建关联到代码仓库、分支、提交、发布标签和托管状态；为分支提供可过期预览，并单独配置查看者权限。
- 本体资源变更和前端代码发布应使用同一变更提案关联，但分别呈现各自检查结果。
- CSP 使用默认拒绝策略，预览和生产配置分离；工作区临时放行不可自动提升到生产。