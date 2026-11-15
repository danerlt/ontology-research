<!-- 页面 URL：https://www.palantir.com/docs/foundry/functions/typescript-v2-getting-started -->
<!-- 研读状态：已完成 -->

# Functions • TypeScript v2 • Getting started • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/functions/typescript-v2-getting-started)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：functions
- 相关性：direct；本体函数文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:02:50Z
- 产品状态：页面当前未标注特定 Beta/预览/弃用状态；关联功能状态按引用子页复核。

## 英文原文短摘录（每个来源不超过 25 词）

> “TypeScript v2 allows users to take advantage of several key improvements over TypeScript v1, including a Node.js runtime and first-class OSDK support.”

## 摘录译文

TypeScript v2 相比 v1 提供 Node.js 运行时和一等 OSDK 支持等改进。

## 中文要点

- TypeScript v2 使用完整 Node.js runtime，并原生集成 OSDK；需在 TypeScript functions repository 中的 `src/functions` 目录写 `.ts` 文件，并以 `export default` 导出函数。
- 文件名必须与函数名匹配，函数只能默认导出一个函数；输入/输出类型必须符合平台类型参考。导入对象/链接类型前需从资源侧栏导入并生成、安装 OSDK。
- Live preview 可测试函数；提交后运行 checks，再通过 Tag version 发布仓库内所有函数。发布权限可能需要传播时间后才可在应用中搜索到。
- 入门指南把 Ontology SDK、Ontology edits 和 Beta staged writes 列为后续主题；这些不是创建最小函数所必需的。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Node.js runtime | Node.js 运行时 | TypeScript v2 函数执行环境。 |
| default export | 默认导出 | Foundry 发现并注册函数的模块导出方式。 |
| Live preview | 实时预览 | 在发布前运行函数并检查输出的开发工具。 |
| Tag version | 版本标签 | 将仓库函数发布至 Function Registry 的版本操作。 |

## 疑问与待验证项

- 页面示例创建仓库后把提交路径写作 `master`，分支名称和工作流会随仓库配置变化，不能当作固定要求。
- 更新发布后搜索结果可能延迟；需区分发布步骤完成与权限/索引传播完成。

## 复刻启示

- 函数定义可以与本体画布上的规则节点关联：输入/输出 schema、资源依赖、分支版本、预览结果和发布版本都可追踪。
- 发布全仓函数前执行静态检查、依赖检查和权限传播状态提示，记录产物 hash 以便回滚。
