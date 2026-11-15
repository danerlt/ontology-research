<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/linked-objects/linked-object-basics -->
<!-- 研读状态：已完成 -->

# Linked Object basics • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/linked-objects/linked-object-basics)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/ontologies-v2-resources/linked-objects
- 相关性：direct；Ontology REST API v2 参考
- 官方更新时间：2026-11-12T17:46:46.921Z
- 目录核对时间：2026-11-14T14:53:47Z
- 产品状态：按当前 API 参考整理；列表一致性、分支和部分媒体能力有明确限制。

## 英文原文短摘录（每个来源不超过 25 词）

> “A Linked Object describes a object that is linked to another object.”

## 摘录译文

Linked Object 描述的是与另一个对象关联的对象。

## 中文要点

- 该规范页只有一句定义：Linked Object 是通过链接与另一对象关联的对象。
- 页面正文信息非常有限；列表与点查端点补充主对象、链接 API 名称、目标主键和对象属性的具体读取语义。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Linked Object | 链接对象 | 与其他本体对象建立链接的对象视图。 |
| link | 链接 | 对象间关系实例。 |

## 疑问与待验证项

- 本页没有解释链接是否携带独立属性、基数或关系约束。

## 复刻启示

- 画布把关系定义和关系实例区分：schema 图展示 Link Type，实例图展示对象之间实际存在的边。
- 点击边时调用链接对象 API 确认该实例关系，不从 schema 静态边推断数据实例。
