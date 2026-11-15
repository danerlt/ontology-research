<!-- 页面 URL：https://www.palantir.com/docs/foundry/palantir-mcp/overview -->
<!-- 研读状态：已完成 -->

# Palantir MCP • Overview • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/palantir-mcp/overview)
- 官方中文来源：目录中未发现对应中文页面
- 页面语言：英文
- 主题栏目：palantir-mcp
- 相关性：direct；Palantir MCP 文档
- 官方更新时间：页面未提供
- 目录核对时间：2026-11-15
- 产品状态：Palantir MCP 已公告 Generally available；提供开发者上下文与平台构建工具。

## 英文原文短摘录（每个来源不超过 25 词）

> “Palantir MCP is designed for ontology builders and can modify ontology types, but cannot write ontology data.”

## 摘录译文

Palantir MCP 面向本体构建者，可修改本体类型，但不能写入本体数据。

## 中文要点

- Palantir MCP 是 MCP 实现，可让 IDE/Agent 搜索文档与库、访问 Foundry 项目，辅助端到端应用开发、数据集/代码工作流和本体配置。
- Agent 可以搜本体并建议创建/修改 object/link/action type，也能操作 Developer Console 应用和代码资源；本体定义变更要生成 proposal，不能直接修改生产实例数据。
- 与 OMCP 分工：Palantir MCP 是构建侧；OMCP 是运行侧，通过应用限制让外部 Agent 读取对象并执行已定义的 Action。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| builder workflow | 构建工作流 | 使用代码与 MCP 工具建立/修改本体和应用。 |
| ontology consumer | 本体消费者 | 在生产工作流查询对象或运行既有 Action 的 Agent。 |
| context injection | 上下文注入 | 按当前仓库/资源类型给模型提供匹配文档和示例。 |

## 疑问与待验证项

- Palantir MCP 在本地连接外部 LLM 时，数据治理会延伸到该外部 Agent/模型供应商，不能只看 Foundry 授权。
- 结构修改需 proposal review；具体哪些工具在本地/Code Workspace 可调用取决于环境。

## 复刻启示

- 将系统工具按“建模与开发”“生产对象查询”“生产 Action 写入”做权限隔离与独立审计。
- 建立面向 Agent 的本体搜索、受控结构变更 proposal、代码上下文检索和安全写入接口；绝不把 schema 编辑工具当成数据操作工具。
