<!-- 页面 URL：https://www.palantir.com/docs/foundry/ontologies/shared-ontologies -->
<!-- 研读状态：已完成 -->

# Ontologies • Shared ontologies • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/ontologies/shared-ontologies)
- 官方中文来源：[https://www.palantir.com/docs/zh/foundry/ontologies/shared-ontologies](https://www.palantir.com/docs/zh/foundry/ontologies/shared-ontologies)
- 页面语言：英文
- 主题栏目：ontologies
- 相关性：direct；本体管理与治理文档
- 官方更新时间：页面未提供
- 目录核对时间：2026-11-15
- 产品状态：共享空间创建时自动生成共享本体；其组织标记和角色授权与共享空间一致。

## 英文原文短摘录（每个来源不超过 25 词）

> “A shared ontology is a special kind of ontology that allows multiple organizations to collaborate on shared workflows.”

## 摘录译文

共享本体是一种特殊类型的本体，可让多个组织在共享工作流中协作。

## 中文要点

- 共享本体驻留在专门为协作工作流建立的共享空间中，可将多个组织的资源放入同一工作流；普通本体则面向单个组织。
- 共享空间创建时会自动创建对应本体，并继承相同组织标记和角色授权。
- 共享本体解决跨组织资源协作边界；它不意味着所有参与组织自动拥有底层数据访问权，具体数据仍受来源资源的安全要求约束。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| shared ontology | 共享本体 | 供多个组织共同使用本体资源的边界。 |
| shared space | 共享空间 | 承载跨组织协作资源的专用空间。 |
| role grant | 角色授权 | 授予主体访问本体资源的角色配置。 |

## 疑问与待验证项

- 该页概述未展开权限标记移除流程；执行跨组织共享前仍需检查数据来源项目的继承要求。
- 本地多项目需求并不天然等同于 Palantir 的跨组织共享，权限主体和共享边界须由业务明确。

## 复刻启示

- 项目共享需有独立的共享策略、审计和成员范围，默认拒绝跨项目读取。
- 数据源连接保留来源系统和项目标识，推理读取及画布详情都遵循来源数据授权。
