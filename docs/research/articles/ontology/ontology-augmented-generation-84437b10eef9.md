<!-- 页面 URL：https://www.palantir.com/docs/foundry/ontology/ontology-augmented-generation -->
<!-- 研读状态：已完成 -->

# Semantic search • Ontology augmented generation • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/ontology/ontology-augmented-generation)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：ontology
- 相关性：direct；本体模型与治理文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:04:03Z
- 产品状态：本体增强生成指南；上下文长度和检索方案应按具体模型/应用评估。

## 英文原文短摘录（每个来源不超过 25 词）

> “If your application's full context is within this limit, we recommend you start without search.”

## 摘录译文

如果应用的完整上下文能放入该限制内，建议先从不使用搜索开始。

## 中文要点

- Ontology-Augmented Generation（OAG）关注为 LLM 找到相关本体/业务上下文；检索常是 RAG 设计中最困难的一步。
- 文档建议先检查完整上下文能否直接进入提示词；若能容纳，可先不做 semantic search。基础文档搜索则采用 chunk、chunk object（含 media reference）、搜索和 PDF Viewer 溯源。
- 若基础检索不足，可逐步尝试 HyDE、关键词排序、query augmentation 或 hybrid search；先确认相关上下文是否真的被取回并传入 prompt。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Ontology-Augmented Generation | 本体增强生成 | 通过本体与业务上下文增强模型输入。 |
| retrieval | 检索 | 为当前任务选择并注入相关上下文。 |
| HyDE | 假设文档嵌入 | 用假设答案/文档辅助检索的技术路线。 |
| hybrid search | 混合搜索 | 结合语义与关键词检索。 |

## 疑问与待验证项

- 文档给出的 128,000-token 示例取决于具体模型，不应作为当前所有模型的固定窗口。
- 检索文档主要讲非结构化文本；本体关系对象直接上下文的截断、排序和证据格式需另行设计。

## 复刻启示

- 先提供有预算的本体上下文装配：按当前对象、授权关系和字段挑选小型邻域；超出预算后再启用检索。
- 将实体关系遍历、全文检索、向量召回标成不同策略，输出每条证据的对象/来源/链路。
- Agent 回答无法找到信息时，界面先检查召回证据与权限过滤，再调整查询策略。
