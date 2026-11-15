<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/ontology-resources/object-types/list-outgoing-link-types -->
<!-- 研读状态：已完成 -->

# List Outgoing Link Types (v1) • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/ontology-resources/object-types/list-outgoing-link-types)
- 官方中文来源：尚未确认（配对状态：needs_review）
- 页面语言：英文
- 主题栏目：api/ontology-resources/object-types
- 相关性：direct；Ontology API v1 端点参考；保留作兼容性对照，并优先关注 v2
- 官方更新时间：2026-11-12T17:46:46.923Z
- 目录核对时间：2026-11-14T14:55:08Z
- 产品状态：正式 API（v1/v2 页面均未标注 Preview）

## 英文原文短摘录（每个来源不超过 25 词）

> “List the outgoing links for an object type.”

## 摘录译文

列出某个对象类型的所有出向链接。

## 中文要点

- 接口按 ontology 与源对象类型分页返回 LinkTypeSide 列表，包含链接 API 名称、目标对象类型、ONE/MANY 基数及可选外键属性。
- v2 响应还提供链接发布状态和 link type RID，并允许指定 branch；v1 以 ontology RID 访问且没有 branch 参数。
- 两版都采用 nextPageToken 续页，OAuth 应用需要 `api:ontologies-read`。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Link type side | 链接端定义 | 从特定对象类型视角暴露的链接元数据 |
| Cardinality | 基数 | ONE 或 MANY |
| Next page token | 下一页令牌 | 继续列举链接定义 |

## 疑问与待验证项

- 本端列表对反向关系是否有独立表示、无权限链接是否过滤，页面没有展开解释。
- v2 状态字段值含 ACTIVE、ENDORSED、EXPERIMENTAL、DEPRECATED；其状态转换和发布治理需参考本体编辑文档。

## 复刻启示

- 画布可用此接口按节点按需加载出边，呈现链接名称、基数、状态和外键提示；节点的入边需要从相邻类型或全局关系索引补齐。
- 保留分页、branch 与 API 版本差异，才能在大型多项目图中局部展开并切换草稿定义。
