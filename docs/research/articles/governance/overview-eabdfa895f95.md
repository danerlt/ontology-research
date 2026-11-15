<!-- 页面 URL：https://www.palantir.com/docs/zh/foundry/functions/overview -->
<!-- 研读状态：已完成 -->

# 函数 • 概述 • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/functions/overview)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/functions/overview)
- 页面语言：中文（官方 AIP 机器翻译，需与英文原文交叉核对）
- 主题栏目：functions
- 相关性：direct；本体函数文档
- 官方更新时间：2026-11-12T17:46:46.935Z
- 目录核对时间：2026-11-14T14:59:26Z
- 产品状态：Functions 是运行于隔离服务端环境的逻辑层，并原生支持读取 Ontology 属性、遍历链接及执行 Ontology 编辑；现有文档支持 TypeScript 与 Python。

## 英文原文短摘录（每个来源不超过 25 词）

> “Functions enable code authors to write logic that can be executed quickly in operational contexts, such as dashboards and applications designed to empower decision-making processes.”

## 摘录译文

Functions 允许开发者编写可在仪表板、应用等运营场景中快速执行的逻辑，以支持决策流程。

## 中文要点

- 函数可为应用提供对象集或变量、计算列和图表指标，也可封装跨对象变更、外部系统查询或增量流式结果。
- 它把本体读取、链接遍历和编辑能力与业务代码放在同一执行层，应用可以调用该逻辑而不必复制业务规则。
- Python 函数还可作为 Pipeline Builder 的 sidecar UDF 使用；该嵌入执行模式与常规已发布函数服务不是同一运行形态。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| server-side function | 服务端函数 | 在隔离执行环境中运行的业务逻辑 |
| Ontology edit | 本体编辑 | 通过函数/Action 对本体对象产生的变更 |
| sidecar container | 边车容器 | 随 Pipeline Builder 流水线运行的函数容器 |

## 疑问与待验证项

- 概览罗列函数可执行的能力，但授权、Action 写入、外部调用与流式输出各有不同约束，不能仅凭概览推断安全边界。
- 文档表示服务端隔离执行；实际可用 CPU、内存、超时及并发上限应以运行模式和治理配置为准。

## 复刻启示

- 将函数作为可部署、版本化并受权限策略约束的计算资源；Action 负责提交变更，查询函数保持只读，外部连接通过显式连接器授权。
- 本体画布可从属性和链接生成函数依赖图，并在试算结果中显示依赖对象、聚合步骤和变更计划。
- 区分用户交互查询、批处理 UDF、实时流式函数与模型推理等运行时，分别限制资源并记录审计。
