<!-- 页面 URL：https://www.palantir.com/docs/zh/foundry/manage-models/models-in-the-ontology -->
<!-- 研读状态：已完成 -->

# 管理模型 • Modeling deployment FAQ • Ontology中的模型 • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/manage-models/models-in-the-ontology)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/manage-models/models-in-the-ontology)
- 页面语言：中文
- 主题栏目：manage-models
- 相关性：direct；标题或简介提及本体、对象、动作、权限或 Agent 主题
- 官方更新时间：2026-11-12T17:46:46.934Z
- 目录核对时间：2026-11-14T14:59:53Z
- 产品状态：待核对 Beta、预览、弃用或更名信息

## 英文原文短摘录（每个来源不超过 25 词）

> “For instance, you may want to define a model-backed Action or connect UI elements in Workshop directly to model output.”

## 摘录译文

例如，你可能希望定义由模型支持的 Action，或将 Workshop UI 元素直接连接到模型输出。

## 中文要点

- 这是一条建模部署 FAQ：操作型工作流可把本体对象属性绑定为模型输入，并通过 Ontology 解释推理结果。
- 文档给出两种产品用法：定义由模型支持的 Action，或把 Workshop UI 元素直接连接到模型输出；实现路径是 Object 上的 Function 调用建模目标实时部署。
- 代码开发细节被链接到“模型上的函数”文档；本页本身没有定义特征变换、部署版本选择、回退、延迟与推理历史的接口契约。
- 当前中文页面明确提示由 AIP 从英文机器翻译且未验证。本地目录尚未确认可配对的英文页面，应继续以实际链接和原文复核。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| 模型推理 | model inference | 在本体对象数据上下文中生成预测或评分。 |
| Object function | 对象函数 | 接收对象属性并可调用实时部署的扩展函数。 |
| 实时部署 | live deployment | 在应用交互流程中同步调用的模型部署。 |

## 疑问与待验证项

- 页面没有说明模型推理输出如何物化为本体属性，也没有描述其审计与敏感字段处理；不能把“上下文解释”直接等同于完整可解释 AI。
- 应结合模型函数与推理历史文档查明输入输出 schema、部署版本和计算用量的治理方式。

## 复刻启示

- 推理画布可提供模型节点：绑定本体属性到输入、关联部署版本、输出结果边到 Action/界面，并沿图展示来源对象与特征。
- 将模型计算标为概率性推理，保留模型版本、输入快照、时间与结果置信信息；把读取权限继承到特征输入，避免模型调用绕开字段安全。
