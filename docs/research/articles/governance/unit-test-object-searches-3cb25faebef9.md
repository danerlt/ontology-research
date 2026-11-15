<!-- 页面 URL：https://www.palantir.com/docs/zh/foundry/functions/unit-test-object-searches -->
<!-- 研读状态：已完成 -->

# 函数 • Unit testing • 存根对象搜索和聚合 • Palantir

- 英文来源：[现行英文原文](https://www.palantir.com/docs/foundry/functions/unit-test-object-searches)
- 官方中文来源：[官方中文页（AIP 机器翻译，准确性未独立验证）](https://www.palantir.com/docs/zh/foundry/functions/unit-test-object-searches)
- 页面语言：中文（官方 AIP 机器翻译，需与英文原文交叉核对）
- 主题栏目：functions
- 相关性：direct；本体函数文档
- 官方更新时间：2026-11-12T17:46:46.935Z
- 目录核对时间：2026-11-14T14:59:45Z
- 产品状态：TSv1 函数测试可用 `whenObjectSet` 为特定对象集查询、过滤、搜索或聚合配置固定响应，验证业务代码对本体查询结果的处理。

## 原文短摘录与翻译

> “Use stubs to dictate the responses to object set searches or object aggregations.”

## 摘录译文

使用 stub 为对象集搜索或对象聚合指定返回结果。

## 中文要点

- 从 `@foundry/functions-testing-lib` 导入 `whenObjectSet`，将特定对象集表达式与测试返回值绑定。
- stub 可针对对象集过滤器、聚合值或搜索结果设置 canned response，测试代码随后执行函数并断言其输出。
- 查询表达式与 stub 条件需匹配被测代码发出的对象集操作；这使业务逻辑可脱离真实本体数据运行。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| stub | 存根/模拟响应 | 预先规定依赖查询应返回的测试数据 |
| `whenObjectSet` | 对象集 stub | 为对象集查询或聚合设置 mock 的测试 API |
| aggregation | 聚合 | 对对象属性集合进行 sum/count 等汇总计算 |

## 疑问与待验证项

- stub 验证函数如何处理被模拟的数据，不覆盖真实 Ontology 查询服务、权限过滤、索引一致性或查询性能。
- 若函数对 ObjectSet 改写了 filter/order/take 链，测试要核对完整查询链是否命中 stub，否则可能误把未匹配查询当作空结果。

## 复刻启示

- 画布中的派生属性公式测试支持固定对象/链接集合与聚合结果，并展示每个 stub 的查询路径和覆盖范围。
- 将纯规则计算测试与真实数据权限/索引集成验证分开，报告中明确哪些依赖被模拟。
- 对多跳推理验证对象集边界、空集合、重复目标和聚合类型，避免只测试一个正常样例。
