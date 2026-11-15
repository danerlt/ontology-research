<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/ontology-object-sets/load-object-set-objects-or-interfaces -->
<!-- 研读状态：已完成 -->

# Load Object Set Objects Or Interfaces • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/ontology-object-sets/load-object-set-objects-or-interfaces)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/ontologies-v2-resources/ontology-object-sets
- 相关性：direct；Ontology REST API v2 参考
- 官方更新时间：2026-11-12T17:46:46.922Z
- 目录核对时间：2026-11-14T14:54:08Z
- 产品状态：Preview API，调用需显式带 `preview=true`；其中本体定义派生属性加载目前仍为实验性且尚未普遍开放。

## 英文原文短摘录（每个来源不超过 25 词）

> “The result object set cannot contain a mix of objects with \"interface\" properties and \"object type\" properties.”

## 摘录译文

返回集合不能混用接口属性视图和对象类型属性视图。

## 中文要点

- POST `/api/v2/ontologies/{ontology}/objectSets/loadObjectsOrInterfaces` 可将集合中的对象统一投影为接口视图；能投影到接口时返回接口定义属性，否则返回对象类型属性，并附接口属性到对象属性的映射。
- 结果集合不能混合接口属性和对象类型属性；同一对象若匹配多个接口，端点会报 `UnsupportedObjectSet`，应改用 `loadObjectsMultipleObjectTypes`。此 API 标记为 Preview，需加 `preview=true`。
- 分页的 `pageSize` 是上限，内存限制可能使实际页较小，必须依据 `nextPageToken` 判断是否还有结果。`snapshot=true` 提供跨页一致视图；默认实时读取可能在并发写入下漏项或重复。
- OSv1 对象最多返回 10,000 条，OSv2 没有该端点级上限；null 属性不返回，向量属性需显式选择。OTDP 默认加载开关仅在未显式选择属性时生效，且该能力尚未普遍开放。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| interface view | 接口视图 | 将不同对象类型的实例按共同接口属性读取。 |
| pageToken | 分页令牌 | 指向下一页；是否完成应以令牌是否存在判断。 |
| snapshot | 快照一致性 | 固定分页开始前的数据视图，降低重复或漏项。 |
| OTDP | 本体定义派生属性 | 本体中定义的派生属性；当前相关加载能力仍属实验性。 |

## 疑问与待验证项

- 接口视图冲突时为何不能由此端点选择一个接口，需结合多对象类型加载端点设计兼容的投影方案。
- Preview API 可变更或移除；复刻实现应把接口视图加载做成可替换能力，并明确标出自身稳定性。

## 复刻启示

- 在画布中把接口定义与具体对象类型分开建模；运行轨迹保存所选视图及属性映射，避免把同名字段误当成同一物理属性。
- 对象列表加载应实现游标分页和可选快照，并暴露空值、向量字段、派生属性是否加载等选择；界面不要把短页误判为结果结束。
