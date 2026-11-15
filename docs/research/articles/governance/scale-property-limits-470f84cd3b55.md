<!-- 页面 URL：https://www.palantir.com/docs/foundry/action-types/scale-property-limits -->
<!-- 研读状态：已完成 -->

# 动作类型 • 规模与属性限制 • Scale and property limits • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/action-types/scale-property-limits)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/action-types/scale-property-limits)（配对状态：matched）
- 页面语言：英文
- 主题栏目：action-types
- 相关性：direct；本体动作文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:02:12Z
- 产品状态：Action 执行设有参数、对象、对象类型、单次编辑大小和批量调用上限，超限会失败。

## 英文原文短摘录（每个来源不超过 25 词）

> “Actions submitted that exceed these limits will not succeed and will display an error message to the user.”

## 摘录译文

超过这些限制提交的 Action 不会成功，并会向用户显示错误。

## 中文要点

- 参数列表：基础值列表最多 10,000 项；对象引用列表和提交条件中的列表各最多 1,000 项。
- 一次提交最多编辑 50 种对象类型、10,000 个对象；单个对象编辑上限为 OSv1 32 KB、OSv2 3 MB。
- 批量 Action 最多 10,000 次调用；函数支持 Action 未启用批量执行时批次上限降为 20；整批编辑作为一个组共同受编辑限制约束。
- 支持属性类型随单值/数组和存储版本变化；例如 OSv2 才支持部分 Struct、MediaReference、TimeSeriesReference 和 Vector，数组形式并非都可写。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Edit limit | 编辑上限 | 单个提交可变更的对象数量/类型/字节限制 |
| Batch call limit | 批量调用上限 | 单次批量 Action 可包含的调用数限制 |
| Property type support | 属性类型支持 | 某类值能否作为 Action 参数和写入目标 |

## 疑问与待验证项

- 配额可能随平台版本和调用应用变化；上述数字应与当前租户官方页面同步，不要编译成不可更新的常量。
- 批次整体编辑数限额与服务端分块策略如何交互，需通过边界请求验证。

## 复刻启示

- 按平台版本维护 Action 配额能力表，前端预估编辑对象/类型/字节和批次数，服务端仍做权威校验。
- 提交失败返回已达到的限制、当前消耗、版本差异和可拆分建议，避免只给通用错误。
