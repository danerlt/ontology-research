<!-- 页面 URL：https://www.palantir.com/docs/foundry/developer-console/how-to-bootstrapping-java -->
<!-- 研读状态：已完成 -->

# Developer Console • How-to guides • Bootstrap a Java application • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/developer-console/how-to-bootstrapping-java)
- 官方中文来源：[OSDK Java 启动中文页](https://www.palantir.com/docs/zh/foundry/ontology-sdk/how-to-bootstrapping-java)（配对状态：ambiguous）
- 页面语言：英文
- 主题栏目：developer-console
- 相关性：direct；通过 Developer Console 创建 Java OSDK 客户端应用
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:05:11Z
- 产品状态：本页未标注 Preview；SDK 工具链要求需按最新指南复核

## 英文原文短摘录（每个来源不超过 25 词）

> “The Java OSDK requires a Java version between 17 and 21.”

## 摘录译文

Java OSDK 要求 Java 版本为 17 至 21。

## 中文要点

- 创建 Java OSDK 应用前，先在 Developer Console 新建应用并配置权限、选择应用将使用的本体对象类型；再为本地环境设置个人访问 token。
- `FOUNDRY_TOKEN` 只从环境变量读取，页面明确要求不要把 token 提交到源代码管理。使用 Gradle 或等价工具时，在依赖中配置应用专属 SDK Maven 仓库和 generator 仓库。
- 仓库 URL 与依赖包名是应用特定值，应从 Developer Console 的应用概览复制；不要在全局构建配置中硬编码共享凭证。
- 同名中文 OSDK 页面使用旧的 `ontology-sdk` 路由；英文页面当前位于 Developer Console，两者流程对应但须以英文当前版本为准。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Java OSDK | Java 本体 SDK | 供 Java 应用调用本体 API 的生成客户端 |
| Developer Console application | Developer Console 应用 | 授权、资源范围与 SDK 包来源的配置主体 |
| Generator repository | 生成器仓库 | 获取生成客户端依赖所需的 Maven 仓库 |
| Personal access token | 个人访问 token | 本地构建访问 Foundry 资源的凭证 |

## 疑问与待验证项

- 页面未说明 Java 22+ 的支持状态；不可只按本页把版本范围外推到新版本。
- 访问 Maven 仓库需要的用户名为空、密码放 `FOUNDRY_TOKEN` 的示例要结合组织 token 规范核验。
- Java OSDK 生成结果如何绑定本体 schema 修订和分支，需参考 SDK 生成与部署文档。

## 复刻启示

- SDK 包生成应与应用授权、项目/本体选择绑定，构建元数据记录 package、schema 版本和权限范围。
- 凭证以短期/受控 secret 注入 CI 和本地环境，禁止写入源代码；权限按所需对象类型和 API 操作收敛。
- 为本体管理系统提供 API/SDK 客户端时，避免把一个项目的 SDK 凭据复用于其他项目的本体。
