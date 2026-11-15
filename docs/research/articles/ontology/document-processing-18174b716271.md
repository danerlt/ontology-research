<!-- 页面 URL：https://www.palantir.com/docs/foundry/ontology/document-processing -->
<!-- 研读状态：已完成 -->

# Semantic search • Document processing • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/ontology/document-processing)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：ontology
- 相关性：direct；本体模型与治理文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:03:45Z
- 产品状态：Pipeline Builder 文档处理指南；示例面向 PDF 与语义搜索。

## 英文原文短摘录（每个来源不超过 25 词）

> “Primarily, the objective is to split long text into smaller "chunks", each with an associated Ontology object linked back to the original object.”

## 摘录译文

主要目标是把长文本切成更小的“块”，并为每个块建立一个关联回原始对象的 Ontology 对象。

## 中文要点

- PDF 经 Media Set 导入后，可在 Pipeline Builder 提取文字、切块、生成 embedding，再按 chunk 建立独立对象并关联原始文档。
- Chunking 可配置近似字符大小、相邻块 overlap 和分隔符优先级；overlap 用于保留切块边界附近的上下文。
- 工作流把匹配 chunk 与原 PDF 页面并列展示，便于用户对照原文校验来源；该路线适合非结构化内容检索，不替代对象间的本体关系。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| chunk | 文本块 | 长文本切分后的检索单元。 |
| chunk overlap | 块重叠 | 相邻文本块共享的尾部上下文。 |
| Media Set | 媒体集 | 导入 PDF 等媒体文件的资源。 |
| source-of-truth validation | 原始来源校验 | 将检索片段与原始 PDF 对照。 |

## 疑问与待验证项

- 文档未规定 chunk 对齐页码/字符偏移的标准结构，引用精确定位需在数据模型中补充。
- OCR/VLM 抽取置信度、文档版本更新后的索引失效策略需要结合其他页面设计。

## 复刻启示

- Chunk 对象保留来源文档 RID、页码/偏移、chunk 次序、正文、embedding 模型和索引版本；画布通过关系边回链。
- Agent 检索结果显示引用原文片段及 PDF 页面，支持打开源文件校验。
- 将非结构化 chunk 检索与 1–3 跳结构化本体推理分开，并可在 Agent 上层组合。
