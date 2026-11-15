<!-- 页面 URL：https://www.palantir.com/docs/foundry/agents/branching -->
<!-- 研读状态：已完成 -->

# Pro-code agents • Core concepts • Develop pro-code agents on a global branch • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/agents/branching)
- 官方中文来源：尚未确认（配对状态：ambiguous）
- 页面语言：英文
- 主题栏目：agents
- 相关性：direct；Agent 文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:05:32Z
- 产品状态：页面标注 Beta。分支支持有边界：OSDK/OMCP 数据操作可针对分支，但 schema 仍取 main；Palantir MCP 与平台 API 不具备分支上下文。

## 英文原文短摘录（每个来源不超过 25 词）

> “OSDK and Ontology MCP operations target the selected global branch.”

## 摘录译文

OSDK 和 Ontology MCP 操作会指向当前选中的全局分支。

## 中文要点

- 将 Agent 仓库加入 Global Branching 后，本地运行可继承对应分支；OSDK/OMCP 读写以及同分支发布的 Agent function 可与 main 隔离。
- 分支中的类型变更尚未反映到 schema/生成工具；Palantir MCP 不支持分支上下文，不能用于检查或修改分支资源。
- 分支预发布经仓库 UI 的 Tag version/Tag and release 创建，合入 main 走 Global Branch proposal；不能直接用 Git tag 发布分支版本。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Global Branching | 全局分支 | 对代码、本体及其他资源变更进行隔离开发和评审。 |
| branched pre-release | 分支预发布版本 | 仅由对应分支资源解析的 Agent 版本。 |
| global branch proposal | 全局分支提案 | 经检查与评审后将变更合入 main 的载体。 |

## 疑问与待验证项

- - Agent 在分支运行不代表所有工具都隔离；每个连接器都应声明分支能力。
- - Beta 能力可能变化，应分别记录 branch、schema revision、数据 revision。

## 复刻启示

- - branch_id 要贯穿对象读写、推理试算、Agent 调用、变更集和审计；不支持分支的工具必须明确阻止写主线。
- - 发布检查展示 schema/data 目标与不支持分支的依赖；合并前校验基线、冲突和评审状态。
