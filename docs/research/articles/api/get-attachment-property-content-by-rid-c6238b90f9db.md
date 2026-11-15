<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/attachment-properties/get-attachment-property-content-by-rid -->
<!-- 研读状态：已完成 -->

# Get Attachment Property Content By Rid • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/attachment-properties/get-attachment-property-content-by-rid)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/ontologies-v2-resources/attachment-properties
- 相关性：direct；Ontology REST API v2 参考
- 官方更新时间：2026-11-12T17:46:46.921Z
- 目录核对时间：2026-11-14T14:53:37Z
- 产品状态：按当前 API 参考整理；批量与分支能力以页面限制为准。

## 英文原文短摘录（每个来源不超过 25 词）

> “The RID must exist in the attachment array of the property.”

## 摘录译文

该 RID 必须存在于该属性的附件数组中。

## 中文要点

- GET 路径在对象与 Attachment Property 后附加 attachment RID，再读取该特定文件内容。
- RID 必须属于该属性的附件数组；第三方 OAuth 需 `api:ontologies-read`，可选指定 branch。
- 与不带 RID 的 Content 端点相比，此端点在多附件情况下显式选择文件，成功正文为内容字符串。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| attachment array | 附件数组 | 属性当前关联的附件集合。 |
| content by RID | 按 RID 读取内容 | 显式定位集合中的某一附件。 |
| parent object | 父对象 | 持有附件属性的本体对象。 |

## 疑问与待验证项

- 文档没有说明附件元数据变更后缓存如何失效。
- 下载响应的流式/范围请求能力需以实际 API 行为为准。

## 复刻启示

- 下载前验证 RID 确实属于当前对象属性，并在授权失败时返回不暴露文件是否存在的错误。
- 把“列元数据、选具体 RID、读文件内容”设计为清晰的三步交互。
