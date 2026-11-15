<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/object-types/object-type-basics -->
<!-- 研读状态：已完成 -->

# Object Type basics (v2, latest) • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/object-types/object-type-basics)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/v2/ontologies-v2-resources
- 相关性：direct；对象类型与本体建模文档
- 官方更新时间：2026-11-12T17:46:46.921Z
- 目录核对时间：2026-11-14T14:57:04Z
- 产品状态：基础概念页（无 Preview 标注；内容仅为概念入口）

## 英文原文短摘录（每个来源不超过 25 词）

> “This represents an object type within a Foundry Ontology.”

## 摘录译文

这表示 Foundry 本体中的一种对象类型。

## 中文要点

- 本页是 v1/v2 Ontology API 参考的导航型基础条目，只给出对象类型这一资源概念，并指向 Foundry 用户文档的 Object Type 说明。
- 它没有定义字段、主键、标题属性、索引、权限或链接的详细 schema，因此不能单独作为完整实现规格。
- 旧版 `/api/ontology-resources/` 路由与 v1 页面指向同类接口；`ontologies-v2-resources` 别名与显式 v2 页面对应新版 API。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Object type | 对象类型 | 本体中描述一类对象及其可用操作的资源 |
| API reference | API 参考 | 本页只做概念入口，详细语义在用户文档 |
| Versioned route | 版本化路由 | 区分 v1 与 v2 API 资源模型 |

## 疑问与待验证项

- 对象类型的完整建模语义要由它链接的 Object Type 用户文档和 Get/List Object Type 端点补足。
- 基础页没有说明接口版本的兼容策略；旧路由何时移除需以官方版本与弃用公告为准。

## 复刻启示

- 在设计规格中把“对象类型”作为带属性、主键、标题键、来源和发布状态的建模实体，但这些细节需要由其他官方页面证据支撑。
- 目录卡应保留这个基础条目，标明其信息密度低并链接到具体 API，避免把导航页误当作详尽能力说明。
