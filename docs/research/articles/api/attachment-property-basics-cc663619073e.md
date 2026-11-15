<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/attachment-properties/attachment-property-basics -->
<!-- 研读状态：已完成 -->

# Attachment Property basics • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/attachment-properties/attachment-property-basics)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/ontologies-v2-resources/attachment-properties
- 相关性：direct；Ontology REST API v2 参考
- 官方更新时间：2026-11-12T17:46:46.921Z
- 目录核对时间：2026-11-14T14:53:34Z
- 产品状态：按当前 API 参考整理；批量与分支能力以页面限制为准。

## 英文原文短摘录（每个来源不超过 25 词）

> “An Attachment Property is a property that references a file attachment.”

## 摘录译文

Attachment Property 是引用文件附件的属性。

## 中文要点

- Attachment Property 本身是对象属性的一类，其值指向文件附件；不同于普通文本或数值属性。
- 本基础页只给出概念定义，附件元数据、内容读取与单/多文件结构由相关 API 端点说明。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Attachment Property | 附件属性 | 值引用一个文件附件的本体属性。 |
| attachment | 附件 | 关联到对象的文件资源。 |
| property schema | 属性 schema | 定义属性值类型和读写约束。 |

## 疑问与待验证项

- 此概念页没有说明属性是单附件还是附件数组，须以具体属性配置和响应 union 类型为准。
- 附件容量、类型白名单和生命周期策略不在此页定义。

## 复刻启示

- 把附件作为有类型的对象属性引用，并在画布属性检查器中区分文件元数据和文件内容。
- 校验附件数量、MIME 类型、大小和访问权限，具体范围需按项目策略配置。
