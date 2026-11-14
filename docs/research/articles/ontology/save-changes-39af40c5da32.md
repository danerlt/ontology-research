<!-- 页面 URL：https://www.palantir.com/docs/foundry/ontology-manager/save-changes -->
<!-- 研读状态：已完成 -->

# Ontology Manager • Change management • Save changes to the Ontology • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/ontology-manager/save-changes)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/ontology-manager/save-changes)（配对状态：matched）
- 页面语言：英文
- 主题栏目：ontology-manager
- 相关性：direct；本体管理器文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:04:15Z
- 产品状态：待核对 Beta、预览、弃用或更名信息

## 英文原文短摘录（每个来源不超过 25 词）

> “Any changes you make in the Ontology Manager are stored locally in a work-in-progress state.”

## 摘录译文

“在 Ontology Manager 中所做的变更会先保存在本地的进行中状态。”

## 中文要点

变更先处于本地未发布状态。用户需要打开 Review edits 检查变更，再明确保存到本体。阻止保存的错误必须处理，警告可继续但应审阅。若其他用户已保存新版本，操作者需要先更新并解决冲突。文档也说明对象类型和属性的变更可能破坏依赖应用；对启用写回的类型，还要保护对象编辑历史。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Work-in-progress state | 进行中状态 | 尚未对其他用户/应用生效的本地变更集 |
| Review edits | 审阅编辑 | 保存前查看受影响资源、错误和警告的步骤 |
| Merge conflict | 合并冲突 | 更新到较新本体后出现的并发变更冲突 |
| Writeback | 写回 | 对象编辑结果落入对象类型写回数据集的机制 |

## 疑问与待验证项

- 页面提到“更新后解决冲突”，但具体字段级冲突规则依赖界面与其他变更历史页面，需另查；不可假设所有冲突都只是 revision 不同。
- 函数需要在独立 Functions 仓库修改，而非本体管理器，体现资源编辑边界。

## 复刻启示

- 用提案草稿和显式审阅/合并状态隔离工作中修改；保存前显示校验错误和非阻断警告。
- 合并需检测基础版本变化，并呈现冲突供决策；当前原型对 schema revision 做乐观锁，但没有工作区草稿、多资源错误清单或警告级别。
