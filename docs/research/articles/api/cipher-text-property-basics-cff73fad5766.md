<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/cipher-text-properties/cipher-text-property-basics -->
<!-- 研读状态：已完成 -->

# Cipher Text Property basics • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/cipher-text-properties/cipher-text-property-basics)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/v2/ontologies-v2-resources
- 相关性：direct；本体 CipherText 属性概念定义
- 官方更新时间：2026-11-12T17:46:46.921Z
- 目录核对时间：2026-11-14T14:56:44Z
- 产品状态：基础概念页未标注 Preview

## 英文原文短摘录（每个来源不超过 25 词）

> “A CipherText property is a property that contains data encrypted with Cipher.”

## 摘录译文

CipherText 属性是一种包含由 Cipher 加密数据的属性。

## 中文要点

- 页面给出 CipherText property 的单句定义：它是保存 Cipher 加密数据的本体属性。
- 该类型与普通文本属性语义不同；明文不应被假定可通过普通对象读取返回。v2 导航另有 Decrypt 端点，负责读取属性的明文结果。
- 本页没有定义加密算法、密钥轮换、密文格式、可比较性、写入方式或明文权限；它只给出概念定义。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| CipherText property | 密文属性 | 含加密数据的本体属性 |
| Cipher | Cipher 加密机制 | 页面所指的加密机制名 |
| Encrypted data | 加密数据 | 属性中保存的密文值 |
| Plaintext | 明文 | 解密后可读的值 |

## 疑问与待验证项

- Cipher 与密钥归属、租户隔离、轮换和恢复机制需查 Cipher 文档及平台管理员说明。
- 普通对象 API 对密文属性返回的具体值是什么、是否可写或仅返回占位信息，本页未描述。
- 权限模型是否区分“读密文”和“解密”需要从对应 API 与 Foundry 授权文档确认。

## 复刻启示

- 类型系统中单列敏感加密字段，不让表单、日志、搜索索引和 Agent 通用序列化器默认当成普通字符串。
- 将明文访问设置为显式解密动作，与一般读取权限分离；保存用途与授权决策审计，但避免日志写入明文。
- 对密钥服务、加密算法与轮换流程应复用成熟 KMS/密码库并做安全评审，不根据这句 API 定义自行发明密码格式。
