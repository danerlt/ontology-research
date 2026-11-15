<!-- 页面 URL：https://www.palantir.com/docs/foundry/functions/branching-functions -->
<!-- 研读状态：已完成 -->

# Functions • 分支中的函数 • Branching functions • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/functions/branching-functions)
- 官方中文来源：尚未确认（配对状态：ambiguous）
- 页面语言：英文
- 主题栏目：functions
- 相关性：direct；本体函数文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:02:26Z
- 产品状态：全局分支支持开发与使用函数预览版本；函数依赖分支资源并在合并时转为稳定版本。

## 英文原文短摘录（每个来源不超过 25 词）

> “Functions published on your branch will not be accessible from other branches, including main.”

## 摘录译文

在当前分支发布的函数无法被其他分支使用，包括 main。

## 中文要点

- Global Branching 支持 TypeScript v1/v2、Python、AIP Logic 和直连模型部署函数。
- TSv1、TSv2、Python 对应仓库模板有最低版本要求；TSv2/Python 还需启用本地 Ontology SDK。
- 分支函数依赖同分支上的本体变更，发布为不稳定预览版本；Workshop、AIP Logic 和函数支持 Action 可在该分支消费。
- 同一版本目标后续发布的新版本可被分支资源自动获取；合并后版本目标对应 main 的稳定版本。TS/ Python 查询函数暂不支持依赖分支版本。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Global Branching | 全局分支 | 跨多个资源开发和评审的隔离工作分支 |
| Branched pre-release | 分支预发布版 | 仅当前分支可访问的函数版本 |
| Version target | 版本目标 | 合并后映射为稳定发布版本的目标标记 |

## 疑问与待验证项

- 模板最低版本和分支函数可消费资源会随产品演进，应从当前官方页面与仓库状态同步。
- 查询函数不能依赖分支版本，分支内 API/应用测试的替代路径需另查。

## 复刻启示

- 函数版本应和本体分支绑定；预览版本只对分支内资源可见，评审合并时同步检查函数依赖和对象 schema。
- 版本目标使迭代资源能自动拾取最新分支版本，需记录每次试算实际解析到的函数版本。
