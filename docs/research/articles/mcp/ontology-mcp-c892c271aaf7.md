<!-- 页面 URL：https://www.palantir.com/docs/foundry/ontology-mcp -->
<!-- 研读状态：已完成 -->

# Ontology MCP • Overview • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/ontology-mcp)
- 官方中文来源：目录中未发现对应中文页面
- 页面语言：英文
- 主题栏目：ontology-mcp
- 相关性：direct；Ontology MCP 文档
- 官方更新时间：页面未提供
- 目录核对时间：2026-11-15
- 产品状态：Ontology MCP 与 Palantir MCP 均已于 2026 年 6 月公告为 Generally available，面向不同工作阶段。

## 英文原文短摘录（每个来源不超过 25 词）

> “Ontology MCP enables controlled writes to ontology data, while Palantir MCP enables modifications to ontology structure.”

## 摘录译文

Ontology MCP 通过受控方式写入本体数据；Palantir MCP 则用于修改本体结构。

## 中文要点

- Ontology MCP（OMCP）把 Developer Console 应用中的对象类型、动作和查询函数暴露为 MCP 工具，供外部 Agent 发现并调用。
- OMCP 面向本体消费者：在应用 restrictions 限制下读取对象、执行预定义动作和查询本体数据；Palantir MCP 面向本体构建者，可修改对象/链接/动作结构，但不能写本体实例数据。
- 连接外部模型提供商会把平台数据交给外部 MCP 客户端/模型处理；应明确应用暴露资源、授权、模型提供商和数据治理边界。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Ontology MCP (OMCP) | 本体 MCP | 供外部 Agent 受控消费本体对象/动作/查询的 MCP Server。 |
| Palantir MCP | Palantir MCP | 供开发者 Agent 获取 Foundry 上下文并修改结构/开发资源的 MCP。 |
| application restrictions | 应用限制 | 配置 OMCP 可暴露的本体资源范围。 |

## 疑问与待验证项

- OMCP 的 OAuth 身份、工具范围和底层对象权限必须同时检查；应用限制不是替代最终用户权限的全局授权。
- 本地 Agent 连接和平台内托管 Agent 的数据流不同，外部模型供应商如何使用请求数据须查看相应服务条款。

## 复刻启示

- 把“本体开发工具”与“生产数据操作工具”拆为不同 MCP 服务/角色，结构修改走分支提案，实例数据变更只调用预定义动作。
- 启用前显示外部数据去向、OAuth 身份、可见对象类型/动作/查询函数，并把限制默认设为最小授权。
