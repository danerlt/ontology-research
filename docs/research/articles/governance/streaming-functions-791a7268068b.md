<!-- 页面 URL：https://www.palantir.com/docs/foundry/functions/streaming-functions -->
<!-- 研读状态：已完成 -->

# Functions • Language-agnostic features • Streaming functions • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/functions/streaming-functions)
- 官方中文来源：尚未确认（配对状态：ambiguous）
- 页面语言：英文
- 主题栏目：functions
- 相关性：direct；本体函数文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:02:49Z
- 产品状态：页面当前未标注特定 Beta/预览/弃用状态；关联功能状态按引用子页复核。

## 英文原文短摘录（每个来源不超过 25 词）

> “Python and TypeScript v2 functions can stream the result of an execution in chunks.”

## 摘录译文

Python 和 TypeScript v2 函数可按数据块流式返回执行结果。

## 中文要点

- Python 与 TypeScript v2 支持按块流式返回；Python 函数以 `Iterable[T]` 返回类型并通过 `yield` 逐步产出，TypeScript v2 使用 async generator 与 `AsyncIterable<T>`。
- 分块输出适合结果逐步生成的长任务，例如模型生成；消费端可在完整执行结束前先处理已经到达的内容。
- 发布后可由 Ontology SDK React 应用、Workshop 自定义 widget 或另一函数调用；流式函数是特定语言/宿主能力，不代表所有普通函数调用都可流式。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| streaming function | 流式函数 | 执行期间分块返回结果的函数。 |
| Iterable[T] | 可迭代返回类型 | Python 以迭代器逐步产出 T 类型元素。 |
| AsyncIterable<T> | 异步可迭代返回类型 | TypeScript 异步生成器逐步产出元素的类型。 |
| yield | 产出 | 暂停并输出一个流式结果项的语句。 |

## 疑问与待验证项

- 各消费端对取消、超时、部分结果错误和背压的处理细节没有在摘要段说明，需与具体 OSDK/Workshop API 文档一并确认。
- 流式输出中间片段是否能够安全展示，应考虑用户权限、数据分类和生成内容审核。

## 复刻启示

- 为 Agent 响应和推理试算提供流式事件协议，区分进度、部分结果、最终结果和错误终止。
- 记录每个 chunk 的序号、来源计算步骤和取消状态；用户中断后停止后续昂贵计算。
