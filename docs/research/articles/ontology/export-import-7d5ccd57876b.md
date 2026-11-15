<!-- 页面 URL：https://www.palantir.com/docs/zh/foundry/ontology-manager/export-import -->
<!-- 研读状态：已完成 -->

# 本体管理器 • 导出、编辑和导入Ontology • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/ontology-manager/export-import)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/ontology-manager/export-import)
- 页面语言：中文
- 主题栏目：ontology-manager
- 相关性：direct；本体管理器文档
- 官方更新时间：2026-11-12T17:46:46.935Z
- 目录核对时间：2026-11-15
- 产品状态：官方中文页标注为未经验证的 AIP 机器翻译；本卡对照英文原文整理。

## 英文原文短摘录（每个来源不超过 25 词）

> “You should not depend on the exported JSON schema as it may change over time.”

## 摘录译文

不要依赖导出 JSON 的 schema，因为它可能随时间变化。

## 中文要点

- 管理器可将当前工作状态导出为 JSON，供文本编辑或复制到另一个本体；再次导入后会把文件中的差异重建为待保存更改。
- 导出包括工作状态中的变更，而不只是已发布本体；导入后需查看变更数量，再按正常保存流程审核。
- 包含条件格式规则的导出文件不能导入到不同本体；未引用的规则集也会导致导入失败。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| working state | 工作状态 | 尚未正式保存发布的本体编辑快照。 |
| schema compatibility | 格式兼容性 | 导出 JSON 结构随产品演进变化的风险。 |
| conditional formatting | 条件格式 | 依赖特定本体规则集的属性显示配置。 |

## 疑问与待验证项

- 文档明确提醒 JSON schema 可能变化，因此文件格式不可作为长期稳定集成 API。
- 跨本体复制有规则兼容限制；本地导入工具应展示不可迁移项而不是悄悄丢弃。

## 复刻启示

- 提供带版本号、校验、预览差异和错误定位的备份/迁移包；导入只生成草稿差异，不直接覆盖已发布模型。
- 把内部 schema 与导出格式版本分离，校验关系端点、字段引用、ID 冲突和环境特定配置。
