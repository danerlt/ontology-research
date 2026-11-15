<!-- 页面 URL：https://www.palantir.com/docs/foundry/functions/decorators -->
<!-- 研读状态：已完成 -->

# Functions • 装饰器（TypeScript v1） • Decorators • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/functions/decorators)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/functions/decorators)（配对状态：matched）
- 页面语言：英文
- 主题栏目：functions
- 相关性：direct；本体函数文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:03:04Z
- 产品状态：TSv1 函数由公开方法、导出类和装饰器共同发现；通用函数、编辑函数和只读 Query 用途不同。

## 英文原文短摘录（每个来源不超过 25 词）

> “The method must be public.”

## 摘录译文

该方法必须是 public。

## 中文要点

- 类方法须为 public，所属类从 functions-typescript/src/index.ts 导出，并由 @foundry/functions-api 的装饰器标记，才会被发现并发布。
- @Function() 定义通用函数；@OntologyEditFunction() 定义用于支撑 Action 的编辑函数，可用 @Edits([object type]) 声明对象来源范围。
- 若缺少 @Edits，平台会尽力从代码静态分析推断编辑对象范围，属于 best effort。
- @Query({ apiName }) 定义只读、通过 Foundry API 执行的查询，须单独使用，不与 @Function 同时装饰。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| @Function | 通用函数装饰器 | 标记可被平台调用的一般函数 |
| @OntologyEditFunction | 本体编辑装饰器 | 标记可用于 Action 的对象编辑函数 |
| @Query | 查询装饰器 | 定义只读 API 查询函数 |

## 疑问与待验证项

- 依赖静态推断的对象来源只是 best effort；代码重构后应显式声明 @Edits 以免元数据范围漂移。
- TSv1 装饰器发现规则不能直接套用到 TSv2/Python 导出模型。

## 复刻启示

- 代码导出扫描应检查方法可见性、导出入口、函数类别与唯一 API Name，错误提示具体到文件/方法。
- 把只读 Query 与写入 Action 函数分开标注，构建阶段禁止误将 Query 当编辑动作暴露。
