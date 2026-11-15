<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/ontology-resources/objects/ontology-object-basics -->
<!-- 研读状态：已完成 -->

# Ontology Object basics (v1) • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/ontology-resources/objects/ontology-object-basics)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/ontology-resources/objects
- 相关性：direct；Ontology API v1 端点参考；保留作兼容性对照，并优先关注 v2
- 官方更新时间：2026-11-12T17:46:46.923Z
- 目录核对时间：2026-11-14T14:55:15Z
- 产品状态：v1 对象基础页兼容路由，canonical 为对象基础页面

## 英文原文短摘录（每个来源不超过 25 词）

> “An Object is a data container for a specific instance of an Object Type.”

## 摘录译文

Object 是某个 Object Type 具体实例的数据容器。

## 中文要点

此 v1 兼容路由对应 Object 基础说明：每个 Object 是 Object Type 的一个具体实例，并携带该实例的数据。页面还说明 List Objects 的属性过滤语法，包括相等、范围、数组包含和空值检查。目录 canonical 路径为 `/api/v1/ontology-resources/objects/ontology-object-basics`；本卡保留兼容入口。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Object Type | 对象类型 | 定义实例 schema 的类型 |
| Object | 对象 | 类型下的一个实例及其属性数据 |
| `p.` | 属性过滤简写 | `properties.` 的短形式 |
| Canonical URL | 规范地址 | 目录记录的主页面路由 |

## 疑问与待验证项

- 兼容路由不是另一版运行时语义；过滤规则应以 v1 canonical 页面和 List Objects 端点为准。
- 此概念页没有覆盖对象级权限细节。

## 复刻启示

- 原始页面 URL 与 canonical URL 分开保存，避免别名重复实体，同时保留覆盖证据。
- 对象关系可视化需要把 schema 关系和实例关系做成不同图层，防止概念边与数据边混淆。
