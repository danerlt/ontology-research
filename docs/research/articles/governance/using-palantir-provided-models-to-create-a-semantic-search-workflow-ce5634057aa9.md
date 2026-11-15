<!-- 页面 URL：https://www.palantir.com/docs/zh/foundry/functions/using-palantir-provided-models-to-create-a-semantic-search-workflow -->
<!-- 研读状态：已完成 -->

# 函数 • Semantic search • 使用Palantir提供的模型创建语义搜索工作流 • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/ontology/using-palantir-provided-models-to-create-a-semantic-search-workflow)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/functions/using-palantir-provided-models-to-create-a-semantic-search-workflow)
- 页面语言：中文（官方 AIP 机器翻译，需与英文原文交叉核对）
- 主题栏目：functions
- 相关性：direct；本体函数文档
- 官方更新时间：2026-11-12T17:46:46.935Z
- 目录核对时间：2026-11-14T14:59:49Z
- 产品状态：旧中文路由已迁移到 Ontology 语义搜索工作流；使用 Palantir 提供的 embedding 模型生成对象 Vector 属性，再以 KNN 检索；AIP enrollment 与开发权限是前提。

## 英文原文短摘录（每个来源不超过 25 词）

> “To use Palantir-provided language models, AIP must first be enabled on your enrollment.”

## 摘录译文

使用 Palantir 提供的语言模型前，必须先在 enrollment 中启用 AIP。

## 中文要点

- 先用 Pipeline Builder 将文本生成 embedding 并保存到 Ontology 对象的 Vector 属性，再在 Workshop、AIP Chatbot 或函数中查询。
- 无代码 Workshop KNN 对象集适合快速起步，但文档注明它不支持按相关性排序；需要排序时使用支持 relevance 的函数方式。
- TSv1 需将查询文本单独嵌入再做 nearest-neighbor 搜索，K 最大 100；TSv2 可直接传文本并请求 relevance 排序，K 最大 500。
- Python `nearest_neighbors` 可直接接受文本，但文档标为 Beta，且没有说明等价的相关性排序接口；AIP Chatbot 可通过本体上下文或语义搜索工具接入。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| KNN (k-nearest neighbors) | K 近邻 | 按向量相似度寻找最近邻对象的检索方式 |
| Vector property | 向量属性 | 存储文本/对象 embedding 的本体属性类型 |
| embedding | 嵌入向量 | 模型从文本生成、用于语义相似度比较的数值向量 |
| relevance ordering | 相关性排序 | 按检索相关度从高到低排序结果 |

## 疑问与待验证项

- TSv1、TSv2 与 Python 对查询 embedding、排序和邻居数量上限差异明显；单一的跨语言实现会掩盖能力差异。
- 页面中 TSv1 `functions.json` 的 `enableVectorProperties` 设置没有文档化的 TSv2/Python 等价项；若这些语言查询失败，需要针对具体租户核验。
- AIP enrollment、开发权限、模型可用名单及向量维度/相似度函数都受部署环境限制。

## 复刻启示

- 将语义检索设计为独立 Agent 工具：记录 embedding 模型、向量字段、相似度函数、查询数值与召回对象，后续由只读 Query 将证据传给 LLM。
- UI 清晰区分“未排序 KNN 集合”与“按相关性排序的函数检索”；推理轨迹显示 K 值、结果分数和来源对象。
- 能力矩阵按语言版本配置 K 上限、文本/向量输入方式、排序能力与 Beta 标记，不以统一 SDK 类型掩盖差别。
