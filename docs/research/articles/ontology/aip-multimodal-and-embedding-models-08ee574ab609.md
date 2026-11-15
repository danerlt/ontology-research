<!-- 页面 URL：https://www.palantir.com/docs/foundry/ontology/aip-multimodal-and-embedding-models -->
<!-- 研读状态：已完成 -->

# Semantic search • Choose multimodal and embedding models • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/ontology/aip-multimodal-and-embedding-models)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：ontology
- 相关性：direct；本体模型与治理文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:03:45Z
- 产品状态：模型选择指南；支持型号会变化，并因 enrollment 而不同。

## 英文原文短摘录（每个来源不超过 25 词）

> “Text-only LLMs cannot read images.”

## 摘录译文

纯文本 LLM 无法读取图像。

## 中文要点

- 包含图表、图像的文档应采用带 vision 能力的模型；可用 AIP Document Intelligence 比较 OCR 与 VLM 抽取，再决定部署策略。
- Pipeline Builder 的 Use LLM 节点可将 media reference 传给 Vision 模型。语义搜索命中后，也可把对应页图和问题交给 Vision 模型。
- 若使用页图检索，每个 chunk object 应保存页码和页面图像 media reference；embedding 模型应在文档块和查询侧保持兼容。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Vision model | 视觉模型 | 可读取并理解图像内容的模型。 |
| OCR | 光学字符识别 | 从图像/扫描文档提取文本。 |
| VLM | 视觉语言模型 | 同时处理视觉输入和语言任务的模型。 |
| media reference | 媒体引用 | 指向 Foundry 图像/文档页的引用。 |

## 疑问与待验证项

- 支持的模型列表会变化且受 enrollment 影响；部署前应从 Supported LLMs/Model Catalog 动态核对，不把文档示例硬编码。
- OCR 文本召回与 Vision 图像问答的引用定位方式和成本控制需要单独验证。

## 复刻启示

- 文档/对象 schema 支持文本、向量、页码和媒体引用，Agent 可先检索再对命中页做视觉复核。
- 模型目录记录 provider、vision/embedding 能力、可用环境和版本；混合流程保留模型选择与耗用记录。
- 画布将数据抽取、chunk、embedding、检索和 VLM 复核表示为可追踪流水线。
