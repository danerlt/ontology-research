<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/ontology-scenarios/list-scenario-edited-link-types -->
<!-- 研读状态：已完成 -->

# List Scenario Edited Link Types • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/ontology-scenarios/list-scenario-edited-link-types)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/v2/ontologies-v2-resources
- 相关性：direct；Ontology REST API v2 参考
- 官方更新时间：2026-11-12T17:46:46.922Z
- 目录核对时间：2026-11-14T14:57:32Z
- 产品状态：预览（Preview；请求需显式启用 `preview=true`）

## 英文原文短摘录（每个来源不超过 25 词）

> “Returns the list of outgoing links that have been modified within a given scenario for an object type.”

## 摘录译文

返回情景内某对象类型上已修改的出向链接。

## 中文要点

- 该接口返回指定对象类型中的已编辑出向链接 API 名称，但只覆盖多对多链接类型。
- 一对多链接通常通过拥有外键属性的对象类型上的对象变更呈现，不会作为独立的 link type 编辑返回。
- 端点处于 Preview，需 `preview=true`；OAuth 应用需要读取权限范围。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Many-to-many | 多对多 | 此接口列举的链接类型基数 |
| One-to-many | 一对多 | 改动会显示为外键所属对象上的对象编辑 |
| Foreign key owner | 外键所属方 | 承载链接外键属性的对象类型 |

## 疑问与待验证项

- 本接口的 “link type edits” 是否只列定义变更，或也包含关系实例边数据变化，应结合 edited links 接口区分。
- 按 source object type 分组的关联映射具体结构需进一步读取响应 schema。

## 复刻启示

- 评审汇总不能只调用本接口；需要将 M:M 链接改动和 1:M 外键对象改动合并到统一关系 diff 视图。
- 对画布边使用基数元数据区分变更呈现策略，防止一对多对象字段改动被遗漏。
