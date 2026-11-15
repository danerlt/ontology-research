<!-- 页面 URL：https://www.palantir.com/docs/zh/foundry/functions/enforced-limits -->
<!-- 研读状态：已完成 -->

# 函数 • Performance and limits • 强制限制 • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/functions/manage-functions)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/functions/enforced-limits)
- 页面语言：中文
- 主题栏目：functions
- 相关性：direct；本体函数文档
- 官方更新时间：2026-11-12T17:46:46.935Z
- 目录核对时间：2026-11-14T14:59:12Z
- 产品状态：官方中文页标注为未经验证的 AIP 机器翻译；英文原文为核对依据。

## 英文原文短摘录（每个来源不超过 25 词）

> “Once published, all types of functions can be viewed and managed using the Ontology Manager.”

## 摘录译文

函数发布后，可以通过 Ontology Manager 查看和管理所有类型的函数。

## 中文要点

- 该目录路由当前重定向到已发布函数管理页的“强制限制”章节；时限依执行环境不同：普通函数默认约 60 秒，live preview 最长 280 秒，Automate 异步函数可运行更久。
- TSv1 还有不可配置的 CPU 时间/内存与对象集加载上限；Python、TSv2、deployed 与 serverless 的默认内存不同。
- TSv1 `.all()`/`.allAsync()` 一次超过 100,000 个对象或同时使用过多 Search Around 会报错；推荐改用聚合或限制结果集。
- 限制数值和语言/执行模式绑定，中文翻译页面未校验准确性；请以当前英文管理页和租户配置为准。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Execution limit | 执行限制 | 函数时长、内存、并发或查询加载规模等上限。 |
| Serverless | 无服务器执行 | 按调用触发、平台自动管理资源的函数运行方式。 |
| Deployed function | 已部署函数 | 运行在长期服务容器中的函数模式。 |

## 疑问与待验证项

- 函数限制在平台更新时可能变化；不能将抓取到的单组数值作为跨租户永久常量。
- 长运行工作流是否切到 Automate、deployed 函数还是拆分异步任务，应按一致性、外部副作用与成本共同评估。

## 复刻启示

- 把限制放入按运行时/环境版本管理的策略配置，提交前估算对象加载和执行时长，并在 API 错误中提示恢复方式。
- 对象集提供流式/分页/聚合接口，避免将资源边界交由客户端 `.all()` 内存行为决定。
