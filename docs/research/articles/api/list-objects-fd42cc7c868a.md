<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/ontology-resources/objects/list-objects -->
<!-- 研读状态：已完成 -->

# List Objects (v1) • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/ontology-resources/objects/list-objects)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/ontology-resources/objects
- 相关性：direct；Ontology API v1 端点参考；保留作兼容性对照并优先关注 v2
- 官方更新时间：2026-11-12T17:46:46.923Z
- 目录核对时间：2026-11-14T14:55:15Z
- 产品状态：页面未标注 Preview；v1 存储限制需注意

## 英文原文短摘录（每个来源不超过 25 词）

> “Changes to the data could result in missing or repeated objects in the response pages.”

## 摘录译文

数据变更可能导致响应分页中遗漏或重复对象。

## 中文要点

- `GET /api/v1/ontologies/{ontologyRid}/objects/{objectType}` 列出指定本体和对象类型的实例；支持属性过滤、投影、排序与游标分页。默认页大小 1,000，OAuth2 第三方应用需要 `api:ontologies-read`。
- 此端点不保证分页一致性，数据变化可能造成跨页重复或遗漏。若需要稳定遍历，v1 本页没有提供快照开关。
- Object Storage v1 支持最多返回 10,000 个对象，超过后继续翻页会得到 `ObjectsExceededLimit`；OSv2 对象没有这一页内所述总量上限。
- 页面大小可以小于或大于请求值；有下一页时看 `nextPageToken`，不要仅根据页长度推断结束。null 属性不会出现在返回值中。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| List Objects | 对象列表 | 按对象类型读取实例集合 |
| page token | 分页令牌 | 通过 `nextPageToken` 继续遍历 |
| snapshot consistency | 快照一致性 | v1 此端点未提供该选项 |
| ObjectsExceededLimit | 对象数量超限 | OSv1 分页达到 10,000 个对象后的错误 |

## 疑问与待验证项

- `totalCount` 是字符串类型；页面未阐释计数与快速变化数据的时点关系。
- v1 的过滤语法通过查询参数表达；复合逻辑能力与 v2 JSON 搜索语法不同，迁移时应比较支持操作符而不是做机械转换。
- null 属性省略会让客户端无法仅凭属性缺席区分 null、未请求或不可见，需结合对象 schema 和权限语义处理。

## 复刻启示

- 默认分页应明确一致性级别；控制台/Agent 对完整清单的操作提供快照模式或异步导出，普通交互可选择最新数据模式。
- 以游标是否存在判断后续页，并防重复地合并实例；当底层为受限存储时显式呈现 10,000 条上限。
- 属性投影和 null 语义应与权限裁剪分开表达，避免把“字段缺失”误认为“字段值为空”。
