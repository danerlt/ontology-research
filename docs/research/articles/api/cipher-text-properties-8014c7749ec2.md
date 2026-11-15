<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/cipher-text-properties -->
<!-- 研读状态：已完成 -->

# Cipher Text Property basics • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/cipher-text-properties)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/ontologies-v2-resources/cipher-text-properties
- 相关性：direct；Ontology REST API v2 参考
- 官方更新时间：2026-11-12T17:46:46.921Z
- 目录核对时间：2026-11-14T14:53:40Z
- 产品状态：目录页按版本化 API 规范页核对；涉及 Preview 的端点可能变化。

## 英文原文短摘录（每个来源不超过 25 词）

> “A CipherText property is a property that contains data encrypted with Cipher.”

## 摘录译文

CipherText 属性是存储由 Cipher 加密数据的属性。

## 中文要点

- 该目录路由重定向到版本化 API 规范页 `/cipher-text-properties/cipher-text-property-basics`。
- 定义指出 CipherText 属性承载使用 Cipher 加密的数据；读取密文与调用 Decrypt 获取明文是不同能力。
- 本目录路由与嵌套基础页语义一致，保留是为了覆盖 catalog 中不同 URL。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| CipherText property | CipherText 属性 | 保存加密数据的本体属性。 |
| Cipher | Cipher 加密服务 | 文档中提供加密能力的服务。 |

## 疑问与待验证项

- 概念页未说明加密算法、密钥轮换或属性级授权配置。

## 复刻启示

- 敏感值默认按密文处理；模型与 Agent 工具默认不获得明文读取能力。
- 画布将 CipherText 属性标记为敏感类型，并把解密建模为单独授权的动作。
