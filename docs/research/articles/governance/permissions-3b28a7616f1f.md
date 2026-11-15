<!-- 页面 URL：https://www.palantir.com/docs/zh/foundry/functions/permissions -->
<!-- 研读状态：已完成 -->

# 函数 • 权限 • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/functions/permissions)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/functions/permissions)
- 页面语言：中文（官方 AIP 机器翻译，需与英文原文交叉核对）
- 主题栏目：functions
- 相关性：direct；本体函数文档
- 官方更新时间：2026-11-12T17:46:46.935Z
- 目录核对时间：2026-11-14T14:59:30Z
- 产品状态：函数权限覆盖仓库作者权限、本体/数据源导入、已发布函数读取权限、调用者对象权限以及扩展执行白名单；对象行权限在执行读取时按最终用户身份生效。

## 英文原文短摘录（每个来源不超过 25 词）

> “Authoring and executing functions in the platform is subject to many kinds of permission checks.”

## 摘录译文

在平台中编写和执行函数会经过多种权限检查。

## 中文要点

- 函数仓库需要获得 Ontology 与对象类型资源权限以生成代码绑定；Live Preview 还需要导入对象类型背后的数据源，受限视图类型可能需要导入 Restricted View。
- 发布函数的调用者通常必须拥有发布仓库的 Viewer 权限；函数被注册到 Developer Console 与仓库读权限是两类不同检查。
- 函数读取对象时依据最终执行用户的行级权限过滤；但读时行/列权限不会自动保护函数输出，敏感信息流转需配合 marking 或分类访问控制。
- 扩展能力由管理员通过发布、执行、Marketplace 安装等白名单分别控制。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| live preview | 实时预览 | 在代码作者环境中试运行函数的模式 |
| row-level permission | 行级权限 | 根据用户权限决定可读取哪些对象行 |
| extended capability | 扩展能力 | 如函数内调用 Action 或获取长效令牌的受控能力 |
| marking | 标记 | 用于数据传播和下游访问控制的敏感级别标识 |

## 疑问与待验证项

- 页面特别说明读权限不扩展到函数输出；若函数把敏感字段编码进返回值，必须评估分类标记传播，而非只检查对象查询权限。
- 仓库 Viewer、Developer Console 注册权限、Action 权限和资源连接器权限的组合矩阵需按每个调用路径验收。
- 函数的扩展能力白名单允许特权操作；具体审批和审计责任取决于租户管理设置。

## 复刻启示

- 在 API 层区分项目成员、仓库/函数读取权、本体资源访问权、对象行/属性权限、Action 写权限和连接器凭据权限，避免一个角色覆盖全部授权。
- 每次运行按调用者身份执行对象权限过滤；运行结果建立敏感级别标签并沿 Agent/函数/导出链路传播，防止“读时授权、输出泄漏”。
- 高权限外部调用或本体写操作采用单独白名单、审批、短时凭据和逐次审计；权限不足时返回包含资源上下文的明确错误。
