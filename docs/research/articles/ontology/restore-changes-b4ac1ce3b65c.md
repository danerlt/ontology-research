<!-- 页面 URL：https://www.palantir.com/docs/zh/foundry/ontology-manager/restore-changes -->
<!-- 研读状态：已完成 -->

# 本体管理器 • Change management • 审查和恢复更改 • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/ontology-manager/restore-changes)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/ontology-manager/restore-changes)（已直接核验；页面声明未经验证的机器翻译）
- 页面语言：中文
- 主题栏目：ontology-manager
- 相关性：direct；本体管理器变更治理文档
- 官方更新时间：2026-11-12T17:46:46.935Z
- 目录核对时间：2026-11-14T15:00:34Z
- 产品状态：官方中文页为 AIP 机器翻译；英文现行页 UI 路径和恢复说明更简洁。

## 原文短摘录与翻译

> “这些更改将被添加到您的工作状态中，您需要保存更改到Ontology，以便您的恢复生效。”

**对应英文：** “The changes will be added to your working state and you will need to save your changes to the Ontology for your restore to take effect.”

## 摘录译文

恢复先改写当前工作状态；只有保存到 Ontology 后，历史恢复才真正生效。

## 中文要点

- 中文页讲全局编辑历史和单个资源历史：条目记录保存者、时间与修改内容，权限不足时可隐藏受限对象和链接的详细变化；可把同一作者的变更合并查看。
- 对单个对象类型选择历史版本会撤销所选记录之后的变更，但恢复不会立即修改已保存 Ontology；它先进入当前工作状态，再由用户保存。
- 该页是未经验证的机器翻译；英文现行文档把入口表述为全局 History tab、资源页 History tab，并强调一次记录对应一次用户保存。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| 编辑历史 | edits history | 逐次记录用户保存 Ontology 定义的历史。 |
| 资源历史 | resource history | 单个对象类型、链接类型或动作类型的局部历史。 |
| 恢复工作状态 | restore to working state | 先形成未保存差异，再由用户确认保存。 |

## 疑问与待验证项

- 中文页截图与当前英文 UI 路径描述不完全一致，界面迭代可能改变具体按钮位置；用户体验应围绕“查看差异—恢复到工作区—显式保存”建模。
- 本页的恢复入口主要针对 Object Type；其他资源的历史可以查看，但是否支持同样恢复流程需要逐类验证。

## 复刻启示

- “查看历史”和“恢复历史”分开呈现。恢复仅生成工作区差异，不直接发布；执行保存前展示将被覆盖的后续版本变化。
- 对无权读取的资源在全局历史中可隐藏细节但保留变更存在提示；审计查询同时执行资源级 ACL。
