<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/object-types -->
<!-- 研读状态：已完成 -->

# Object Type basics (v2, latest) • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/object-types)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/ontologies-v2-resources/object-types
- 相关性：direct；对象类型与本体建模文档
- 官方更新时间：2026-11-12T17:46:46.921Z
- 目录核对时间：2026-11-14T14:53:50Z
- 产品状态：按当前 API 参考整理；列表一致性、分支和部分媒体能力有明确限制。

## 英文原文短摘录（每个来源不超过 25 词）

> “This represents an object type within a Foundry Ontology.”

## 摘录译文

这代表 Foundry Ontology 中的一个对象类型。

## 中文要点

- 目录路由指向 `/api/v2/.../object-types/object-type-basics` 规范页；正文把它定义为 Foundry Ontology 中的对象类型。
- 对象类型的属性、主键、标题字段、状态和数据来源需查询 Get Object Type schema。
- 这是目录兼容入口，与嵌套基础页同义，保留是为了逐条覆盖编目 URL。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Object Type | 对象类型 | 本体中表示一类业务实体的 schema。 |
| primary key | 主键 | 定位该对象类型实例的唯一属性。 |
| canonical route | 规范路由 | 版本化 API 文档的目标页面。 |

## 疑问与待验证项

- 概念页没有给出对象类型包含的全部字段或生命周期规则。

## 复刻启示

- schema 画布节点绑定对象类型 RID/API name，并通过属性与 Link Type 表达可查询结构。
- 目录 alias 与规范页做映射，避免将 URL 数量误当作 schema 类型数。
