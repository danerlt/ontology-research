<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/linked-objects/linked-object-basics -->
<!-- 研读状态：已完成 -->

# Linked Object basics • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/linked-objects/linked-object-basics)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/v2/ontologies-v2-resources
- 相关性：direct；Ontology REST API v2 参考
- 官方更新时间：2026-11-12T17:46:46.921Z
- 目录核对时间：2026-11-14T14:56:50Z
- 产品状态：常规 v2 概念页；本页未标注预览状态。

## 英文原文短摘录（每个来源不超过 25 词）

> “A Linked Object describes a object that is linked to another object.”

## 摘录译文

Linked Object 描述一个与另一个对象建立链接的对象。

## 中文要点

- Linked Object 表示通过本体链接与起始对象关联的对象；具体关系由 Link Type 和两个对象的身份共同确定。
- 该概念页只有简短定义，不涉及方向、基数、分页、权限或链接不存在时的行为，需结合 Link Type 与查询 API 阅读。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Linked Object | 链接对象 | 相对于给定起点，通过本体链接关联的对象。 |
| Link Type | 链接类型 | 定义对象类型之间关系的本体资源。 |
| originating object | 起始对象 | 查询链接时作为关系出发点的对象。 |

## 疑问与待验证项

- 不同方向的链接是否拥有独立 API 名及反向语义，需结合 Link Type 定义核验。
- 该页英文原文存在语法拼写 `a object`，翻译按其预期语义处理。

## 复刻启示

- 画布将链接对象呈现为关系边两端的对象实例；边携带 Link Type、方向和基数元数据。
- 在关系检查器中显示起点、目标与关系名称，避免把链接对象误当成新的对象类型定义。
