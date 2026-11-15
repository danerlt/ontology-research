<!-- 页面 URL：https://www.palantir.com/docs/zh/foundry/action-types/rules -->
<!-- 研读状态：已完成 -->

# 动作类型 • 规则 • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/action-types/rules)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/action-types/rules)
- 页面语言：中文
- 主题栏目：action-types
- 相关性：direct；本体动作文档
- 官方更新时间：2026-11-12T17:46:46.935Z
- 目录核对时间：2026-11-14T14:58:25Z
- 产品状态：官方中文页标注为未经验证的 AIP 机器翻译；英文原文为核对依据。

## 英文原文短摘录（每个来源不超过 25 词）

> “Rules define the logic of the action type that transforms the parameters into Ontology edits or other effects.”

## 摘录译文

规则定义操作类型逻辑，将参数转换为 Ontology 编辑或其他效果。

## 中文要点

- 规则可直接创建、修改、删除对象或链接；对象的一对一/一对多外键链接需通过修改对象外键属性来创建或删除。
- 支持以接口为目标的对象和链接规则；对象规则映射主键、属性值与参数，函数规则将输入映射至本体编辑函数。
- 使用 Function rule 时不得同时配置其他规则，因为函数代码承担完整逻辑；有些对象修改/删除规则不能引用本次动作新建的对象。
- 中文页面的 AIP 机器翻译准确性未验证；接口规则和关系基数应以英文能力表为准。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Ontology rule | 本体规则 | 直接描述对象或链接的创建、修改、删除。 |
| Foreign key link | 外键链接 | 通过对象属性存储链接目标的关系表达。 |
| Function rule | 函数规则 | 调用本体编辑函数执行动作写入。 |

## 疑问与待验证项

- 不同规则组合的执行顺序、失败回滚边界和并发冲突须结合一致性/隔离文档确认。
- 对象接口规则的可用操作依赖接口契约及具体实现对象类型，跨类型的细节需要进一步核对。

## 复刻启示

- 将规则建模为可类型检查的编辑计划节点，并在画布中展示输入参数→对象属性/链接写集的有向映射。
- 保存规则的依赖图与执行顺序，校验主键、外键基数、对象新旧引用和函数互斥约束。
