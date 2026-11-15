<!-- 页面 URL：https://www.palantir.com/docs/foundry/functions/python-functions-workshop -->
<!-- 研读状态：已完成 -->

# Functions • Python • Use Python functions in Workshop • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/functions/python-functions-workshop)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/functions/python-functions-workshop)（配对状态：matched）
- 页面语言：英文
- 主题栏目：functions
- 相关性：direct；本体函数文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:02:59Z
- 产品状态：页面未标注 Beta；部署可用性由具体函数版本状态决定。

## 英文原文短摘录（每个来源不超过 25 词）

> “Serverless functions can always be run at any version and do not need to be manually deployed.”

## 摘录译文

无服务器函数可以使用任意版本运行，无需手动部署。

## 中文要点

- Workshop Variables 面板可选择已发布 Python 函数；serverless 函数可按任意版本运行，deployed 函数只有 Running 状态可服务。
- 函数选择器会标出 Running、Stopped 和 Upgrading 状态；停止或升级中的版本不能处理请求。
- 同一仓库同时仅托管一个已部署版本；切换部署会停止旧版本，应用迁移时可能有短暂停机。页面建议用并存函数名逐步迁移消费者。
- 部署升级通过 Ontology Manager 选择仓库版本；下游应用需更新引用。函数 registry 多版本和部署中的单版本概念不同。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| serverless function | 无服务器函数 | 按调用执行，不需人工常驻部署。 |
| deployed function | 已部署函数 | 分配部署资源并有运行状态的函数。 |
| Running / Stopped / Upgrading | 运行中/已停止/升级中 | Workshop 选择器显示的部署状态。 |

## 疑问与待验证项

- 同仓库只能有一个部署版本这一限制与代码 tag 可并存需分别建模。
- 短暂停机窗口取决于函数命名、应用切换顺序和部署状态。

## 复刻启示

- 画布区分逻辑函数版本与运行部署实例，显示所有下游引用和版本切换状态。
- 升级流程先准备新入口，逐个迁移应用，再回收旧入口并提供回退。
