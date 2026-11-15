<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/ontology-scenarios/list-scenario-edited-entity-types -->
<!-- 研读状态：已完成 -->

# List Scenario Edited Entity Types • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/ontology-scenarios/list-scenario-edited-entity-types)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/v2/ontologies-v2-resources
- 相关性：direct；Ontology REST API v2 参考
- 官方更新时间：2026-11-12T17:46:46.922Z
- 目录核对时间：2026-11-14T14:57:31Z
- 产品状态：预览（Preview；请求需显式启用 `preview=true`）

## 英文原文短摘录（每个来源不超过 25 词）

> “One-to-many link type edits are surfaced as object edits on the object type that owns the foreign key property.”

## 摘录译文

一对多链接类型的编辑会以外键属性所属对象类型的对象编辑形式呈现。

## 中文要点

- 聚合响应分别给出 scenario 改动的对象类型列表和按源对象类型分组的多对多链接类型列表。
- 多对多 link type 修改在 `linkTypes` 字段；一对多链接修改被归入持有外键属性的对象编辑。
- 接口为 Preview，要求 `preview=true` 与本体读取权限范围。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Object types | 对象类型列表 | 情景中已修改的类型 API 名称 |
| Link types | 链接类型列表 | 按源对象类型分组的多对多关系 |
| One-to-many | 一对多 | 以拥有外键的对象变更来追踪 |

## 疑问与待验证项

- 该聚合结果中对象类型变更与对象实例字段变更是否有单独标识，需要核对完整响应定义。
- 接口名 Entity Types 容易让人误解为包括接口类型资源；页面描述实际只列 object types 与 link types。

## 复刻启示

- 评审数据模型应采用实际响应结构而非端点名称推断对象类别，保留 `objectTypes` / `linkTypes` 两个独立栏目。
- 重建变更边时，对 1:N 依据拥有方外键字段计算，对 M:N 读取 edited links，并在 diff 中显示来源方式。
