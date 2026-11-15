<!-- 页面 URL：https://www.palantir.com/docs/zh/foundry/action-types -->
<!-- 研读状态：已完成 -->

# 动作类型 • 概述 • Palantir

- 英文来源：[现行英文原文](https://www.palantir.com/docs/foundry/action-types)
- 官方中文来源：[官方中文页（页面翻译准确性未验证）](https://www.palantir.com/docs/zh/foundry/action-types)
- 页面语言：中文（官方中文内容需与英文原文交叉核对）
- 主题栏目：action-types
- 相关性：direct；本体 Action 定义、验证和多应用写入一致性
- 官方更新时间：2026-11-12T17:46:46.937Z
- 目录核对时间：2026-11-14T14:58:13Z
- 产品状态：Action 是本体上的写入操作定义；可配置参数、规则、提交条件和副作用

## 英文原文短摘录（不超过 25 词）

> “An action is a single transaction that changes the properties of one or more objects, based on a user-defined logic.”

## 摘录译文

Action 是基于用户定义逻辑、改变一个或多个对象属性的单次事务操作。

## 中文要点

- Action Type 定义用户一次可提交的一组对象、属性和链接变更，并包含提交时触发的副作用行为。
- 通过参数收集结构化输入；规则定义如何写属性/建关系；submission criteria 可校验授权用户或业务条件；通知等 side effect 可在提交时执行。
- 示例 Assign Employee：改变员工 role 并关联新 Manager，可在一次动作体验中抽象成“调整岗位”而不是让用户手工改多个字段。
- 用户实际提交 Action 后变更进入 Ontology，并反映到用户应用；相同 Action 逻辑和校验可在不同应用共用，当前对象值包含用户编辑并写入对象类型 writeback dataset。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Action Type | Action 类型 | 一组可复用的本体变更定义及提交行为 |
| parameter | 参数 | 提交时用户提供的结构化输入 |
| submission criteria | 提交条件 | 检查用户/数据是否满足执行要求的逻辑 |
| side effect | 副作用 | 提交后可执行的通知或外部集成行为 |

## 疑问与待验证项

- 概览页称 Action 为 single transaction；是否原子、并发冲突及部分失败语义要看一致性/隔离和批量执行专页。
- Action 视图和逻辑可跨应用复用，但每个应用的用户权限和提交条件仍需各自评估。
- writeback dataset 是用户编辑纳入对象最终状态的承载表；底层流水线和数据落地细节需读对象编辑说明。

## 复刻启示

- 将 Action 建模为可版本化的命令定义：输入 schema、变更计划、提交校验、权限策略、副作用和执行审计。
- 先显示业务目标和影响对象/关系，再由系统生成属性级差异预览；提交前可验证、提交时做授权复核。
- 跨应用复用 Action 定义，但不可复用调用者权限；成功后生成可追踪的对象编辑与 side effect 记录。