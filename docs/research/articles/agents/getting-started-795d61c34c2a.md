<!-- 页面 URL：https://www.palantir.com/docs/foundry/agent-builder/getting-started -->
<!-- 研读状态：已完成 -->

# Agent Builder • Getting started • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/agent-builder/getting-started)
- 官方中文来源：目录中未发现对应中文页面
- 页面语言：英文
- 主题栏目：agent-builder
- 相关性：direct；Agent 构建文档
- 官方更新时间：页面未提供
- 目录核对时间：2026-11-15
- 产品状态：Agent Builder Beta；工作流包含配置、预览和资源发布。

## 英文原文短摘录（每个来源不超过 25 词）

> “Create an agent in Agent Builder, test it in Preview, and publish it.”

## 摘录译文

在 Agent Builder 中创建 Agent，在 Preview 中测试并发布。

## 中文要点

- Agent 配置由模型、系统提示词、初始用户消息、输入、预计算变量、工具和会话完成条件组成。变量可通过对象集过滤、函数或 Action 准备上下文。
- 预览面板可启动会话，Debug 可检查预计算变量、消息和工具调用；配置变更后应启动新会话验证。
- 预览期 Action 仍会运行，但不会应用本体编辑；发布到生产后，预计算变量内 Action 的编辑才会落地。发布 Agent 成 Compass 资源后可在 Workshop 或 Automate 使用，并在 Agent Manager 查看 session。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| pre-computed variable | 预计算变量 | 在 Agent 推理开始前执行并向 prompt/tool 提供的上下文计算。 |
| Preview | 预览 | 隔离本体编辑副作用的交互式 Agent 测试会话。 |
| session completion | 会话完成条件 | 决定 Agent 持续对话或结构化输出后结束。 |

## 疑问与待验证项

- 文档提到预计算变量可以包含 Action，而且即使变量未被引用也会执行；配置者需要识别这类隐式副作用。
- Preview 的本体写入行为与真实发布运行不同，测试 UI 必须明确告知用户数据不会持久写入。

## 复刻启示

- 在 Agent 配置流程中将读取/计算/写入工具分组，Action 标注会产生写入并提供权限与提交预览。
- 提供 Preview、逐步执行轨迹、发布版本和运行会话列表；预览运行不提交数据，真实运行需有单独授权与审计。
