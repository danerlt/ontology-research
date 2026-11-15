<!-- 页面 URL：https://www.palantir.com/docs/foundry/developer-console/branching-integration -->
<!-- 研读状态：已完成 -->

# Developer Console • Core concepts • Branching Developer Console applications • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/developer-console/branching-integration)
- 官方中文来源：尚未确认（配对状态：needs_review）
- 页面语言：英文
- 主题栏目：developer-console
- 相关性：direct；开发者控制台与本体集成文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:05:05Z
- 产品状态：待核对 Beta、预览、弃用或更名信息

## 英文原文短摘录（每个来源不超过 25 词）

> “A global branch coordinates resources across Foundry; a Git branch alone does not establish that context.”

## 摘录译文

全局分支协调 Foundry 内的多类资源；单独创建 Git 分支并不会建立这一上下文。

## 中文要点

- Developer Console 应用的 Global Branching 把 Ontology 变更、SDK 资源、源代码和预览环境放在同一全局分支中；它不等同于本地 Git 分支。分支上测试 Action 前，所有会被编辑的对象类型都要完成索引。
- 修改分支 Ontology 资源后，在 Developer Console 更新 SDK 资源并在该分支生成新 SDK；代码库切换到同名分支，安装依赖以同步 SDK。分支 Action 的对象编辑不会合并到 `main`。
- 非默认分支不能移除应用限制，且项目、操作、标记和 OAuth 设置为只读；应用级限制对所有分支共享，所以在分支修改限制会影响默认分支。
- 提案生成代码拉取请求和分支预览；预览会读写该全局分支。合并提案本身不会发布生产站点，需在默认分支另行发布。
- Workshop 嵌入应用需满足严格条件才能继承分支上下文，例如双向 Iframe、`@osdk/client` 至少 `2.77.0`、OAuth `useHistory: false` 且客户端不覆盖分支。条件缺失时可能无提示地回落到 `main` 并写入主分支。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Global Branching | 全局分支 | 跨 Foundry Ontology、应用与代码资源协调的开发分支。 |
| branched SDK | 分支 SDK | 根据分支上的 Ontology 定义生成的类型绑定和客户端依赖。 |
| proposal preview | 提案预览 | 评审者可在合并前测试分支数据和应用的部署预览。 |
| branch context | 分支上下文 | 请求实际读取或写入的 Foundry 分支，需通过网络请求确认。 |

## 疑问与待验证项

- 本页的分支体验依赖应用模板、Vite、OSDK 客户端和代码库配置版本，不能抽象为任意 Git 工作流都自动具备的能力。
- 嵌入应用回落到 `main` 不一定会触发错误；评审流程应通过实际请求中的 branch RID 验证上下文。

## 复刻启示

- 复刻系统的分支需要覆盖 schema、SDK 快照、服务端计算配置和 UI 草稿；合并前在隔离分支试算派生属性与 Actions，并保留审阅记录。
- 分支预览需显示数据分支、SDK 版本和访问限制；嵌入式模块若无法继承上下文，应阻止危险写入或在界面明确提示，不能静默切回主分支。
