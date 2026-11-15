<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/v1/ontology-resources/attachments -->
<!-- 研读状态：已完成 -->

# Attachment basics (v1) • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/v1/ontology-resources/attachments)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/v1/ontology-resources
- 相关性：direct；Ontology API v1 附件基础页，保留兼容性对照并优先关注 v2
- 官方更新时间：2026-11-12T17:46:46.923Z
- 目录核对时间：2026-11-14T14:55:35Z
- 产品状态：分组基础路由；概念由同组官方附件说明交叉验证

## 英文原文短摘录（每个来源不超过 25 词）

> “Attachments are configured in the Ontology Manager.”

摘录来源：[Attachment basics (v1)](https://www.palantir.com/docs/foundry/api/ontology-resources/attachments/attachment-basics)。

## 摘录译文

附件能力在 Ontology Manager 中配置。

## 中文要点

- 附件是可作为对象参数的文件，需配置到本体对象类型；上传后通过动作将文件关联到对象。可读取附件元数据与内容，并由对象权限约束可见性。
- 此显式 v1 分组路由和不带 `/v1` 的同组基础路由重复；可读取子页提供概念说明，根路由本身没有增加独有 endpoint 契约。
- 附件与 Media Reference 是两类能力；本页不宣称两者在规模、预览或处理能力上等价，适用场景需对照各自文档。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Attachment | 附件 | 通过本体动作关联对象的文件 |
| Ontology Manager | 本体管理器 | 配置对象附件属性的管理应用 |
| object parameter | 对象参数 | 可在对象操作中传入/关联的附件值 |
| Media Reference | 媒体引用 | 与传统 Attachment 分开的媒体资源类型 |

## 疑问与待验证项

- 该基础页根路由具体呈现内容与子页有何差异，读取结果无法确认。
- 文件容量、格式转换与权限继承细节不由此基础路由定义，应查附件和 Media Reference 专题。

## 复刻启示

- schema 元数据区分附件引用和媒体资源引用，并在属性类型/上传动作表单中给出不同约束。
- 上传、绑定、访问是不同生命周期阶段；管理界面应提供关联状态与孤儿资源清理能力。
- 权限检查与对象资源绑定，文件下载调用要重新授权并写入审计。
