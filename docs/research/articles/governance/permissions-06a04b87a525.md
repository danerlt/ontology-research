<!-- 页面 URL：https://www.palantir.com/docs/zh/foundry/action-types/permissions -->
<!-- 研读状态：已完成 -->

# 动作类型 • 权限 • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/action-types/permissions)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/action-types/permissions)
- 页面语言：中文
- 主题栏目：action-types
- 相关性：direct；动作权限文档
- 官方更新时间：2026-11-12T17:46:46.935Z
- 目录核对时间：2026-11-14T14:58:25Z
- 产品状态：中文页提示权限模型正从旧版权限迁移到 Ontology 角色；以英文现行页复核配置细节。

## 英文原文短摘录（每个来源不超过 25 词）

> “Permissions apply to action types in the following ways:”

## 摘录译文

权限对操作类型的作用方式如下：

## 中文要点

- 页面按用户能否查看、编辑、提交某动作类型说明权限；执行者还要能查看动作涉及的对象、链接类型及其数据源，并通过提交标准。
- 仅允许通过动作编辑时，用户对目标对象只需 Read 权限；对象可被写入而不对执行者可见。若同时开放其他编辑渠道，执行者可能需要写回数据集 Edit 权限，而该权限可揭示数据集中的更多信息。
- 中文页提醒旧版权限迁移到 Ontology 角色。它是官方 AIP 机器翻译且未验证；英文页比此处更详细地说明读时行列策略不保护写出数据、日志对象权限及通知收件人可见性。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Object edit permissions | 对象编辑权限 | 决定对象可通过哪些入口修改。 |
| Ontology roles | Ontology 角色 | 中文页提到的权限模型迁移方向。 |
| Check access panel | 检查访问面板 | 查询工作流及依赖动作访问权的工具。 |

## 疑问与待验证项

- 中文页摘要没有包含英文页完整的 side effect、通知收件人和读时授权边界；实施应以英文现行页及环境角色配置为准。
- 旧权限迁移的具体阶段、兼容期和新旧控制之间的优先级需要读取专门的 Ontology roles 文档确认。

## 复刻启示

- 在 UI 和 API 把动作定义权限、提交权限、对象读取权限、写回权限与副作用配置权限分开返回，形成可解释的授权检查清单。
- 允许 Action-only 写入而用户不可读时，在界面清晰标记“可提交但结果不可见”，防止用户误以为提交失败；审计日志也要保留有权管理员可查的路径。
