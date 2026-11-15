<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/object-types -->
<!-- 研读状态：已完成 -->

# Object Type basics (v2, latest) • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/object-types)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/v2/ontologies-v2-resources
- 相关性：direct；对象类型与本体建模文档
- 官方更新时间：2026-11-12T17:46:46.921Z
- 目录核对时间：2026-11-14T14:56:55Z
- 产品状态：v2 对象类型基础页入口，未标 Preview

## 英文原文短摘录（每个来源不超过 25 词）

> “This represents an object type within a Foundry Ontology.”

## 摘录译文

表示 Foundry 本体中的一种对象类型。

## 中文要点

`/api/v2/.../object-types` 路由在目录中 canonical 到对象类型基础页。本体用户文档将对象类型定义为真实实体或事件的 schema；Object 是该类型的单个实例，Object Set 是实例集合。对象类型可映射已有数据源，也可由 Action 创建对象。基础 API 页本身不是完整 schema 字段参考。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Object Type | 对象类型 | 真实实体或事件的结构定义 |
| Object Instance | 对象实例 | 一个具体实体或事件记录 |
| Object Set | 对象集合 | 多个对象实例的集合 |
| Backing datasource | 支撑数据源 | 提供本体对象数据的企业数据源 |

## 疑问与待验证项

- 对象类型属性、主键、标题字段与来源绑定细节不在基础页描述；需查对象类型创建及 Get Object Type 页面。
- v2 路由的 canonical 指向 `/object-type-basics` 子页，本卡保留编目中的原始入口。

## 复刻启示

- 画布 schema 视图以对象类型作为实体节点，并把数据源映射和 Action 创建方式作为来源信息；对象实例留给运行时图查看。
- 项目隔离模型将本体对象类型与来源系统绑定在项目域下，防止跨项目误用对象数据。
