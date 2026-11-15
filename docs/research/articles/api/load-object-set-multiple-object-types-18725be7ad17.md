<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/ontology-object-sets/load-object-set-multiple-object-types -->
<!-- 研读状态：已完成 -->

# Load Object Set Multiple Object Types • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/ontology-object-sets/load-object-set-multiple-object-types)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/v2/ontologies-v2-resources
- 相关性：direct；Ontology REST API v2 参考
- 官方更新时间：2026-11-12T17:46:46.922Z
- 目录核对时间：2026-11-14T14:57:23Z
- 产品状态：预览接口；必须传 `preview=true`；分支与事务也有实验性限制。

## 英文原文短摘录（每个来源不超过 25 词）

> “Load the ontology objects present in the `ObjectSet` from the provided object set definition.”

## 摘录译文

根据给定 Object Set 定义加载集合中的 Ontology 对象。

## 中文要点

- POST `/api/v2/ontologies/{ontology}/objectSets/loadObjectsMultipleObjectTypes` 支持返回多对象类型/接口范围的集合结果，调用需 `preview=true`。
- 结果可按对象类型提供所选对象属性，或按接口范围仅提供接口所实现的属性；接口范围结果附带接口到对象实现的映射。
- OSv1 最多返回 10,000 条、OSv2 无此上限；null 属性不返回，Vector 属性需显式选择，元数据字段前缀为 `$` 而非普通 loadObjects 的 `__`。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| interface scope | 接口范围 | 只投影接口定义且由对象类型实现的属性。 |
| implementation mapping | 实现映射 | 把接口属性对应回对象属性。 |
| preview | 预览 | 该端点的当前发布状态。 |
| property metadata | 属性元数据 | 该端点使用 `$` 前缀标识元数据字段。 |

## 疑问与待验证项

- 该端点的 preview 状态意味着 schema 与行为可能改变，需通过适配层封装。
- 不同对象类型映射到同一接口属性时的冲突及空值解释，需要结合完整响应 schema 验证。

## 复刻启示

- 多类型对象集可作为统一画布视图：以接口做共同字段投影，同时保存接口属性到具体属性的映射。
- 在 API 兼容层显式转换 `$` 与 `__` 元数据前缀，避免客户端对同一对象使用两套隐含约定。
