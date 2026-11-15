<!-- 页面 URL：https://www.palantir.com/docs/foundry/functions/model-aliases -->
<!-- 研读状态：已完成 -->

# Functions • Aliases • Model aliases • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/functions/model-aliases)
- 官方中文来源：尚未确认（配对状态：ambiguous）
- 页面语言：英文
- 主题栏目：functions
- 相关性：direct；本体函数文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:03:23Z
- 产品状态：未见本页另标 Beta、预览或弃用状态。

## 英文原文短摘录（每个来源不超过 25 词）

> Model aliases are named references to language models that provide a convenient way to reference language models in code.

## 摘录译文

模型别名是指向语言模型的命名引用，可让代码方便地引用模型。

## 中文要点

- 模型别名在 TSv2/Python 代码仓库的 Platform SDK 资源导入中配置；别名 key 在仓库内唯一，运行时通过名称解析出模型 RID 后交给模型客户端。
- 别名可以用于 Marketplace 产品中的函数，但安装期间不能重新映射；如果目标环境没有对应模型，函数会在运行时解析失败。
- 文档将模型别名与 custom aliases 区分：后者可承载字符串型配置、功能开关和环境设置，允许安装者在 Marketplace 安装中定制。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Model alias | 模型别名 | 在仓库范围内命名引用特定模型资源。 |
| RID | 资源标识符 | 平台对模型资源的标识；由别名解析得到。 |
| Custom alias | 自定义别名 | 用于配置值、功能标志或环境参数的可安装期别名。 |

## 疑问与待验证项

- 模型别名无法在 Marketplace 安装时改指向，因此跨环境一致性依赖模型资源存在和可用；应在部署前验证 RID 解析。
- 文档未将其定义为自动模型路由或回退策略；若要多模型切换，应在应用层明确策略和审计。

## 复刻启示

- 把模型逻辑名称、目标资源 RID、仓库作用域和环境可用性作为显式依赖，安装前做资源解析检查。
- 将模型路由别名与普通环境配置 alias 分为两类，并在 UI 中说明是否允许安装方重映射。
