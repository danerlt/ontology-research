<!-- 页面 URL：https://www.palantir.com/docs/foundry/action-types/dropdown-security -->
<!-- 研读状态：已完成 -->

# 动作类型 • 对象下拉菜单安全注意事项 • Object dropdown security considerations • Palantir

- 英文来源：[英文原文](https://www.palantir.com/docs/foundry/action-types/dropdown-security)
- 官方中文来源：[官方中文页面](https://www.palantir.com/docs/zh/foundry/action-types/dropdown-security)（配对状态：matched）
- 页面语言：英文
- 主题栏目：action-types
- 相关性：direct；本体动作文档
- 官方更新时间：未提供
- 目录核对时间：2026-11-14T15:01:56Z
- 产品状态：静态属性值筛选可能通过动作定义与对象集 RID 暴露无权查看对象的敏感值。

## 英文原文短摘录（每个来源不超过 25 词）

> “Static value filters in object dropdown validations are exposed to all users who can view the action type.”

## 摘录译文

对象下拉验证中的静态值筛选会暴露给所有能查看该 Action 类型的用户。

## 中文要点

- 若对象参数的下拉验证写入静态敏感值，即使用户无权查看被筛对象，也可能从筛选条件推断该属性值存在。
- 表单调用时验证会转换成对象集；用户可检查网络请求中的对象集 RID，因此仅隐藏 UI 或 Action 配置详情并不足以消除泄露。
- 改用用户输入参数或另一个对象的属性进行动态筛选，不会把同一个硬编码值暴露在 Action 定义中；对象筛选仍受该用户可见性限制。

## 术语对照

| 英文术语 | 中文译法 | 本页语境 |
|---|---|---|
| Static value filter | 静态值筛选 | 直接把敏感字面值写入对象参数筛选 |
| Object set RID | 对象集 RID | 请求中可能携带筛选语义的对象集标识 |
| Dynamic filter | 动态筛选 | 由输入参数或对象属性产生筛选条件 |

## 疑问与待验证项

- 具体请求中哪些过滤表达式会被序列化到 RID、是否可能被日志记录，需在本地实现的传输链路中实测。
- 安全过滤需要同时评估对象权限、属性权限和查询表达式，单靠不显示敏感值不能证明安全。

## 复刻启示

- 禁止将机密常量直接写入可供普通用户查看的 Action 下拉校验；优先使用经授权的动态对象集过滤。
- Action 安全审查应检查定义、表单请求、对象集查询和审计日志四个面，而不只检查前端显示。
