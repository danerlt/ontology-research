<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/ontology-object-sets/load-object-set-multiple-object-types -->
<!-- 研读状态：已完成 -->

# Load Object Set Multiple Object Types • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/ontology-object-sets/load-object-set-multiple-object-types)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/ontologies-v2-resources/ontology-object-sets
- 相关性：direct；Ontology REST API v2 参考
- 官方更新时间：2026-11-12T17:46:46.922Z
- 目录核对时间：2026-11-14T14:54:08Z
- 产品状态：Preview 兼容路由；必须传 `preview=true`，分支与事务存在实验性限制

## 英文原文短摘录（每个来源不超过 25 词）

> “Load the ontology objects present in the `ObjectSet` from the provided object set definition.”

## 摘录译文

根据给定的 Object Set 定义加载本体对象。

## 中文要点

`POST /api/v2/ontologies/{ontology}/objectSets/loadObjectsMultipleObjectTypes` 支持对多种对象类型或接口范围的集合加载结果，调用需带 `preview=true`。按对象类型范围可选择返回对应对象属性；按接口范围则只投影接口定义且由对象类型实现的属性，并返回接口到具体对象实现的映射。OSv1 最多返回 10,000 条、OSv2 无该上限；null 属性不会出现在结果中，Vector 属性需显式选择。该端点的元数据字段以 `$` 前缀标识，与普通 `loadObjects` 的 `__` 前缀不同。本卡对应的非 v2 显式路径是兼容入口，canonical v2 URL 保存在目录中。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Interface scope | 接口范围 | 只投影接口定义且由对象类型实现的属性 |
| Implementation mapping | 实现映射 | 将接口属性映射回具体对象属性 |
| Preview | 预览 | 该端点需显式启用的发布状态 |
| Property metadata | 属性元数据 | 本端点使用 `$` 前缀标识元数据字段 |

## 疑问与待验证项

- 不同对象类型实现同一接口属性时的映射冲突、空值差异与报错行为，需要通过完整响应模型验证。
- OSv2 无结果数量上限不等于无资源或超时限制；不能据此认为一次请求可以安全载入任意规模集合。

## 复刻启示

- 多类型画布可使用接口契约做共同字段投影，同时保留接口属性到每个对象类型属性的可追踪映射。
- API 适配层应显式规范 `$` 与 `__` 元数据前缀、空值和 Vector 属性选择，避免混淆不同端点语义。
