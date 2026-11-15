<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/ontology-objects -->
<!-- 研读状态：已完成 -->

# Ontology Object basics (v2, latest) • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/ontology-objects)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/ontologies-v2-resources/ontology-objects
- 相关性：direct；Ontology REST API v2 参考
- 官方更新时间：2026-11-12T17:46:46.921Z
- 目录核对时间：2026-11-14T14:54:08Z
- 产品状态：v2 Object 基础页兼容路由，未标 Preview

## 英文原文短摘录（每个来源不超过 25 词）

> “An Object is a data container for a specific instance of an Object Type.”

## 摘录译文

Object 是某个 Object Type 具体实例的数据容器。

## 中文要点

该兼容入口映射到 v2 Object 基础页：Object 是 Object Type 的单个实例数据容器。对象类型 schema、运行时对象与对象集合是三个不同层次；本页定义的是运行时对象。目录 canonical 路径为 `/api/v2/ontologies-v2-resources/ontology-objects/ontology-object-basics`。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Object | 对象 | 对象类型的一条具体实例数据 |
| Object Type | 对象类型 | 实例所遵循的本体结构定义 |
| Object Set | 对象集合 | 多个对象实例的集合 |
| API route alias | API 路由别名 | 指向 canonical v2 基础页的目录路由 |

## 疑问与待验证项

- 此兼容入口本身不定义对象读取 schema；需要通过 canonical 页与具体端点查看字段和分页。
- API 路由别名不能与实际运行对象的 RID/API 标识混为一谈。

## 复刻启示

- 页面路由 canonical 映射应只用于文档去重；画布对象节点仍以类型 ID/主键表示实际资源。
- 根据对象查询权限过滤实例属性，避免从运行时图视图绕过对象安全策略。
