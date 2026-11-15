<!-- 页面 URL：https://www.palantir.com/docs/foundry/functions/python-functions-local-development -->
<!-- 研读状态：已完成 -->

# Functions • Python • Local development • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/functions/python-functions-local-development)
- 官方中文来源：尚未确认（配对状态：ambiguous）
- 页面语言：英文
- 主题栏目：functions
- 相关性：direct；本体函数文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:03:00Z
- 产品状态：页面未标注 Beta；本地环境需匹配最新仓库模板和 Java 21 要求。

## 英文原文短摘录（每个来源不超过 25 词）

> “You can carry out local development of Python functions repositories, allowing for high-speed iteration in your customized environment.”

## 摘录译文

可以在本地开发 Python 函数仓库，以便在自定义环境中快速迭代。

## 中文要点

- 使用仓库 Work locally 地址 clone；clone token 短时有效且只读（允许 push 回原仓库）。要发布 artifacts、运行 checks 或 build，仍需将修改推回 Foundry。
- 环境需安装 Java 21、升级到最新模板，并确保 `CI`、`JEMMA`、`CA` 环境变量未设置；Apple Silicon 另需 Rosetta 2。
- VS Code 可运行 `./gradlew vsCode` 生成解释器配置；PyCharm 可运行 `./gradlew condaDevelop` 创建环境。
- 该页是本地仓库环境说明，不保证本地环境与 Foundry 预览/生产的权限、凭据或运行时完全一致。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Work locally | 本地开发入口 | 生成本地克隆用仓库地址的入口。 |
| read-only token | 只读令牌 | 短时仓库访问令牌，允许回推原仓库。 |
| repository template | 仓库模板 | 包含构建脚本和本地配置的仓库基础结构。 |

## 疑问与待验证项

- 仓库模板版本过旧会导致 Gradle 插件/任务错误；本地配置步骤需与模板同步更新。
- 预览与本地开发的身份和对象权限是否一致，需要单独验证。

## 复刻启示

- 区分本地迭代、服务端预览、发布检查和生产部署的授权上下文。
- 本地通过后仍在服务端校验 schema、依赖、权限和运行资源后才允许发布。
