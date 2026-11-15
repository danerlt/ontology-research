<!-- 页面 URL：https://www.palantir.com/docs/zh/foundry/ontology-sdk -->
<!-- 研读状态：已完成 -->

# OSDK • Ontology SDK • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/ontology-sdk)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/ontology-sdk)
- 页面语言：中文（官方机器翻译，准确性未验证）
- 主题栏目：ontology-sdk
- 相关性：direct；Ontology SDK 文档
- 官方更新时间：2026-11-12T17:46:46.937Z
- 目录核对时间：2026-11-14T15:00:35Z
- 产品状态：OSDK 多语言客户端和 Developer Console 文档总览

<!-- 研读状态：已完成 -->
# 英文原文短摘录（每个来源不超过 25 词）

> “The Ontology Software Development Kit (OSDK) allows you to access the full power of the Ontology directly from your development environment.”

## 英文原文短摘录（每个来源不超过 25 词）

> “The Ontology Software Development Kit (OSDK) allows you to access the full power of the Ontology directly from your development environment.”

## 摘录译文

Ontology Software Development Kit（OSDK）使你能在开发环境中直接使用 Ontology 的全部能力。

## 中文要点

- OSDK 支持 TypeScript 的 NPM、Python 的 Pip/Conda、Java 的 Maven，以及其他语言的 OpenAPI 规范；依据应用选择的本体子集生成类型和调用函数。
- 它让应用以 Foundry 为后端执行高规模查询与数据写回，并沿用 Foundry 细粒度治理。
- Token 限定应用可访问的本体资源，并叠加当前用户数据权限；行/列权限只在读取时过滤响应，数据进入应用后不自动受这些控制保护，需用 marking 或分类访问控制保护后续传播。
- 如果本体和应用都以代码定义，可放入 SuperRepo 同版本发布；本体变化时本地重新生成 SDK，形成编辑与预览闭环。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Generated OSDK | 生成式本体 SDK | 从本体资源子集生成的语言类型与调用接口 |
| Token scope | Token 范围 | 限定应用可以请求的本体资源 |
| Read-time enforcement | 读取时强制控制 | 权限在取数时过滤，不自动约束应用后续使用 |
| SuperRepo | SuperRepo | 将本体代码定义、函数和前端放在同一代码库的工作流 |

## 疑问与待验证项

- OSDK 响应数据离开查询层后的处理不会自动继承行列权限；应用缓存、导出、日志和模型提示仍需自身保护策略。
- SDK 版本策略与应用权限关系可能更新，需结合 Developer Console 最新文档核验。

## 复刻启示

- 客户端生成物限定到明确的本体资源子集，但服务端仍须逐次按用户权限校验；静态类型生成不是授权机制。
- 数据离开查询层后的脱敏、分类标记和审计应覆盖前端缓存与 Agent 上下文。