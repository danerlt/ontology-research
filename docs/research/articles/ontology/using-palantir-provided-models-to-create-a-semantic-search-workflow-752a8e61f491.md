<!-- 页面 URL：https://www.palantir.com/docs/foundry/ontology/using-palantir-provided-models-to-create-a-semantic-search-workflow -->
<!-- 研读状态：已完成 -->

# Semantic search • Use Palantir-provided models to create a semantic search workflow • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/ontology/using-palantir-provided-models-to-create-a-semantic-search-workflow)
- 官方中文来源：尚未确认（配对状态：ambiguous）
- 页面语言：英文
- 主题栏目：ontology
- 相关性：direct；本体模型与治理文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:04:03Z
- 产品状态：官方 embedding 模型语义搜索流程；AIP 权限和模型可用性受 enrollment 控制。

## 英文原文短摘录（每个来源不超过 25 词）

> “To begin, you need to generate embeddings and store them in an object type with a `vector` type.”

## 摘录译文

首先需要生成 embeddings，并将其存入具有 `vector` 类型属性的对象类型中。

## 中文要点

- 官方模型路线将文本生成 embeddings 并写入 Ontology vector 属性，再选 Workshop KNN Object Set、AIP Chatbot Ontology Search，或 Functions/AIP Logic 实现。
- Workshop KNN Object Set 无代码且 K 值为 1–100，但结果不能按相关性排序；需要排序时走 Function。TS v1、TS v2、Python 的 nearest-neighbor 参数及上限不同。
- Chatbot 可添加 Ontology context 或语义搜索工具；TS v2/Python 示例可直接用文本执行 nearest-neighbors，Python 方法在页面标为 beta。AIP 需启用且调用者具备开发权限。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| KNN Object Set | KNN 对象集合 | Workshop 中无代码的近邻对象查询。 |
| nearestNeighbors | 近邻查询 | 按 embedding 找相似对象的函数 API。 |
| vector property | 向量属性 | 存放对象 embedding 的 Ontology 属性。 |
| Ontology context | 本体上下文 | Agent 可消费的已授权本体对象信息。 |

## 疑问与待验证项

- 文档示例引用的 embedding 型号可能变化；当前可用型号和 enrollment 限制应从模型目录确认。
- Workshop KNN 无相关性排序，Function 各语言的邻居上限和 beta 状态不同，UI/API 不能将其简化成统一承诺。
- Vector 属性检索授权、模型切换后的重嵌入和 KNN index 更新时序需继续研读对应治理与 API 文档。

## 复刻启示

- 让 Agent 在“上下文直读、语义搜索、Ontology Function”三种取数路线间显式选择；结果显示对象关系证据与 embedding 召回分数。
- 推理服务需区分确定性属性派生与概率式语义召回，不能把近邻分数作为业务事实。
- 向量模型与检索参数成为版本化资源；按项目权限过滤候选对象并留存召回/排序日志。
