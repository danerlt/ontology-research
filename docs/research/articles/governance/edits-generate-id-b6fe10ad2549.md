<!-- 页面 URL：https://www.palantir.com/docs/foundry/functions/edits-generate-id -->
<!-- 研读状态：已完成 -->

# Functions • 为新对象生成唯一 ID（TypeScript） • Generate unique IDs for new objects • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/functions/edits-generate-id)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/functions/edits-generate-id)（配对状态：matched）
- 页面语言：英文
- 主题栏目：functions
- 相关性：direct；本体函数文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:03:05Z
- 产品状态：生成对象主键的 UUID 方式按 TypeScript 代际不同：TSv2 使用标准 npm 包，TSv1 使用平台工具包。

## 英文原文短摘录（每个来源不超过 25 词）

> “TypeScript v2 has no built-in or platform-specific UUID generator.”

## 摘录译文

TypeScript v2 没有内置或平台专属的 UUID 生成器。

## 中文要点

- 创建对象的本体编辑函数通常需要生成唯一 ID 作为主键；TSv2 页面建议通过 npm 的 uuid 包生成。
- TSv1 使用预装的 @foundry/functions-utils 的 Uuid.random()；若包缺失需加入依赖并重启 Code Assist。
- 两代函数都须在创建对象时把生成 ID 作为主键使用；随机生成并不替代服务端对主键唯一性的约束。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| UUID | 通用唯一标识符 | 用于新对象主键的高熵唯一 ID |
| Primary key | 主键 | 在对象类型内唯一识别本体对象的属性 |
| Uuid.random() | 平台 UUID 工具 | TSv1 functions-utils 提供的 ID 生成方法 |

## 疑问与待验证项

- 示例讨论 UUID 生成，未定义主键冲突出现后的重试策略；数据库唯一索引仍应作为最终保障。
- TSv2 标准 uuid 包的版本、依赖锁定和是否支持目标函数运行时要按仓库策略确认。

## 复刻启示

- 对象创建 API 支持服务端主键生成或调用者提供两种路径，统一校验唯一性并将冲突反馈为可重试错误。
- 按 SDK/runtime 版本选择 ID 能力，保留生成来源与幂等请求键，避免重试时重复创建对象。
