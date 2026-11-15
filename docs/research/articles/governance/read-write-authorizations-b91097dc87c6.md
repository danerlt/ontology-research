<!-- 页面 URL：https://www.palantir.com/docs/foundry/action-types/read-write-authorizations -->
<!-- 研读状态：已完成 -->

# Action types • Read and write authorizations • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/action-types/read-write-authorizations)
- 官方中文来源：未发现精确配对页面（配对状态：missing）
- 页面语言：英文
- 主题栏目：action-types
- 相关性：direct；本体动作文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:02:16Z
- 产品状态：Beta；是否可用取决于环境 enrollment，功能和平台支持可能变化。

## 英文原文短摘录（每个来源不超过 25 词）

> “Read and write authorizations are in the beta phase of development and may not be available on your enrollment.”

## 摘录译文

读写授权仍处于 Beta 阶段，可能受环境 enrollment 影响而不可用；功能及平台支持也可能变化。

## 中文要点

- Read authorization 为 Action 在读取或接收数据时设定安全上界；Write authorization 为动作新建或修改的数据设定最低安全级别。两者补充用户既有权限与 Action 提交条件，不能赋予访问权或替代权限检查。
- 提交时会验证最终写入安全级别是否达到配置下界；表单的最低安全级别提示只是预览，权威检查仍发生在提交时。动作执行者仍须具备访问权限和有效 marking 值。
- 读写边界不一致可能允许动作读取更敏感数据后写出较低敏感级别，形成去分类或数据泄漏。发布者需要有被切断 mandatory marking 的去分类权限；若没有配置读授权，保存/发布时不会做该项去分类检查，因此官方建议可能读取标记数据时配置读授权。
- Write authorization 不约束平台托管写入的 Action log 和 edit history 对象；不同 marking 类别的组合规则也有差异，Organization 的读授权要求所有配置组织，写授权至少命中一个。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| read authorization | 读授权 | 限制动作可读取或接收的数据安全级别上界。 |
| write authorization | 写授权 | 限制动作所产生数据的最低安全要求。 |
| declassification | 去分类 | 允许派生输出低于敏感输入标记的安全级别。 |

## 疑问与待验证项

- 该能力当前为 Beta，必须按环境实际 enrollment 验证 UI、API 和运行时拒绝行为；文档中的最低安全状态提示不构成最终放行依据。
- action log/edit history 被排除在写授权之外，意味着审计数据可能比被审计对象暴露给更广人群；实现时要单独设计日志对象权限和敏感参数过滤。

## 复刻启示

- 将读授权和写授权作为动作 schema 的两条独立边界保存，发布检查时比较两者并显式显示去分类授权与标记传播断点；在实际提交事务中重新验证结果数据。
- 不把授权配置当成用户 ACL：仍执行项目成员、对象/字段读取权限、Action submission criteria 与 marking 值检查。审计对象使用独立安全策略。
- 为 Agent 工具调用和函数驱动动作建立相同的读集与写集约束；记录哪些敏感字段被读取、如何聚合，以及输出安全级别为何满足下界。
