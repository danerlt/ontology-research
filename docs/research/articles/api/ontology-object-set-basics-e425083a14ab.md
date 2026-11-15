<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/ontology-object-sets/ontology-object-set-basics -->
<!-- 研读状态：已完成 -->

# Ontology Object Set basics • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/ontology-object-sets/ontology-object-set-basics)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/v2/ontologies-v2-resources
- 相关性：direct；Ontology REST API v2 参考
- 官方更新时间：2026-11-12T17:46:46.922Z
- 目录核对时间：2026-11-14T14:57:23Z
- 产品状态：常规 v2 概念页；本页未标注预览状态。

## 英文原文短摘录（每个来源不超过 25 词）

> “An object set represents a set of objects in the Ontology.”

## 摘录译文

Object Set 表示 Ontology 中一组对象。

## 中文要点

- Object Set 是在本体中代表一组对象的查询/操作对象，可用它对多个对象执行操作。
- 它描述的是对象集合，不等同于单条对象记录或对象类型定义；如何构造集合由 Load Object Set 等接口继续定义。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Object Set | 对象集合 | 在本体中聚合一组对象供后续操作。 |
| Ontology | 本体 | 集合中对象类型与关系的语义环境。 |
| object set definition | 对象集合定义 | 描述哪些对象属于该集合的表达式。 |

## 疑问与待验证项

- 概念页未说明 Object Set 是否总是惰性求值、是否持久化或有生命周期。
- 集合定义可使用的过滤器、链接遍历和集合运算需参考 load 接口 schema。

## 复刻启示

- 把对象集合建模为可序列化的查询表达式，保留筛选和关系路径，而不是复制对象行。
- 画布支持从当前选中类型、过滤条件和关系展开生成临时集合，显示预计命中数量与执行成本。
