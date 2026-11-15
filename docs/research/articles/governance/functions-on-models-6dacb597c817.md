<!-- 页面 URL：https://www.palantir.com/docs/zh/foundry/functions/functions-on-models -->
<!-- 研读状态：已完成 -->

# 函数 • 模型上的函数 • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/functions/functions-on-models)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/functions/functions-on-models)
- 页面语言：中文
- 主题栏目：functions
- 相关性：direct；本体函数文档
- 官方更新时间：2026-11-12T17:46:46.935Z
- 目录核对时间：2026-11-14T14:59:18Z
- 产品状态：官方中文页标注为未经验证的 AIP 机器翻译；英文原文为核对依据。

## 英文原文短摘录（每个来源不超过 25 词）

> “You can deploy models in the context of the Ontology by using functions that invoke models during their runtime.”

## 摘录译文

你可以在 Ontology 上下文中部署模型，让函数在运行时调用模型。

## 中文要点

- 模型函数包装 live deployment，接口输入输出与模型 API 对齐；可用于给预测增加业务逻辑、连接 Ontology 对象或编排多次模型调用。
- 函数可从直接部署或 Modeling Objective 的 live deployment 发布；TSv1、TSv2、Python均支持，但后两者只允许导入绑定到 Ontology 的模型函数。
- 自 2026 年 2 月起新模型函数会绑定 Ontology；旧 space-bound 函数需按迁移路线处理。Marketplace 会追踪仓库导入的模型函数及部署依赖。
- 部署模型必须运行才能提供推理；模型 API 变更后，消费者和已发布函数绑定需同步更新。中文页为未经验证 AIP 机器翻译。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Model function | 模型函数 | 包裹在线模型部署并呈现为函数 API 的资源。 |
| Live deployment | 在线部署 | 供应用/函数执行推理请求的已启动模型服务。 |
| Ontology-bound function | 绑定本体的函数 | 模型函数依赖于某 Ontology 资源上下文。 |

## 疑问与待验证项

- Modeling Objective 的 API 变更对消费者的自动迁移/版本策略有破坏性，具体发布警告需结合 developer guide 核验。
- 模型部署资源如何在 Marketplace 安装环境启动、等待健康检查和轮换，应与 live deployment 安装页联合设计。

## 复刻启示

- 模型推理资源应有显式版本 API、部署状态和 schema 契约；本体函数调用前可显示模型输入输出映射。
- 模型调用与本体对象/动作之间建立 provenance 边，保存 deployment/model 版本及目标环境状态。
