<!-- 页面 URL：https://www.palantir.com/docs/zh/foundry/ontology -->
<!-- 研读状态：已完成 -->

# Ontology搭建 • Palantir

- 英文来源：[当前英文原文](https://www.palantir.com/docs/foundry/ontology)
- 官方中文来源：[中文原文](https://www.palantir.com/docs/zh/foundry/ontology)
- 页面语言：中文（官方机器翻译，准确性未验证）
- 主题栏目：ontology
- 相关性：direct；本体模型与治理文档
- 官方更新时间：2026-11-12T17:46:46.937Z
- 目录核对时间：2026-11-14T15:00:13Z
- 产品状态：Ontology 搭建总览；英文页面使用 Ontology building 标题

<!-- 研读状态：已完成 -->
# 英文原文短摘录（每个来源不超过 25 词）

> “The Palantir Ontology is an operational layer for the organization.”

## 摘录译文

Palantir Ontology 是组织的运营层。

## 中文要点

- Ontology 位于数据集、虚拟表和模型等数字资产之上，把它们连接到真实业务实体；包含对象、属性、链接等语义元素，以及 Action、Function、动态安全等驱动工作流的能力。
- 它不只是目录或 schema，而是把业务数据、可执行操作和治理规则整合为最终用户应用的共同基础。
- 对象和链接表达业务语义；Action 捕获操作员输入或编排与既有系统相连的决策流程；Function 承载可演化的业务逻辑。
- Interface 描述对象形状与能力，为共享结构的对象类型提供多态建模与一致交互。
- Ontology 与 Object Views、Object Explorer、Quiver、Workshop 等分析和运营工具集成。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Operational layer | 运营层 | 连接数据资产、业务实体与工作流的语义运行层 |
| Semantic elements | 语义元素 | 对象、属性和链接等模型结构 |
| Kinetic elements | 驱动元素 | Action、Function 与动态安全等可执行能力 |
| Interface | 接口 | 多个对象类型可共享的形状与能力契约 |

## 疑问与待验证项

- 本页是产品理念总览，不是可执行 schema 规范；类型基数、编辑状态和权限须结合专题文档研读。
- 中文路由提示 AIP 机器翻译未验证；核心概念已与当前英文 Ontology building 页核对。

## 复刻启示

- 同时管理语义结构与可执行动作，并把数据来源、权限和消费者应用连到同一资源图。
- 画布呈现真实资产和类型关系，区分定义图、运行实例图和操作依赖，不能简化为数据库 ER 图。