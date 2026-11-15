<!-- 页面 URL：https://www.palantir.com/docs/foundry/ontology/overview-semantic-search -->
<!-- 研读状态：已完成 -->

# Semantic search • Overview • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/ontology/overview-semantic-search)
- 官方中文来源：尚未确认（配对状态：ambiguous）
- 页面语言：英文
- 主题栏目：ontology
- 相关性：direct；本体模型与治理文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:03:45Z
- 产品状态：语义搜索概念页；所列模型和功能可用性随 enrollment 变化。

## 英文原文短摘录（每个来源不超过 25 词）

> “Semantic search is a way to search for text based on the inherent meaning or context.”

## 摘录译文

语义搜索依据文本内在含义或上下文进行检索。

## 中文要点

- 语义搜索把文本交给 AI 模型转换为向量（embedding），再通过向量距离寻找语义相近的文本。
- 当向量与 Ontology 对象关联后，搜索结果可进入业务工作流；其核心是向量近邻检索，不等同于本体关系推理或派生属性计算。
- 页面将 Palantir 模型、custom model、chunking 和 PDF 文档处理列为后续路线。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| embedding | 嵌入向量 | 由模型把文本映射成数值向量。 |
| nearest vector | 最近向量 | 向量空间中与查询向量最接近的记录。 |
| semantic search | 语义搜索 | 按意义相似度检索文本/对象。 |

## 疑问与待验证项

- 本概念页没有限定向量距离度量、索引更新时效或相似度阈值策略。
- 向量检索的相关性分数不能解释为确定的业务因果或对象关系。

## 复刻启示

- 画布分开呈现对象关系边与语义检索索引/向量边；查询路径显示命中的对象和原始证据。
- Agent 可调用语义检索工具取得上下文，但派生属性仍由确定性表达式和关系路径计算。
- 存储 embedding 所用模型、维度、数据版本和原对象 RID，以支持索引重建与审计。
