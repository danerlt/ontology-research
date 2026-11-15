<!-- 页面 URL：https://www.palantir.com/docs/foundry/functions/webhooks -->
<!-- 研读状态：已完成 -->

# Functions • TypeScript v1 • Use webhooks • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/functions/webhooks)
- 官方中文来源：尚未确认（配对状态：ambiguous）
- 页面语言：英文
- 主题栏目：functions
- 相关性：direct；本体函数文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:03:10Z
- 产品状态：当前页面代码示例针对 TSv1；TSv2 与 Python 需将 webhook 发布为 webhook function 后再经 OSDK 调用。

## 英文原文短摘录（每个来源不超过 25 词）

> “This guide will walk you through setting up a function that can make requests to external systems using webhooks.”

## 摘录译文

本指南介绍如何在函数中设置 webhook，以便向外部系统发起请求。

## 中文要点

- TSv1 函数导入 REST API source 后可通过 `@foundry/external-systems` 调用 webhook；要启用相关导入需打开 `enableExternalSystems`。
- Query 中的 webhook 只能执行只读 Read API，因为 Query 可能重试或在页面加载时静默触发；写 API 应放到有明确用户意图和授权的 Ontology Edit Action。
- Webhook 支持常用标量、日期时间、列表和 record 类型，但不支持 OR 参数类型；发布函数时会固定当前 webhook 版本。改 webhook 后需要重新发布/升级消费者。
- 函数写入本体与外部系统并非一个原子事务：外部写成功而本体写失败时会产生不一致。页面建议用明确类型、测试工具、isOk/isErr 错误检查和状态补偿。
- 通过 Function-backed Action 调用 webhook 时，终端用户按 Action 提交条件授权，不一定需要 webhook/source 权限；配置者仍需相应授权。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| webhook | Webhook / 网络钩子 | 通过 Data Connection source 向外部 API 发起请求。 |
| Read API / Write API | 只读 API / 写入 API | 标识 webhook 是否会修改外部系统。 |
| webhook function | Webhook 函数 | 可作为可复用本体函数导入调用的 webhook。 |
| dual write | 双系统写入 | 同一工作流同时写本体和外部系统。 |

## 疑问与待验证项

- Webhook 版本在发布 Function 时固定，需在 source、webhook 和函数版本之间维护兼容矩阵。
- 本体与外部系统无法共享事务；重试、幂等、补偿、审计和用户可见状态必须明确。

## 复刻启示

- 把只读查询工具和外部写入动作分离；Agent 不能通过读取 Query 意外触发外部写副作用。
- 跨系统写回建立幂等标识、事务状态对象和失败补偿流程，并在画布显示外部节点结果。
