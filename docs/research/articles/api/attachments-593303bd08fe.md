<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/ontology-resources/attachments -->
<!-- 研读状态：已完成 -->

# Attachment basics (v1) • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/ontology-resources/attachments)
- 官方中文来源：尚未确认（配对状态：ambiguous）
- 页面语言：英文
- 主题栏目：api/ontology-resources/attachments
- 相关性：direct；Ontology API v1 参考，保留兼容性对照并优先关注 v2
- 官方更新时间：2026-11-12T17:46:46.923Z
- 目录核对时间：2026-11-14T14:55:01Z
- 产品状态：目标分组路由未能独立载入；按可读取的官方 Attachment basics 子页核对

## 英文原文短摘录（每个来源不超过 25 词）

> “An Attachment is a file that acts like a parameter of an object.”

摘录来源：[Attachment basics (v1)](https://www.palantir.com/docs/foundry/api/ontology-resources/attachments/attachment-basics)。

## 摘录译文

Attachment 是一种作为对象参数的文件。

## 中文要点

- 可读取的同组基础页称 Attachment 是对象的文件型参数；它先作为临时文件上传，再通过 Action 附加到对象，相关能力在 Ontology Manager 配置。
- Attachment 绑定对象后成为可管理对象属性的文件内容，后续读取元数据和内容由不同 API 端点负责。
- 此分组根路由在读取端不可独立载入；以上概念依同组子页交叉确认。未从该根页推断 API 参数或文件大小限制。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Attachment | 附件 | 以对象属性/参数形式关联到对象的文件 |
| temporary file | 临时文件 | 上传后、经 Action 绑定前的暂存文件 |
| Action | 动作 | 将附件关联到对象的操作路径 |
| Ontology Manager | 本体管理器 | 配置 Attachment 属性能力的管理界面 |

## 疑问与待验证项

- 根路由本身是否只是目录入口、是否含额外通用定义，当前读取端无法确认。
- 临时文件的有效期、最大尺寸及孤立文件清理规则需结合上传附件和用户文档核对。

## 复刻启示

- 附件应作为独立资源实体保存，再通过对象属性/动作引用关联，避免把二进制内容塞入对象 JSON。
- 上传生命周期应区分“已暂存”与“已提交关联”；取消或失败时执行可审计清理，并依对象权限推导文件可见性。
- 画布属性端口可显示附件类型和单/多值基数，动作流程中展示上传、关联、读取的状态边界。
