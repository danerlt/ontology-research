<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/ontology-scenarios/list-scenario-edited-object-types -->
<!-- 研读状态：已完成 -->

# List Scenario Edited Object Types • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/ontology-scenarios/list-scenario-edited-object-types)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/v2/ontologies-v2-resources
- 相关性：direct；Ontology REST API v2 参考
- 官方更新时间：2026-11-12T17:46:46.922Z
- 目录核对时间：2026-11-14T14:57:32Z
- 产品状态：预览（Preview；请求需显式启用 `preview=true`）

## 英文原文短摘录（每个来源不超过 25 词）

> “Returns the list of object type API names that have been modified within a given scenario.”

## 摘录译文

返回给定情景中已修改的对象类型 API 名称。

## 中文要点

- 这是情景改动目录接口，只返回被改动对象类型的 API 名称，不返回对象类型详情或编辑内容。
- 端点为 Preview，必须启用 `preview=true`；只需本体读取 OAuth scope。
- 可与编辑对象、链接类型列表联合调用，生成情景评审的资源总览。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Edited object type | 已编辑对象类型 | 情景改动涉及的类型名称 |
| API name | API 名称 | 机器可用的类型标识 |
| Scenario RID | 情景 RID | 查询情景变更时的范围键 |

## 疑问与待验证项

- 对象类型 API 名列表是否包含没有可见实例变更、仅 schema 被编辑的类型，页面未说明。
- 响应不带排序和分页信息，对大量类型是否完整返回需进一步核对。

## 复刻启示

- 评审面板可按类型分组展示改动，但必须再加载类型详情与对象级 diff；不要把名字列表当成完整变更集。
- 把所有相关列表快照与 scenario RID、抓取时间绑定，避免异步加载后混合不同情景的数据。
