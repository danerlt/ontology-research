<!-- 页面 URL：https://www.palantir.com/docs/foundry/agent-sdk/overview -->
<!-- 研读状态：已完成 -->

# Agent SDK • Overview • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/agent-sdk/overview)
- 官方中文来源：尚未确认（配对状态：ambiguous）
- 页面语言：英文
- 主题栏目：agent-sdk
- 相关性：direct；Agent SDK 文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:04:29Z
- 产品状态：本页未标记 Beta 或弃用状态；核对日期 2026-11-14

## 英文原文短摘录（每个来源不超过 25 词）

> “The Palantir Agent SDK is a pro-code way to build agents on the Agent Stack.”

## 摘录译文

Palantir Agent SDK 是在 Agent Stack 上以代码构建 Agent 的方式。

## 中文要点

Agent SDK 用 TypeScript 将自定义 Agent 发布为 Foundry 资源，适用于需要自定义观测界面、人机协作和确定性逻辑的场景。运行框架可扩展类型化上下文项、事件和 effects，并且模型与 Agent harness 解耦，可调用开源或主权模型。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Pro-code agent | 代码式 Agent | 通过 TypeScript SDK 定义并发布的 Agent |
| Context item | 上下文项 | SDK 可自定义的会话数据结构 |
| Event handler | 事件处理器 | 响应用户/工具/外部事件的确定性逻辑 |
| Effect | 效果 | Agent 执行中封装的外部操作 |
| Model agnostic | 模型无关 | 运行逻辑不绑定单一模型提供方 |

## 疑问与待验证项

- 该概览只说明能力边界，未列出 Agent 版本发布、依赖、回滚和扩缩容细节；需阅读 SDK 开发文档。
- 开源/主权模型接入仍需遵循组织数据流和密钥治理，文档概览未给出具体安全策略。

## 复刻启示

- 抽象 Agent runtime 接口，区分 session store、typed context、event handler、tool adapter 与 model adapter。
- 允许开发者注入确定性校验与人审节点；Agent 的模型选择不应改变授权判断和动作执行策略。
- 用资源版本发布 SDK Agent，并让管理 UI 能关联源码、构建信息与会话观测。
