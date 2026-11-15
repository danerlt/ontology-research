<!-- 页面 URL：https://www.palantir.com/docs/foundry/functions/undefined-values -->
<!-- 研读状态：已完成 -->

# Functions • TypeScript v1 • Handle undefined values • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/functions/undefined-values)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/functions/undefined-values)（配对状态：matched）
- 页面语言：英文
- 主题栏目：functions
- 相关性：direct；本体函数文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:03:05Z
- 产品状态：TSv1 专属指南；页面推荐显式检查，并建议对更强类型支持评估 TSv2。

## 英文原文短摘录（每个来源不超过 25 词）

> “Below are two useful patterns for handling `undefined` values which may be returned from accessing properties or links.”

## 摘录译文

下面介绍两种处理读取属性或链接时可能返回的 undefined 值的方法。

## 中文要点

- TSv1 属性或单链接读取可能得到 `undefined`，调用代码需在严格类型检查下处理缺值。
- 首选显式条件检查：在缺少必需字段时抛出有意义的 `UserFacingError`，并让编译器收窄类型。
- 非空断言 `!` 只压制编译器的 undefined 检查；如果运行时确实为空，会产生难理解的失败，文档建议尽量显式检查。
- TypeScript v1 页面提示迁移到 TSv2 可获得 OSDK 等能力；不同版本的链接读取缺值行为需参照迁移指南。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| undefined | 未定义值 | 对象属性未设置或链接无匹配时可能出现的值。 |
| explicit check | 显式检查 | 先判断值是否存在，再执行后续逻辑。 |
| non-null assertion operator | 非空断言运算符 | 用 `!` 告诉编译器假定值非空，不会做运行时校验。 |

## 疑问与待验证项

- 非空断言是否会令运行时错误更难定位，关键在缺值约束是否由 schema/Action 提交条件保证。
- TSv1 与 TSv2 单链接读取在缺失对象时的异常语义不同，迁移需专项检查。

## 复刻启示

- 在本体属性 schema 中区分必填、可空和链接零匹配，生成语言 SDK 对应的 Optional 类型。
- 编辑器对未经守卫的可空值给出就地提示，并提供明确的空值处理分支和用户可读错误。
