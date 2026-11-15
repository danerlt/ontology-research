<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/media-reference-properties -->
<!-- 研读状态：已完成 -->

# Media Reference Property basics • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/media-reference-properties)
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

- 目录路由重定向到带版本号的 Media Reference Property basics 规范页。
- 规范页的重要限制是：对象加载响应只包含与 Media Set View 关联的媒体引用；直接引用 Media Set item 或 dataset file 的值会被忽略。
- 底层当前只支持 `mediaSetViewItem`；其他两种引用形态可能在 Foundry 中存在但在对象响应中看起来为空。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| MediaReference Property | 媒体引用属性 | 引用 Media Set 媒体项的对象属性。 |
| Media Set View | 媒体集视图 | 本体 API 当前支持的媒体引用来源。 |
| mediaSetItem | Media Set 项 | 直接引用形式，目前不在对象加载响应中支持。 |

## 疑问与待验证项

- 页面未给出不支持引用形态的替代读取 API。
- “对象响应空值”容易与源数据缺失混淆，应检查底层引用类型。

## 复刻启示

- 数据来源适配层要保留媒体引用的来源类型，区分无值、无权限与当前 API 不支持的引用形态。
- 界面给出“媒体引用存在但加载响应不支持”的诊断状态，避免用户误判源数据。
