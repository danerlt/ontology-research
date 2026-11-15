<!-- 页面 URL：https://www.palantir.com/docs/zh/foundry/ontology-sdk/how-to-bootstrapping-python -->
<!-- 研读状态：已完成 -->

# OSDK • 启动一个新的Ontology SDK Python应用程序 • Palantir

- 英文来源：[现行英文原文](https://www.palantir.com/docs/foundry/developer-console/how-to-bootstrapping-python)
- 官方中文来源：[官方中文页（AIP 机器翻译）](https://www.palantir.com/docs/zh/foundry/ontology-sdk/how-to-bootstrapping-python)
- 页面语言：中文（官方机器翻译，准确性未验证）
- 主题栏目：ontology-sdk
- 相关性：direct；Python OSDK 应用启动与身份验证
- 官方更新时间：2026-11-12T17:46:46.932Z
- 目录核对时间：2026-11-14T15:00:48Z
- 产品状态：Developer Console 下的 Python OSDK 启动指南；旧中文路由仍可访问

## 英文原文短摘录（不超过 25 词）

> “This token should not be checked into source control because it is your personal access token.”

## 摘录译文

此 token 是个人访问令牌，不应提交到源代码仓库。

## 中文要点

- 现行英文指南已迁到 Developer Console 栏目，目标是从应用专属包仓库安装 SDK，并在 Python 项目里初始化 Foundry 客户端。
- 开发者需先创建 Developer Console 应用并从 Getting started 获取包名、索引地址等应用专属信息；个人 token 通过环境变量提供。
- 安装示例以 `pip install` 配合应用专属 extra index；初始化示例使用 `FoundryClient` 和 `UserTokenAuth`，从环境变量读取 token，再访问生成客户端上的本体对象集。
- 文档补充证书错误排查：优先修正 CA 信任链；`--trusted-host` 仅用于临时确认诊断，不应进入生产或自动化命令。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| application-specific package registry | 应用专属包注册表 | 存放按 Developer Console 应用生成的 SDK 包 |
| extra index URL | 额外索引地址 | pip 除默认索引外查询 SDK 的私有索引 |
| personal access token | 个人访问令牌 | 用于本地获取 SDK/访问 Foundry 的开发者凭据 |
| CA trust configuration | CA 信任配置 | HTTPS 证书链验证所需的根/中间证书配置 |

## 疑问与待验证项

- 页面代码示例使用用户 token；这与后端服务的 confidential client/service user 流程不同，不能共享同一凭据模型。
- Python SDK 版本和生成包名由应用配置决定；应查相邻 Python SDK 参考页确认生成器与运行时支持矩阵。
- 文档提到用 `--trusted-host` 作诊断，但未列出所有网络代理场景的安全处置；生产端应以修复信任链为准。

## 复刻启示

- 为每个应用记录 SDK 生成版本、私有索引、所选本体和资源范围，启动命令从应用元数据生成。
- 凭据通过受保护的环境/密钥存储注入，卡片或仓库中只保留变量名，不保留 token 值。
- 认证类型应明确区分个人开发身份与服务身份，权限检查在服务端执行。