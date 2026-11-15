<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/ontology-resources/attachments/upload-attachment -->
<!-- 研读状态：已完成 -->

# Upload Attachment (v1) • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/ontology-resources/attachments/upload-attachment)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/ontology-resources/attachments
- 相关性：direct；Ontology API v1 端点参考，保留兼容性对照并优先关注 v2
- 官方更新时间：2026-11-12T17:46:46.923Z
- 目录核对时间：2026-11-14T14:55:02Z
- 产品状态：页面未标注 Preview；附件临时清理周期由接口文档明确

## 英文原文短摘录（每个来源不超过 25 词）

> “Any attachment which has not been linked to an object via an action within one hour after upload will be removed.”

## 摘录译文

上传后一小时内未通过动作关联到对象的附件会被移除。

## 中文要点

- `POST /api/v1/attachments/upload?filename=...` 以原始二进制请求体上传文件，`Content-Type` 必须是 `application/octet-stream`；OAuth2 第三方应用需要 `api:ontologies-write`。
- 成功响应返回附件元数据对象（RID、文件名、字节数、媒体类型），随后需通过 Action 把它关联到对象。
- 未在上传后一小时内关联对象的附件会被清理；曾经映射、后来不再关联任何对象的附件按双周周期清理。此两种情况的周期不同。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| upload attachment | 上传附件 | 生成临时附件资源的二进制上传接口 |
| filename | 文件名 | 上传请求的查询参数 |
| application/octet-stream | 八位字节流媒体类型 | 请求必须使用的 Content-Type |
| api:ontologies-write | 本体写入范围 | OAuth2 客户端执行上传所需范围 |

## 疑问与待验证项

- API 页未定义最大文件尺寸、重试/幂等键、分块上传或病毒扫描行为，应在应用层按部署要求补足。
- 元数据响应中 `sizeBytes` schema 标为字符串，但示例响应使用 JSON 数字；调用端应按实测和生成 SDK 确认。
- 清理周期为平台描述，未说明是否精确到小时或执行窗口，业务不得依赖临界点提交。

## 复刻启示

- 上传与对象关联分成两个状态和权限动作；短期上传令牌/附件 RID 应带过期时间，后台清理孤立资源。
- 提供幂等上传、进度和校验结果；附件元数据在上传后返回，关联对象后才进入正常对象授权范围。
- 兼容二进制请求体，避免 Base64 放大文件；设置明确上传限制、扫描策略及失败重试语义。
