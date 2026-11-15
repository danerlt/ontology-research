<!-- 页面 URL：https://www.palantir.com/docs/zh/foundry/ontologies/ontologies-overview -->
<!-- 研读状态：已完成 -->

# 本体 • 概述 • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/ontologies/ontologies-overview)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/ontologies/ontologies-overview)
- 页面语言：中文
- 主题栏目：ontologies
- 相关性：direct；本体管理与治理文档
- 官方更新时间：2026-11-12T17:46:46.935Z
- 目录核对时间：2026-11-15
- 产品状态：官方中文页提示其为未经验证的 AIP 机器翻译；已对照英文原文。

## 英文原文短摘录（每个来源不超过 25 词）

> “An ontology is an artifact which stores ontological resources or entities, including the following:”

## 摘录译文

Ontology 是存储本体资源或实体的工件，其中包括：

## 中文要点

- 本体容纳对象、链接、动作、接口等资源；可私有归属一个组织，也可由多个组织共享。
- Foundry 文档将 Ontology 与 Space 定义为一对一映射；Space 的组织标记和角色会影响对应本体资源访问。
- 跨团队协作通常仍可在一个私有本体中按项目资源授予角色；跨组织共享则需要共享本体，而且底层数据仍受来源访问标记约束。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| ontology | 本体 | 保存业务语义资源的容器与授权边界。 |
| private ontology | 私有本体 | 限制在单一组织中的本体。 |
| shared ontology | 共享本体 | 面向多个组织共同使用资源的本体。 |

## 疑问与待验证项

- 中文页将“一对一映射”翻译为本体与空间的关系；不应据此推断每个业务项目只能有一个本体。
- 公开页描述 Foundry 的 Space/组织模型；本地产品的项目隔离需要独立定义和迁移。

## 复刻启示

- 建立项目层访问控制和本体层资源角色两级模型；来源系统是另一个维度，应挂在项目或数据集映射上。
- 将项目切换器、组织共享状态与来源连接器健康状态分开展示，避免用户混淆隔离层级。
