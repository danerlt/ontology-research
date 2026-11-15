<!-- 页面 URL：https://www.palantir.com/docs/foundry/action-types/action-reverts -->
<!-- 研读状态：已完成 -->

# Action types • Undo or revert Actions • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/action-types/action-reverts)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/action-types/action-reverts)（配对状态：matched）
- 页面语言：英文
- 主题栏目：action-types
- 相关性：direct；本体动作文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:02:20Z
- 产品状态：页面未标注 Beta；撤销能力仅支持 OSv2 对象，具体开关受动作创建时间影响。

## 英文原文短摘录（每个来源不超过 25 词）

> “The toast below is your only opportunity to revert the action.”

## 摘录译文

成功提示中的撤销入口是文档描述的唯一撤销机会；执行删除动作前尤其要注意该提示的时限性。

## 中文要点

- Action revert 仅适用于修改或创建 OSv2 对象类型的 Action，当前只能由执行者本人撤销；新建动作默认可撤销，但配置仍可关闭，OSv1 对象不可撤销。
- 撤销入口仅在成功 toast 中提供。某对象发生任何后续编辑后，原 Action 对该对象的修改即不能再撤销；提交后关闭撤销设置也会使该动作不可撤销，即便后来重新打开。
- 撤销只反向修改对象实例，不会撤回或重放通知、Webhook 等副作用。删除动作错过 toast 后，文档给出的补救方式较重：迁移到新对象类型并用函数复制，或清除该对象类型的全部编辑。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Action revert | 操作撤销 | 对最近一次 Action 的对象编辑执行逆向恢复。 |
| Object Storage v2 | 对象存储 v2（OSv2） | 文档中支持 Action 撤销的对象存储版本。 |
| side effect | 副作用 | 通知、Webhook 等非对象字段编辑效果，不随对象编辑撤销。 |

## 疑问与待验证项

- 页面把撤销定位为紧随成功提交的即时能力，不是可随时从历史记录执行的通用回滚；删除和后续并发编辑场景尤需验证。
- 对函数写入、跨对象部分失败和重复点击撤销的精确原子性/幂等语义没有在本页完整展开，应从运行时 API 与冲突文档继续核对。

## 复刻启示

- 记录每次 Action 产生的 before/after 或可重放补偿数据、执行人、目标对象及事件版本；撤销前对全部受影响对象做最新版本检查，确保任何对象有后续编辑时拒绝整次撤销并说明冲突对象。
- 将“撤销对象编辑”和“补偿通知/Webhook”建成不同能力；向用户提供可见的撤销窗口、受支持存储类型与不可恢复删除提醒，并在事件日志中另记撤销时间。
