<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/v1/ontology-resources/attachments/upload-attachment -->
<!-- 研读状态：已完成 -->

# Upload Attachment (v1) • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/v1/ontology-resources/attachments/upload-attachment)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/v1/ontology-resources
- 相关性：direct；Ontology API v1 上传端点，保留兼容性对照并优先关注 v2
- 官方更新时间：2026-11-12T17:46:46.923Z
- 目录核对时间：2026-11-14T14:55:40Z
- 产品状态：页面未标注 Preview；平台临时清理规则明确

## 英文原文短摘录（每个来源不超过 25 词）

> “Any attachment which has not been linked to an object via an action within one hour after upload will be removed.”

## 摘录译文

附件上传后一小时内若未通过动作关联到对象，就会被移除。

## 中文要点

- `POST /api/v1/attachments/upload?filename=...` 上传原始二进制文件，请求 `Content-Type` 固定为 `application/octet-stream`；OAuth2 第三方应用需要 `api:ontologies-write`。
- 成功返回附件元数据对象；文件需要后续由 Action 与对象关联。上传后 1 小时仍未关联的附件将清理；旧的已映射附件若再无对象关联则每两周清理。
- 以上两类孤儿文件有不同清理周期。页面未定义最大文件尺寸、幂等重试和分块传输。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| upload endpoint | 上传端点 | 产生待关联附件资源的 API |
| octet-stream | 二进制流 | 上传请求必须提供的媒体类型 |
| orphan attachment | 孤立附件 | 未及时关联或已失去所有对象关联的资源 |
| api:ontologies-write | 本体写入 scope | 上传操作所需的 OAuth2 权限 |

## 疑问与待验证项

- 一小时清理与双周清理的执行窗口、失败上传暂存行为未说明，业务不可依赖清理时点。
- v1 页面未标最大文件大小、总配额或允许 MIME 类型；需要由部署策略和应用网关限制。
- `sizeBytes` 响应 schema 与示例数字类型不一致，见 Get Attachment 卡。

## 复刻启示

- 用短时暂存记录实现上传生命周期，动作提交时完成对象引用；动作取消/失败时由后台清理任务收敛资源。
- 将写 scope 和对象修改授权分层检查，上传成功并不等于用户已能访问关联对象。
- 对上传实行文件大小/MIME 限制、内容扫描、幂等键和可恢复分块，补足文档没有约定的工程安全边界。
