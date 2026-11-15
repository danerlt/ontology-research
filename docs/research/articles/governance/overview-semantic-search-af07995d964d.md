<!-- 页面 URL：https://www.palantir.com/docs/zh/foundry/functions/overview-semantic-search -->
<!-- 研读状态：已完成 -->

# 函数 • Semantic search • 概述 • Palantir

- 英文来源：[现行英文原文](https://www.palantir.com/docs/foundry/ontology/overview-semantic-search)
- 官方中文来源：[官方中文页（AIP 机器翻译，准确性未独立验证）](https://www.palantir.com/docs/zh/foundry/functions/overview-semantic-search)
- 页面语言：中文（官方 AIP 机器翻译，需与英文原文交叉核对）
- 主题栏目：functions
- 相关性：direct；本体函数文档
- 官方更新时间：2026-11-12T17:46:46.935Z
- 目录核对时间：2026-11-14T14:59:26Z
- 产品状态：目录中的 Functions 旧中文路由已迁移至 Ontology 下的语义搜索概览；页面讲述 embedding、向量相似度和关联 Ontology 对象的检索工作流。

## 原文短摘录与翻译

> “Semantic search is a way to search for text based on the inherent meaning or context, rather than relying solely on keywords.”

## 摘录译文

语义搜索依据文本内在含义或上下文检索，而不只依赖关键词。

## 中文要点

- 语义搜索由模型把文本转换为 embedding 向量，再按向量空间的相近程度检索语义相似内容；结果可关联 Ontology 实体供业务流程使用。
- 文档导航把该概览与模型选择、PDF 处理、分块、Palantir 提供模型及自定义模型的工作流串联。
- 该能力处理文本语义召回；Ontology 链接遍历是确定性关系查询，不能把向量相似度误作关系推理。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| embedding | 嵌入向量 | 模型将文本语义映射成的数值向量 |
| nearest-neighbor search | 近邻搜索 | 按向量相似度取回相关文本或对象 |
| semantic search | 语义搜索 | 按含义而非仅按关键词匹配文本 |

## 疑问与待验证项

- 目录中的旧路由会重定向到 `/foundry/ontology/overview-semantic-search`；该重定向与英文 canonical 页一致，中文版术语和示例是否同步需继续校验。
- 本页只给概念和关联文档，向量维度、距离函数、索引刷新和召回分数阈值需看具体模型/工作流配置。
- 若把 embedding 搜索接入 Agent，应保存命中 chunk、原始对象引用与模型/索引版本，避免回答只留下无来源文本。

## 复刻启示

- 将语义检索结果作为 Agent 候选上下文，并保留每个 chunk 对应的对象 ID、原文位置和检索分数；回答需附可追溯引用。
- 本体规则推理与向量召回在 UI 和 API 中拆成不同步骤，可组合排序但不可混淆确定性和概率性结果。
- 实现先提供关键词/语义基础检索，再用命中分析决定是否增加混合检索、查询扩展或 HyDE。
