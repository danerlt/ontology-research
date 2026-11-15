<!-- 页面 URL：https://www.palantir.com/docs/zh/foundry/functions/unit-test-stub-objects -->
<!-- 研读状态：已完成 -->

# 函数 • Unit testing • 创建存根对象 • Palantir

- 英文来源：[现行英文原文](https://www.palantir.com/docs/foundry/functions/unit-test-stub-objects)
- 官方中文来源：[官方中文页（AIP 机器翻译，准确性未独立验证）](https://www.palantir.com/docs/zh/foundry/functions/unit-test-stub-objects)
- 页面语言：中文（官方 AIP 机器翻译，需与英文原文交叉核对）
- 主题栏目：functions
- 相关性：direct；本体函数文档
- 官方更新时间：2026-11-12T17:46:46.935Z
- 目录核对时间：2026-11-14T14:59:47Z
- 产品状态：TSv1 测试可通过 `Objects.create()` 构造带主键和属性的 mock Ontology 对象，再像普通对象一样传给被测函数。

## 原文短摘录与翻译

> “You can create and define your mock objects using Objects.create().”

## 摘录译文

可以使用 `Objects.create()` 创建并定义 mock 对象。

## 中文要点

- 测试可创建类型化模拟对象并设置属性值，然后把该对象传入函数，断言业务逻辑对对象字段的读取/计算结果。
- 该方式适合不需要真实对象搜索或持久化服务的纯逻辑测试，也可以作为对象集查询测试中固定返回项。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| mock object | 模拟对象 | 单元测试中构造的本体对象替身 |
| `Objects.create()` | 对象构造器 | 创建测试对象实例的 TSv1 SDK API |
| fixture | 测试夹具 | 为测试准备的固定输入对象和属性值 |

## 疑问与待验证项

- 使用 `Objects.create()` 创建的是测试用对象实例，不会因此写入真实 Ontology；具体测试隔离由测试环境保证。
- 对象实例可以直接测试字段逻辑，但其权限、索引状态和链接加载与真实运行环境不同。

## 复刻启示

- 将函数/派生属性示例的对象身份与字段 fixture 固定化，使试算结果可重复，也可一键生成画布测试案例。
- UI 明确“模拟对象”与真实实例差异；用模拟数据跑通过后，仍单独检查权限过滤和多跳链接查询行为。
- 在对象图变更测试里使用临时身份构造新对象，验证 Action 计划引用它时不会依赖已持久化 RID。
