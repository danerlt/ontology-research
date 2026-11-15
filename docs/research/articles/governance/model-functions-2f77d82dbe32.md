<!-- 页面 URL：https://www.palantir.com/docs/zh/foundry/functions/model-functions -->
<!-- 研读状态：已完成 -->

# 函数 • Models and graphs • 创建模型函数 • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/model-integration/functions-on-models)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/functions/model-functions)
- 页面语言：中文（官方 AIP 机器翻译，需与英文原文交叉核对）
- 主题栏目：functions
- 相关性：direct；本体函数文档
- 官方更新时间：2026-11-12T17:46:46.935Z
- 目录核对时间：2026-11-14T14:59:26Z
- 产品状态：模型可发布为函数供 Workshop、Slate、Actions 等应用调用，也可被其他函数组合；2026 年 2 月起新建模型函数关联 Ontology，TSv2/Python 仅支持关联 Ontology 的模型函数。

## 英文原文短摘录（每个来源不超过 25 词）

> “You can deploy models as functions to enable live usage of models in end-user applications like Workshop, Slate, Actions, and more.”

## 摘录译文

你可以将模型部署为函数，让 Workshop、Slate、Actions 等终端用户应用实时调用模型。

## 中文要点

- 模型函数把已配置的实时部署或 Modeling Objective 实时部署包装成可调用函数，供终端应用消费或组合进业务逻辑。
- TypeScript v1、TypeScript v2 与 Python 均可调用模型函数；TSv2/Python 通过生成的 Ontology SDK 暴露该函数。
- 新旧模型函数存在空间绑定与 Ontology 绑定的迁移差异，不能只按函数名称或调用语法推断兼容性。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Model function | 模型函数 | 将模型部署包装为可在应用或代码中调用的函数 |
| live deployment | 实时部署 | 提供在线推理能力的模型部署 |
| ontology-bound | 关联 Ontology | 函数通过 Ontology 资源与对象/查询 SDK 绑定 |

## 疑问与待验证项

- 中文目录路由“创建模型函数”与当前英文“Functions on models”并非同一路径；需以现行模型集成文档和实际租户 UI 核实发布入口。
- 新函数与旧空间绑定函数的迁移期限和兼容策略仍需结合模型函数指南确认。
- 函数调用模型会产生独立推理成本；限额、超时与重试策略需查目标部署配置。

## 复刻启示

- 将模型部署作为版本化资源，再通过函数定义声明模型版本、输入输出 schema 和所属项目/本体；调用记录保存部署版本。
- 编辑器应校验函数绑定方式与运行时 SDK 能力，避免把旧式空间绑定函数发布到不支持的语言模板。
- 运行轨迹分开展示函数逻辑耗时与模型推理耗时，并把推理调用标记为外部计算成本。
