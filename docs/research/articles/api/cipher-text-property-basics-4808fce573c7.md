<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/cipher-text-properties/cipher-text-property-basics -->
<!-- 研读状态：已完成 -->

# Cipher Text Property basics • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/cipher-text-properties/cipher-text-property-basics)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/ontologies-v2-resources/cipher-text-properties
- 相关性：direct；Ontology REST API v2 参考
- 官方更新时间：2026-11-12T17:46:46.921Z
- 目录核对时间：2026-11-14T14:53:41Z
- 产品状态：目录页按版本化 API 规范页核对；涉及 Preview 的端点可能变化。

## 英文原文短摘录（每个来源不超过 25 词）

> “A CipherText property is a property that contains data encrypted with Cipher.”

## 摘录译文

CipherText 属性是存储由 Cipher 加密数据的属性。

## 中文要点

- CipherText Property 是保存经 Cipher 加密数据的属性类型；它不同于普通 String 属性。
- 此基础页没有定义加密和解密操作细节；具体明文读取通过独立 Decrypt API 完成。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| CipherText | 密文类型 | 表示数据经 Cipher 加密的本体属性类型。 |
| plaintext | 明文 | 解密操作返回的原始值。 |

## 疑问与待验证项

- 属性类型是否允许参与搜索、过滤、索引或派生属性计算，需要查看 Cipher 文档与权限规则。
- 基础页没有说明明文落日志或缓存的策略。

## 复刻启示

- 密文值与明文响应使用不同类型和权限路径；禁止默认把解密后的结果写进可观察日志。
- 在本体模型和画布上显式展示敏感性标记及可使用的受控读取操作。
