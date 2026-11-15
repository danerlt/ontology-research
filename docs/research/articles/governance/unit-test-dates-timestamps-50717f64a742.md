<!-- 页面 URL：https://www.palantir.com/docs/foundry/functions/unit-test-dates-timestamps -->
<!-- 研读状态：已完成 -->

# Functions • Unit testing (TSv1) • Mock dates, timestamps, and UUIDs • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/functions/unit-test-dates-timestamps)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/functions/unit-test-dates-timestamps)（配对状态：matched）
- 页面语言：英文
- 主题栏目：functions
- 相关性：direct；本体函数文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:03:26Z
- 产品状态：TSv1 Jest 测试技巧；TSv2 UUID 应按其标准 UUID 库直接模拟。

## 英文原文短摘录（每个来源不超过 25 词）

> “You can specify the output of non-deterministic functions by utilizing `jest.spyOn()` to inject a mock to run the test.”

## 摘录译文

可通过 jest.spyOn() 注入 mock，指定非确定性函数的输出以运行测试。

## 中文要点

- 通过 `jest.spyOn()` mock `LocalDate.now()`、`Timestamp.now()` 和 TSv1 `Uuid.random()`，让日期、时间戳与新对象 ID 在每次测试中固定。
- UUID 还能通过构造函数注入 supplier 完全控制；TypeScript v2 应按其使用的标准 UUID npm 库直接 mock。
- 固定时间与 ID 可验证编辑函数写入的精确字段和对象主键，避免测试受系统当前时间、时区或随机值影响。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| non-deterministic function | 非确定性函数 | 同一输入下输出随时间或随机数变化的函数。 |
| jest.spyOn() | Jest 监视/模拟 | 替换目标方法实现以返回可控测试值。 |
| Timestamp.now() | 当前时间戳 | 产生当前时刻的平台时间戳函数。 |
| Uuid.random() | 随机 UUID | TSv1 生成新对象 ID 的工具方法。 |

## 疑问与待验证项

- 时区和日期边界在 mock 值中仍需明确；测试应覆盖 UTC 偏移、夏令时和日期跨界。
- TSv1 与 TSv2 UUID 来源不同，应避免迁移后沿用原测试 mock。

## 复刻启示

- 规则执行的当前时间应作为可注入依赖，预览和重放使用明确固定的 `as_of` 时间。
- 对自动生成的 ID 使用可替换标识供应器，支持可重复测试和执行审计追踪。
