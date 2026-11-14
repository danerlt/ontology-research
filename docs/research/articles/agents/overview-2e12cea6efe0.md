<!-- 页面 URL：https://www.palantir.com/docs/foundry/agent-builder/overview -->
<!-- 研读状态：已完成 -->

# Agent Builder • Overview • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/agent-builder/overview)
- 官方中文来源：尚未确认（配对状态：ambiguous）
- 页面语言：英文
- 主题栏目：agent-builder
- 相关性：direct；Agent 构建文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T14:53:18Z
- 产品状态：Beta；官方说明仍在开发中且功能可能变化；核对日期 2026-11-14

## 英文原文短摘录（每个来源不超过 25 词）

> “Agent Builder is a visual interface for creating and publishing agents.”

## 摘录译文

Agent Builder 是用于创建和发布 Agent 的可视化界面。

## 中文要点

Agent Builder 允许配置系统提示词、输入、预计算变量和工具，并通过 Preview 调试 Agent。官方示例把对象集筛选、Ontology SQL 查询、自定义酒店库存工具和动作组合起来。发布后 Agent 成为 Compass 资源，可在 Agent Manager 查看会话，也可嵌入 Workshop 或由 Automate 触发。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Agent Builder | Agent 构建器 | 可视化编排和发布 Agent 的工具；当前为 Beta |
| Pre-computed variable | 预计算变量 | 在 Agent 启动前准备对象集或其他值 |
| Tool | 工具 | 让 Agent 查询 Ontology、调用动作或连接自定义能力 |
| Preview | 预览 | 测试会话输入、对话、工具调用和调试过程 |
| Compass resource | Compass 资源 | 已发布 Agent 的平台资源与访问入口 |

## 疑问与待验证项

- 页面标明 Beta，能力和配置方式可能变化；权限、模型、工具与发布版本的具体限制需以当前 enrollment 为准。
- 自定义工具和 Ontology 动作各自采用什么鉴权上下文，需结合安全文档核实。

## 复刻启示

- 用声明式 Agent 配置保存模型、系统提示词、初始消息、输入、预计算变量、工具及输出结构；发布时形成不可变版本。
- 将工具目录按只读查询、可写动作和外部自定义工具分组，并在运行前展示可能产生写入的步骤。
- Preview 要能重放输入和工具调用，同时明确哪些动作写入会被模拟或抑制。
