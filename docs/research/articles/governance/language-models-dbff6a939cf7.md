<!-- 页面 URL：https://www.palantir.com/docs/foundry/functions/language-models -->
<!-- 研读状态：已完成 -->

# Functions • Models • Language models in TypeScript v1 functions • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/functions/language-models)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/functions/language-models)（配对状态：matched）
- 页面语言：英文
- 主题栏目：functions
- 相关性：direct；本体函数文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:03:19Z
- 产品状态：AIP 能力可因客户而异；模型可能受 token 速率限制。

## 英文原文短摘录（每个来源不超过 25 词）

> Palantir provides a set of language models which can be used within functions.

## 摘录译文

Palantir 提供一组可在函数中使用的语言模型。

## 中文要点

- 本页针对 TypeScript v1 函数；使用前需租户启用 AIP 且当前用户具备 AIP Builder 权限。模型先导入函数仓库，再生成代码绑定供函数调用。
- 更新后的 TSv1 模型支持视觉与流式能力；文档同时给出生成式模型与 embedding 用例，embedding 可用于语义搜索流程。
- 模型可能有独立 token 速率限制，且叠加函数常规限制；AIP 能力可能因客户/租户而异。TSv1 页面建议新项目考虑迁移到 TSv2，以获得 OSDK 与可配置资源请求。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Model import | 模型导入 | 把可用模型加入代码仓库并生成可调用绑定。 |
| Embedding | 嵌入向量 | 将文本转换成向量，可用于语义检索。 |
| AIP Builder | AIP 构建权限 | 使用平台 AI 能力所需的权限前提之一。 |

## 疑问与待验证项

- 文档把模型可用性与速率限制留给租户/模型配置；具体可用模型、地区和配额必须在当前 enrollment 查看。
- 此页是 TSv1 路线的说明；升级前需核对仓库绑定/API 变化，不能直接假设代码兼容 TSv2。

## 复刻启示

- Agent/函数连接模型时应校验模型导入、租户能力开关、操作者权限和配额，并在运行记录中保存模型标识与版本。
- 将 embedding 与生成式调用作为不同能力类型；把模型调用纳入 trace，并避免写入完整敏感提示词。
