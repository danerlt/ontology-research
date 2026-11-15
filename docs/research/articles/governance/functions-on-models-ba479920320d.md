<!-- 页面 URL：https://www.palantir.com/docs/foundry/functions/functions-on-models -->
<!-- 研读状态：已完成 -->

# Functions • 在函数中调用模型 • Functions on models • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/functions/functions-on-models)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/functions/functions-on-models)（配对状态：matched）
- 页面语言：英文
- 主题栏目：functions
- 相关性：direct；本体函数文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:03:18Z
- 产品状态：模型函数是模型在线部署的生成包装器，可在函数中编排预测并连接 Ontology 对象。

## 英文原文短摘录（每个来源不超过 25 词）

> “Model functions are automatically generated wrappers around live model deployments.”

## 摘录译文

模型函数是围绕在线模型部署自动生成的包装器。

## 中文要点

- 可把推理模型发布成输入/输出 API 一致的 Model Function，再导入函数仓库调用，用于在预测周围加业务逻辑、结合本体对象和编排多个模型调用。
- 可从直接模型部署或 Modeling Objective 在线部署发布；TSv1/TSv2/Python 均支持模型函数。
- Python 与 TSv2 仅支持绑定 Ontology 的模型函数；自 2026 年 2 月起，新模型函数都绑定 Ontology。TSv1 还能导入旧的 Space 绑定模型函数，但语义略不同。
- 使用旧 Modeling Objectives API Name 卡片发布的遗留函数仍可导入，但已进入 Sunset。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Model function | 模型函数 | 模型在线部署生成的函数封装 |
| Direct model deployment | 直接模型部署 | 从模型页直接发布的在线部署 |
| Ontology-bound function | 本体绑定函数 | 资源依赖绑定到 Ontology 的模型函数 |

## 疑问与待验证项

- 2026 年 2 月前的模型函数可能绑定 Space；迁移到 Python/TSv2 时须检查资源依赖和 API 语义。
- 遗留 Modeling Objective 发布方式已 Sunset；具体可用时间和迁移窗口需核对目标环境。

## 复刻启示

- 本体对象函数可组合预测、业务校验和对象查询，但应把模型版本、输入对象和输出写入 Action/派生属性分层记录。
- 模型调用只提供推理结果，不自动创建本体编辑；发布与模型部署更新需共同纳入兼容审查。
