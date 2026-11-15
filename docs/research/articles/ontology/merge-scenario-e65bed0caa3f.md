<!-- 页面 URL：https://www.palantir.com/docs/foundry/ontology/merge-scenario -->
<!-- 研读状态：已完成 -->

# Merge scenarios • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/ontology/merge-scenario)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：ontology
- 相关性：direct；本体模型与治理文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:04:06Z
- 产品状态：页面说明将 Scenario 应用到本体主数据需要专门配置的 Apply Scenario Action rule，而不是场景保存后自动覆盖主数据。

## 英文原文短摘录（每个来源不超过 25 词）

> “Scenarios are merged through action types.”

## 摘录译文

Scenario 通过 Action 类型合并。

## 中文要点

- 场景内创建/修改/删除对象以及添加/移除链接都留在隔离沙箱；merge Action 将场景编辑以单次事务应用到本体。
- 最小 merge action 参数是 scenario reference RID；调用方可从 Workshop 变量或 OSDK app 传递。
- 可新建只承担 merge 的 Action，在配置中限定允许合并的 Object types 和 Link types，再在 Security & Submission Criteria 中决定谁可执行。
- 已有 Action 也能通过 Apply Scenario rule 扩展为合并入口。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Apply Scenario rule | 应用场景规则 | 将 scenario 中的编辑纳入 Action 执行的规则。 |
| scenario reference | 场景引用 | 指向待合并隔离场景的 RID。 |
| merge action | 合并 Action | 在安全和提交条件控制下将场景编辑提交到本体。 |

## 疑问与待验证项

- - 页面说明单次事务语义，但未在此页展开并发基线变化时的冲突处理；merge 前需要检查 scenario 的 base/rebase 状态。
- - 合并范围可配置对象和链接类型，复刻应验证新增、删除、属性修改和链接更新都不会越过 allowlist。

## 复刻启示

- - 提案/合并审核界面应展示受影响对象与链接的 before/after diff，并对对象类型/链接类型执行白名单检查。
- - merge 要独立授权、幂等、事务化并记录 scenario RID、基线版本、执行人、审核结论与结果；场景试算成功不代表有生产写权限。
