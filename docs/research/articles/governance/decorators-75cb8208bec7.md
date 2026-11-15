<!-- 页面 URL：https://www.palantir.com/docs/zh/foundry/functions/decorators -->
<!-- 研读状态：已完成 -->

# 函数 • TypeScript basics • 装饰器 • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/functions/decorators)
- 官方中文来源：尚未确认（配对状态：not_applicable）
- 页面语言：中文
- 主题栏目：functions
- 相关性：direct；本体函数文档
- 官方更新时间：2026-11-12T17:46:46.935Z
- 目录核对时间：2026-11-14T14:59:08Z
- 产品状态：官方中文页标注为未经验证的 AIP 机器翻译；英文原文为核对依据。

## 原文短摘录与翻译

> 英文原文：The method must be decorated with one of the following decorators imported from the @foundry/functions-api package.

> 中文译文：方法必须使用从 `@foundry/functions-api` 包导入的以下装饰器之一。

## 摘录译文

以上为英文短摘录及中文译文。官方中文页面为 AIP 机器翻译，准确性未经验证。

## 中文要点

- TSv1 函数必须是导出类的 public 方法，并使用 `@Function()`、`@OntologyEditFunction()` 或单独使用 `@Query({apiName})` 才会被发现和发布。
- 普通查询装饰器面向只读 API；OntologyEditFunction 用于 Action 支持的写入函数，可选以 `@Edits` 指示对象来源。
- 私有或未加正确装饰器的方法不会出现在函数注册表中，适合用作仓库内部辅助方法；类名和方法名共同决定函数标识。
- 此页专属 TypeScript v1；中文页是未经验证的机器翻译，TSv2/Python 使用不同的函数发现机制。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Decorator | 装饰器 | 在 TSv1 方法上标记查询、编辑或通用函数类型的元数据。 |
| Function registry | 函数注册表 | 平台发现并发布的函数清单。 |
| Query decorator | 查询装饰器 | 声明只读且可通过 Foundry API 调用的自定义查询。 |

## 疑问与待验证项

- 装饰器参数、导出路径和发布标识的变更是否创建新资源取决于函数版本管理规则，需结合版本文档确认。
- TSv2默认导出函数的注册和权限语义与 TSv1 装饰器不同，不可直接复制编程模型。

## 复刻启示

- 将函数类型（查询、编辑、通用）、输入输出 schema、写集和发布 API 名作为显式元数据。
- 函数编辑能力应单独申请写权限；私有 helper 不生成 API 端点，避免辅助逻辑被误公开。
