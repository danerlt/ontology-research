<!-- 页面 URL：https://www.palantir.com/docs/foundry/functions/unit-test-stub-objects -->
<!-- 研读状态：已完成 -->

# Functions • Unit testing (TSv1) • Create stub objects • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/functions/unit-test-stub-objects)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/functions/unit-test-stub-objects)（配对状态：matched）
- 页面语言：英文
- 主题栏目：functions
- 相关性：direct；本体函数文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:03:25Z
- 产品状态：TSv1 Jest 单测示例；stub 对象是内存 mock，不是真实持久化对象。

## 英文原文短摘录（每个来源不超过 25 词）

> “You can create and define your mock objects using `Objects.create()`, which can be used the same way as if it was a regular function.”

## 摘录译文

可使用 Objects.create() 创建和定义 mock 对象，再像普通对象一样用于测试函数。

## 中文要点

- `Objects.create()` 可构造 mock Ontology object 并设置属性，作为普通函数输入；测试可验证函数基于对象字段计算的输出。
- 此机制适合单测对象属性逻辑而不调用线上数据；链接、对象搜索和编辑写入另有对应 stub/verify API。
- mock 对象让测试不依赖环境中实际存在的对象和数据，但不会验证权限、索引、数据源映射或实际事务。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| stub object | 存根对象 | 测试中构造的模拟 Ontology 对象。 |
| mock object | 模拟对象 | 以可控属性和行为代替真实平台资源的测试对象。 |
| Objects.create() | 创建测试对象 | TSv1 测试 API，用于创建对象 mock。 |

## 疑问与待验证项

- 对象属性默认值、链接构造能力和未配置字段的行为需按 stub API 文档确认。
- 使用 mock 测试得到通过，不代表用户在真实权限下能读到该对象。

## 复刻启示

- 画布试算提供可重复样例对象和关系，并区分 mock 模式与真实数据源预览模式。
- 单元测试输出列出覆盖字段/链接；上线评审仍要求权限、查询和 Action 写入的集成验证。
