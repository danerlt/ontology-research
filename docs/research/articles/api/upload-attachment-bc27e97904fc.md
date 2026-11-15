<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/attachments/upload-attachment -->
<!-- 研读状态：已完成 -->

# Upload Attachment (v2, latest) • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/attachments/upload-attachment)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/v2/ontologies-v2-resources
- 相关性：direct；Ontology REST API v2 附件二进制上传接口
- 官方更新时间：2026-11-12T17:46:46.922Z
- 目录核对时间：2026-11-14T14:56:44Z
- 产品状态：本页未标注 Preview

## 英文原文短摘录（每个来源不超过 25 词）

> “Any attachment which has not been linked to an object via an action within one hour after upload will be removed.”

## 摘录译文

附件上传后一小时内未通过动作关联到对象，就会被删除。

## 中文要点

- 端点：`POST /api/v2/ontologies/attachments/upload`。文件以二进制请求体上传，`Content-Type` 必须为 `application/octet-stream`；`filename` 作为查询参数传入。OAuth 操作范围为 `api:ontologies-write`。
- 成功返回 `AttachmentV2`，含 RID、文件名、大小和媒体类型；得到 RID 代表临时附件已上传，尚不代表已经绑定某对象。
- 附件必须在一小时内经 Action 关联到对象，否则被清理；过去曾绑定但后来已不再关联任何对象的附件，每两周清理一次。
- `sizeBytes` schema 标为字符串，示例 JSON 却使用数字，再次出现元数据类型差异。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Binary request body | 二进制请求体 | 上传文件字节的请求内容 |
| Temporary attachment | 临时附件 | 获得 RID 但尚未通过 Action 绑定 |
| `application/octet-stream` | 通用二进制媒体类型 | 此上传端点要求的 Content-Type |
| Orphan cleanup | 孤儿附件清理 | 清理由对象解绑的附件资源 |

## 疑问与待验证项

- 一小时按哪种时间戳计算、Action 失败后是否可刷新有效期，页面未说明。
- 每两周清理是周期性规则，具体运行时点、回收站/恢复期及保留豁免未在此端点定义。
- 文件大小上限、上传中断续传、同名文件冲突和内容安全扫描需查文件/附件用户文档。

## 复刻启示

- 采用“上传临时文件 → 返回附件引用 → Action 绑定对象”的两步流程；上传和业务对象写入由不同授权与审计事件覆盖。
- 服务端实施最大文件体积、内容校验、隔离扫描和超期清理；暂存状态与最终关联状态需可观察。
- 附件绑定 Action 必须校验临时 RID、上传主体、目标项目、本体对象和属性；失败要保留可诊断状态并按本地生命周期政策回收。
