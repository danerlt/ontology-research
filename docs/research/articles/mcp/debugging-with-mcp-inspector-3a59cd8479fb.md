<!-- 页面 URL：https://www.palantir.com/docs/foundry/ontology-mcp/debugging-with-mcp-inspector -->
<!-- 研读状态：已完成 -->

# Ontology MCP • Debugging with MCP Inspector • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/ontology-mcp/debugging-with-mcp-inspector)
- 官方中文来源：目录中未发现对应中文页面
- 页面语言：英文
- 主题栏目：ontology-mcp
- 相关性：direct；Ontology MCP 文档
- 官方更新时间：页面未提供
- 目录核对时间：2026-11-15
- 产品状态：OMCP 调试指南；需要在 Developer Console 启用服务器并使用客户端认证。

## 英文原文短摘录（每个来源不超过 25 词）

> “MCP Inspector is an open-source developer tool for testing and debugging MCP servers.”

## 摘录译文

MCP Inspector 是用于测试和调试 MCP Server 的开源开发工具。

## 中文要点

- 连接前要为应用启用 Ontology MCP；开发者从 Developer Console 获取连接设置，并在 Inspector 的 Authentication 区填写 client ID，机密客户端还可能需要 secret。
- Inspector 显示受应用 restrictions 限定的工具清单，可查看每个工具的输入 schema、填写参数执行并检查成功/错误响应。
- 工具历史保留请求和响应，便于定位工具缺失、参数错误或权限拒绝；当前 OMCP 不支持 prompts/resources，因此 Inspector 对应标签为空。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| MCP Inspector | MCP Inspector | 连接 MCP server、查看工具和运行测试调用的交互式工具。 |
| application restrictions | 应用限制 | 决定某个 OMCP 应用暴露哪些本体资源与工具。 |
| tool history | 工具历史 | 查看 MCP 请求、执行与响应的调试记录。 |

## 疑问与待验证项

- Inspector 中成功调用的测试可能执行真实 action；测试环境应使用明确的应用身份和安全数据。
- 文档指出 prompts/resources 不支持；不要假设 OMCP 等同于完整 MCP 原语集合。

## 复刻启示

- 增加本地工具调试面板：显示工具 schema、身份、授权结果、输入、响应和错误码。
- 暴露给 Agent 的工具清单必须从应用级 allowlist 派生，并对每次调用验证授权；保留结构化请求历史供排查。
