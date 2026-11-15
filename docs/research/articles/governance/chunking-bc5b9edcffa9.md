<!-- 页面 URL：https://www.palantir.com/docs/zh/foundry/functions/chunking -->
<!-- 研读状态：已完成 -->

# 函数 • Semantic search • 分块 • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/ontology/document-processing)
- 官方中文来源：尚未确认（配对状态：not_applicable）
- 页面语言：中文
- 主题栏目：functions
- 相关性：direct；本体函数文档
- 官方更新时间：2026-11-12T17:46:46.935Z
- 目录核对时间：2026-11-14T14:58:53Z
- 产品状态：官方中文页标注为未经验证的 AIP 机器翻译；英文原文为核对依据。

## 原文短摘录与翻译

> 英文原文：Chunking, in this context, means breaking up larger pieces of text into smaller pieces of text.

> 中文译文：此处的分块，是将较大的文本拆成较小文本片段。

## 摘录译文

以上为英文短摘录及中文译文。官方中文页面为 AIP 机器翻译，准确性未经验证。

## 中文要点

- 分块为 embedding 和语义检索控制输入长度、增加片段语义区分度；每个文本 chunk 需要保留与原始对象/文档的关联，以便搜索后返回可信源。
- 基础流程可在 Pipeline Builder 以文本抽取、Chunk String 和对象引用构建；较复杂策略可放入代码仓库作为管道步骤。
- 文档示例约 256 字符块长，并可按优先级分隔符逐级切分，给连续块保留 20 字符重叠；数值是示例参数，不是强制规范。
- 英文旧 `/functions/chunking` 路由重定向到 `/ontology/document-processing`；卡片引用现行页面。中文翻译标注为未经验证的 AIP 机器翻译。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Chunking | 分块 | 将长文档拆为较短、可单独嵌入/检索的文本片段。 |
| Embedding | 嵌入向量 | 用于语义相似检索的数值表示。 |
| Overlap | 重叠 | 相邻文本块重复保留的上下文内容。 |

## 疑问与待验证项

- 块长/重叠应按模型 token 限制、语种、文档结构和检索评估调节；字符长度不等于 token 数。
- chunk 删除或重切后旧 embedding 的撤销、版本关联和来源定位需要在索引管道中定义。

## 复刻启示

- 检索数据模型保存原文对象 RID、页码/范围、块序号、分块策略版本与 embedding 模型版本。
- 本体/Agent 返回证据时附原文位置和对象引用，让使用者可回到文档核对。
