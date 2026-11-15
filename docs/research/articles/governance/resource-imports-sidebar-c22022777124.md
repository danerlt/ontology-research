<!-- 页面 URL：https://www.palantir.com/docs/foundry/functions/resource-imports-sidebar -->
<!-- 研读状态：已完成 -->

# Functions • TypeScript v1 • Import resources into Code Repositories • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/functions/resource-imports-sidebar)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/functions/resource-imports-sidebar)（配对状态：matched）
- 页面语言：英文
- 主题栏目：functions
- 相关性：direct；本体函数文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:03:07Z
- 产品状态：TSv1 资源导入指南；页面建议需要 OSDK/可配置资源请求时迁移 TSv2。

## 英文原文短摘录（每个来源不超过 25 词）

> “The Resource imports sidebar in Code Repositories offers a centralized interface to manage imported Foundry resources within your TypeScript functions repository.”

## 摘录译文

Code Repositories 中的资源导入侧栏提供集中界面，用于管理 TypeScript 函数仓库导入的 Foundry 资源。

## 中文要点

- Resource imports 侧栏统一管理 Ontology 类型、模型与部署、外部系统等仓库资源；选择后会重新启动 Code Assist 并重新生成代码绑定。
- 导入资源需关联同一 Ontology；切换所选 Ontology 会覆盖原来的其他 Ontology 导入。TSv1 模板将当前导入状态记录在仓库 `resources.json`，可用 Git 分支、审查和回滚。
- 可导入资源受 `functions.json` 中开关控制，例如模型函数、外部系统、Query 和时序属性；缺少开关可能导致 repository checks 失败。
- 具有依赖的资源会显示依赖关系；资源需有 API name 才能被代码引用。不同版本 value type 依赖冲突可能造成编译错误。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Resource imports | 资源导入 | 从平台选择并生成代码绑定的本体/平台资源配置。 |
| resources.json | 资源导入清单 | TSv1 仓库中可版本控制的资源导入状态文件。 |
| Code Assist | 代码辅助服务 | 根据当前导入资源生成类型绑定和代码补全。 |

## 疑问与待验证项

- 该侧栏所示导入位于 Project/仓库的关系不同于单仓依赖配置；文档明确部分 Ontology 导入会影响项目级资源权限。
- 资源切换、依赖升级和启用开关应一并通过版本控制评审。

## 复刻启示

- 本体资源画布旁提供依赖面板，把对象/链接/模型/外部连接器引用纳入分支 diff。
- schema 或连接器变更后重新生成绑定，展示生成版本、依赖冲突与受影响函数。
