<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/v1/ontology-resources/objects/list-objects -->
<!-- 研读状态：已完成 -->

# List Objects (v1) • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/v1/ontology-resources/objects/list-objects)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/v1/ontology-resources
- 相关性：direct；Ontology API v1 列表端点，保留兼容性对照并优先关注 v2
- 官方更新时间：2026-11-12T17:46:46.923Z
- 目录核对时间：2026-11-14T14:55:51Z
- 产品状态：页面未标注 Preview；分页一致性和 OSv1 限制需注意

## 英文原文短摘录（每个来源不超过 25 词）

> “This endpoint does not guarantee consistency.”

## 摘录译文

此端点不保证一致性。

## 中文要点

- `GET /api/v1/ontologies/{ontologyRid}/objects/{objectType}` 列出对象实例，支持过滤、`properties` 字段选择、`orderBy` 排序与 cursor 分页；默认 `pageSize` 为 1,000。
- 数据变化时分页可能漏项或重复；响应页可大于或小于请求页大小，只能依赖 `nextPageToken` 是否存在继续读取。第三方 OAuth2 需要 `api:ontologies-read`。
- OSv1 对象总计最多返回 10,000 条，超出时继续翻页触发 `ObjectsExceededLimit`；OSv2-backed objects 在本页描述中没有总数上限。null 属性不会返回。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| List Objects | 列出对象 | 读取某一对象类型的实例页 |
| orderBy | 排序 | 指定一个或多个属性及升降序 |
| pageSize | 页大小 | 默认 1,000 的期望分页数量 |
| nextPageToken | 下一页令牌 | 是否还有结果的判断依据 |
| ObjectsExceededLimit | 对象数量超限 | OSv1 超过 10,000 条时继续分页的错误 |

## 疑问与待验证项

- v1 endpoint 没有快照一致性参数；在写入活跃期间导出完整集合可能漏/重，需使用平台可用的快照/事务能力。
- `totalCount` 精确性与统计时点未说明；null 属性省略不等于字段不存在或无访问权。
- v1 页大小可短页；客户端必须继续使用令牌直到令牌为空。

## 复刻启示

- 列表结果提供快照选项和明确数据版本，交互场景与完整导出场景分开定义一致性。
- 游标绑定查询条件，支持幂等续页，合并时按稳定对象 RID 去重并展示数据刷新时间。
- 针对 OSv1 等有限后端设置能力说明和结果总量提示，避免 Agent 误认为自己看到了全集。
