<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/media-reference-properties/media-reference-property-basics -->
<!-- 研读状态：已完成 -->

# Media Reference Property basics • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/media-reference-properties/media-reference-property-basics)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/ontologies-v2-resources/media-reference-properties
- 相关性：direct；Ontology REST API v2 参考
- 官方更新时间：2026-11-12T17:46:46.921Z
- 目录核对时间：2026-11-14T14:53:49Z
- 产品状态：按当前 API 参考整理；列表一致性、分支和部分媒体能力有明确限制。

## 英文原文短摘录（每个来源不超过 25 词）

> “The Ontologies API currently returns only media references associated with a Media Set View.”

## 摘录译文

当前 Ontologies API 只返回关联 Media Set View 的媒体引用。

## 中文要点

- MediaReference Property 是引用媒体项的对象属性。
- 对象加载仅返回 Media Set View 关联项；引用 Media Set item 或 dataset file 的值被省略，当前底层引用表示只支持 `mediaSetViewItem`。
- 如果用户在 Foundry 中可看到媒体但本体对象加载没有该属性值，可能是引用类型不受 API 支持，而非媒体已删除。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| MediaReference Property | 媒体引用属性 | 引用媒体项的本体字段。 |
| mediaSetViewItem | 媒体集视图项 | 当前 API 返回所支持的底层引用形式。 |
| object loading response | 对象加载响应 | 读取对象时返回的属性数据。 |

## 疑问与待验证项

- 底层不支持的引用形式由哪个其他接口读取，页面未说明。
- 本页未谈媒体读取所需的应用权限或媒体集视图配置。

## 复刻启示

- 将媒体引用属性的值状态拆分为可读、类型不支持、缺权限和源项不存在。
- 数据接入校验应对照底层引用类型，画布检查器显示受支持的 mediaSetViewItem 关系。
