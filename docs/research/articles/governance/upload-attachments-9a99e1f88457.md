<!-- 页面 URL：https://www.palantir.com/docs/foundry/action-types/upload-attachments -->
<!-- 研读状态：已完成 -->

# 动作类型 • 上传附件 • Upload attachments • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/action-types/upload-attachments)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/action-types/upload-attachments)（配对状态：matched）
- 页面语言：英文
- 主题栏目：action-types
- 相关性：direct；本体动作文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:02:12Z
- 产品状态：附件经 Action 上传并依附对象属性，访问权限继承对象权限且临时孤儿会被清理。

## 英文原文短摘录（每个来源不超过 25 词）

> “There is a global, fixed file size limit of 200MB.”

## 摘录译文

全局固定文件大小上限为 200 MB。

## 中文要点

- Workshop、Object Explorer、Object Views、Quiver、Slate 均可通过 Action 表单/表格上传附件；附件的查看、编辑、删除权限与所属对象一致。
- Action 参数需为 Attachment；对象属性需为 Attachment，底层数据集列为 String；单属性多附件时参数允许多值，底层对象列为 Array。
- 文件会在加入表单时立即上传；取消或提交失败时附件不再可直接访问，并会在一段时间后永久删除。对象删除或移除属性映射时，附件也成为待清理孤儿。
- 附件同时支持规则型和函数型 Action；文件最大 200 MB，每个附件生命周期内最多关联 10 个对象，即使原对象删除也不会返还配额。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Attachment parameter | 附件参数 | Action 表单中承载上传文件的参数类型 |
| Orphan attachment | 孤儿附件 | 已上传但未绑定可访问对象的附件 |
| Object-backed dataset | 对象底层数据集 | 对象附件属性在存储侧的映射字段 |

## 疑问与待验证项

- 清理“经过一段时间”未给出固定时限；复刻系统需定义暂存 TTL、失败回收和用户可见状态。
- 每附件最多关联十个对象为生命周期限制，需要考虑复制对象或删除对象后的重用策略。

## 复刻启示

- 附件建立“暂存上传→Action 授权绑定→继承对象访问→孤儿清理”的状态机，文件权限不要脱离对象授权。
- 限制文件大小和可关联对象数，并在取消、失败、删除属性映射等路径上提供异步清理审计。
