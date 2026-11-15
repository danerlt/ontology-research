<!-- 页面 URL：https://www.palantir.com/docs/zh/foundry/functions/api-attachments -->
<!-- 研读状态：已完成 -->

# 函数 • Functions on objects • API: 附件 • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/functions/attachments)
- 官方中文来源：尚未确认（配对状态：not_applicable）
- 页面语言：中文
- 主题栏目：functions
- 相关性：direct；本体函数文档
- 官方更新时间：2026-11-12T17:46:46.935Z
- 目录核对时间：2026-11-14T14:58:45Z
- 产品状态：官方中文页标注为未经验证的 AIP 机器翻译；英文原文为核对依据。

## 原文短摘录与翻译

> 英文原文：An attachment is a file that acts like an object property.

> 中文译文：附件是一种表现为对象属性的文件。

## 摘录译文

以上为英文短摘录及中文译文。官方中文页面为 AIP 机器翻译，准确性未经验证。

## 中文要点

- 附件可通过动作输入传给函数，也可从对象属性读取；TSv1 提供 `readAsync()` 读取原始 Blob，Python/TSv2 使用 OSDK/API Gateway 相关类型与方法。
- 附件最初是临时文件；经 Action 或本体编辑关联到对象后才持久化并像属性一样访问。未关联文件仅上传者可见，随后会自动删除。
- 页面提醒 TSv1 函数内存限制严格，建议只处理小于 20MB 的附件；较新的 Python/TSv2 默认内存上限更高且可配置。
- 目录旧路由 `/api-attachments` 当前跳转至英文 `/attachments`；卡片使用现行目标链接，保留旧中文页面路径作来源记录。中文译文精度未验证。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Attachment | 附件 | 与对象属性关联的文件资源。 |
| Temporary file | 临时文件 | 尚未持久关联到对象的上传内容。 |
| Blob | 二进制对象 | JavaScript 中用于表示不可变原始文件数据的类型。 |

## 疑问与待验证项

- 旧 API 路由/TSv1 接口与现行共享附件文档的 SDK 名称有差异，需以仓库模板版本为准。
- 原文未在该段统一说明临时附件清理时长、最大文件大小及权限变化的传播延迟。

## 复刻启示

- 把附件实体与本体属性引用分开，先暂存上传、经授权 Action 关联后持久化。
- 为大文件设计流式/分段访问或明确内存限制；附件访问必须继承对象级权限，孤儿文件需定期清理。
