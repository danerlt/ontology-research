<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/media-reference-properties/media-reference-property-basics -->
<!-- 研读状态：已完成 -->

# Media Reference Property basics • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/media-reference-properties/media-reference-property-basics)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/v2/ontologies-v2-resources
- 相关性：direct；本体 MediaReference 属性定义及当前投影支持范围
- 官方更新时间：2026-11-12T17:46:46.921Z
- 目录核对时间：2026-11-14T14:56:55Z
- 产品状态：基础概念页未标注 Preview；对象加载对引用类型有明确限制

## 英文原文短摘录（每个来源不超过 25 词）

> “A MediaReference Property is a property that references a media item.”

## 摘录译文

MediaReference 属性是一种引用媒体项目的属性。

## 中文要点

- MediaReference 表示本体对象属性引用一个媒体项目；它和附件属性是两种不同属性类型。
- Ontologies API 当前只返回关联 Media Set View 的媒体引用。直接标识 Media Set item 或引用 dataset file 的值会从对象加载响应中省略，因此应用可能把属性看作无值，即使媒体仍在 Foundry 中可见。
- 在底层引用结构中支持 `mediaSetViewItem`；`mediaSetItem` 和 `datasetFile` 当前不支持。这里描述的是 API 对象加载投影限制，不等于源数据已被删除。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| MediaReference Property | 媒体引用属性 | 引用媒体项目的本体属性 |
| Media Set View | 媒体集视图 | 当前 API 支持投影的引用类型 |
| mediaSetItem | 媒体集项目引用 | 当前对象加载响应不支持 |
| datasetFile | 数据集文件引用 | 当前对象加载响应不支持 |

## 疑问与待验证项

- “currently”表示支持范围可能变化；需记录 API 版本和检查日期，不能把当前限制当成永远不变的 schema 规则。
- 属性被省略时，客户端如何区分“不支持的引用类型”和“本来没有值”，本页没有给出额外标记或错误码。
- Media Set View 具体资源授权、缩略图生成和内容下载策略需要查询其专门 API 文档。

## 复刻启示

- 反序列化时区分缺省原因，例如 `absent`、`unsupported-reference-kind`、`permission-filtered`，避免将平台投影限制误判为业务空值。
- 属性 schema 保留引用类型 discriminant 与来源信息；在 UI 检查器显示“该引用当前未被对象加载 API 投影”。
- 做多系统连接时将支持矩阵绑定到连接器版本，并允许适配层增加引用种类而不破坏统一对象模型。
