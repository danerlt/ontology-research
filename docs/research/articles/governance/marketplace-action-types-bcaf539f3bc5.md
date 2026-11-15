<!-- 页面 URL：https://www.palantir.com/docs/zh/foundry/action-types/marketplace-action-types -->
<!-- 研读状态：已完成 -->

# 动作类型 • 将操作类型添加到Marketplace产品 • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/action-types/marketplace-action-types)
- 官方中文来源：尚未确认（配对状态：not_applicable）
- 页面语言：中文
- 主题栏目：action-types
- 相关性：direct；本体动作文档
- 官方更新时间：2026-11-12T17:46:46.935Z
- 目录核对时间：2026-11-14T14:58:17Z
- 产品状态：官方中文页标注为未经验证的 AIP 机器翻译；英文原文为核对依据。

## 原文短摘录与翻译

> 英文原文：Most action type features are supported, except actions that reference object types with unsupported features.

> 中文译文：除引用了不支持功能的对象类型的操作外，大多数操作类型功能均受支持。

## 摘录译文

以上为英文短摘录及中文译文。官方中文页面为 AIP 机器翻译，准确性未经验证。

## 中文要点

- Action Type 可由 Foundry DevOps 打包为 Marketplace 产品供其他用户安装；文档建议从 Workshop 等上层内容的依赖关系面板带入动作。
- 打包前应检查对象类型的功能兼容性；Security & Submission criteria 不应引用单个用户，文档建议改为引用组。
- 动作作为产品依赖时，要连同引用对象类型等必要资源一起声明，安装目标环境还需满足功能支持和权限配置。
- 官方中文页标记为未经验证的机器翻译；特别是对象类型兼容清单需查英文页面与最新 Marketplace 文档。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Marketplace product | Marketplace 产品 | 可跨环境分发和安装的一组平台资源。 |
| Dependency panel | 依赖面板 | 从应用内容依赖关系选择需要随产品打包的资源。 |
| Submission criteria | 提交条件 | 动作安全与执行前校验配置。 |

## 疑问与待验证项

- “unsupported features”对应的对象类型能力清单可能更新；打包时应读取当前产品校验结果。
- 更换用户引用为组引用后，目标组织的组映射和成员管理责任需在安装文档确认。

## 复刻启示

- 设计可移植包清单和目标环境预检，明确阻止不兼容对象类型、缺失依赖与未映射权限主体。
- 发布依赖图应把 Action、ObjectType、应用和权限组画成可追踪的有向图，提示变更影响。
