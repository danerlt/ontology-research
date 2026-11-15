<!-- 页面 URL：https://www.palantir.com/docs/foundry/functions/unit-test-object-searches -->
<!-- 研读状态：已完成 -->

# Functions • Unit testing (TSv1) • Stub object searches and aggregations • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/functions/unit-test-object-searches)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/functions/unit-test-object-searches)（配对状态：matched）
- 页面语言：英文
- 主题栏目：functions
- 相关性：direct；本体函数文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:03:26Z
- 产品状态：TSv1 Jest stub API，用于为对象集搜索、聚合与链接遍历提供预设返回。

## 英文原文短摘录（每个来源不超过 25 词）

> “You need to import `{ whenObjectSet }` from `@foundry/functions-testing-lib` to use stubs.”

## 摘录译文

使用对象集存根时，需要从 @foundry/functions-testing-lib 导入 whenObjectSet。

## 中文要点

- `whenObjectSet(query).thenReturn(value)` 为特定 ObjectSet 查询或聚合预设返回结果，使单测可验证过滤逻辑而不访问真实本体数据。
- 可以针对对象搜索、聚合和 `searchAround` 链接遍历设置不同 stub；需要区分查询表达式及每次调用的返回。
- 模拟多个对象集合时，示例要求为传入的 stub 对象设置 RID，便于查询构造匹配预期调用。
- 该机制验证代码如何构造/消费查询，不验证真实后端过滤语义、对象权限或索引一致性。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| whenObjectSet | 对象集存根配置器 | 将指定对象集查询调用映射到固定返回值。 |
| stub | 存根 | 测试期间预设的依赖响应。 |
| searchAround | 关联遍历搜索 | 沿本体链接从对象集查找相关对象集。 |

## 疑问与待验证项

- 复杂链式查询的 stub 匹配依赖表达式结构；需确保测试中的查询和生产函数构造一致。
- mock 的聚合结果可以任意给定，不代表真实集合的聚合性能或权限结果。

## 复刻启示

- 派生属性引擎的单测可 stub 链路查询，验证空集、多路径和聚合逻辑；另设真实数据集集成用例。
- 在测试失败报告中输出查询路径、过滤条件和 stub 命中记录，方便定位关系推理错误。
