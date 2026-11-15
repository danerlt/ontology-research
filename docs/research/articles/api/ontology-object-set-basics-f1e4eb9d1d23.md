<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/ontology-object-sets/ontology-object-set-basics -->
<!-- 研读状态：已完成 -->

# Ontology Object Set basics • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/ontology-object-sets/ontology-object-set-basics)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/ontologies-v2-resources/ontology-object-sets
- 相关性：direct；Ontology REST API v2 参考
- 官方更新时间：2026-11-12T17:46:46.922Z
- 目录核对时间：2026-11-14T14:54:08Z
- 产品状态：v2 REST API 概念说明；本页是对象集合基础定义，不含请求端点。

## 英文原文短摘录（每个来源不超过 25 词）

> “An object set represents a set of objects in the Ontology.”

## 摘录译文

对象集合表示 Ontology 中的一组对象。

## 中文要点

- 本页给出 REST API 中 `ObjectSet` 的概念边界：它是 Ontology 对象的集合表达，可作为对多个对象执行操作的输入。
- 与“已加载的对象数组”不同，ObjectSet 定义可以交给查询、加载或聚合端点继续计算；集合表达式本身不保证已经将实例数据全部读入客户端。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| ObjectSet | 对象集合 | 描述一组 Ontology 对象，并可作为批量操作的输入。 |
| object set definition | 对象集合定义 | 说明集合由何种对象与查询关系构成的表达式。 |

## 疑问与待验证项

- 本页只给定义，没有枚举集合表达式的全部变体；具体结构要查看 v2 API 请求体或 OSDK 类型参考。
- 该概念页未说明集合是否静态、动态、临时或持久；这些是定义形式与存储生命周期的不同维度。

## 复刻启示

- 复刻时把 `ObjectSet` 建模成可序列化的查询 AST，与分页结果列表区分；可在画布中将集合节点连接到筛选、链接遍历、聚合与加载算子。
- 让每个集合节点展示范围、数据读取策略及计算成本，避免把“集合定义”误画成一批已经物化的实例。
