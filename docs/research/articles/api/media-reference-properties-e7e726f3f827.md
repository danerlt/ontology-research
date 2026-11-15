<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/media-reference-properties -->
<!-- 研读状态：已完成 -->

# Media Reference Property basics • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/media-reference-properties)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/v2/ontologies-v2-resources
- 相关性：direct；Ontology REST API v2 媒体引用属性分组入口
- 官方更新时间：2026-11-12T17:46:46.921Z
- 目录核对时间：2026-11-14T14:56:50Z
- 产品状态：分组入口未标注 Preview；读取媒体内容端点为 Preview

## 英文原文短摘录（每个来源不超过 25 词）

> “Media Reference Properties”

## 摘录译文

媒体引用属性。

## 中文要点

- 该页面是 MediaReference 属性的 REST API v2 分组入口；分组路径未能独立读取正文。官方导航包含属性基础页和 Read Media Content 端点。
- 基础页将 MediaReference 定义为引用媒体项目的属性，同时明确 Ontologies API 当前只返回与 Media Set View 关联的引用。直接指向 Media Set item 或 dataset file 的引用，在对象加载响应中会省略。
- 内容读取端点是 Preview；支持单字节范围读取，还可读取指定分支或实验性交易/场景上下文。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| MediaReference property | 媒体引用属性 | 指向媒体项目的对象属性 |
| Media Set View | 媒体集视图 | 当前对象加载支持返回的引用来源 |
| Dataset file | 数据集文件 | 当前对象加载响应不支持的直接引用类型 |
| Byte range | 字节范围 | 内容读取时的部分下载区间 |

## 疑问与待验证项

- 分组入口信息取自官方[v2 Ontology API 导航](https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources)；支持/不支持的引用形式以[属性基础页](https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/media-reference-properties/media-reference-property-basics)为准。
- 省略对象加载响应是否会映射为空、报错或仅在媒体详情接口中可见，需要在具体数据源验证。
- 媒体集权限与本体对象权限如何组合没有在这些基础说明中完整定义。

## 复刻启示

- 媒体引用要保留来源类型/引用 kind；加载器遇到当前不支持的引用形式时，应显式标记“存在但未投影”，不应静默显示空值。
- UI 把对象属性引用与媒体文件内容分开：属性显示预览入口，独立内容 API 负责受控加载和字节范围读取。
- 在接入适配层对 Media Set View、直接媒体集项目和数据集文件做能力矩阵，避免把某一种后端的支持假设成全局规则。
