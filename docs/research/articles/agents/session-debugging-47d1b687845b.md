<!-- 页面 URL：https://www.palantir.com/docs/foundry/agent-manager/session-debugging -->
<!-- 研读状态：已完成 -->

# Agent Manager • Investigate a session • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/agent-manager/session-debugging)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：agent-manager
- 相关性：direct；Agent Manager 文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:04:29Z
- 产品状态：待核对 Beta、预览、弃用或更名信息

## 英文原文短摘录（每个来源不超过 25 词）

> “Every event that occurs over the course of a session is shown on the timeline.”

## 摘录译文

“会话期间发生的每个事件都会显示在时间线上。”

## 中文要点

会话调试视图以事件时间线串起 Agent 的实际行为。可按事件类型或时间范围筛选，也可在类型和 payload 中搜索；Preview 以对话形式呈现消息和工具调用，Raw 显示未格式化上下文。用户可查看初始输入和 Agent 状态、回到历史时间点，并在可用时打开 Trace 和 Logs 定位执行细节。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Timeline | 时间线 | 按顺序呈现会话事件的导航视图 |
| Preview pane | 预览窗格 | 将会话上下文呈现为消息和工具调用 |
| Raw pane | 原始窗格 | 查看未经格式化的上下文项 |
| Agent state | Agent 状态 | 某个历史时点的会话/运行状态 |

## 疑问与待验证项

- Trace 与 Logs 取决于是否有对应数据；UI 不应无数据时渲染成“运行正常”。
- 回看历史状态并非只按创建时间排序事件，需保存足以重建上下文的事件/快照。

## 复刻启示

- 会话记录要有可排序事件、可检索 payload、上下文视图和事件时间点；另提供 trace/log 关联但明确可用性。
- 当前原型有 PostgreSQL 轨迹和 Redis 缓存、按序事件 API，但 UI 尚无筛选、搜索、Raw/Preview 双视图或状态时间旅行。
