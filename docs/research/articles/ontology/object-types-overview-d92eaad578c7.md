<!-- 页面 URL：https://www.palantir.com/docs/foundry/object-link-types/object-types-overview -->
<!-- 研读状态：已完成 -->

# Object and link types • Object types • Overview • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/object-link-types/object-types-overview)
- 官方中文来源：[https://www.palantir.com/docs/zh/foundry/object-link-types/object-types-overview](https://www.palantir.com/docs/zh/foundry/object-link-types/object-types-overview)
- 页面语言：英文
- 主题栏目：object-link-types
- 相关性：direct；本体对象链接类型文档
- 官方更新时间：页面未提供
- 目录核对时间：2026-11-15
- 产品状态：概览页；对象类型既可由数据源供数，也可仅由 Action 创建。

## 英文原文短摘录（每个来源不超过 25 词）

> “An object type is the schema definition of a real-world entity or event.”

## 摘录译文

对象类型是对现实世界实体或事件的模式定义。

## 中文要点

- 对象类型是实体/事件的模式；对象是单条实例；对象集是多个实例的集合。对象集可由条件筛选形成。
- 对象类型像数据集 schema，对象像数据行，但 Foundry 将本体概念映射到实际数据，支持应用基于对象运行。
- 实例可由关联的 backing datasource 提供，也可通过配置 Action 创建；没有来源数据时仍可建立仅由 Action 写入的对象类型。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| object type | 对象类型 | 定义实体/事件实例结构的模式。 |
| object set | 对象集 | 由多个对象实例组成，常由过滤条件限定。 |
| backing datasource | 支撑数据源 | 为对象实例属性提供数据的数据源。 |

## 疑问与待验证项

- 该概览页解释对象与数据集的类比，但不覆盖主键、属性映射和数据刷新细节，需要结合创建/编辑页核对。
- 对象类型是定义层、对象是运行数据层；画布默认不应将海量实例全部铺开。

## 复刻启示

- 对象类型节点提供属性列表、主键、来源数据源和对象数量摘要；双击可进入对象实例浏览。
- 在图上明确区分 schema 节点与对象实例节点；真实边必须由 link type 端点生成，不能使用装饰曲线。
