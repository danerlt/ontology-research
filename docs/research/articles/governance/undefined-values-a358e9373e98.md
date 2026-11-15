<!-- 页面 URL：https://www.palantir.com/docs/zh/foundry/functions/undefined-values -->
<!-- 研读状态：已完成 -->

# 函数 • TypeScript basics • 处理未定义值 • Palantir

- 英文来源：[现行英文原文](https://www.palantir.com/docs/foundry/functions/undefined-values)
- 官方中文来源：[官方中文页（AIP 机器翻译，准确性未独立验证）](https://www.palantir.com/docs/zh/foundry/functions/undefined-values)
- 页面语言：中文（官方 AIP 机器翻译，需与英文原文交叉核对）
- 主题栏目：functions
- 相关性：direct；本体函数文档
- 官方更新时间：2026-11-12T17:46:46.935Z
- 目录核对时间：2026-11-14T14:59:40Z
- 产品状态：该页面专门介绍 TypeScript v1 中处理对象属性或链接访问返回的 undefined；文档推荐显式检查而非滥用非空断言。

## 原文短摘录与翻译

> “Below are two useful patterns for handling undefined values which may be returned from accessing properties or links.”

## 摘录译文

下面介绍两种处理属性或链接访问可能返回的 undefined 值的实用方式。

## 中文要点

- 对可能不存在的对象字段或关联链接做显式判断，可让编译器收窄类型，并在缺失时返回可读的 `UserFacingError`。
- 非空断言 `!` 只是跳过 TypeScript 的 undefined 检查，不会在运行时确保值存在；取值缺失时会引发更难定位的错误。
- 本页明确针对 TSv1 函数，并建议需要更完整能力时迁移 TSv2。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| undefined | 未定义值 | 对象属性或链接不存在/未取到时出现的空缺状态 |
| explicit check | 显式检查 | 在继续计算前确认可选值存在的分支校验 |
| non-null assertion | 非空断言 | 告诉编译器忽略 undefined 可能性的一元 `!` |
| UserFacingError | 用户可见错误 | 以面向用户的消息表达业务输入/状态问题的错误类型 |

## 疑问与待验证项

- 业务中“属性未赋值”和“对象无权限读取”是否均表现为 undefined，需结合对象权限文档确认，不能据此泄露字段是否存在。
- 非空断言不会添加运行时检查；对外输入和 Agent 工具返回值应保留可空 schema 并有显式错误分支。

## 复刻启示

- 派生属性求值器应把缺失值作为独立结果状态呈现，并区分无关联对象、字段未赋值、权限过滤和计算错误。
- 公式与函数编辑器在保存时校验可空类型；危险的“强制非空”需要显式表达并在试算样例中展示失败行为。
- 面向用户的错误保持业务可理解，同时在审计日志附带字段、路径和执行上下文。
