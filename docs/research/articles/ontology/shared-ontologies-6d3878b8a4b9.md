<!-- 页面 URL：https://www.palantir.com/docs/zh/foundry/ontologies/shared-ontologies -->
<!-- 研读状态：已完成 -->

# 本体 • 共享Ontology • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/ontologies/shared-ontologies)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/ontologies/shared-ontologies)
- 页面语言：中文
- 主题栏目：ontologies
- 相关性：direct；本体管理与治理文档
- 官方更新时间：2026-11-12T17:46:46.935Z
- 目录核对时间：2026-11-15
- 产品状态：官方中文页提示其为未经验证的 AIP 机器翻译；已对照英文原文。

## 英文原文短摘录（每个来源不超过 25 词）

> “A shared ontology is a special kind of ontology that allows multiple organizations to collaborate on shared workflows.”

## 摘录译文

共享本体是一种特殊类型的本体，可让多个组织在共享工作流中协作。

## 中文要点

- 共享本体位于专用共享空间，用于多组织在同一工作流中使用资源；普通本体只承载单一组织的资源。
- 共享空间创建时自动产生共享本体，本体采用与空间一致的组织标记和角色授权。
- 该能力描述跨组织的显式共享，不等价于一个组织内部的多项目，也不会自动开放被来源权限保护的数据。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| shared space | 共享空间 | 为多组织协作工作流建立的空间。 |
| organization marking | 组织标记 | 组织级访问控制约束。 |
| workflow | 工作流 | 跨组织共同使用本体资源的业务流程。 |

## 疑问与待验证项

- 此中文页明确声明为机器翻译；“权限标记”等译名需要结合英文文档中的 markings/role grants 理解。
- 本文未说明共享关系怎样撤销及共享资源删除的级联策略，应从跨组织协作文档补充。

## 复刻启示

- 采用显式项目共享授权并记录受众、范围、过期时间与撤销审计；默认情况下项目间互不可见。
- 任何派生属性沿来源系统/项目读取时都要校验数据权限，不能因模型被共享就扩大源数据访问。
