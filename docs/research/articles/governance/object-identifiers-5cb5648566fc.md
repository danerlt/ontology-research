<!-- 页面 URL：https://www.palantir.com/docs/foundry/functions/object-identifiers -->
<!-- 研读状态：已完成 -->

# Functions • Functions on objects • Object identifiers • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/functions/object-identifiers)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/functions/object-identifiers)（配对状态：matched）
- 页面语言：英文
- 主题栏目：functions
- 相关性：direct；本体函数文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:03:12Z
- 产品状态：本页覆盖 TSv1 标识；TSv2 字段对应关系见 Identify objects。

## 英文原文短摘录（每个来源不超过 25 词）

> “The identity of an object in Foundry is represented in a few different ways.”

## 摘录译文

Foundry 对象身份有多种表示方式，理解它们对正确编写函数很重要。

## 中文要点

- TSv1 对象有 RID、`typeId` 和 `primaryKey` 等身份字段。现有对象有 RID，新建对象在编辑函数执行中可能还没有 RID。
- 稳定唯一标识需要对象类型与主键组合：相同 primary key 值可以在不同对象类型中重复。
- 同一 Ontology 对象可能经参数和搜索分别加载成不同 JavaScript 对象，因此 `==`/`===` 对象引用比较会返回 false；应按 typeId 与 primaryKey 比较。
- 不能只用 RID 比较，因为新建对象 RID 为 undefined；也不宜把普通 Ontology object 直接当 JavaScript Map key，TSv1 有 `FunctionsMap` 处理对象键。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| RID | 资源标识符 | 已创建实体的资源 ID；新建对象暂不可用。 |
| typeId | 对象类型 ID | 表示对象所属的本体类型。 |
| primaryKey | 主键 | 在一个对象类型范围内标识对象的属性值。 |
| FunctionsMap | 函数对象映射 | 面向 OntologyObject 键相等语义的映射结构。 |

## 疑问与待验证项

- 复合主键的序列化、不同类型主键值类型相同和临时新建对象的身份行为需与具体 SDK 版本验证。
- TSv2 使用 `$primaryKey` 等方式访问标识，需对照其 Identify objects 文档，不应直接复制 TSv1 `typeId` 模型。

## 复刻启示

- 数据库与 API 用 `(project, ontology, object_type, primary_key)` 构成对象唯一键，而不是仅按主键或内部自增 ID。
- 画布中的对象引用以业务类型/API name 与主键组合，支持对象尚未持久化时的临时节点身份。
