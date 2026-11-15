<!-- 页面 URL：https://www.palantir.com/docs/foundry/ontologies/ontologies-overview -->
<!-- 研读状态：已完成 -->

# Ontologies • Overview • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/ontologies/ontologies-overview)
- 官方中文来源：[https://www.palantir.com/docs/zh/foundry/ontologies/ontologies-overview](https://www.palantir.com/docs/zh/foundry/ontologies/ontologies-overview)
- 页面语言：英文
- 主题栏目：ontologies
- 相关性：direct；本体管理与治理文档
- 官方更新时间：页面未提供
- 目录核对时间：2026-11-15
- 产品状态：概览页；含私有/共享本体与 Space 的关系说明。

## 英文原文短摘录（每个来源不超过 25 词）

> “An ontology is an artifact which stores ontological resources or entities, including the following:”

## 摘录译文

Ontology 是存储本体资源或实体的工件，其中包括：

## 中文要点

- 本体保存对象类型、链接类型、动作类型、接口、共享属性及对象类型组等资源。一个本体可限定给单个组织，也可配置为多个组织共享。
- Foundry 文档定义 Ontology 与 Space 为一对一映射；团队内部协作通常使用同一私有本体并通过项目角色管理资源权限，而不是仅因多团队就拆本体。
- 共享本体用于跨组织共同使用同一组对象和工作流；共享本体不会自动移除底层数据继承来的组织访问限制。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Ontology resource | 本体资源 | 对象类型、链接、动作、接口、共享属性、分组等定义。 |
| Space | 空间 | Foundry 中与本体按一对一关系映射的边界。 |
| organization marking | 组织标记 | 限定资源可访问组织的安全约束。 |

## 疑问与待验证项

- Ontology 与 Space 的一对一关系不等于“每个项目必须有一个本体”；项目资源授权与本体/组织边界是不同层次。
- 本地产品将“项目—本体—来源系统”如何分层属于复刻设计决策，不能直接照搬 Space 的映射关系。

## 复刻启示

- 模型中显式区分项目、一个或多个本体、多个数据源连接和组织/成员授权；不要把数据源连接误建成对象关系。
- 画布区分本体资源图与数据来源血缘；跨项目共享要通过明确授权或受控共享资源，而非默认可见。
