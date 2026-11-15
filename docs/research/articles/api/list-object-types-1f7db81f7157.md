<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/ontology-resources/object-types/list-object-types -->
<!-- 研读状态：已完成 -->

# List Object Types (v1) • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/ontology-resources/object-types/list-object-types)
- 官方中文来源：尚未确认（配对状态：needs_review）
- 页面语言：英文
- 主题栏目：api/ontology-resources/object-types
- 相关性：direct；Ontology API v1 端点参考；保留作兼容性对照，并优先关注 v2
- 官方更新时间：2026-11-12T17:46:46.922Z
- 目录核对时间：2026-11-14T14:55:08Z
- 产品状态：正式 API（v2 列表响应的 aliases 字段恒为空；无 Preview 标注）

## 英文原文短摘录（每个来源不超过 25 词）

> “Lists the object types for the given Ontology.”

## 摘录译文

列出指定本体中的对象类型。

## 中文要点

- v1/v2 都使用分页读取本体中的对象类型；默认 pageSize 为 500，响应页可能大于或小于请求值，但只要还有数据就保证至少返回一条。
- 客户端应把响应的 `nextPageToken` 原样用于下一页，直到没有后续令牌。
- v2 额外支持 branch 与 `includeDatasources`；数据源默认不展开。v2 列表接口的 `aliases` 恒为空，需通过按 RID 读取路径获取别名。v1 使用 ontology RID，v2 接受 API 名称或 RID。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Page token | 分页令牌 | 延续对象类型列表的读取位置 |
| Datasource | 数据源 | 对象类型背后的数据源定义 |
| Alias | 别名 | 列表读取不提供，需另行按 RID 读取 |

## 疑问与待验证项

- 列表页大小不是严格上限，前端不能假设返回条数等于 pageSize。
- 开启数据源展开后具体的权限裁剪与成本未在此页说明，需对照 datasource 字段和权限文档确认。

## 复刻启示

- 对象类型目录应支持游标分页，不要使用 offset/limit 假设；加载状态以 nextPageToken 为准。
- 列表摘要与详情获取分开：列表负责名称/核心字段，按 RID 读取补别名或扩展元数据。
- 多项目复制中应让项目和 branch 成为显式作用域，避免同 API 名跨本体串数据。
