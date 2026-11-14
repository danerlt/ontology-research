<!-- 页面 URL：https://www.palantir.com/docs/foundry/agent-builder/core-concepts -->
<!-- 研读状态：已完成 -->

# Agent Builder • Core concepts • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/agent-builder/core-concepts)
- 官方中文来源：尚未确认（配对状态：ambiguous）
- 页面语言：英文
- 主题栏目：agent-builder
- 相关性：direct；Agent 构建文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:04:28Z
- 产品状态：Agent Builder 当前为 Beta；本页所述行为可能随开发变化；核对日期 2026-11-14

## 英文原文短摘录（每个来源不超过 25 词）

> “Tools let an agent access information or perform tasks during a session.”

## 摘录译文

工具让 Agent 能在会话期间访问信息或执行任务。

## 中文要点

Agent 运行由输入、预计算变量、提示词、工具和完成条件组成。预计算变量可查询对象集、调用函数或应用动作；含动作的变量会在会话启动时自动执行，即使未被其他配置引用。Preview 中动作逻辑会运行，但不会提交 Ontology 编辑；生产会话中则可能写入数据。工具可查询数据、调用动作、函数或自定义逻辑。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Input | 输入 | 会话开始前由应用或用户提供的值 |
| Pre-computed variable | 预计算变量 | 会话开始时预先计算并传入提示词/工具的值 |
| System prompt | 系统提示词 | 约束 Agent 行为、规则和可用上下文 |
| Tool | 工具 | 可被 Agent 选择调用的查询或任务能力 |
| Session completion | 会话完成条件 | 决定会话继续等待消息还是返回指定输出 |

## 疑问与待验证项

- 预计算变量内的动作自动执行，即便未被引用；产品需要验证作者是否能清楚看见这种副作用，并在生产执行前确认。
- Preview 会运行动作逻辑但不写入数据；需核对其他副作用是否同样被拦截，不能把 Preview 当作完整隔离环境。

## 复刻启示

- Agent 运行前做静态依赖分析，列出预计算变量递归引用的查询、函数和动作，并提示自动写入。
- 将 Preview 和生产执行分成不同执行策略：Preview 保留校验与结果展示，但不提交对象变更。
- 对 Agent 写工具记录输入、授权决定、预览差异、操作者确认和最终提交 ID。
