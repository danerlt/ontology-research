<!-- 页面 URL：https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/cipher-text-properties/decrypt -->
<!-- 研读状态：已完成 -->

# Decrypt • API Reference • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/api/v2/ontologies-v2-resources/cipher-text-properties/decrypt)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：api/v2/ontologies-v2-resources
- 相关性：direct；Ontology REST API v2 密文属性解密读取接口
- 官方更新时间：2026-11-12T17:46:46.921Z
- 目录核对时间：2026-11-14T14:56:44Z
- 产品状态：本页未标注 Preview

## 英文原文短摘录（每个来源不超过 25 词）

> “Decrypt the value of a ciphertext property.”

## 摘录译文

解密一个密文属性的值。

## 中文要点

- 端点：`GET /api/v2/ontologies/{ontology}/objects/{objectType}/{primaryKey}/ciphertexts/{property}/decrypt`，定位一个对象上的单个 CipherText 属性。OAuth 操作范围为 `api:ontologies-read`。
- ontology 接受本体 API 名或 RID；对象类型、属性使用 API 名，主键定位对象。可选 `branch` 指定读取分支，未指定使用默认分支；也可携带 SDK 包 RID/版本。
- 成功响应 `DecryptionResult` 含 `plaintext: string`。示例把员工姓名作为明文返回，说明接口输出是可直接读取的敏感值。
- 该页面没有列出密文写入、密钥管理和明文留存策略；它只界定读取/解密端点的路径和响应。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| DecryptionResult | 解密结果 | 响应对象，含明文值 |
| Plaintext | 明文 | 解密后属性的字符串值 |
| CipherText property | 密文属性 | 被选定解密的本体属性 |
| Branch | 分支 | 可选的属性读取上下文 |

## 疑问与待验证项

- 文档使用读取 scope，但没有在此页列出单独的 decrypt scope；需要核对对象/属性层授权规则，不能据此认定所有本体读取者都可解密。
- 解密成功/失败、无权限、空值和类型不匹配时的状态码及审计记录未列出。
- 明文是否有缓存、速率限制、响应脱敏或专用审计事件需要查通用安全/授权文档。

## 复刻启示

- 将解密建模成独立高风险只读操作，配套最小权限、用途提示、审计、速率限制及不记录明文的日志策略。
- 前端字段默认遮罩，用户显式请求且授权通过后才显示，并设定页面离开/超时后的遮罩策略。
- Agent 不应因拥有对象读取工具而自动拥有解密能力；把解密作为独立工具并在策略层校验对象、属性、项目、分支和调用目的。该设计属于本地复刻安全边界建议。
