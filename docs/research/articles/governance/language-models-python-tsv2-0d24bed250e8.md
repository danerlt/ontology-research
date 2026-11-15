<!-- 页面 URL：https://www.palantir.com/docs/foundry/functions/language-models-python-tsv2 -->
<!-- 研读状态：已完成 -->

# Functions • Models • Language models in TypeScript v2 and Python functions • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/functions/language-models-python-tsv2)
- 官方中文来源：尚未确认（配对状态：needs_review）
- 页面语言：英文
- 主题栏目：functions
- 相关性：direct；本体函数文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:03:19Z
- 产品状态：需启用 AIP 且具备 AIP Builder 权限；模型可能受限流。

## 英文原文短摘录（每个来源不超过 25 词）

> Language models in TypeScript v2 and Python functions use proxy endpoints to interact with models.

## 摘录译文

TypeScript v2 和 Python 函数通过代理端点与模型交互。

## 中文要点

- 前提是租户启用 AIP、使用者具备 AIP Builder 权限，并把模型从 Platform SDK/resource imports 加入仓库；每个导入模型配置仓库内唯一别名。
- 函数通过平台代理端点调用模型，示例复用 OpenAI 兼容客户端与 Foundry token/base URL/HTTP client；第三方 `openai` 包并非预装依赖，需在仓库 Libraries 中安装。
- 与 TSv1 绑定模型的代码路径不同，TSv2/Python 以别名解析模型 RID，避免将 RID 写死在源代码。需按可用模型、速率限制及 API 状态逐环境校验。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Proxy endpoint | 代理端点 | 函数通过平台提供的服务端点访问模型。 |
| Platform SDK import | Platform SDK 导入 | 仓库中选择可用模型并生成资源绑定的配置。 |
| Model alias | 模型别名 | 仓库范围内唯一的名称，运行时解析到模型 RID。 |

## 疑问与待验证项

- 文档示例包含 API 与 SDK 依赖，当前模型提供方、端点能力及库版本要以目标租户文档和实际安装结果确认。
- 别名无法替代目标环境的模型可用性检查；Marketplace 安装时模型资源未部署会导致运行时解析失败。

## 复刻启示

- 设计模型连接器时以代理 endpoint、凭据提供器和环境化资源别名为边界；密钥不进入函数源码或资源导出包。
- 模型导入应做仓库唯一性检查、目标环境存在性预检和权限校验，并将模型调用结果挂接审计 trace。
