<!-- 页面 URL：https://www.palantir.com/docs/foundry/functions/api-objects-links -->
<!-- 研读状态：已完成 -->

# Functions • 对象与链接 API（TypeScript v1） • API: Objects and links • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/functions/api-objects-links)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/functions/api-objects-links)（配对状态：matched）
- 页面语言：英文
- 主题栏目：functions
- 相关性：direct；本体函数文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:03:14Z
- 产品状态：本文是 TypeScript v1 对象/链接 API 参考；TSv2/Python 转由 Ontology SDK 提供读取能力。

## 英文原文短摘录（每个来源不超过 25 词）

> “Every object type imported into your project is converted to a TypeScript v1 API.”

## 摘录译文

导入项目的每一种对象类型都会转换为 TypeScript v1 API。

## 中文要点

- 导入对象类型后会生成类型化 API；属性用 Ontology API Name 暴露为字段，并可通过点号访问。
- 属性可能没有具体值，读取类型应处理 undefined，不能把本体属性当成必填字段。
- TSv1 数组属性生成 ReadonlyArray，修改时要复制并赋回整个新数组；TSv2 类型允许原位修改语法，但编辑语义仍是整体替换数组。
- 本页为 TSv1 遗留参考；TSv2 与 Python 的对象读取采用 Ontology SDK，关系遍历也应按新版链接 API 设计。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| API Name | API 名称 | 生成客户端字段时采用的本体属性名 |
| ReadonlyArray | 只读数组 | TSv1 中防止对本体数组属性做局部原位修改的类型 |
| Object API | 对象 API | 函数内读取和访问已导入本体对象的客户端接口 |

## 疑问与待验证项

- 对象/链接查询在 TSv1 与 OSDK 版本间存在代际差异；本文不能作为新实现的统一客户端契约。
- 可空属性在不同 TS 配置、序列化和 schema 更新时的类型生成应有跨版本验证。

## 复刻启示

- 数据库 schema 的空值语义要进入生成类型；属性 API 名与显示名分开保存，客户端生成按稳定 API 名绑定。
- 数组属性采用整值替换并生成明确的编辑差异，避免前端局部变更看似成功但未形成本体编辑。
