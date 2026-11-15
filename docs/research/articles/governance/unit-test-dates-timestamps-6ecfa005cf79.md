<!-- 页面 URL：https://www.palantir.com/docs/zh/foundry/functions/unit-test-dates-timestamps -->
<!-- 研读状态：已完成 -->

# 函数 • Unit testing • 模拟日期、时间戳和UUID • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/functions/unit-test-dates-timestamps)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/functions/unit-test-dates-timestamps)
- 页面语言：中文（官方 AIP 机器翻译，需与英文原文交叉核对）
- 主题栏目：functions
- 相关性：direct；本体函数文档
- 官方更新时间：2026-11-12T17:46:46.935Z
- 目录核对时间：2026-11-14T14:59:40Z
- 产品状态：该单元测试指南演示通过 Jest mock 固定 UUID、当前时间戳与当前日期；示例针对 TSv1，TSv2 对 UUID 的模拟需直接针对标准库。

## 英文原文短摘录（每个来源不超过 25 词）

> “You can specify the output of non-deterministic functions by utilizing jest.spyOn() to inject a mock to run the test.”

## 摘录译文

可使用 jest.spyOn() 注入 mock，为非确定性函数指定输出并运行测试。

## 中文要点

- 使用 `jest.spyOn()` 替换 `Uuid.random()`、`Timestamp.now()` 或 `LocalDate.now()` 的输出，令对象创建/编辑断言可重复。
- 对需要完全控制生成 ID 的代码，可以把 UUID supplier 作为构造参数注入，再在测试中传固定函数。
- TSv1 示例使用 `@foundry/functions-utils` 的 `Uuid`；TSv2 可使用标准 UUID 库并直接 mock 对应实现。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| non-deterministic function | 非确定性函数 | 同一输入下输出会随时间或随机数变化的函数 |
| `jest.spyOn()` | Jest spy/mock | 替换或监视模块函数输出的测试工具 |
| UUID supplier | UUID 生成器 | 负责提供对象唯一 ID、可被测试注入的函数 |
| `Timestamp.now()` | 当前时间戳 | 取得执行时刻的平台时间函数 |

## 疑问与待验证项

- 示例主要使用 Ontology edit verification 校验含随机 ID/当前时间的对象修改；时间时区、系统时钟与固定时区转换还应单独覆盖。
- 本文 TSv1 与 TSv2 的 UUID 库差异提示测试工具不能照搬；其他时间类型的构造/序列化也需核对相应版本 API。

## 复刻启示

- 规则引擎与 Agent 规划器把当前时间、UUID/幂等键等非确定性依赖通过显式 clock/ID provider 注入，支持固定输入重放。
- 运行审计记录真实执行时间和对象身份；模拟试算可固定这些依赖以比较分支前后推导结果。
- 迁移或升级函数运行时要审查测试 mock 边界，避免相同业务函数在 TSv1/TSv2 下出现未预期的随机差异。
