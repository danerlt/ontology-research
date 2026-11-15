<!-- 页面 URL：https://www.palantir.com/docs/foundry/ontology/using-custom-models-to-create-a-semantic-search-workflow -->
<!-- 研读状态：已完成 -->

# Semantic search • Use custom models to create a semantic search workflow • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/ontology/using-custom-models-to-create-a-semantic-search-workflow)
- 官方中文来源：尚未确认（配对状态：ambiguous）
- 页面语言：英文
- 主题栏目：ontology
- 相关性：direct；本体模型与治理文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:04:03Z
- 产品状态：自定义 embedding 旧路线；页面明确指出当前不再推荐，优先查看官方模型路线。

## 英文原文短摘录（每个来源不超过 25 词）

> “This tutorial is for those using an embedding model not supplied by Palantir, which is no longer a recommended workflow.”

## 摘录译文

本教程面向使用非 Palantir 提供的 embedding model 的场景；这已不再是推荐工作流。

## 中文要点

- 本教程以注册自定义 embedding model 为前提，构建“文档数据集 → embedding → Ontology vector 属性 → 自然语言 KNN 查询”的端到端示例。
- 当前页面明确说明此路线已不再推荐，并指向 Palantir 提供模型的工作流；因此它适合作为兼容性/自托管对照，而不是新系统的默认决策。
- 自定义模型仍可能适用于有特定合规、模型或向量生成需求的团队；其部署和函数查询细节应按对应 Model/Functions 文档核验。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| custom embedding model | 自定义嵌入模型 | 非 Palantir 提供的向量生成模型。 |
| vector property | 向量属性 | Ontology 中保存 embedding 的对象属性。 |
| KNN | K 近邻 | 根据查询向量找最近邻对象。 |

## 疑问与待验证项

- 页面称旧路线不再推荐，但未在此页说明撤销日期、兼容期或具体弃用安排。
- 不同模型可能在向量维度和语义空间上不兼容；重建索引时需同步更新查询模型与历史 embedding。

## 复刻启示

- 提供模型注册适配器，但默认接入当前官方支持的 embedding 路线；在设置页明确自定义模型的支持边界。
- 每条向量记录模型 RID/版本与维度，模型切换时建立新索引版本，禁止混用不同向量空间。
