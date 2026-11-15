<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/v1/ontology-resources/object-types -->
<!-- 研读状态：已完成 -->

# Object Type basics (v1) • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/v1/ontology-resources/object-types)
- 官方中文来源：尚未确认（配对状态：needs_review）
- 页面语言：英文
- 主题栏目：api/v1/ontology-resources
- 相关性：direct；Ontology API v1 端点参考；保留作兼容性对照，并优先关注 v2
- 官方更新时间：2026-11-12T17:46:46.923Z
- 目录核对时间：2026-11-14T14:55:41Z
- 产品状态：v1 对象类型基础页入口，未标 Preview

## 英文原文短摘录（每个来源不超过 25 词）

> “This represents an object type within a Foundry Ontology.”

## 摘录译文

表示 Foundry 本体中的一种对象类型。

## 中文要点

此 Ontology API v1 路由在目录中 canonical 到 v1 对象类型基础页。关联用户文档将对象类型描述为实体/事件 schema，并将具体对象与对象集合分别定义为单个实例与多个实例集合。Ontology 可把模型映射到企业实际数据，也可使用 Action 创建对象。该概念与 v2 基础页一致，但这不证明两个版本的 API 字段或运行时行为一致。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Object Type | 对象类型 | Ontology 中的实体/事件 schema |
| Object | 对象实例 | 一条具体实体/事件 |
| Object Set | 对象集合 | 多条对象实例组成的集合 |
| API v1 | API v1 | 本页面所属的旧版 REST API |

## 疑问与待验证项

- 该路由是概念基础页，未列出 v1 响应 schema 与限制；需要结合 v1 Get/List API 核对。
- 与 v2 页面同句只说明概念层相近，不代表迁移无需适配。

## 复刻启示

- 持久化领域 schema 与 API v1/v2 适配层分离，避免旧版响应形状污染画布节点模型。
- 对象类型节点应关联来源系统、映射字段与标识规则；运行时对象集合另行呈现和授权。
