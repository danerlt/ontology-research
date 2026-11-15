<!-- 页面 URL：https://www.palantir.com/docs/foundry/functions/local-sdks -->
<!-- 研读状态：已完成 -->

# Functions • TypeScript v2 • Local Ontology SDKs • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/functions/local-sdks)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：functions
- 相关性：direct；本体函数文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:02:50Z
- 产品状态：未见本页另标 Beta、预览或弃用状态。

## 英文原文短摘录（每个来源不超过 25 词）

> SDK types are always up-to-date with the latest resource imports.

## 摘录译文

SDK 类型始终与最新资源导入保持同步。

## 中文要点

- TSv2 与 Python 函数支持本地 OSDK：从仓库选入的对象类型、链接类型、接口类型等资源自动生成绑定，不再单独安装并手动版本化 OSDK 包。
- 资源导入改变后，代码绑定随之更新；函数打版本时，CI 会把当时本体资源状态对应的 SDK 一并生成并打包。
- 本地 OSDK 是完整 Global Branching 支持的必要条件；文档也给出 rune CLI 生成/再生成和从独立 SDK 迁移的操作。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Local Ontology SDK | 本地本体 SDK | 由仓库资源导入自动生成的类型及客户端绑定。 |
| Resource imports | 资源导入 | 仓库显式依赖的本体对象、链接、接口等资源集合。 |
| Global Branching | 全局分支 | 在分支中协同管理代码和本体资源的能力。 |

## 疑问与待验证项

- 打版本后 SDK 绑定与 Ontology schema 的耦合意味着发布构建应固定并显示资源快照；回滚如何恢复资源状态需查分支/发布文档。
- 自动同步的具体触发时机、生成失败处理及本地工具版本应结合目标仓库模板验证。

## 复刻启示

- 让函数或本体规则显式绑定项目/分支的 schema 版本，并在 CI 构建时生成可复现客户端类型。
- 资源依赖可视化要展示导入清单、生成时间、版本差异和构建失败原因；发布快照不可悄悄漂移。
