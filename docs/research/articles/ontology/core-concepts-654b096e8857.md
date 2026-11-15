<!-- 页面 URL：https://www.palantir.com/docs/foundry/ontology/core-concepts -->
<!-- 研读状态：已完成 -->

# Core concepts • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/ontology/core-concepts)
- 官方中文来源：[https://www.palantir.com/docs/zh/foundry/ontology/core-concepts](https://www.palantir.com/docs/zh/foundry/ontology/core-concepts)
- 页面语言：英文
- 主题栏目：ontology
- 相关性：direct；本体模型与治理文档
- 官方更新时间：页面未提供
- 目录核对时间：2026-11-15
- 产品状态：概念页；包含对象、属性、共享属性、链接、动作、权限角色、函数、接口与对象视图。

## 英文原文短摘录（每个来源不超过 25 词）

> “An Ontology is a categorization of the world.”

## 摘录译文

Ontology 是对现实世界的一种分类。

## 中文要点

- 本体把数据集和模型映射为对象类型、属性、链接类型与动作类型，作为面向组织运营语境的语义模型。
- 对象类型≈数据集，Object≈行，属性≈列，属性值≈字段值，链接≈数据连接关系；该类比便于理解，但本体还包含操作与权限语义。
- 动作类型定义对对象/属性/链接的变更，函数可读取本体对象并用于动作或应用；接口支持共享形状建模，对象视图聚合对象及相关工作流。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Ontology | 本体 | 把数字资产映射到业务实体、关系和行为的语义层。 |
| action type | 动作类型 | 描述一组可提交的对象变更及其副作用。 |
| interface | 接口 | 描述对象类型共同形状和能力的本体类型。 |

## 疑问与待验证项

- 概念页将本体描述为组织数字孪生，但没有提供本体建模质量、粒度和边界的量化验收标准。
- 函数可读取对象/对象集；哪些函数能改对象取决于动作及其权限配置，不能把读写能力混为一谈。

## 复刻启示

- 画布应同时展示对象类型、属性、双向链接、动作和函数关联，并支持按资源种类筛选/分组。
- 用结构化关系而非布局猜测建图；对象实例关系图和 schema 本体图提供不同视图。
