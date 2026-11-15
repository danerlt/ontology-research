<!-- 页面 URL：https://www.palantir.com/docs/foundry/action-types/marketplace-action-types -->
<!-- 研读状态：已完成 -->

# 动作类型 • 添加到 Marketplace 产品 • Add action types to a Marketplace product • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/action-types/marketplace-action-types)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/action-types/marketplace-action-types)（配对状态：matched）
- 页面语言：英文
- 主题栏目：action-types
- 相关性：direct；本体动作文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:02:24Z
- 产品状态：Action 类型可以作为 Marketplace 内容分发；用户引用与不支持的对象能力会影响打包。

## 英文原文短摘录（每个来源不超过 25 词）

> “Most action type features are supported, except actions that reference object types with unsupported features.”

## 摘录译文

除引用了含不支持能力的对象类型的 Action 外，大多数 Action 功能都受支持。

## 中文要点

- 使用 Foundry DevOps 将 Action 类型作为 Marketplace 产品内容分发，使其他用户可以安装复用。
- 打包前检查 Action 引用的对象类型是否含不支持能力；Security & Submission criteria 不应引用具体用户，应将用户条件改为组条件。
- 可直接添加 Action 类型，也可先选 Workshop 应用等内容，再从依赖面板加入其相关 Action。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Marketplace product | Marketplace 产品 | 可安装和复用的打包内容 |
| Dependencies panel | 依赖面板 | 基于应用依赖发现需要分发的 Action |
| Unsupported object feature | 不支持的对象能力 | 会阻止 Action 类型打包的对象侧能力 |

## 疑问与待验证项

- 页面未列完整的对象能力兼容矩阵，打包前需查对象类型 Marketplace 支持文档。
- 目标用户/组身份的解析与目标组织成员映射，需结合安装阶段参数和权限配置验证。

## 复刻启示

- 将 Action 作为可发布资源，并从应用依赖图自动生成打包清单；对不兼容能力和用户硬编码引用提供阻断式检查。
- 发布与安装分开审查：源产品说明依赖，目标组织再绑定组、用户和权限。
