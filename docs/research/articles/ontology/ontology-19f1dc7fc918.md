<!-- 页面 URL：https://www.palantir.com/docs/foundry/code-workspaces/ontology -->
<!-- 研读状态：已完成 -->

# Code Workspaces • Interact with the Ontology • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/code-workspaces/ontology)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/code-workspaces/ontology)（目录配对状态：matched）
- 页面语言：英文
- 主题栏目：code-workspaces
- 相关性：direct；Code Workspace 中选择本体实体和生成 OSDK
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:05:35Z
- 产品状态：每个 Code Workspace 一个 OSDK 配置；生成版本发布成功后才可用

## 英文原文短摘录（不超过 25 词）

> “Each Code Workspace can have one SDK, and multiple versions of each SDK can be created.”

## 摘录译文

每个 Code Workspace 可配置一个 SDK，并可创建该 SDK 的多个版本。

## 中文要点

- 在 Ontology 侧栏创建 SDK，配置包名和关联 Ontology；包名一经发布不可更改。
- Data entities 页签用于导入对象类型和 Action 类型；SDK generation 页签查看、发布与安装 SDK 版本。
- 选中 Action 时，依赖的对象类型会自动加入；对象类型 backing data source 未导入 workspace project scope 时，平台会提示自动导入。
- 改选另一 Ontology 会清空当前 SDK 已选对象、Action 和链接，再生成新版本。
- 版本生成后需等状态变为 Published 才可在代码中安装；引用 Action 未导入依赖对象或 backing source 不在项目范围内会导致发布失败。
- 已发布版本可提供与编辑器语言匹配的安装包和客户端初始化代码片段；具体可见对象/链接的例子可从 Data entities 选择资源查看。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| data entity | 数据实体 | 可由 SDK 导入的对象或 Action 类型 |
| SDK generation | SDK 生成 | 将本体资源选择编译为可安装客户端版本 |
| project scope | 项目范围 | Code Workspace 可访问的来源数据资源范围 |
| Published | 已发布 | SDK 版本完成生成且可被安装使用的状态 |

## 疑问与待验证项

- 每个工作区一个 SDK 的限制是配置层约束，多个不同 SDK 可否通过不同工作区组合未在本文展开。
- changing Ontology 会清空资源选择，操作影响大，需确认是否支持撤销及旧版本回滚。
- 页面示例跨 Python、TypeScript 等语言；具体语法和受支持对象类型需由对应 SDK 文档验证。

## 复刻启示

- SDK Builder 使用“本体选择→对象/Action 选择→依赖闭包→项目数据源范围→生成→发布”的有状态流程。
- 生成版本保留不可变包名、资源快照、生成器、依赖和状态；失败项必须指出缺失的对象/数据源依赖。
- 修改本体或资源范围时预览将清除/新增的资源并形成新版本，已发布版本继续可追溯。