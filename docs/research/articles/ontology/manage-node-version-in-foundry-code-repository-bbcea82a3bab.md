<!-- 页面 URL：https://www.palantir.com/docs/foundry/developer-console/manage-node-version-in-foundry-code-repository -->
<!-- 研读状态：已完成 -->

# Developer Console • How-to guides • Manage Node.js version in a Foundry code repository • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/developer-console/manage-node-version-in-foundry-code-repository)
- 官方中文来源：尚未发现直接对应页面（目录配对状态：missing）
- 页面语言：英文
- 主题栏目：developer-console
- 相关性：direct；OSDK 应用开发环境与 CI 运行时一致性
- 官方更新时间：未提供（页面当前示例含 Node.js v24.13.0）
- 目录核对时间：2026-11-14T15:05:15Z
- 产品状态：Code Repositories 使用 nvm；未配置 nvm 时开发环境和 CI 的默认值来源不同

## 英文原文短摘录（不超过 25 词）

> “Foundry code repositories support Node Version Manager (nvm) to manage the Node.js version used in your project and CI.”

## 摘录译文

Foundry 代码仓库支持用 Node Version Manager（nvm）管理项目和 CI 使用的 Node.js 版本。

## 中文要点

- 在仓库根目录放置 `.nvmrc`，以 `v` 前缀声明项目 Node.js 版本；可通过仓库终端的 `nvm ls-remote` 查看可用版本。
- 在终端执行 `nvm install` 安装并切换到配置版本。
- CI 是否使用相同版本还需编辑 `.jemma/settings.sh`，让 `NODE_INSTALLATION_VERSION` 从 `.nvmrc` 读取。
- 若不使用 nvm，文档写明 CI 采用 `.jemma/settings.sh` 配置，而 Foundry 开发环境采用 18.20.8；因此默认配置可能造成开发与 CI 运行时分歧。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Node Version Manager (nvm) | Node 版本管理器 | 选择并安装指定 Node.js 运行时 |
| `.nvmrc` | nvm 版本文件 | 仓库内统一声明 Node.js 版本 |
| CI | 持续集成 | 自动构建时使用的运行时环境 |
| `NODE_INSTALLATION_VERSION` | Node 安装版本配置 | Foundry CI 安装 Node.js 时读取的值 |

## 疑问与待验证项

- 页面示例的 v24.13.0 和默认 18.20.8 是文档核验时的值，不应固化为长期推荐版本。
- 文档要求在 CI 配置中读取 `.nvmrc`；需要在每种仓库模板和构建镜像上确认 nvm 实际安装行为。
- 若 Node 版本升级，原生依赖、锁文件和打包输出可能改变，需让版本变更走代码评审。

## 复刻启示

- 前端项目模板应把 Node 版本写入仓库并让本地、工作区和 CI 使用同一配置，发布记录关联运行时版本。
- 工作台显示检测到的版本差异，并提供一致性错误提示，避免同代码不同运行环境。
- 不在产品代码中硬编码平台当前默认版本；运行时支持范围作为可更新环境配置维护。