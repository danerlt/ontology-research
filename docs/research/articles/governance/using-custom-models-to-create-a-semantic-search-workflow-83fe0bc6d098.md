<!-- 页面 URL：https://www.palantir.com/docs/zh/foundry/functions/using-custom-models-to-create-a-semantic-search-workflow -->
<!-- 研读状态：已完成 -->

# 函数 • Semantic search • 使用自定义模型创建语义搜索工作流 • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/ontology/using-custom-models-to-create-a-semantic-search-workflow)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/functions/using-custom-models-to-create-a-semantic-search-workflow)
- 页面语言：中文（官方 AIP 机器翻译，需与英文原文交叉核对）
- 主题栏目：functions
- 相关性：direct；本体函数文档
- 官方更新时间：2026-11-12T17:46:46.935Z
- 目录核对时间：2026-11-14T14:59:48Z
- 产品状态：旧中文路由已迁移到当前 Ontology 语义搜索指南；英文页将“自定义 embedding 模型”标为不再推荐的旧路线，介绍 Modeling Objective、数据流水线、Vector 属性与查询函数的历史端到端组合。

## 英文原文短摘录（每个来源不超过 25 词）

> “This tutorial is for those using an embedding model not supplied by Palantir, which is no longer a recommended workflow.”

## 摘录译文

本教程面向使用非 Palantir 提供的 embedding model 的用户；这种工作流已不再推荐。

## 中文要点

- 教程以自定义/开源模型生成文档 embedding，并通过 Foundry Modeling Objective 或模型部署运行 transform；embedding 列需转为与 Ontology Vector 属性兼容的维度和数值类型。
- 将文档与 embedding 写入对象类型，并配置向量维度与 similarity function；为低延迟查询还要部署实时模型函数生成用户查询向量，再执行 KNN。
- 页面明确自定义模型路线已不再推荐，当前实现优先看 Palantir-provided model workflow；该页面保留用于兼容既有模型和理解旧版管线。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| custom embedding model | 自定义嵌入模型 | 由租户自选或托管、用于文本向量化的模型 |
| Modeling Objective | 建模目标 | 管理模型提交、评估和发布的 Foundry 资源 |
| similarity function | 相似度函数 | 计算查询向量和存储向量距离/相似性的算法 |
| live model deployment | 实时模型部署 | 为用户查询提供低延迟在线 embedding 的模型服务 |

## 疑问与待验证项

- 旧版 tutorial 提及特定模型/transform 和 Pandas/Spark/GPU 示例；这些依赖及模型 ID 可用性可能变化，不应直接复制到新方案。
- 页面标题下明确自定义模型方法已不再推荐，但保留支持既有工作流的价值；迁移到 Palantir 模型所需的数据/向量兼容步骤需按新指南确认。
- 历史示例的 KNN 排序和邻居数量限制随 Function SDK 版本不同，需要按语言逐个核实。

## 复刻启示

- 连接器体系应支持平台内置模型和用户自带模型两种路线，但为新租户默认推荐平台治理、受控的模型目录。
- 向量索引记录来源文档/块、embedding 模型和版本、维度及距离函数；模型更换时通过旁路重建和对照评估迁移。
- Agent 的搜索溯源保留被命中的对象和原始文件，不把向量值或训练实现暴露给终端用户；文档标明旧路线的维护状态。
