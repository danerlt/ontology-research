<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/ontology-scenarios/list-scenario-edited-links -->
<!-- 研读状态：已完成 -->

# List Scenario Edited Links • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/ontology-scenarios/list-scenario-edited-links)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/ontologies-v2-resources/ontology-scenarios
- 相关性：direct；Ontology REST API v2 参考
- 官方更新时间：2026-11-12T17:46:46.922Z
- 目录核对时间：2026-11-14T14:54:17Z
- 产品状态：预览（Preview；请求需显式启用 `preview=true`）

## 英文原文短摘录（每个来源不超过 25 词）

> “Returns the list of edited links within a given scenario for a specific object type and link type, grouped by source object.”

## 摘录译文

按源对象分组返回情景中指定对象类型与链接类型下的已编辑链接。

## 中文要点

- 端点仅适用于多对多链接；返回按 source object 分组的链接对象关系变更。
- 只有当前用户同时有权查看关系两端对象时，链接才会返回；分页量可能小于请求值。
- 端点为 Preview，需要 `preview=true`，并需 `api:ontologies-read`。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Edited link | 已编辑链接 | 情景中创建或移除的关系边 |
| Source object | 源对象 | 作为关系分组键的起点对象 |
| Both-object visibility | 双端可见权限 | 关系两端均可读才出现在结果中 |

## 疑问与待验证项

- 此接口是否区分新增边与删除边，返回的 `LinksFromObject` 数据结构需进一步核验。
- 一对多关系不由此接口返回，需联合对象编辑追踪外键字段变化。

## 复刻启示

- 变更画布要把新增、删除、未授权隐藏和未加载状态分开表示；缺少边不等于关系已删除。
- 多对多边按源对象分组读取，并检查两端对象可读权限；对一对多关系再从外键字段推导边差异。
