<!-- 页面 URL：https://www.palantir.com/docs/zh/foundry/functions/api-media -->
<!-- 研读状态：已完成 -->

# 函数 • Functions on objects • API：媒体 • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/functions/media)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/functions/api-media)
- 页面语言：中文
- 主题栏目：functions
- 相关性：direct；本体函数文档
- 官方更新时间：2026-11-12T17:46:46.935Z
- 目录核对时间：2026-11-14T14:58:48Z
- 产品状态：官方中文页标注为未经验证的 AIP 机器翻译；英文原文为核对依据。

## 英文原文短摘录（每个来源不超过 25 词）

> “Functions enable you to access and modify media in TypeScript v2, Python, and TypeScript v1.”

## 摘录译文

Functions 支持使用 TypeScript v2、Python 和 TypeScript v1 访问及修改媒体。

## 中文要点

- 旧中文 API 页介绍 TSv1 MediaItem：可通过对象媒体引用读取原始数据、元数据，并调用与特定媒体格式相关的内置操作；若缺少处理能力可安装依赖或写自定义逻辑。
- 文档提醒函数内存限制，旧 TSv1 路径建议交互媒体小于 20MB；当前功能矩阵显示 TSv1 媒体操作更完整，TSv2/Python 的文档/音频专用操作能力有限。
- 媒体输入/处理本身不等同于把媒体永久挂到对象；是否持久关联需通过 Ontology edit 更新媒体引用属性。
- 目录 `/api-media` 英文目标当前返回 404；卡片链接到现行 `/functions/media`，但旧 TSv1 API 的精细差异需按当前 SDK 版本重核。官方中文页机器翻译未经验证。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Media item | 媒体项 | 封装媒体引用并提供内容/元数据操作。 |
| Media reference property | 媒体引用属性 | 存放媒体资源引用的本体对象属性。 |
| Media metadata | 媒体元数据 | 文件类型、大小等描述媒体资源的信息。 |

## 疑问与待验证项

- 旧路由详情已不再有同 slug 英文页面；应核实现行 TSv1 MediaItem 文档是否完整涵盖旧 API 中的文档/音频操作。
- 对大媒体的内容读取是否流式、临时引用寿命及跨权限下载限制需查媒体集和 SDK 版本文档。

## 复刻启示

- 为媒体属性使用资源引用而非把二进制塞入关系图；内容存储、元数据、对象授权和派生处理各有独立生命周期。
- 对不同 SDK 运行时展示媒体能力矩阵和大小限制，并把 OCR/转录作为独立可审计处理器。
