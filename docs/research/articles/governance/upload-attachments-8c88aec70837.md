<!-- 页面 URL：https://www.palantir.com/docs/zh/foundry/action-types/upload-attachments -->
<!-- 研读状态：已完成 -->

# 动作类型 • 上传附件 • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/action-types/upload-attachments)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/action-types/upload-attachments)
- 页面语言：中文
- 主题栏目：action-types
- 相关性：direct；本体动作文档
- 官方更新时间：2026-11-12T17:46:46.935Z
- 目录核对时间：2026-11-14T14:58:32Z
- 产品状态：官方中文页标注为未经验证的 AIP 机器翻译；英文原文为核对依据。

## 英文原文短摘录（每个来源不超过 25 词）

> “Actions support uploading attachments from Workshop, Object Explorer, Object Views, Quiver, and Slate.”

## 摘录译文

Action 支持从 Workshop、Object Explorer、Object Views、Quiver 和 Slate 上传附件。

## 中文要点

- 动作参数需使用 Attachment 类型，对象目标属性也必须是 Attachment；对象后端数据列按文档约束使用 String，数组附件属性需对应 Array。
- 附件上传后权限继承其关联对象：可查看对象的用户可查看/下载附件，替换附件需要对象编辑权限。
- 附件在表单选择后立即上传；若提交失败或取消、对象删除或映射属性删除，孤儿附件会变为不可直接访问并在一段时间后永久删除。
- 当前文档列出全局文件大小上限 200MB，单个附件生命周期最多关联 10 个对象；限制和类型映射应在部署版本核实。中文页机器翻译未经验证。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Attachment parameter | 附件参数 | 动作表单中用于接收上传文件的参数类型。 |
| Orphan attachment | 孤儿附件 | 未再关联本体对象、等待清理的附件。 |
| Attachment property | 附件属性 | 对象类型上承载附件引用的属性。 |

## 疑问与待验证项

- 孤儿清理的准确延迟、对象权限变化传播时间以及 200MB 上限例外，需查附件 API/租户配置。
- 原文提及单个附件最多关联十个对象，删除关联不释放次数；需要在附件重复使用的数据模型上预先考虑复制。

## 复刻启示

- 附件上传和对象提交应采用暂存→关联→清理生命周期，并明确超时孤儿扫描和永久删除审计。
- 附件授权跟随所属对象，单独访问附件时重复检查对象权限；上传、替换、关联次数和文件大小均做服务端限制。
