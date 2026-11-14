<!-- 页面 URL：https://www.palantir.com/docs/foundry/ontology/core-concepts -->
<!-- 研读状态：已完成 -->

# Core concepts • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/ontology/core-concepts)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/ontology/core-concepts)（配对状态：matched）
- 页面语言：英文
- 主题栏目：ontology
- 相关性：direct；本体模型与治理文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:01:31Z
- 产品状态：待核对 Beta、预览、弃用或更名信息

## 英文原文短摘录（每个来源不超过 25 词）

> “An Ontology is a categorization of the world.”

## 摘录译文

“Ontology 是对现实世界的分类。”

## 中文要点

本体把组织的数据和模型映射成业务对象、属性、对象之间的关系以及修改对象的 Action。文档用数据表作类比：对象类型对应数据集，对象对应行，属性对应列，链接对应 join。它进一步区分定义与实例：对象类型定义实体/事件的 schema，对象是具体实例；Link Type 是关系定义，link 是具体关系实例。共享属性用于跨对象类型复用属性定义。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Ontology | 本体 | 描述组织业务实体、关系与可执行行为的语义模型 |
| Object type / Object | 对象类型 / 对象 | 前者是实体或事件的 schema；后者是具体实例 |
| Property / Link type | 属性 / 链接类型 | 分别定义对象特征与对象类型之间的关系 |
| Action type | Action 类型 | 定义一次可执行的对象变更集合 |
| Shared property | 共享属性 | 多种对象类型共用并集中管理的属性定义 |

## 疑问与待验证项

- 本页把 Ontology 描述为组织的数字孪生，但数据来源、对象物化和同步行为由其他数据连接与索引页面说明；不能仅据此推断底层数据一定复制进本体数据库。
- 本体角色可授予在 Ontology 或单个资源层级；权限模型需与更新后的对象权限文档一起读。

## 复刻启示

- 将 schema 定义与对象实例分开持久化，并显式建模链接定义和链接实例。
- 让 Action 成为对象写入入口，使应用、Agent 和审计围绕相同业务语义工作。当前原型尚无共享属性、接口类型和函数。
