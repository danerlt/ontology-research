<!-- 页面 URL：https://www.palantir.com/docs/zh/foundry/functions/pdf-handling -->
<!-- 研读状态：已完成 -->

# 函数 • Semantic search • PDF处理 • Palantir

- 英文来源：[现行英文原文](https://www.palantir.com/docs/foundry/ontology/document-processing)
- 官方中文来源：[官方中文页（AIP 机器翻译，准确性未独立验证）](https://www.palantir.com/docs/zh/foundry/functions/pdf-handling)
- 页面语言：中文（官方 AIP 机器翻译，需与英文原文交叉核对）
- 主题栏目：functions
- 相关性：direct；本体函数文档
- 官方更新时间：2026-11-12T17:46:46.935Z
- 目录核对时间：2026-11-14T14:59:30Z
- 产品状态：目录中的 PDF 处理中文路径已迁移到 Ontology 文档处理页面；现行内容覆盖 PDF/图像文本抽取、分块、语义检索及在 Workshop 中展示原文件。

## 原文短摘录与翻译

> “This page offers a basic guide for using Pipeline Builder to parse PDFs for semantic search.”

## 摘录译文

本页介绍如何使用 Pipeline Builder 解析 PDF，以支持语义搜索。

## 中文要点

- 基本管线是导入 PDF 媒体集、获取媒体引用、抽取文本，再按块切分并将搜索结果与原始文档关联。
- 分块配置包括文本列、近似字符长度、相邻块重叠长度和按优先级排列的分隔符；重叠用于保留跨块上下文。
- 每个 chunk 作为 Ontology 对象关联回原始对象，Workshop 可同时显示命中片段和 PDF，供用户核验原始证据。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| media set | 媒体集 | 用于承载导入 PDF 等文件的媒体数据集合 |
| chunk | 文本块 | 为检索和嵌入拆分出的局部文本单元 |
| chunk overlap | 分块重叠 | 相邻块之间重复保留的文本长度 |
| source-of-truth validation | 原始来源核验 | 用户回看原文件确认检索片段是否准确 |

## 疑问与待验证项

- 当前文档称 chunk size 是近似字符数；不同语言 token 长度、PDF OCR 质量和版面结构对切分效果的影响需通过样例验证。
- 机器提取文本与版面阅读顺序可能不一致；生产系统应让 Agent 输出页码、位置和原始媒体引用，方便业务人员复核。
- 旧中文路由 `/functions/pdf-handling` 迁移到 `/ontology/document-processing` 的关系来自官方导航，中文版本覆盖范围需继续核对。

## 复刻启示

- 建立 Document、DocumentChunk 与来源系统/原始文件的对象关系；chunk 保存页码、偏移、分块策略版本、embedding 模型版本和提取状态。
- 检索面板同时渲染文本命中与原 PDF 页面，允许用户回查证据；Agent 只能引用有来源定位的片段。
- 对 PDF 解析、分块、索引和权限继承分别建流水线状态，不把文件全文复制到研读卡或日志中。
