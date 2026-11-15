<!-- 页面 URL：https://www.palantir.com/docs/foundry/action-types/trigger-schedule-build -->
<!-- 研读状态：已完成 -->

# 动作类型 • 触发排程构建 • Trigger schedule build • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/action-types/trigger-schedule-build)
- 官方中文来源：尚未确认（配对状态：missing）
- 页面语言：英文
- 主题栏目：action-types
- 相关性：direct；本体动作文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:02:10Z
- 产品状态：Schedule 规则可在 Action 执行时触发项目级构建，编辑不等待构建完成。

## 英文原文短摘录（每个来源不超过 25 词）

> “Edits do not wait for the build to finish.”

## 摘录译文

本体编辑不会等待构建完成。

## 中文要点

- Action 可配置 Schedule 规则触发重算资源集合；所选 Schedule 必须处于项目级模式，参数化排程需为每个排程参数提供值。
- 触发后先启动构建并取得 Schedule run RID，再立即应用其余规则和本体编辑，不阻塞等待构建结束。
- Action 的提交条件管理用户通过 Action 触发排程的权限；首次引用及编辑排程规则时仍要校验排程运行权限。
- Schedule run RID 可写入对象字符串属性，并格式化成显示 Running、Ignored、Failed、Succeeded 状态的链接。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Schedule rule | 排程规则 | Action 应用时触发项目排程构建 |
| Schedule run RID | 排程运行 RID | 标识某次排程运行的资源引用 |
| Project-scoped mode | 项目级模式 | 该规则要求的排程作用域 |

## 疑问与待验证项

- 构建启动后本体编辑可成功而构建稍后失败；产品应避免向用户暗示两者是同一事务。
- 通过 Action 授予排程运行能力属于权限委托，需评审哪些管理员可编辑动作规则。

## 复刻启示

- 运行轨迹把排程触发、异步构建和本体编辑记录为独立状态，并把 RID 关联回对象。
- 权限检查要验证动作维护者是否有权委托构建，调用者则由 Action 提交条件授权。
