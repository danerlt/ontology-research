<!-- 页面 URL：https://www.palantir.com/docs/foundry/palantir-mcp/security -->
<!-- 研读状态：已完成 -->

# Palantir MCP • Security • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/palantir-mcp/security)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：palantir-mcp
- 相关性：direct；Palantir MCP 文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:04:56Z
- 产品状态：待核对 Beta、预览、弃用或更名信息

## 英文原文短摘录（每个来源不超过 25 词）

> “All ontology modifications (including deletions) must be processed through a proposal review; human approval is required to merge changes into your main ontology.”

## 摘录译文

“所有本体结构修改（包括删除）都必须经过提案审阅；合并到主本体需要人工批准。”

## 中文要点

PMCP 的安全文档区分平台内与本地开发的数据流。平台内 IDE 集成沿用组织在 Foundry 的治理边界；本地 MCP 默认禁用，启用后工具输出可能传给外部 AI 厂商，数据治理依赖组织与厂商的协议。写工具范围有限，不提供破坏性写入；本体结构修改必须经提案审阅和人工批准。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Data flow | 数据流 | MCP 工具结果进入 Agent/模型后的传输路径 |
| Non-destructive write | 非破坏性写入 | 不覆盖或删除既有数据的受限写入操作 |
| Proposal review | 提案审阅 | 本体结构修改进入主分支前的人工治理步骤 |
| Local development | 本地开发 | 在 Foundry 外部电脑上运行 MCP 客户端的环境 |

## 疑问与待验证项

- 文档要求本地使用前显式启用，并提醒外部模型供应商可能获得工具输出；部署时需让用户能辨别数据是否离开组织平台。
- 对“非破坏性”的允许范围应结合具体工具列表和平台版本检查，不能把这一概述当作完整 API 清单。

## 复刻启示

- 把 Agent 的数据平面和 schema 管理平面分开：Agent 可调用有界 Action，结构改动进入人工审阅/合并。
- 当前原型的提案合并需要管理员批准；如开放外部 MCP，应增加工具数据流提示、用途范围、模型接收方说明以及按资源审查机制。
