<!-- 页面 URL：https://www.palantir.com/docs/foundry/functions/language-models-legacy -->
<!-- 研读状态：已完成 -->

# Functions • Models • Legacy language models in functions • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/functions/language-models-legacy)
- 官方中文来源：尚未确认（配对状态：ambiguous）
- 页面语言：英文
- 主题栏目：functions
- 相关性：direct；本体函数文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:03:20Z
- 产品状态：页面明确标为 Legacy；AIP 能力可因客户而异。

## 英文原文短摘录（每个来源不超过 25 词）

> This page documents legacy language models within functions.

## 摘录译文

本页介绍函数中的旧版语言模型。

## 中文要点

- 页面显式标注 Legacy，并建议 TSv2/Python 使用代理端点与模型别名路线；TSv1 更新版模型提供视觉和流式等能力，旧仓库应按迁移步骤升级。
- 使用 Palantir 托管语言模型前，需启用 AIP 并获得 AIP Builder 权限；模型通过资源导入加入仓库。
- 旧版路径仍记录 embedding 和限流信息，但页面说明新旧接口代码语法可能不同，升级会引发编译期修改，必须按当前模型代码片段改写。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Legacy | 旧版/遗留 | 文档标记该调用方式属于旧路径，需与现行能力区分。 |
| Model import | 模型导入 | 将模型选择和绑定加入函数代码仓库。 |
| Rate limit | 速率限制 | 模型按一定时间窗口约束 token 调用量。 |

## 疑问与待验证项

- 文档未在此页给出统一的移除期限；需要追踪发布说明并盘点仓库中是否仍有 legacy imports。
- TSv1 现行模型、Legacy 模型及 TSv2/Python 代理端点的功能差异需以对应专页和目标租户实测为准。

## 复刻启示

- 对模型连接器/调用模式标注生命周期状态和迁移目标；旧接口可运行但应展示弃用提示、迁移指南和依赖影响。
- 发布前检查模型绑定、权限与调用配额；迁移流程应保留版本差异并能在分支中编译/试跑。
