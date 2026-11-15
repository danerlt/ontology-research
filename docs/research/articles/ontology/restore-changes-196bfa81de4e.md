<!-- 页面 URL：https://www.palantir.com/docs/foundry/ontology-manager/restore-changes -->
<!-- 研读状态：已完成 -->

# Ontology Manager • Change management • Review and restore changes • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/ontology-manager/restore-changes)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/ontology-manager/restore-changes)（配对状态：matched）
- 页面语言：英文
- 主题栏目：ontology-manager
- 相关性：direct；本体管理器版本与变更治理文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:04:15Z
- 产品状态：页面未标注 Beta 或 Preview；恢复动作只作用于单个对象类型并进入工作状态。

## 英文原文短摘录（每个来源不超过 25 词）

> “Restored changes must be saved to take effect”

## 摘录译文

恢复的变更还必须保存到 Ontology 才会生效。

## 中文要点

- 全局视图能分开查看当前用户的未保存变更和已保存历史；历史条目给出保存时间与操作者，默认折叠，可展开详情，也可把同一作者的多个保存合并展示。
- 历史按用户每次保存记录一个条目。可按权限隐藏看不到详情的对象/链接变更；若不隐藏，仍能知道存在变更，但不会显示受限细节。
- 单个 Ontology 资源页可以查看该资源的未保存修改与已保存历史。文档描述的恢复范围是单个 Object Type：选择历史版本后，所选记录之后的修改会被撤回到工作状态，需再次保存才生效。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Unsaved changes | 未保存变更 | 用户当前工作状态中尚未写入 Ontology 的修改。 |
| History tab | 历史选项卡 | 按用户保存行为查看变更时间线。 |
| restore | 恢复 | 将对象类型回到历史版本并生成待保存变更。 |
| working state | 工作状态 | 还未提交到当前 Ontology 的编辑状态。 |

## 疑问与待验证项

- 页面没有承诺一次恢复可对多个资源同时回滚，也没有描述跨分支合并冲突；不可把它当作完整发布提案/事务回滚系统。
- 资源级审计的保留期、差异算法与恢复失败条件需与 Save changes、Ontology proposal/branching 文档配合理解。

## 复刻启示

- 将保存历史建模成带操作者、时间、资源、差异快照和版本前后引用的事件；管理器支持全局历史与资源局部历史，并按权限过滤细节。
- 恢复动作生成一个新的未保存差异，要求用户再次审阅并保存；在差异面板明确列出将被撤销的后续修改与影响资源。
- 多项目场景按资源和项目授权过滤历史，隐藏未授权细节同时保留“有变更”的审计事件。
