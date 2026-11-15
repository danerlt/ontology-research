<!-- 页面 URL：https://www.palantir.com/docs/foundry/functions/python-functions-builder -->
<!-- 研读状态：已完成 -->

# Functions • Python • Use Python functions in Pipeline Builder • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/functions/python-functions-builder)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/functions/python-functions-builder)（配对状态：matched）
- 页面语言：英文
- 主题栏目：functions
- 相关性：direct；本体函数文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:02:59Z
- 产品状态：页面未标注 Beta；UDF 访问边界由 Pipeline Builder 的运行安全模型决定。

## 英文原文短摘录（每个来源不超过 25 词）

> “Pipeline Builder UDFs do not support direct Ontology access through `FoundryClient()` or the Ontology SDK (OSDK).”

## 摘录译文

Pipeline Builder UDF 不支持通过 FoundryClient() 或 OSDK 直接访问本体。

## 中文要点

- Python UDF 在 Pipeline Builder 中作为 sidecar container 逐行执行；每次获得映射行的列值并返回新列值，不会接收整张表或 DataFrame。
- UDF 从 Reusables 或 Transform picker 导入，配置输入列与参数后可预览输出；容器按管道规模动态扩展。
- UDF 不可用 `FoundryClient`/OSDK 直接查 Ontology，防止标记/权限绕过；可从允许导入 pipeline 的 external source 取数，或先将相关数据集成后 join。
- 外部 API 所用 source 必须允许 Code import configuration，且函数引用的所有来源都需允许导入管道。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| UDF | 用户定义函数 | 按管道行执行的自定义数据变换。 |
| sidecar container | 旁路容器 | 为 Pipeline Builder 函数动态运行的容器。 |
| row-wise execution | 逐行执行 | 一次函数调用处理一个数据行。 |

## 疑问与待验证项

- 外部 source 替代直接查本体时，需要核对权限标签、刷新频率、数据去重与语义一致性。
- 函数动态扩展仍受平台任务并行度和成本限制。

## 复刻启示

- 将离线行变换与在线本体查询放在不同执行器中，并在图上标示数据来源和授权主体。
- 外部系统连接先登记并授权，再让变换节点显式引用，不允许函数暗中读取全域凭据。
