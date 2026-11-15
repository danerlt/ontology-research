<!-- 页面 URL：https://www.palantir.com/docs/foundry/functions/navigating-vscode -->
<!-- 研读状态：已完成 -->

# Functions • Navigating VS Code • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/functions/navigating-vscode)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：functions
- 相关性：direct；本体函数文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:02:27Z
- 产品状态：未见本页声明 Beta/预览/弃用；以页面当前说明为准。

## 英文原文短摘录（每个来源不超过 25 词）
> “Tagging publishes all functions in the repository, not only the function you most recently edited.”

## 摘录译文
打标签会发布仓库中的所有函数，而不只是最近编辑的函数。

## 中文要点
- Palantir VS Code 扩展提供 Ontology/平台资源导入、函数预览、分支管理、提交、提案评审、版本发布和仓库升级入口。
- Code 分支是仓库 Git 分支；Global 分支可承载多个受支持 Foundry 应用/资源的相关变更，适用范围取决于语言和仓库配置。
- 函数预览展示输出、日志、编辑等运行信息；Global 分支上的预览针对当前选中分支。提交后可提出变更评审，再通过 Tag version 发布。
- 版本标签会发布仓库内全部函数；升级仓库会生成改动，完成后仍需重新检查、预览和提交。

## 术语对照
| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Code branch | 代码分支 | 承载函数仓库代码变更的 Git 分支。 |
| Global branch | 全局分支 | 可承载多个 Foundry 资源变更的协作分支。 |
| Function preview | 函数预览 | 带输入试运行函数并查看输出、日志和编辑。 |
| Tag version | 版本标签 | 生成/发布一版仓库内的函数。 |

## 疑问与待验证项
- Global 分支支持依赖函数语言和仓库配置；具体哪些资源可跨应用纳入同一提案需按部署能力确认。
- Tag 发布范围是仓库中全部函数，发布前需核实版本兼容及资源依赖，避免把未完成函数一起发布。

## 复刻启示
- 本体画布和规则编辑可采用分支工作区：预览影响、提交差异、评审意见、合并与发布版本分离。
- 发布按钮必须在 UI 中清楚显示影响范围；提供全量变更清单、依赖检查和回滚版本入口。
