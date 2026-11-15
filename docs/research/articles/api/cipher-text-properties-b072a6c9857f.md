<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/cipher-text-properties -->
<!-- 研读状态：已完成 -->

# Cipher Text Property basics • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/cipher-text-properties)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/v2/ontologies-v2-resources
- 相关性：direct；Ontology REST API v2 CipherText 属性分组入口
- 官方更新时间：2026-11-12T17:46:46.921Z
- 目录核对时间：2026-11-14T14:56:44Z
- 产品状态：分组入口未标注 Preview；具体操作状态以子页为准

## 英文原文短摘录（每个来源不超过 25 词）

> “Cipher Text Properties”

## 摘录译文

密文属性。

## 中文要点

- 这是 Ontology REST API v2 的密文属性分组入口，目标分组 URL 无法独立读取正文。官方 v2 API 导航列出 CipherText Property basics 与 Decrypt 两项。
- 子页将 CipherText 属性定义为包含由 Cipher 加密数据的属性；Decrypt 接口则按本体、对象类型、主键和属性定位并返回明文。
- 分组页没有提供密钥管理、字段写入、密文序列化或授权细节。下文复刻建议应视为安全设计要求，不代表 Palantir 的内部密码系统配置。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| CipherText property | 密文属性 | 存储加密数据的特殊本体属性 |
| Cipher | Cipher 加密机制 | 该属性定义所引用的加密机制 |
| Decrypt | 解密 | 从本体属性读出明文的独立 API |
| Ciphertext | 密文 | 加密后的值，不等同于明文展示值 |

## 疑问与待验证项

- 分组入口内容依据官方 v2 API 导航中的“Cipher Text Properties”及两项子页；密文属性详情见[基础页](https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/cipher-text-properties/cipher-text-property-basics)，明文读取见[Decrypt](https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/cipher-text-properties/decrypt)。
- `api:ontologies-read` 操作 scope 是否充分表达解密授权并不明确；需要区别 OAuth scope 与数据访问/解密权限。
- 页面没有说明明文是否出现在查询缓存、日志、审计事件或 Agent 上下文中。

## 复刻启示

- 密文属性应在 schema 中标为敏感类型，列表与画布默认显示遮罩状态；明文读取通过专门服务端操作和明确授权触发。
- 解密操作需强制审计调用人、对象、属性、项目/本体、分支、用途与结果状态，并限制日志记录明文。
- Agent 工具编排应默认只接收密文/脱敏投影；只有在明确授权的工具步骤内短暂解密，且不把结果自动写入长期记忆或追踪日志。这是本地安全设计推论。
