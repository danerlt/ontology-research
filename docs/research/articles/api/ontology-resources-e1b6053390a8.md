<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/ontology-resources -->
<!-- 研读状态：已完成 -->

# Ontology basics (v1) • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/ontology-resources)
- 官方中文来源：尚未确认（配对状态：needs_review）
- 页面语言：英文
- 主题栏目：api/ontology-resources
- 相关性：direct；Ontology API v1 参考，保留兼容性对照并优先关注 v2
- 官方更新时间：2026-11-12T17:46:46.922Z
- 目录核对时间：2026-11-14T14:54:39Z
- 产品状态：目标根路由未能独立载入；按可读取的官方 v1 Ontology basics 同主题页交叉核对

## 英文原文短摘录（每个来源不超过 25 词）

> “Ontologies are categorizations of data into real-world concepts.”

摘录来源：[Ontology basics (v1)](https://www.palantir.com/docs/foundry/api/v1/ontology-resources)。

## 摘录译文

本体是对数据进行分类、以表达现实世界概念的方式。

## 中文要点

- 可读取的 v1 基础页把 Ontology 描述为现实概念的数据分类；这些概念由对象类型、属性、链接类型和动作类型表达，组成连接组织内关键实体的描述性对象图。
- API 读取可能不是强一致：官方说明新增 Ontology 后，API 反映变更可能需要几分钟，期间可能短暂返回 `OntologyNotFound`。
- 本卡目标 URL 与 `/api/v1/ontology-resources` 路由表现为重复/不同版本路径；目标根路由无法单独读取，正文定义由官方 v1 同主题页验证，未推断更多 v1 独有能力。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Ontology | 本体 | 组织数据的概念语义层 |
| object type | 对象类型 | 描述实体类别及其属性 |
| link type | 链接类型 | 描述对象类型间的关系 |
| eventually consistent | 最终一致 | 新建本体后 API 视图可能延迟可见 |

## 疑问与待验证项

- 目标根路径和显式 v1 路径的 canonical/版本关系需复核；目录将其分别列出，卡片按唯一 URL 保留。
- 延迟可见的时长使用“几分钟”描述，没有给出 SLA 或客户端重试建议；应以短暂重试、退避和可观察错误处理。

## 复刻启示

- 本体的最小图模型应包含对象类型、属性、链接类型和动作类型，并让链接关系成为可查询、可绘制的语义边。
- API/UI 在本体创建或发布后应暴露索引/发布状态，容忍短暂传播延迟，不把暂时未查到误判为永久不存在。
- v1 兼容层可共享同一领域模型，但路由、字段命名和一致性承诺需单独记录版本契约。
