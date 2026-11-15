<!-- 页面 URL：https://www.palantir.com/docs/zh/foundry/ontology-sdk/how-to-bootstrapping-java -->
<!-- 研读状态：已完成 -->

# OSDK • 引导启动一个新的 Ontology SDK (OSDK) Java 应用程序 • Palantir

- 英文原文：[英文对应页](https://www.palantir.com/docs/foundry/developer-console/how-to-bootstrapping-java)
- 官方中文来源：[中文页面](https://www.palantir.com/docs/zh/foundry/ontology-sdk/how-to-bootstrapping-java)
- 页面语言：中文（官方机器翻译，准确性未验证）
- 主题栏目：ontology-sdk
- 相关性：direct；Java OSDK 启动指南的中文路由
- 官方更新时间：2026-11-12T17:46:46.932Z
- 目录核对时间：2026-11-14T15:00:48Z
- 产品状态：页面未标注 Preview；Java OSDK 要求版本范围需按当前指南复核

## 英文原文短摘录（每个来源不超过 25 词）

> “Do not check this token into source control, as this can create a security vulnerability.”

## 摘录译文

不要将该 token 提交到源代码管理中，否则可能造成安全漏洞。

## 中文要点

- 中文指南要求先创建 Developer Console 应用，配置权限并选择 Java OSDK 将使用的对象；随后在本地环境设置个人访问 token。
- 个人 token 用于本地访问 Foundry 资源，不应写入 Git。安装 SDK 需配置应用专属和 generator Maven 仓库，使用 `FOUNDRY_TOKEN` 环境变量作为仓库密码。
- 文档要求 Java 17–21；仓库 URL 与依赖坐标应从当前应用概览页取得。
- 页面明确提示正文机器翻译准确性未验证；本卡通过链接映射到当前英文 Developer Console 版本。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| OSDK | Ontology SDK / 本体 SDK | 生成式本体 API 客户端 |
| Personal access token | 个人访问 token | 用于本地 SDK 仓库和资源认证的凭证 |
| Maven repository | Maven 仓库 | 获取应用专属 OSDK 包的位置 |
| Environment variable | 环境变量 | 本地注入 `FOUNDRY_TOKEN` 的方式 |

## 疑问与待验证项

- 中文路由虽有英文迁移对应，但目录登记为配对状态 not_applicable；应用到新页面的链接关系仍需后续核实。
- Java 版本要求可能随 SDK 版本更新变化；新项目应以 Java OSDK 官方当前页面为准。
- 个人 token 是否适合所有 CI/生产场景，指南只用于本地启动示例，生产授权需另行设计。

## 复刻启示

- 用应用专属权限和依赖包绑定项目/本体，生成客户端不应被视为跨项目通用凭证。
- token 经 secret store 注入构建环境，提供过期、轮换和泄漏撤销流程；CI 日志需要遮蔽凭证。
- 将本体 schema 与生成 SDK 版本一起登记，避免客户端类型定义和当前分支 schema 不一致。
