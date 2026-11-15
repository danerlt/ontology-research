<!-- 页面 URL：https://www.palantir.com/docs/zh/foundry/functions/language-models -->
<!-- 研读状态：已完成 -->

# 函数 • 函数中的语言模型 • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/functions/language-models)
- 官方中文来源：尚未确认（配对状态：not_applicable）
- 页面语言：中文
- 主题栏目：functions
- 相关性：direct；本体函数文档
- 官方更新时间：2026-11-12T17:46:46.935Z
- 目录核对时间：2026-11-14T14:59:26Z
- 产品状态：官方中文页标注为未经验证的 AIP 机器翻译；英文原文为核对依据。

## 原文短摘录与翻译

> 英文原文：To use Palantir-provided language models, ensure that AIP is enabled on your enrollment.

> 中文译文：要使用 Palantir 提供的语言模型，需确认 enrollment 已启用 AIP。

## 摘录译文

以上为英文短摘录及中文译文。官方中文页面为 AIP 机器翻译，准确性未经验证。

## 中文要点

- 这是 TypeScript v1 函数专属调用路线；需要 AIP enrollment 能力与 AIP Builder 权限，先把具体模型导入仓库再使用生成的强类型接口。
- 模型 API 能力可能包含对话、视觉、流式响应和 embeddings；用 `@Uses` 声明模型方法，平台静态扫描未识别的调用可能导致发布运行错误。
- 页面建议新实现迁移 TSv2 或 Python；后两者使用代理端点和模型别名，不是此页的 TSv1 绑定机制。模型还可能受 token 速率限制。
- 官方中文页是未经验证的 AIP 机器翻译；功能可用性可能因客户 enrollment 而异。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| AIP Builder | AIP 构建权限 | 访问平台模型能力所需的授权能力。 |
| Uses decorator | Uses 装饰器 | 声明 TSv1 函数使用的模型方法或其他查询依赖。 |
| Embedding | 嵌入向量 | 语义检索使用的模型输出向量。 |

## 疑问与待验证项

- TSv1 与代理路线支持的模型、视觉/流式响应 schema 和费用/限流政策必须按 enrollment 确认。
- 静态扫描未覆盖的间接调用需要 `@Uses` 显式声明；代码审查应核对运行依赖而非只看源码直接调用。

## 复刻启示

- Agent/LLM 模型调用应记录运行时、模型版本、方法能力、权限和 token 限额；不同 SDK 接入作为明确 adapter。
- 模型 import/schema 绑定在分支和发布版本间固定，减少环境切换时模型 API 漂移。
