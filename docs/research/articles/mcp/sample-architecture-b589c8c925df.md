<!-- 页面 URL：https://www.palantir.com/docs/foundry/ontology-mcp/sample-architecture -->
<!-- 研读状态：已完成 -->

# Ontology MCP • Sample architecture • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/ontology-mcp/sample-architecture)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：ontology-mcp
- 相关性：direct；Ontology MCP 文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:04:48Z
- 产品状态：待核对 Beta、预览、弃用或更名信息

## 英文原文短摘录（每个来源不超过 25 词）

> “Each action type included in the application becomes its own MCP tool”

## 摘录译文

“应用中每个纳入的 Action 类型都会成为一个独立 MCP 工具。”

## 中文要点

示例架构说明 MCP 工具集合来自应用显式包含的本体资源：对象类型通过 SQL 查询工具供 Agent 读取；每个 Action 类型对应一个写入工具；查询函数可作为定制读取/计算工具；Agent 本身也可包装成上层 Agent 的工具。文档把本体视作系统记录源，由专门 Agent 完成局部任务，再由编排 Agent 协调。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Tool exposure | 工具暴露 | 应用所选资源映射为 Agent 可调用的工具 |
| SQL tool | SQL 查询工具 | 读取应用暴露对象类型的数据接口 |
| Query function | 查询函数 | 作者定义的专用读取或计算工具 |
| Orchestration agent | 编排 Agent | 分解工作并调用其他 Agent/工具的上层 Agent |

## 疑问与待验证项

- 该示例只将选入 Developer Console 应用的资源暴露出来；工具目录并不等价于 Foundry 全环境资源目录。
- 读取 SQL 与 Action 写入是不同权限面，不能把对查询工具的授权推导为 Action 写权限。

## 复刻启示

- 维护 Agent 可见的工具注册表，并按对象类型、Action 与 query function 分别授权；Agent-to-Agent 组合也应记录调用链。
- 当前 Agent allowlist 已限制工具和 Action，但没有应用范围的对象白名单、查询函数工具或 Agent 编排层。
