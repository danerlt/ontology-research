<!-- 页面 URL：https://www.palantir.com/docs/foundry/developer-console/how-to-bootstrapping-python -->
<!-- 研读状态：已完成 -->

# Developer Console • How-to guides • Bootstrap a Python application • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/developer-console/how-to-bootstrapping-python)
- 官方中文来源：[中文候选（同主题多页，目录配对为 ambiguous）](https://www.palantir.com/docs/zh/foundry/ontology-sdk/how-to-bootstrapping-python)
- 页面语言：英文
- 主题栏目：developer-console
- 相关性：direct；Python OSDK 应用初始化与包安装
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:05:11Z
- 产品状态：Developer Console 现行启动指南；安全示例把个人 token 放在环境变量

## 英文原文短摘录（不超过 25 词）

> “Run the following command to install the latest version of the SDK”

## 摘录译文

运行以下命令安装 SDK 的最新版本。

## 中文要点

- 先创建 Developer Console 应用；从应用的 Getting started 页面取得生成 SDK 包所需的应用专属名称、包索引 URL 等值。
- 本地设置 `FOUNDRY_TOKEN` 后，通过 pip 使用额外索引安装生成的 SDK；指南示例使用个人访问令牌，因此明确不要把 token 提交到源代码仓库。
- 初始化时以生成包中的 `FoundryClient` 配合 `UserTokenAuth`，从环境读取 token 和 Foundry 主机名，再调用生成客户端访问对象类型。
- 若 pip 出现证书验证错误，先通过 `SSL_CERT_FILE`、`REQUESTS_CA_BUNDLE` 配齐证书链；`--trusted-host` 只用于一次性定位问题，之后必须移除。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| SDK package index | SDK 包索引 | 提供应用专属 Python SDK 制品的私有索引 |
| extra index URL | 额外索引 URL | pip 默认源之外查询生成包的地址 |
| `UserTokenAuth` | 用户令牌认证 | 以当前开发者的个人令牌访问 Foundry |
| certificate authority (CA) | 证书颁发机构 | TLS 服务端证书信任链的根与中间证书 |

## 疑问与待验证项

- 同主题中文候选存在 Python、TypeScript、Java 和服务端 TypeScript 多篇，不能仅按 slug 相似断定目录一对一。
- 个人 PAT 用于开发启动示例；生产后端应转用服务身份/机密客户端，不应长期复用开发者凭据。
- SDK 的 Python 版本兼容矩阵、生成包版本与离线安装方式需查 Python SDK 主参考页。

## 复刻启示

- 应用初始化页按应用生成带参数的安装命令，同时显示 SDK 版本、包源、所选本体和可用对象/Action。
- 凭据使用用户环境变量或安全密钥存储，启动文档、日志和命令历史均避免泄漏 token。
- 证书问题要引导补齐 CA 信任链，不把关闭 TLS 校验作为解决方案。