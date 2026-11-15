<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/cipher-text-properties/decrypt -->
<!-- 研读状态：已完成 -->

# Decrypt • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/ontologies-v2-resources/cipher-text-properties/decrypt)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/ontologies-v2-resources/cipher-text-properties
- 相关性：direct；Ontology REST API v2 参考
- 官方更新时间：2026-11-12T17:46:46.921Z
- 目录核对时间：2026-11-14T14:53:41Z
- 产品状态：目录页按版本化 API 规范页核对；涉及 Preview 的端点可能变化。

## 英文原文短摘录（每个来源不超过 25 词）

> “Decrypt the value of a ciphertext property.”

## 摘录译文

解密 CipherText 属性值。

## 中文要点

- GET `/api/v2/ontologies/{ontology}/objects/{objectType}/{primaryKey}/ciphertexts/{property}/decrypt` 对指定对象属性取明文。
- 响应为 `DecryptionResult`，包含 plaintext 字符串；第三方 OAuth scope 为 `api:ontologies-read`，可选择 SDK 版本或 branch。
- 从对象、主键与属性路径定位值，意味着解密操作须保留完整资源上下文以做授权和审计。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| DecryptionResult | 解密结果 | 响应中包含 plaintext 字段。 |
| plaintext | 明文 | 经授权解密返回的敏感值。 |
| primaryKey | 主键 | 定位持有 CipherText 属性的对象。 |

## 疑问与待验证项

- 本页仅列读取 scope，没有完整描述平台侧 Cipher 解密策略或附加审计规则。
- branch 上解密与当前对象数据版本的关系需在目标环境确认。

## 复刻启示

- 实现独立 decrypt 权限并记录谁、何时、对哪个对象和字段取了明文。
- UI 默认遮蔽敏感值，用户主动查看后短时展示且不进入普通查询缓存。
