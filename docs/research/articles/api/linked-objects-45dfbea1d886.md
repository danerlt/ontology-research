<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/linked-objects -->
<!-- 研读状态：已完成 -->

# Linked Object basics • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/linked-objects)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/v2/ontologies-v2-resources
- 相关性：direct；Ontology REST API v2 参考
- 官方更新时间：2026-11-12T17:46:46.921Z
- 目录核对时间：2026-11-14T14:56:50Z
- 产品状态：v2 Linked Object 基础概念页

## 英文原文短摘录（每个来源不超过 25 词）

> “A Linked Object describes a object that is linked to another object.”

## 摘录译文

Linked Object 描述一个与另一个对象相连的对象。

## 中文要点

该 API v2 基础页把 Linked Object 定义为通过本体链接关联到另一对象的对象。概念重点是链接访问路径：来源对象加上 Link Type 决定可查询的目标对象；它不是独立于 Object 的实体类型，也不是 Link Type schema 本身。配套读取接口提供按单个目标主键读取和按来源对象枚举目标的操作。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Linked Object | 链接对象 | 通过链接关系从来源对象到达的目标对象 |
| Link Type | 链接类型 | 定义对象类型之间连接的 schema |
| Source object | 来源对象 | 链接查询起点对象实例 |
| Target object | 目标对象 | 被链接到的对象实例 |

## 疑问与待验证项

- 基础页没有说明链接方向、基数、反向链接和多跳遍历规则；这些要从 Link Type 文档及运行 API 确认。
- 文档句子本身存在语法错误；本卡翻译表达其语义，没有据此推断额外功能。

## 复刻启示

- 画布把对象类型之间的 Link Type 定义作为建模边；运行时对象图中的边则携带来源/目标实例标识和链接类型。
- 从源对象进入相邻对象时保留 Link Type API 名、方向、目标类型与授权上下文，支持后续可解释推理路径。
